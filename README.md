# JE26-PolicyGenie-AI
GEN AI

🧾💬 PolicyGenie AI – Insurance Policy Explainer & Custom Advisor
🔍 Overview
PolicyGenie AI is a smart insurance advisor powered by a Retrieval-Augmented Generation (RAG) pipeline and AI agents. Users can upload complex insurance documents (life, health, auto), and the system extracts key insights, answers questions, and suggests tailored plans—all offline using Ollama.

🌟 Key Features
Feature	Description
📄 Policy Upload & Parsing	Upload PDFs of insurance documents for analysis
🧠 AI Q&A Agent via RAG	Ask policy-related questions (e.g., "What is the claim limit?")
🤖 Custom Advisor Agent	Agent suggests best policies based on user goals and needs
📊 Risk & Coverage Summary	Summarize policy highlights like premium, term, exclusions
📝 Generate Personalized Summary	Auto-generate a summary PDF from extracted insights

# 🧾 PolicyGenie AI – Smart Insurance Explainer & Advisor

An AI-based tool to explain and summarize insurance documents using RAG + AI agents.

## 💡 Features
- Upload PDFs of policies
- Ask document-specific questions (RAG)
- Get insurance suggestions from an AI agent
- Summarize risks and premiums

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/PolicyGenie-AI.git
cd PolicyGenie-AI
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start Ollama:

bash
Copy
Edit
ollama serve
ollama pull tinyllama
Run the app:

bash
Copy
Edit
streamlit run app.py
