# 🩺 HealthAlly – Your Wellness Partner Chatbot

**HealthAlly** is a smart healthcare chatbot built with **Python**, **Flask**, and **NLP**, designed to provide **basic health guidance** based on your symptoms or disease input. It offers **diet advice**, **medication suggestions**, and can recommend **doctors nearby** based on your pincode.

---

## 🔍 Features

- 🧠 **Symptom Detection & Disease Prediction**  
  Understands your symptoms and suggests the most likely health condition.

- 🍎 **Personalized Health Advice**  
  Provides food to eat/avoid and medicine suggestions for common diseases.

- 📍 **Doctor Locator**  
  Recommends local doctors based on Indian pincodes with contact, location & timing.

- 💬 **Chat Interface with Voice Support**  
  Speaks responses using Web Speech API and offers a modern chat UI.

- 🌙 **Dark Mode & Responsive UI**  
  Toggle dark/light themes. Fully mobile-friendly.

- 📹 **Background Video**  
  Subtle animated background for a more engaging UI experience.

---

## Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | HTML, Tailwind CSS, JavaScript |
| Backend   | Flask (Python)     |
| NLP       | NLTK, Scikit-Learn |
| Voice     | Web Speech API     |
| Data      | JSON (diseases & pincodes)     |
----------------------------------------------
---

## Getting Started

**1. Install dependencies**
pip install flask nltk scikit-learn

**2. Download NLTK data (first time only)**
import nltk
nltk.download('punkt')
nltk.download('wordnet')

**3. Run the app**
python serve.py

**4.Open in browser**
Visit http://127.0.0.1:5000/

---

## 💡 Example Queries

"I have sore throat and mild headache"
→ Suggests Common Cold with food & medicine advice.

"Tell me about dengue"
→ Gives symptoms, recommended diet, and precautions.

"My pincode is 530001"
→ Shows local doctor & hospital details for Visakhapatnam.

---

## 🖥️ Screenshots

### 💡 Disease Prediction Based on Symptoms
![Disease prediction](https://github.com/Tushikamahipada/HealthAlly---Your-Wellness-Partner-Chatbot/blob/main/Images/disease%20prediction.png)

### 📍 Doctor Suggestion Based on Pincode
![Doctor suggestion](https://github.com/Tushikamahipada/HealthAlly---Your-Wellness-Partner-Chatbot/blob/main/Images/pincode%20based%20doctor%20suggestion.png)

### 🌙 Dark Mode View
![Dark mode](https://github.com/Tushikamahipada/HealthAlly---Your-Wellness-Partner-Chatbot/blob/main/Images/dark%20mode.png)

---

## 📌 Future Enhancements

1. User login for history tracking

2. Language translation & multilingual support

3. ChatGPT/LLM integration for smarter responses

---

Feel free to explore HealthAlly and see how it can assist with your health-related inquiries.
