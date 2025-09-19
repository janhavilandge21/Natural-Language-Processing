🤖 HR Interview FAQ Chatbot

An AI-powered FAQ Chatbot designed to assist job seekers with HR Interview preparation. The chatbot provides instant answers to frequently asked interview questions, built using Natural Language Processing (NLP) and Machine Learning techniques.

🚀 Features

📌 Answers common HR interview questions in real time

🧠 Uses NLP techniques for text preprocessing & understanding

🔍 Employs TF-IDF & ML models for response matching

💬 Interactive chatbot interface (console/streamlit)

📊 Scalable for adding custom FAQs & datasets


⚙️ Installation

Create a virtual environment & install dependencies:

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

Download required NLTK resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

▶️ Usage
Run the chatbot
python app.py

Example Conversation
User: Tell me about yourself.  
Bot: This is usually the first question in an HR interview. Prepare a short and professional introduction including your education, experience, and career goals.  

📌 Requirements
nltk
scikit-learn
pandas
numpy
streamlit (if using web app)


Install with:

pip install -r requirements.txt

📊 Future Enhancements

🌐 Deploy chatbot on Streamlit / Flask

🎙️ Add speech-to-text support for voice interaction

🤖 Integrate transformer-based models (BERT, GPT) for better accuracy

📱 Deploy as a web app or mobile app
