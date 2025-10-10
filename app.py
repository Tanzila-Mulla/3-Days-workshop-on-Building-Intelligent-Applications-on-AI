import streamlit as st
from difflib import get_close_matches

# -------------------------------
# 🧠 Knowledge Base by Branch
# -------------------------------
knowledge_base = {
    "Computer Science Engineering": {
        "What is CSE?": "CSE stands for Computer Science Engineering. It focuses on computer systems, programming, algorithms, and software development.",
        "What is a stack?": "A stack is a linear data structure that follows the Last In First Out (LIFO) principle.",
        "What is a compiler?": "A compiler translates source code into machine code."
    },
    "Artificial Intelligence & Machine Learning": {
        "What is AI?": "Artificial Intelligence enables machines to mimic human intelligence, including learning and decision-making.",
        "What is machine learning?": "Machine learning is a subset of AI that allows systems to learn from data and improve over time.",
        "What is deep learning?": "Deep learning uses neural networks with many layers to model complex patterns in data."
    },
    "Data Science": {
        "What is data science?": "Data science involves extracting insights from data using statistics, programming, and domain knowledge.",
        "What is feature engineering?": "Feature engineering creates input variables that improve model performance.",
        "What is data cleaning?": "Data cleaning involves correcting or removing inaccurate records from a dataset."
    },
    "Information Science": {
        "What is information science?": "Information science studies how information is collected, stored, retrieved, and used.",
        "What is metadata?": "Metadata is data that describes other data, such as author, date, and format.",
        "What is data governance?": "Data governance manages data availability, usability, integrity, and security."
    }
}

# -------------------------------
# 🔍 Match Function
# -------------------------------
def find_answer(user_question, branch):
    qa_dict = knowledge_base.get(branch, {})
    matches = get_close_matches(user_question, qa_dict.keys(), n=1, cutoff=0.5)
    if matches:
        return qa_dict[matches[0]]
    else:
        return "🤖 Sorry, I don't know the answer to that yet. Try rephrasing or ask another question!"

# -------------------------------
# 🌐 Streamlit Frontend
# -------------------------------
st.set_page_config(page_title="Tech Branch Chatbot", layout="wide")
st.title("💬 Tech Branch Chatbot")
st.markdown("Explore topics in **Computer Science Engineering**, **AI/ML**, **Data Science**, and **Information Science**. Ask questions and get instant answers!")

# Sidebar for branch selection
branch = st.sidebar.selectbox("Choose a Branch", list(knowledge_base.keys()))
st.sidebar.markdown("📘 Selected branch: **{}**".format(branch))

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("Ask a question about {}:".format(branch), placeholder="e.g., What is AI?")
if user_input:
    answer = find_answer(user_input, branch)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", answer))

# Display chat history
st.subheader("🗨️ Chat History")
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"🧑 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")

# Branch overview
st.subheader("📚 Branch Overview")
if branch == "Computer Science Engineering":
    st.markdown("""
    **CSE** covers programming, algorithms, operating systems, databases, and software engineering. It's the foundation of modern computing.
    - 🔹 Topics: Data Structures, OS, DBMS, Networks
    - 🔹 Careers: Software Developer, Systems Engineer, QA Analyst
    """)
elif branch == "Artificial Intelligence & Machine Learning":
    st.markdown("""
    **AI/ML** focuses on building intelligent systems that learn and adapt.
    - 🔹 Topics: Neural Networks, NLP, Computer Vision
    - 🔹 Careers: AI Engineer, ML Scientist, Robotics Developer
    """)
elif branch == "Data Science":
    st.markdown("""
    **Data Science** extracts insights from data using analytics and modeling.
    - 🔹 Topics: Statistics, Data Visualization, Predictive Modeling
    - 🔹 Careers: Data Scientist, Data Analyst, BI Developer
    """)
elif branch == "Information Science":
    st.markdown("""
    **Information Science** deals with organizing and managing data and knowledge.
    - 🔹 Topics: Metadata, Information Retrieval, Data Governance
    - 🔹 Careers: Information Architect, Librarian, Data Steward
    """)
