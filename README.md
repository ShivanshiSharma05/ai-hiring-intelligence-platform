# 🚀 AI-Powered Hiring Intelligence Platform

An end-to-end AI system that automates resume screening, candidate ranking, and interview preparation using NLP and semantic similarity.

---

## 🧠 Overview

This project simulates a real-world recruiter workflow by analyzing resumes against a job description and generating actionable insights such as:

* Candidate ranking
* Skill gap analysis
* Resume improvement suggestions
* AI-generated interview questions

---

## ✨ Key Features

* 📄 Upload and analyze multiple resumes (PDF)
* 📊 Intelligent resume vs job description matching
* 🏆 Automated candidate ranking system
* ❌ Skill gap detection (only relevant technical keywords)
* 💡 Resume improvement suggestions
* 🎯 Context-aware interview question generation
* ⚡ Fast and interactive UI using Streamlit

---

## 🏗️ System Architecture

1. Resume Parsing → Extract text using pdfplumber
2. Skill Extraction → Identify technical skills via NLP (spaCy)
3. Matching Engine:

   * Keyword-based scoring
   * Semantic similarity using embeddings (sentence-transformers)
4. Ranking Engine → Sort candidates based on final score
5. Insight Generation:

   * Missing skills
   * Suggestions
   * Interview questions

---

## ⚙️ Tech Stack

Frontend: Streamlit
NLP: spaCy
Embeddings: Sentence Transformers
ML Backend: PyTorch
PDF Parsing: pdfplumber

---

## 🚀 Live Demo

(Add your deployed link here after deployment)

---

## 📦 Installation (Local Setup)

1. Clone Repository
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer

2. Create Virtual Environment
   python -m venv venv
   venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Download NLP Model
   python -m spacy download en_core_web_sm

5. Run Application
   streamlit run app.py

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Click New App
4. Select repository
5. Set main file: app.py
6. Deploy

---

## ⚠️ Important Notes

* First run may take time due to model download
* Ensure en_core_web_sm is installed
* Internet connection required for embedding model

---

## 📊 Example Output

* Ranked candidates based on relevance
* Accurate match scores (skill + semantic)
* Meaningful missing skills (no noise words)
* Context-based interview questions

---

## 🔮 Future Enhancements

* LLM-based question generation (OpenAI / Llama)
* Resume scoring dashboard for recruiters
* Candidate analytics & visualization
* Integration with ATS systems
* Cloud deployment with Docker

---

## 👩‍💻 Author

Shivanshi Sharma

---

## ⭐ If you found this useful

Give this repo a ⭐ and share your feedback!
