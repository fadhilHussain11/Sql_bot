# SQLBot – AI-Powered SQL Query Assistant

## Project Overview
SQLBot is an AI-driven assistant that allows users to query SQL databases using natural language through text or voice. It leverages LangChain SQL agents and SQLDatabaseToolkit to safely convert natural language questions into SQL queries. The system integrates OpenAI Whisper for speech-to-text functionality, a Flask backend for processing, and a responsive frontend built with HTML, CSS, and JavaScript. Query results are displayed as tables or charts for easy analysis.

## Features
- Speech-to-Text input via OpenAI Whisper  
- Natural language to SQL query translation with LangChain agents  
- Secure SQL execution on databases using SQLDatabaseToolkit  
- Interactive visualizations of query results  
- Web interface powered by Flask and standard web technologies  

## Installation
1. Clone the repository:  
   git clone https://github.com/YourUsername/SQLBot.git  
   cd SQLBot

2. Create and activate a virtual environment:  
   python -m venv venv  
   # Windows: venv\Scripts\activate  
   # macOS/Linux: source venv/bin/activate

3. Install dependencies:  
   pip install -r requirements.txt

4. Make sure FFmpeg is installed and in your system PATH: https://ffmpeg.org/download.html

5. Create a `.env` file and add your OpenAI API key:  
   OPENAI_API_KEY=your_api_key_here

## Usage
Run the Flask application:  
python app.py  

Open http://127.0.0.1:5000 in your browser.  
Use voice or text input to query the database naturally.

## Requirements
- langchain  
- python-dotenv  
- langchain-community  
- langchain_huggingface  
- langchain_chroma  
- streamlit  
- langchain_groq  
- langchain_core  
- langserve  
- openai-whisper  
- ffmpeg-python  
- flask  

## Project Structure
SQLBot/  
├── app.py  
├── requirements.txt  
├── templates/  
├── static/  
├── utils/  
├── assets/  
└── .env  

## Credits
Database source and inspiration: [SQL E-Commerce Dataset by youssefismail20 on Kaggle](https://www.kaggle.com/code/youssefismail20/sql-e-commerce/notebook)


