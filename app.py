import random
import streamlit as st
import nltk
from textblob import TextBlob
from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

# Load or train a simple AI model
try:
    model = joblib.load("love_model.pkl")
except:
    X_train = np.array([[80, 70, 90], [40, 50, 60], [90, 85, 95], [30, 40, 50], [60, 70, 80]])
    y_train = np.array([85, 50, 92, 40, 75])
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, "love_model.pkl")

def ai_compatibility_analysis(name1, name2, desc):
    name_sentiment = (TextBlob(name1).sentiment.polarity + TextBlob(name2).sentiment.polarity) * 50
    desc_sentiment = TextBlob(desc).sentiment.polarity * 100
    return int((name_sentiment + desc_sentiment) / 2)

def ml_based_compatibility(zodiac_score, vacation_score, pet_score):
    features = np.array([[zodiac_score, vacation_score, pet_score]])
    return int(model.predict(features)[0])

def zodiac_compatibility(sign1, sign2):
    compatibility_chart = {
        ("Aries", "Leo"): 90, ("Aries", "Sagittarius"): 85, ("Aries", "Gemini"): 75, ("Aries", "Cancer"): 50,
        ("Taurus", "Virgo"): 88, ("Taurus", "Capricorn"): 80, ("Taurus", "Gemini"): 45, ("Taurus", "Libra"): 55,
        ("Gemini", "Libra"): 92, ("Gemini", "Aquarius"): 89, ("Gemini", "Pisces"): 60, ("Gemini", "Cancer"): 50,
        ("Cancer", "Scorpio"): 95, ("Cancer", "Pisces"): 90, ("Cancer", "Aries"): 50, ("Cancer", "Leo"): 60,
        ("Leo", "Sagittarius"): 93, ("Leo", "Aquarius"): 70, ("Leo", "Virgo"): 65,
        ("Virgo", "Capricorn"): 88, ("Virgo", "Pisces"): 72,
        ("Libra", "Aquarius"): 91, ("Libra", "Sagittarius"): 80,
        ("Scorpio", "Pisces"): 96, ("Scorpio", "Capricorn"): 90,
        ("Sagittarius", "Aquarius"): 85,
        ("Capricorn", "Taurus"): 87,
    }
    return compatibility_chart.get((sign1, sign2), random.randint(40, 90))

def dream_vacation_match(vacation1, vacation2):
    if vacation1 == vacation2:
        return 95
    return random.randint(50, 85)

def pet_preference_match(pet1, pet2):
    if pet1 == pet2:
        return 90
    return random.randint(50, 80)

def main():
    st.set_page_config(page_title="AI Love Calculator", page_icon="💘", layout="wide")
    page_bg = "https://source.unsplash.com/1600x900/?love,romance"
    st.markdown(f"""
        <style>
            .stApp {{
                background: url({page_bg});
                background-size: cover;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("💘 AI Love Calculator 💘")
    
    name1 = st.text_input("Enter your name:")
    name2 = st.text_input("Enter your partner's name:")
    relationship_desc = st.text_area("Describe your relationship in one sentence:")
    
    zodiac1 = st.selectbox("Select your zodiac sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac2 = st.selectbox("Select your partner's zodiac sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac_score = zodiac_compatibility(zodiac1, zodiac2)
    
    vacation1 = st.selectbox("Choose your dream vacation:", ["Beach", "Mountains", "City Escape", "Safari", "Cruise"])
    vacation2 = st.selectbox("Choose your partner's dream vacation:", ["Beach", "Mountains", "City Escape", "Safari", "Cruise"])
    vacation_score = dream_vacation_match(vacation1, vacation2)
    
    pet1 = st.selectbox("Pick a favorite pet:", ["Dog", "Cat", "Bird", "Rabbit", "Fish"])
    pet2 = st.selectbox("Pick your partner's favorite pet:", ["Dog", "Cat", "Bird", "Rabbit", "Fish"])
    pet_score = pet_preference_match(pet1, pet2)
    
    if st.button("💓 Calculate Love Score 💓"):
        ai_score = ai_compatibility_analysis(name1, name2, relationship_desc)
        ml_score = ml_based_compatibility(zodiac_score, vacation_score, pet_score)
        final_score = (zodiac_score + vacation_score + pet_score + ai_score + ml_score) // 5
        
        st.markdown("### 💕 Love Score Results 💕")
        st.markdown(f"<h2 style='color: #FF69B4;'>Love Score for {name1} and {name2}: {final_score}%</h2>", unsafe_allow_html=True)
        
        st.success(f"AI Analysis: Your names and relationship description give a compatibility score of {ai_score}%")
        st.info(f"Machine Learning Prediction: Based on your preferences, compatibility is {ml_score}%")
        st.warning(f"🦸 Your couple superpower is **{random.choice(['telepathic communication', 'finishing each other’s sentences', 'unbeatable dance duo'])}**.")

if __name__ == "__main__":
    main()
