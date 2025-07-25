import os
import fitz  # PyMuPDF
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Job Description
def load_job_description(path="job_description.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

# Load and process resumes
def load_resumes(folder="resumes/"):
    resume_data = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            full_path = os.path.join(folder, filename)
            text = extract_text_from_pdf(full_path)
            resume_data.append({"filename": filename, "text": text})
    return resume_data

# Rank resumes based on cosine similarity
def rank_resumes(job_desc, resumes):
    documents = [job_desc] + [r["text"] for r in resumes]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Add score to each resume
    for i in range(len(resumes)):
        resumes[i]["score"] = round(similarity[i] * 100, 2)  # percentage

    # Sort by score descending
    ranked = sorted(resumes, key=lambda x: x["score"], reverse=True)
    return ranked

# Main function
def main():
    print("🔍 Loading Job Description...")
    job_desc = load_job_description()

    print("📄 Loading Resumes...")
    resumes = load_resumes()

    print(f"🧠 Ranking {len(resumes)} resumes against the job description...")
    ranked = rank_resumes(job_desc, resumes)

    df = pd.DataFrame(ranked)
    df = df[["filename", "score"]]
    print("\n📊 Top Matching Resumes:\n")
    print(df.head(10))

    df.to_csv("ranked_resumes.csv", index=False)
    print("\n✅ Ranking saved to 'ranked_resumes.csv'.")

if __name__ == "__main__":
    main()
