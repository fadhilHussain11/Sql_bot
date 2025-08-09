const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const micBtn = document.getElementById("mic-btn");
const textInput = document.getElementById("text-input");


function appendMessage(content, className) {
  const msg = document.createElement("div");
  msg.className = `message ${className}`;
  msg.textContent = content;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

//send text to flask
sendBtn.onclick = async () => {
  console.log("iam wroking");
  const text = textInput.value.trim();
  if (!text) return;

  appendMessage(text,"user-msg"); // show user message
  textInput.value = "";

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text }),
  });

  const data = await res.json();
  appendMessage(data.response, "bot-msg");
};

// 🎤 Voice Recording
micBtn.onclick = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const mediaRecorder = new MediaRecorder(stream);
  let chunks = [];

  mediaRecorder.ondataavailable = e => chunks.push(e.data);
  mediaRecorder.onstop = async () => {
    const blob = new Blob(chunks, { type: "audio/webm" });
    const formData = new FormData();
    formData.append("audio", blob, "input.webm");

    const res = await fetch("/voice", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    //appending transcription
    appendMessage(data.transcription, "user-msg");

    //poll for final bot 
    pollForResponse(data.request_id)
    
  };

  mediaRecorder.start();
  setTimeout(() => mediaRecorder.stop(), 7000);
};

// function to keep checking until result is ready
function pollForResponse(request_id){
  const interval = setInterval(async () => {
    const res = await fetch('/result/${request_id}');
    const data = await res.json();

    if (data.status == 'ready'){
      clearInterval(interval);
      appendMessage(data.response, "bot-msg");
    }
  }, 2000);
}