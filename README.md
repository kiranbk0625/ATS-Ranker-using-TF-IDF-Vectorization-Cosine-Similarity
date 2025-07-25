# 🧠 ATS Resume Ranker (Streamlit App)

![Streamlit](https://img.shields.io/badge/Streamlit-ML%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Complete-brightgreen)

This is a smart, AI-powered Resume Ranking System that simulates an **Applicant Tracking System (ATS)**. It allows recruiters or hiring teams to **upload multiple resumes** and **paste a job description**, and then **ranks resumes** based on similarity using **TF-IDF + Cosine Similarity**.

Built with 🧠 `scikit-learn` and ⚡️ `Streamlit` for interactive UI.

---

## 🎥 Demo

> 📌 Run locally:

```bash
streamlit run app.py

🚀 Features
📤 Upload multiple PDF resumes at once

📋 Paste any job description directly in the app

🧠 NLP-based similarity scoring

📊 Resume match ranking table

📥 Download ranked results as CSV

🎨 Clean light-theme UI with .streamlit/config.toml

🧠 How It Works
Extracts text from uploaded PDFs

Vectorizes resumes + JD using TF-IDF

Computes Cosine Similarity

Ranks resumes based on match % to JD

🛠 Tech Stack
Tool	Purpose
Python	Core language
Streamlit	Web app framework
scikit-learn	TF-IDF + similarity calculation
pandas	Data handling
PyMuPDF (fitz)	PDF parsing

🗂 Folder Structure
graphql
Copy
Edit
ats-ranker/
├── app.py                 # Main Streamlit UI
├── utils.py               # PDF text extraction logic
├── .streamlit/
│   └── config.toml        # Light theme settings
├── requirements.txt       # All dependencies
└── README.md              # This file
📦 Setup & Installation
bash
Copy
Edit
git clone https://github.com/your-username/ats-resume-ranker.git
cd ats-resume-ranker

# Create a virtual environment (optional)
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
✅ Requirements
nginx
Copy
Edit
streamlit
scikit-learn
pandas
PyMuPDF
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📄 License
This project is licensed under the MIT License.

✨ Author
🔗 Kiran

⚠️ For educational and demonstration purposes only. This is a simplified simulation of ATS logic used in real-world recruitment pipelines.
