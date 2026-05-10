import pytesseract
from PIL import Image
from pypdf import PdfReader


def extract_resume_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_jd_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


if __name__ == "__main__":
    resume = extract_resume_text(r"C:\Users\asus\Downloads\Chayan_Banga_Resume (1).pdf")
    print("=== RESUME TEXT ===")
    print(resume[:])
    Job_description = extract_jd_text(r"C:\Users\asus\Downloads\WhatsApp Image 2026-05-10 at 12.42.44 PM.jpeg")
    print("\n\n\n")
    print(Job_description[:])
