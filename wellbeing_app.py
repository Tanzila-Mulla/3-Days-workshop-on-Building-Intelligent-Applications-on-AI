import streamlit as st
import datetime
import random
import pandas as pd
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container




# --- Data Storage (in-memory for demo) ---
if 'mood_entries' not in st.session_state:
    st.session_state['mood_entries'] = []
if 'pet_state' not in st.session_state:
    st.session_state['pet_state'] = 'Content'
if 'profile' not in st.session_state:
    st.session_state['profile'] = {"name": "Guest", "theme": "Light"}
if 'quote' not in st.session_state:
    st.session_state['quote'] = ""

MOODS = [
    {"emoji": "😊", "label": "Happy", "suggestion": "Keep spreading positivity! Try sharing your joy with a friend."},
    {"emoji": "😢", "label": "Sad", "suggestion": "It's okay to feel sad. Consider journaling or talking to someone you trust."},
    {"emoji": "😠", "label": "Angry", "suggestion": "Take a deep breath. Try a calming exercise or a short walk."},
    {"emoji": "😨", "label": "Anxious", "suggestion": "Try a breathing exercise or mindfulness meditation."},
    {"emoji": "😌", "label": "Calm", "suggestion": "Enjoy your calmness! Maybe help someone else find peace today."},
    {"emoji": "😐", "label": "Neutral", "suggestion": "A neutral day is a blank canvas. Try something new!"},
    {"emoji": "🤩", "label": "Excited", "suggestion": "Channel your excitement into a creative project!"},
    {"emoji": "🥱", "label": "Tired", "suggestion": "Rest is important. Try a short nap or some gentle stretching."}
]
PET_STATES = ["Content", "Playful", "Sleepy", "Hungry", "Excited", "Curious", "Relaxed"]
EXERCISES = [
    "Gratitude journaling: Write 3 things you're grateful for.",
    "Breathing exercise: Inhale for 4, hold for 4, exhale for 4, repeat 5 times.",
    "Mindfulness: Spend 2 minutes focusing on your breath.",
    "Positive affirmation: Say something kind to yourself!",
    "Go for a short walk and notice your surroundings.",
    "Listen to your favorite song and relax.",
    "Draw or doodle something that represents your mood.",
    "Try a 5-minute guided meditation on YouTube."
]
QUOTES = [
    "You are stronger than you think.",
    "Every day is a fresh start.",
    "Your feelings are valid.",
    "Small steps every day lead to big changes.",
    "Be gentle with yourself.",
    "Happiness is found in the little things."
]
MENTAL_HEALTH_RESOURCES = [
    ("Find a Therapist", "https://www.psychologytoday.com/us/therapists"),
    ("Mental Health America", "https://mhanational.org/"),
    ("Crisis Text Line", "https://www.crisistextline.org/")
]



# --- Custom Styles & Theme Switcher ---
theme = st.sidebar.selectbox("Theme", ["Light", "Dark", "Pastel"], index=["Light", "Dark", "Pastel"].index(st.session_state['profile']['theme']))
st.session_state['profile']['theme'] = theme
if theme == "Dark":
    st.markdown("""
        <style>
        .main {background: #232526; color: #f8f8f2;}
        .stButton>button {background: #232526; color: #f8f8f2;}
        </style>
    """, unsafe_allow_html=True)
