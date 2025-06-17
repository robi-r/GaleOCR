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
