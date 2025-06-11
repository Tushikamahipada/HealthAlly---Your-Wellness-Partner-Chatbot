# 🩺 HealthAlly – Your Wellness Partner Chatbot

**HealthAlly** is a smart healthcare chatbot built with **Python**, **Flask**, and **NLP**, designed to provide **basic health guidance** based on your symptoms or disease input. It offers **diet advice**, **medication suggestions**, and can recommend **doctors nearby** based on your pincode.

---

## Features

-  **Symptom Detection & Disease Prediction**  
  Understands your symptoms and suggests the most likely health condition.

-  **Personalized Health Advice**  
  Provides food to eat/avoid and medicine suggestions for common diseases.

-  **Doctor Locator**  
  Recommends local doctors based on Indian pincodes with contact, location & timing.

-  **Chat Interface with Voice Support**  
  Speaks responses using Web Speech API and offers a modern chat UI.

-  **Dark Mode & Responsive UI**  
  Toggle dark/light themes. Fully mobile-friendly.

-  **Background Video**  
  Subtle animated background for a more engaging UI experience.

---

## Tech Stack

Frontend: HTML, Tailwind CSS, Vanilla JS

Backend: Python (Flask)

Data: JSON-based knowledge base for diseases and doctor information

NLP: NLTK + TF-IDF vectorization for matching symptoms and generating responses

Voice: Web Speech API for speech synthesis

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

Feel free to explore HealthAlly and see how it can assist with your health-related inquiries.
