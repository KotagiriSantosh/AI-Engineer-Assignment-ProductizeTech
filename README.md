# AI Engineer Assignment – ProductizeTech

This repository contains my submission for the AI Engineer (Full-Time) hiring assignment from **ProductizeTech**. It covers end-to-end implementation of three AI-focused tasks involving computer vision, image change detection, and a Streamlit-powered insurance report generation pipeline using LLMs.

---

## 🚀 Tasks Overview

### 🧠 Task 1 – RGB-Thermal Overlay Algorithm

- Aligned RGB and thermal images using perspective transformation
- Overlaid thermal data on top of RGB frames
- Saved annotated outputs with `_AT.JPG` suffix

📁 Folder: `task_1_submission/`

- `task_1_code.ipynb`
- `task_1_output/` – overlaid image outputs

---

### 🧠 Task 2 – Change Detection Algorithm

- Compared `before` and `after` images using pixel difference
- Detected and annotated changes using bounding boxes
- Saved results in the format `X~3.jpg`

📁 Folder: `task_2_submission/`

- `task_2_code.ipynb`
- `task_2_output/` – annotated image comparisons

---

### 🧠 Task 3 – Streamlit LLM Report Pipeline

- Built an interactive Streamlit app for generating insurance claim reports
- Uploads `.docx` template + `.pdf` photo reports
- Extracts text, sends to OpenRouter LLM, and fills template
- Outputs downloadable filled report

📁 Folder: `task_3_submission/`

- `task_3_code.py` – Streamlit app code
- `task_3_output/` – 3 generated `.docx` reports
- `task_3.mp4` – demo video of the app in action

---

## 🛠 Tech Stack

- Python (OpenCV, Streamlit, PyPDF2, python-docx)
- OpenRouter LLM (Mixtral 8x7B)
- Jupyter Notebook
- Git, GitHub

---

## 📁 Repository Structure

