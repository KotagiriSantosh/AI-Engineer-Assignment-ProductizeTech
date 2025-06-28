# AI Engineer Assignment – ProductizeTech

This repository contains my completed submission for the **AI Engineer (Full-Time)** hiring assignment from **ProductizeTech**. It consists of three tasks focused on computer vision, change detection, and intelligent document automation using Streamlit and LLMs.

---

## ✅ Overview of Tasks

### 🔹 Task 1 – RGB-Thermal Overlay Algorithm

- Applied homographic transformation to align RGB and thermal images using OpenCV.
- Warped and overlaid thermal images onto RGB frames.
- Final outputs are saved with `_AT.JPG` suffix.

📄 Notebook: `task_1_code.ipynb`  
🗂️ Output Folder: `task_1_output/` *(included in submitted Drive)*

---

### 🔹 Task 2 – Change Detection Algorithm

- Compared `before` and `after` image pairs using absolute pixel difference.
- Highlighted changed areas using bounding boxes.
- Saved annotated outputs as `X~3.jpg`.

📄 Notebook: `_task_2_code.ipynb`  
🗂️ Output Folder: `task_2_output/` *(included in submitted Drive)*

---

### 🔹 Task 3 – GLR Streamlit App with LLM Integration

- Built an interactive Streamlit application to automate insurance report generation.
- Features:
  - Upload `.docx` insurance templates
  - Upload `.pdf` photo reports
  - Extract text from PDF reports (`PyPDF2`)
  - Send extracted text to OpenRouter's Mixtral LLM
  - Receive structured key-value JSON from LLM
  - Fill and download the populated `.docx` file

📄 File: `task_3_code.py`  
📦 Input ZIP: `Task 3 - GLR Pipeline-20250625T091124Z-1-001.zip`  
📹 Demo: `task_3.mp4` *(included in submitted Drive)*

---

## 🛠 Tech Stack

- Python 3.x
- OpenCV
- Streamlit
- PyPDF2
- python-docx
- OpenRouter API (Mixtral-8x7B)
- Jupyter Notebook
- Git & GitHub

---

## ▶️ How to Run Task 3 (Streamlit App)

### 1. Install Dependencies

```bash
pip install streamlit python-docx PyPDF2 requests
