import pytesseract
from PIL import Image
import fitz
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\e.quiatol\Tesseract-OCR\tesseract.exe'

def extractScannedPDF(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        print(f"Le PDF '{os.path.basename(pdf_path)}' contient {num_pages} pages.")

        for page_num in range(num_pages):
            print(f"Traitement de la page {page_num + 1}/{num_pages}...")
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            try:
                page_text = pytesseract.image_to_string(img, lang='fra')
                if page_text.strip():
                    print(f"  -> Texte extrait de la page {page_num + 1} (début) : '{page_text.strip()[:100]}...'")
                else:
                    print(f"  -> Aucun texte détecté sur la page {page_num + 1}.")

                text += page_text + "\n--- Fin de la page " + str(page_num + 1) + " ---\n\n"
            except Exception as page_e:
                print(f"  -> Erreur lors de l'extraction OCR de la page {page_num + 1} : {page_e}")
                text += f"\n--- Erreur sur la page {page_num + 1} : {page_e} ---\n\n"
        doc.close()
        return text
    except Exception as e:
        print(f"Une erreur générale est survenue lors de l'ouverture ou du traitement du PDF : {e}")
        return None

pdf_file = "../data/pdf/del_2025_124.pdf"
output_file = "../data/ExtractedText/del_2025_124.txt"

extracted_content = extractScannedPDF(pdf_file)

if extracted_content:
    print("\n--- Processus d'extraction terminé ---")
    print(f"Le texte complet a été enregistré dans '{output_file}'.")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_content)
else:
    print("\nImpossible d'extraire le texte du PDF.")