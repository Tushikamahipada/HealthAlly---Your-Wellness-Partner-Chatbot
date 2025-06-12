import nltk
import warnings
import numpy as np
import random
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings("ignore")

# Load JSON data
with open('pincodes.json', 'r', encoding='utf-8') as fjson:
    pincode_data = json.load(fjson)
pincode_lookup = {str(entry["pincode"]): entry for entry in pincode_data}

with open("diseases.json", "r", encoding="utf-8") as f:
    disease_data = json.load(f)
disease_lookup = {d['disease'].lower(): d for d in disease_data}

# Example base content for NLP
raw = """Welcome to HealthBot. This bot provides primary health care advice."""
rawone = """This module provides additional information related to your queries."""

# NLP setup
nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
sent_tokensone = nltk.sent_tokenize(rawone)
word_tokensone = nltk.word_tokenize(rawone)

lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greetings
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = [
    "Hi, are you suffering from any health issues? (Y/N)",
    "Hey, are you having any health issues? (Y/N)",
    "Hii there, are you having any health issues? (Y/N)",
    "Hello, are you having any health issues? (Y/N)"
]

Basic_Q = ("yes", "y")
Basic_Om = ("no", "n")
Basic_Ans = "Okay, tell me about your symptoms"
Basic_AnsM = "Thank you, visit again"

awaiting_pincode = False  # Global state

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

def basic(sentence):
    return Basic_Ans if sentence.lower() in Basic_Q else None

def basicM(sentence):
    return Basic_AnsM if sentence.lower() in Basic_Om else None

def IntroduceMe(_):
    return "I’m your Health Assistant 🤖. Let me know your symptoms or pincode."

def handle_pincode(pincode):
    pincode = pincode.strip()
    data = pincode_lookup.get(pincode)
    if data:
        return (
            f"🧑‍⚕️ Doctor: {data.get('name', 'Doctor')}\n"
            f"🏥 Hospital: {data.get('hospital', 'Hospital')}\n"
            f"📍 Location: {data.get('location', 'Not provided')}\n"
            f"📞 Contact: {data.get('contact', 'Not available')}\n"
            f"⏰ Timings: {data.get('timings', 'Not listed')}"
        )
    return "❌ Sorry, no doctor found for that pincode."

def handle_disease_query(user_input):
    global awaiting_pincode
    for disease in disease_lookup:
        if disease in user_input.lower():
            d = disease_lookup[disease]
            awaiting_pincode = True
            return (
                f"🦠 Disease: {d.get('disease', 'N/A')}\n"
                f"🤒 Symptoms: {', '.join(d.get('symptoms', []))}\n"
                f"🥗 Food to Take: {', '.join(d.get('food_to_take', []))}\n"
                f"🚫 Food to Avoid: {', '.join(d.get('food_to_avoid', []))}\n"
                f"💊 Medicines: {', '.join(d.get('medicines', ['Consult a doctor']))}\n\n"
                f"📍 Now, please tell me your pincode to find nearby doctors."
            )
    return None

def predict_disease_from_symptoms(user_input):
    global awaiting_pincode
    user_symptoms = set(LemNormalize(user_input))
    match_scores = []

    for disease, info in disease_lookup.items():
        disease_symptoms = set(LemNormalize(' '.join(info.get('symptoms', []))))
        match_count = len(user_symptoms & disease_symptoms)
        if match_count > 0:
            match_scores.append((disease, match_count))

    if not match_scores:
        return None

    match_scores.sort(key=lambda x: x[1], reverse=True)
    top_disease = match_scores[0][0]
    d = disease_lookup[top_disease]

    awaiting_pincode = True  # ✅ Set flag to expect pincode next

    return (
        f"🧠 Based on your symptoms, the most likely disease is:\n\n"
        f"🦠 Disease: {d.get('disease', 'N/A')}\n"
        f"🤒 Symptoms: {', '.join(d.get('symptoms', []))}\n"
        f"🥗 Food to Take: {', '.join(d.get('food_to_take', []))}\n"
        f"🚫 Food to Avoid: {', '.join(d.get('food_to_avoid', []))}\n"
        f"💊 Medicines: {', '.join(d.get('medicines', ['Consult a doctor']))}\n\n"
        f"📍 Now, please enter your pincode to find nearby doctors."
    )

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    robo_response = "I am sorry! I don't understand you." if req_tfidf == 0 else sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    robo_response = "I am sorry! I don't understand you." if req_tfidf == 0 else sent_tokensone[idx]
    sent_tokensone.remove(user_response)
    return robo_response

def handle_basic_conversations(user_response):
    user_response = user_response.lower()

    if "your name" in user_response or "who are you" in user_response:
        return "I’m your Health Assistant 🤖. I'm here to help you with symptoms, diseases, and local doctors."
    if "thank" in user_response:
        return "You're welcome! 😊 Let me know if you need more help."
    if "help" in user_response:
        return (
            "Sure! You can:\n"
            "- Tell me your symptoms (e.g., 'I have cold and fever')\n"
            "- Mention a disease (e.g., 'malaria')\n"
            "- Ask for doctors by giving your pincode (e.g., '560001')\n"
            "I'm here to guide you with basic healthcare advice."
        )
    if "how are you" in user_response:
        return "I'm doing well, thank you for asking! How can I assist you today?"
    if "what can you do" in user_response:
        return "I can help with basic health advice, symptom checks, food & medicine suggestions, and suggest doctors near you."
    return None

def chat(user_response):
    global awaiting_pincode
    user_response = user_response.strip()

    if awaiting_pincode:
        awaiting_pincode = False
        return handle_pincode(user_response)

    if user_response.lower() == 'bye':
        return "Bye! Take care.."
    if user_response.lower() in ['thanks', 'thank you']:
        return "You're welcome!"

    if (reply := basicM(user_response)): return reply
    if (reply := greeting(user_response)): return reply
    if (reply := basic(user_response)): return reply
    if (reply := handle_disease_query(user_response)): return reply
    if (reply := predict_disease_from_symptoms(user_response)): return reply
    if "module" in user_response.lower():
        return responseone(user_response)
    if (reply := handle_basic_conversations(user_response)): return reply

    return response(user_response)
