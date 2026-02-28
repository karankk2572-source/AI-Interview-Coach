import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_interview_questions(resume, role):

    prompt = f"""
    Analyze this resume:

    {resume}

    Job Role: {role}

    Generate:
    1. Technical Interview Questions
    2. HR Questions
    3. Missing Skills
    4. Preparation Tips
    """

    response = model.generate_content(prompt)

    return response.text