# 📖 ManhwaOCR – Styled OCR for Korean Manhwa/Webtoons

**ManhwaOCR** is a lightweight, browser-based web app that uses Optical Character Recognition (OCR) to extract text from Korean manhwa or webtoons, classifies the text into types (dialogue, narration, inner thoughts), and formats them in a visually distinct style for better readability and translation context.

---

## 🚀 Features

- 🧠 **OCR-powered text extraction** using EasyOCR
- 🎭 **Manhwa-specific formatting**:
  - `""` → Dialogue
  - `//` → Narration
  - `()` → Inner thoughts
- 🎨 **Styled output** in distinct colors and formats
- 📷 Upload image and extract text in one click
- 🌐 Built with Flask (backend) + HTML/CSS (frontend)

---

## 🖼️ Example Output

```text
"" Who sent you?
// Seems he drank poison.
() So they’re still after me…

🛠️ Tech Stack
Backend: Python, Flask, EasyOCR, PyKoSpacing (optional)

Frontend: HTML, CSS, JavaScript

Deployment: Hugging Face Spaces

📦 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/ManhwaOCR.git
cd ManhwaOCR
pip install -r requirements.txt
python app.py
🌐 Usage
Open the web app in your browser (http://localhost:5000)

Upload a manhwa/webtoon image

Click Extract Text

View styled, classified output

📁 Project Structure
php
Copy
Edit
ManhwaOCR/
│
├── app.py               # Flask app
├── templates/
│   └── index.html       # UI layout
├── static/
│   └── styles.css       # Custom styling
├── utils.py             # Text classification and formatting
├── requirements.txt     # Dependencies
└── README.md
✅ TODO
 Add language translation support (Korean → English)

 Add multi-image upload

 Drag-and-drop interface

 GPU acceleration support

