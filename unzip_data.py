import zipfile
import os

# Corrected path with exact filename
zip_path = r"C:\Users\HP\OneDrive\Desktop\Task_3_streamlit_app\Task 3 - GLR Pipeline-20250625T091124Z-1-001.zip"
extract_path = "task_3_data"

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("✅ Files successfully extracted to:", extract_path)
import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Insurance Report Generator", layout="centered")

st.title("📄 GLR Insurance Template Auto-Filler")
st.markdown("Upload your `.docx` template and one or more `.pdf` photo reports below.")

# Upload the template file
template_file = st.file_uploader("Upload Insurance Template (.docx)", type=["docx"])

# Upload multiple PDF reports
report_files = st.file_uploader("Upload Photo Reports (.pdf)", type=["pdf"], accept_multiple_files=True)

if template_file and report_files:
    st.success(f"✅ Template uploaded: {template_file.name}")
    st.info(f"📎 {len(report_files)} report(s) uploaded")

    # Extract and display text from all PDFs
    full_text = ""
    for file in report_files:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            full_text += page.extract_text() + "\n"

    st.subheader("📋 Extracted Text from PDF Reports")
    st.text_area("Text from all uploaded reports", full_text, height=300)

