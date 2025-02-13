import random
import streamlit as st

def zodiac_compatibility(sign1, sign2):
    compatibility_chart = {
        ("Aries", "Leo"): 90, ("Aries", "Sagittarius"): 85, ("Aries", "Cancer"): 50,
        ("Taurus", "Virgo"): 88, ("Taurus", "Capricorn"): 80, ("Taurus", "Gemini"): 45,
        # Add more combinations...
    }
    return compatibility_chart.get((sign1, sign2), random.randint(40, 90))

def mbti_match(type1, type2):
    perfect_matches = [("INTJ", "ENTP"), ("INFJ", "ENFP"), ("ISTP", "ESTJ")]
    if (type1, type2) in perfect_matches or (type2, type1) in perfect_matches:
        return 90
    return random.randint(40, 85)

def love_language_match(lang1, lang2):
    if lang1 == lang2:
        return 95
    return random.randint(50, 80)

def fantasy_match(role1, role2):
    good_matches = [("Knight", "Mage"), ("Rogue", "Healer"), ("Warrior", "Archer")]
    if (role1, role2) in good_matches or (role2, role1) in good_matches:
        return 90
    return random.randint(40, 85)

def love_story(name1, name2, score):
    if score > 85:
        return f"{name1} and {name2} were destined to be together, traveling the world in love!"
    elif score > 60:
        return f"{name1} and {name2} have a beautiful journey ahead, with ups and downs."
    else:
        return f"{name1} and {name2} have an interesting chemistry—opposites attract!"

def relationship_prediction():
    predictions = ["a cute pet", "a dreamy vacation", "matching tattoos", "a viral TikTok trend", "a surprise proposal"]
    return random.choice(predictions)

def couple_superpower():
    superpowers = ["telepathic communication", "finishing each other's sentences", "unbeatable dance duo", "cooking together like chefs"]
    return random.choice(superpowers)

def love_challenge(score):
    if score < 60:
        return "Send a cute meme to your crush!"
    return "Plan a surprise date idea!"

def main():
    st.title("AI Love Calculator 💖")
    
    name1 = st.text_input("Enter your name:")
    name2 = st.text_input("Enter your partner's name:")
    
    zodiac1 = st.selectbox("Select your zodiac sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac2 = st.selectbox("Select your partner's zodiac sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac_score = zodiac_compatibility(zodiac1, zodiac2)
    
    mbti1 = st.selectbox("Select your MBTI personality type:", ["INTJ", "ENTP", "INFJ", "ENFP", "ISTP", "ESTJ", "ISFP", "ESFJ"])
    mbti2 = st.selectbox("Select your partner's MBTI type:", ["INTJ", "ENTP", "INFJ", "ENFP", "ISTP", "ESTJ", "ISFP", "ESFJ"])
    mbti_score = mbti_match(mbti1, mbti2)
    
    love_lang1 = st.selectbox("Select your love language:", ["Words of Affirmation", "Acts of Service", "Receiving Gifts", "Quality Time", "Physical Touch"])
    love_lang2 = st.selectbox("Select your partner's love language:", ["Words of Affirmation", "Acts of Service", "Receiving Gifts", "Quality Time", "Physical Touch"])
    love_lang_score = love_language_match(love_lang1, love_lang2)
    
    fantasy1 = st.selectbox("Choose your fantasy role:", ["Knight", "Mage", "Rogue", "Healer", "Warrior", "Archer"])
    fantasy2 = st.selectbox("Choose your partner's fantasy role:", ["Knight", "Mage", "Rogue", "Healer", "Warrior", "Archer"])
    fantasy_score = fantasy_match(fantasy1, fantasy2)
    
    if st.button("Calculate Love Score 💘"):
        final_score = (zodiac_score + mbti_score + love_lang_score + fantasy_score) // 4
        
        st.subheader(f"Love Score for {name1} and {name2}: {final_score}%")
        st.write(love_story(name1, name2, final_score))
        st.write(f"In five years, you’ll have {relationship_prediction()} together.")
        st.write(f"Your couple superpower is {couple_superpower()}.")
        st.write(f"Love Challenge: {love_challenge(final_score)}")

if __name__ == "__main__":
    main()
