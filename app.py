import streamlit as st
from ai_engine import generate_interview_questions
from resume_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Interview Coach")

st.title("🤖 AI Interview Question Generator")

# ✅ Resume Upload
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

# ✅ Job Role Input
job_role = st.text_input("Enter Job Role")

# ✅ Button
if st.button("Generate Questions"):

    if uploaded_file and job_role:

        # Extract resume text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Generate AI Questions
        result = generate_interview_questions(
            resume_text,
            job_role
        )

        st.write(result)

    else:
        st.warning("Please upload resume and enter job role")