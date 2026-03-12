import pdfplumber
import pytesseract
from pdf2image import convert_from_path


def extract_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

            else:
                images = convert_from_path(file_path, first_page=page.page_number, last_page=page.page_number)

                for img in images:
                    ocr_text = pytesseract.image_to_string(img)
                    text += ocr_text + "\n"

    return text


if __name__ == "__main__":

    file_path = r"C:\Users\Divyamsh\OneDrive\Desktop\RAG-project\Divyamsh-resume.pdf"

    extracted_text = extract_text(file_path)

    print(extracted_text[:2000])