elif theme == "Pastel":
    st.markdown("""
        <style>
        .main {background: linear-gradient(120deg, #fbc2eb 0%, #a6c1ee 100%);}
        .stButton>button {background: #fbc2eb; color: #232526;}
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main {background: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);}
        .stButton>button {background: #6a11cb; color: white;}
        </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Navigation ---
st.sidebar.title("🌈 Emotional Well-being App")
with st.sidebar.expander("👤 Profile", expanded=True):
    st.session_state['profile']['name'] = st.text_input("Your Name", st.session_state['profile']['name'])
    st.write(f"Welcome, {st.session_state['profile']['name']}!")
    if st.button("Show Inspirational Quote"):
        st.session_state['quote'] = random.choice(QUOTES)
    if st.session_state['quote']:
        st.info(f"💡 {st.session_state['quote']}")
page = st.sidebar.radio("Go to", [
    "🌤️ Mood Logging", "🐾 Virtual Companion", "🧘 Guided Exercises", "📅 Mood Calendar", "📊 Analytics Dashboard", "🩺 Mental Health Resources", "ℹ️ About"
])


# --- Mood Logging ---
if page.startswith("🌤️"):
    st.header("🌤️ Log Your Mood")
    mood_choice = st.selectbox(
        "How are you feeling?",
        [f"{m['emoji']} {m['label']}" for m in MOODS]
    )
    mood_idx = [f"{m['emoji']} {m['label']}" for m in MOODS].index(mood_choice)
    mood = MOODS[mood_idx]
    intensity = st.slider("Intensity", 1, 10, 5, help="How strong is this feeling?")
    tags = st.text_input("Tags (comma separated)", help="Add context, e.g., work, family, health")
    note = st.text_area("Add a note (optional)")
    if st.button("Log Mood"):
        entry = {
            "date": datetime.date.today(),
            "mood": mood['label'],
            "emoji": mood['emoji'],
            "intensity": intensity,
            "tags": tags,
            "note": note,
            "user": st.session_state['profile']['name']
        }
        st.session_state['mood_entries'].append(entry)
        st.success(f"Mood logged! {mood['emoji']} {mood['label']}")
        st.info(mood['suggestion'])
        if mood['label'] == "Happy":
            rain(emoji="✨", font_size=32, falling_speed=5, animation_length="infinite")
        elif mood['label'] == "Sad":
            rain(emoji="💧", font_size=24, falling_speed=3, animation_length="short")
    st.subheader("Mood History")
    if st.session_state['mood_entries']:
        df = pd.DataFrame(st.session_state['mood_entries'])
        st.dataframe(df)
    else:
        st.info("No mood entries yet.")

# --- Virtual Companion ---
elif page.startswith("🐾"):
    st.header("🐾 Your Virtual Companion")
    pet_state = random.choice(PET_STATES)
    st.session_state['pet_state'] = pet_state
    st.image("https://cdn.pixabay.com/photo/2017/01/31/13/14/avatar-2026510_1280.png", width=150)
    st.write(f"Your pet is feeling: **{pet_state}**")
    if st.session_state['mood_entries']:
        last_mood = st.session_state['mood_entries'][-1]['mood']
        if "Happy" in last_mood:
            st.balloons()
            st.success("Your happiness makes your pet playful!")
        elif "Sad" in last_mood:
            st.warning("Your pet wants to cheer you up!")
        elif "Angry" in last_mood:
            st.info("Your pet suggests a calming walk together.")
        elif "Anxious" in last_mood:
            st.info("Your pet recommends a breathing exercise.")
        elif "Calm" in last_mood:
            st.info("Your pet is relaxed with you.")
        elif "Excited" in last_mood:
            st.info("Your pet is jumping with joy!")
        elif "Tired" in last_mood:
            st.info("Your pet suggests a nap together.")
    else:
        st.write("Log your mood to see your pet's reaction!")

# --- Guided Emotional Exercises ---
elif page.startswith("🧘"):
    st.header("🧘 Guided Emotional Exercises")
    exercise = random.choice(EXERCISES)
    st.write(f"**Today's exercise:** {exercise}")
    if st.button("Show another exercise"):
        st.experimental_rerun()
    st.markdown("---")
    st.write("Try to do at least one exercise daily for your well-being!")
    st.info("You can also add your own exercise ideas in the notes section of Mood Logging!")

# --- Mood Calendar ---
elif page.startswith("📅"):
    st.header("📅 Mood Calendar")
    if st.session_state['mood_entries']:
        df = pd.DataFrame(st.session_state['mood_entries'])
        df['date'] = pd.to_datetime(df['date'])
        calendar_data = df[['date', 'emoji', 'mood']].drop_duplicates()
        st.write("### Your moods by day:")
        for _, row in calendar_data.iterrows():
            st.markdown(f"- **{row['date'].date()}**: {row['emoji']} {row['mood']}")
        st.info("A full calendar visualization can be added in the future.")
    else:
        st.info("No mood data to show on the calendar yet.")

# --- Analytics Dashboard ---
elif page.startswith("📊"):
    st.header("📊 Mood Analytics Dashboard")
    if st.session_state['mood_entries']:
        df = pd.DataFrame(st.session_state['mood_entries'])
        st.subheader("Mood Trend Over Time")
        st.line_chart(df.set_index('date')[['intensity']])
        st.subheader("Mood Distribution")
        mood_counts = df.groupby(['emoji', 'mood']).size().reset_index(name='count')
        mood_counts['label'] = mood_counts['emoji'] + ' ' + mood_counts['mood']
        st.bar_chart(mood_counts.set_index('label')['count'])
        st.subheader("AI-Powered Insights")
        most_common = df['mood'].mode()[0]
        st.info(f"You most often feel: {most_common}")
        st.write("Tip: Try a gratitude exercise or mindfulness break today!")
        if most_common == "Happy":
            st.success("Keep up the positive vibes!")
        elif most_common == "Sad":
            st.warning("Consider reaching out to a friend or professional.")
        st.markdown("---")
        st.write("**Mood Intensity by Tag:**")
        if 'tags' in df.columns:
            tag_df = df.copy()
            tag_df['tags'] = tag_df['tags'].fillna('')
            tag_df = tag_df[tag_df['tags'] != '']
            if not tag_df.empty:
                tag_df = tag_df.assign(tag=tag_df['tags'].str.split(",")).explode('tag')
                tag_df['tag'] = tag_df['tag'].str.strip()
                st.bar_chart(tag_df.groupby('tag')['intensity'].mean())
    else:
        st.info("No mood data to analyze yet.")

# --- Mental Health Resources ---
elif page.startswith("🩺"):
    st.header("🩺 Professional Mental Health Resources")
    for name, url in MENTAL_HEALTH_RESOURCES:
        st.markdown(f"- [{name}]({url})")
    st.write("If you need urgent help, please reach out to a professional or a helpline in your country.")
    st.info("Remember: Seeking help is a sign of strength!")

# --- About ---
elif page.startswith("ℹ️"):
    st.header("ℹ️ About This App")
    st.write("""
    This Emotional Well-being App helps you track your mood, gain AI-powered insights, interact with a virtual companion, and access guided exercises and mental health resources. 
    
    Built with ❤️ using Streamlit.
    """)
    st.write("PRD-based features: AI analysis, gamified pet, guided exercises, analytics, and more.")
    st.write("For feedback or suggestions, contact the developer.")
    st.markdown("---")
    st.write("""
    **UI/UX Enhancements:**
    - Calming color palette
    - Emoji and animation
    - Mood-based suggestions
    - Easy navigation
    """)
