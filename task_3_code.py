import streamlit as st
import requests
import json
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO

# Set page config
st.set_page_config(page_title="Insurance Report Generator", layout="centered")
st.title("📄 GLR Insurance Template Auto-Filler")
st.markdown("Upload a `.docx` template and `.pdf` photo reports. The LLM will auto-fill your insurance document.")

# Upload the template
template_file = st.file_uploader("Upload Insurance Template (.docx)", type=["docx"])

# Upload PDF photo reports
pdf_files = st.file_uploader("Upload Photo Report PDFs", type=["pdf"], accept_multiple_files=True)

if template_file and pdf_files:
    st.success("✅ Files uploaded successfully.")
    
    # Extract text from PDFs
    all_text = ""
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                all_text += content + "\n"

    st.subheader("📋 Extracted PDF Text")
    st.text_area("Text extracted from reports:", all_text.strip(), height=250)

    if st.button("🚀 Generate Filled Template using LLM"):
        with st.spinner("Contacting OpenRouter and generating response..."):
            # Define OpenRouter prompt
            prompt = f"""
You are a document assistant helping populate an insurance claim form.
Extract key fields and values from this text and return them as a clean JSON object (no explanation):

Text:
{all_text}
"""

            headers = {
                "Authorization": "Bearer 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",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "mistralai/mixtral-8x7b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            }

            try:
                res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

                if res.status_code == 200:
                    llm_response = res.json()['choices'][0]['message']['content']
                    st.code(llm_response, language="json")

                    try:
                        fields = json.loads(llm_response)

                        doc = Document(BytesIO(template_file.read()))

                        for para in doc.paragraphs:
                            for key, val in fields.items():
                                if key in para.text:
                                    para.text = para.text.replace(key, val)

                        output = BytesIO()
                        doc.save(output)

                        st.success("✅ Filled document ready!")
                        st.download_button(
                            label="📥 Download Filled Template",
                            data=output.getvalue(),
                            file_name="filled_insurance_template.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    except json.JSONDecodeError:
                        st.error("⚠️ LLM response is not valid JSON.")
                else:
                    st.error(f"❌ LLM call failed with status code {res.status_code}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
