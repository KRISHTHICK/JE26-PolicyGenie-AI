import streamlit as st
from rag_engine import ask_policy_question
from advisor_agent import get_custom_advice
import os

st.set_page_config(page_title="PolicyGenie AI", layout="wide")
st.title("🧾 PolicyGenie AI – Smart Insurance Explainer & Advisor")

uploaded = st.file_uploader("📤 Upload Insurance Policy PDF", type=["pdf"])
if uploaded:
    file_path = os.path.join("uploads", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.read())
    st.success("✅ Policy uploaded successfully.")

    st.divider()
    st.subheader("📚 Ask About This Policy")
    q1 = st.text_input("Example: What is the maturity benefit?")
    if q1:
        answer = ask_policy_question(q1, file_path)
        st.markdown(answer)

    st.divider()
    st.subheader("🤖 Get Personalized Insurance Advice")
    prompt = st.text_input("Example: I’m 30 with a family, suggest a life cover.")
    if prompt:
        reply = get_custom_advice(prompt)
        st.markdown(reply)
