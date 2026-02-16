from pathlib import Path
import sys
from gtts import gTTS
from pypdf import PdfReader


def pdf_to_speech(pdf_path: str, output_path: str = "output.mp3", lang: str = "en"):
    pdf_file = Path(pdf_path)

    if not pdf_file.exists() or pdf_file.suffix.lower() != ".pdf":
        raise ValueError("Please provide a valid PDF file path.")

    reader = PdfReader(str(pdf_file))
    extracted_text = []

    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            extracted_text.append(text)
        else:
            print(f"[WARN] Page {i} has no extractable text.")

    full_text = "\n".join(extracted_text).strip()
    if not full_text:
        raise RuntimeError("No readable text found in the PDF.")

    tts = gTTS(text=full_text, lang=lang)
    tts.save(output_path)

    print(f"✅ Audio file generated: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Python app.py <path_to_pdf> [output.mp3]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.mp3"

    pdf_to_speech(pdf_path, output_path)
