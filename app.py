# app.py
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from utils import extract_text_from_pdf

# Page config
st.set_page_config(page_title="ATS Resume Ranker", layout="centered")
st.title("🧠 ATS Resume Ranker")
st.markdown("Upload resumes and paste a job description to see who's the best match.")

# Input: Job Description
job_desc = st.text_area("📋 Paste the Job Description Here:", height=250)

# Input: Resume Upload
uploaded_files = st.file_uploader("📤 Upload Resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

# Button click handler
if st.button("🔍 Rank Resumes", key="rank_btn"):
    if not job_desc:
        st.warning("❗ Please enter a job description.")
    elif not uploaded_files:
        st.warning("❗ Please upload at least one resume.")
    else:
        resume_data = []
        for uploaded_file in uploaded_files:
            text = extract_text_from_pdf(uploaded_file)
            resume_data.append({"filename": uploaded_file.name, "text": text})

        # TF-IDF vectorization
        docs = [job_desc] + [r["text"] for r in resume_data]
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(docs)
        similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        # Add score and display
        for i in range(len(resume_data)):
            resume_data[i]["score"] = round(similarity[i] * 100, 2)

        ranked = sorted(resume_data, key=lambda x: x["score"], reverse=True)
        df = pd.DataFrame(ranked)[["filename", "score"]]

        st.success("✅ Resumes ranked successfully!")
        st.dataframe(df)

        # Optional: download results
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results as CSV", csv, "ranked_resumes.csv", "text/csv")
