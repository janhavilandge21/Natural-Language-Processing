import streamlit as st
import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# FAQ Database (You can expand this list)
# ---------------------------
faq_data = {
    "what is your company leave policy": "Our company provides 12 paid leaves per year along with public holidays.",
    "how many working hours per week": "We follow a 40-hour work week, Monday to Friday.",
    "does the company provide work from home": "Yes, work-from-home is allowed based on project requirements and manager approval.",
    "what is the notice period": "The standard notice period is 2 months.",
    "do you provide health insurance": "Yes, we provide health insurance for employees and their immediate family.",
    "what are the office working hours": "Our office hours are from 9:30 AM to 6:30 PM.",
    "is there an internship program": "Yes, we offer internship programs for students and freshers.",
    "do you have a referral policy": "Yes, employees can refer candidates and get rewards under our referral policy.",
    "does the company support skill training": "Yes, we provide training sessions, workshops, and reimbursements for certifications.",
    "what is the dress code": "Our dress code is smart casuals from Monday to Friday."
}

# ---------------------------
# Clean text function
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

# ---------------------------
# Chatbot Logic using TF-IDF + Cosine Similarity
# ---------------------------
def chatbot_response(user_input):
    user_input = clean_text(user_input)
    faq_questions = list(faq_data.keys())

    # Vectorize
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_input] + faq_questions)

    # Cosine similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    max_sim_idx = similarity.argmax()
    max_score = similarity[max_sim_idx]

    if max_score > 0.4:  # threshold
        return faq_data[faq_questions[max_sim_idx]]
    else:
        return random.choice([
            "I'm sorry, I don’t have information about that.",
            "Could you please ask something else?",
            "I’m not sure about this, but you can check with HR directly."
        ])

# ---------------------------
# Streamlit App UI
# ---------------------------
st.set_page_config(page_title="HR Interview Q&A Chatbot", layout="centered")
st.title("🤖 HR Interview FAQ Chatbot")
st.write("Ask me questions about company policies, work hours, leave policy, and more!")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("💬 You:", "")

if st.button("Ask") and user_input.strip() != "":
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**👤 {role}:** {message}")
    else:
        st.markdown(f"**🤖 {role}:** {message}")
