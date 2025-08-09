import os
import uuid
import threading
import whisper
from flask import Flask,request,render_template,jsonify
from dotenv import load_dotenv
from src.db_conncetion import configure 
from src.agent_tools import generate_by_agent
from langchain_groq import ChatGroq
load_dotenv()


# database connection and llm
db = configure()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key,model="meta-llama/llama-4-maverick-17b-128e-instruct",streaming=True,max_tokens=400)

#whisper model 
model = whisper.load_model("base")

#flask backend
application = Flask(__name__)
app = application

response_cache = {}
def save_response_to_cache(request_id,response):
    response_cache[request_id] = response

def get_response_from_cache(request_id):
    return response_cache.get(request_id)

def run_agent_async(transcription, request_id):
    response = generate_by_agent(db=db,llm=llm,input=transcription)
    save_response_to_cache(request_id,response)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask',methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message")
    respone = generate_by_agent(db=db,llm=llm,input=user_message)
    bot_response = respone
    return jsonify({"response":bot_response})

@app.route('/result/<request_id>',methods=["GET"])
def get_result(request_id):
    response = get_response_from_cache(request_id)
    if response:
        return jsonify({"status":"ready","response":response})
    else:
        return jsonify({"status":"pending"})
    

@app.route('/voice',methods=["POST"])
def voice():
    audio = request.files["audio"]
    filepath = os.path.join("uploads",audio.filename)
    audio.save(filepath)
    result = model.transcribe(filepath)
    transcription = result["text"]

    request_id = str(uuid.uuid4())
    threading.Thread(target=run_agent_async,args=(transcription,request_id)).start()
    return jsonify({"request_id":request_id, "transcription":transcription})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
