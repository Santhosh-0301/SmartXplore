import streamlit as st
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import re

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="SmartXplore - Research Paper Summarizer", page_icon="📄", layout="wide")

# ============================
# CUSTOM CSS
# ============================
st.markdown("""
    <style>
    body {
        background-color: #111827;
        color: #F3F4F6;
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #60A5FA;
        margin-bottom: 20px;
    }
    .upload-box, .summary-box {
        background: #1F2937;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }
    .summary-box h2 {
        color: #FBBF24;
        margin-bottom: 15px;
    }
    .summary-box h3 {
        color: #34D399;
        margin-top: 15px;
    }
    .success-box {
        background-color: #065F46;
        padding: 10px;
        border-radius: 10px;
        color: #D1FAE5;
        margin-bottom: 15px;
    }
    ul {
        padding-left: 25px;
    }
    li {
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================
# HEADER
# ============================
st.markdown('<div class="main-title">📘 SmartXplore - Research Paper Summarizer & Explorer</div>', unsafe_allow_html=True)

# ============================
# UPLOAD SECTION
# ============================
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
st.subheader("📤 Upload Your Research Paper (PDF)")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
st.markdown('</div>', unsafe_allow_html=True)

# ============================
# SUMMARIZATION LOGIC
# ============================
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    if text.strip() == "":
        st.error("❌ No text found in the PDF. Please upload a valid research paper.")
    else:
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.subheader("📝 Summary of the Research Paper")

        # Summarize using Sumy LSA
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, 12)

        summary_text = " ".join(str(sentence) for sentence in summary_sentences)

        # ✅ Split into sections based on keywords
        structured_sections = {
            "Principle": [],
            "Process": [],
            "Key Features": [],
            "Challenges": [],
            "Roadmap": [],
            "Other Points": []
        }

        # Assign sentences to relevant section
        for sentence in summary_sentences:
            s = str(sentence)
            if re.search(r"\bPrinciple\b", s, re.IGNORECASE):
                structured_sections["Principle"].append(s)
            elif re.search(r"\bProcess\b", s, re.IGNORECASE):
                structured_sections["Process"].append(s)
            elif re.search(r"\bFeature|Key Feature\b", s, re.IGNORECASE):
                structured_sections["Key Features"].append(s)
            elif re.search(r"\bChallenge\b", s, re.IGNORECASE):
                structured_sections["Challenges"].append(s)
            elif re.search(r"\bRoadmap|Plan|Day\b", s, re.IGNORECASE):
                structured_sections["Roadmap"].append(s)
            else:
                structured_sections["Other Points"].append(s)

        # Success message
        st.markdown('<div class="success-box">✅ Summary generated successfully!</div>', unsafe_allow_html=True)

        # Display in structured format
        st.markdown("## 📌 Key Highlights")
        for section, points in structured_sections.items():
            if points:
                st.markdown(f"### {section}")
                st.markdown("<ul>" + "".join([f"<li>{p}</li>" for p in points]) + "</ul>", unsafe_allow_html=True)

        # Download button
        download_text = "\n\n".join([f"{section}:\n" + "\n".join(points) for section, points in structured_sections.items() if points])
        st.download_button(
            label="⬇ Download Summary",
            data=download_text,
            file_name="smartxplore_summary.txt",
            mime="text/plain"
        )

        st.markdown('</div>', unsafe_allow_html=True)
