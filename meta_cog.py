
import streamlit as st

st.set_page_config(page_title="MindTree Library", layout="wide")

st.title("📚 MindTree Knowledge Library")

tabs = st.tabs([
    "Psychology",
    "Spirituality",
    "Philosophy",
    "Models"
])

# -------------------------
# Psychology
# -------------------------
with tabs[0]:

    st.header("CBT Resources")

    st.link_button(
        "CBT Thought Record",
        "https://drive.google.com/drive/folders/1edl6N84R8J5xwlqLi2Ai_YJ6IshWdyZO"
    )

    st.link_button(
        "Emotional Map Worksheet",
        "https://drive.google.com/drive/folders/1edl6N84R8J5xwlqLi2Ai_YJ6IshWdyZO"
    )

# -------------------------
# Spirituality
# -------------------------
with tabs[1]:

    st.header("Spiritual Framework")

    st.link_button(
        "99 Names Reflection Guide",
        "https://drive.google.com/drive/folders/1edl6N84R8J5xwlqLi2Ai_YJ6IshWdyZO"
    )

    st.link_button(
        "Faith and Emotional Regulation",
        "https://drive.google.com/drive/folders/1edl6N84R8J5xwlqLi2Ai_YJ6IshWdyZO"
    )

# -------------------------
# Philosophy
# -------------------------
with tabs[2]:

    st.header("Philosophy Notes")

    st.link_button(
        "Meaning and Consciousness",
        "https://docs.google.com/document/d/your_doc_link"
    )

# -------------------------
# Models
# -------------------------
with tabs[3]:

    st.header("Personal Models")

    st.link_button(
        "Attractor Model of Emotions",
        "https://docs.google.com/document/d/your_doc_link"
    )

    st.link_button(
        "Unified Spiritual Psychology Framework",
        "https://docs.google.com/document/d/your_doc_link"
    )