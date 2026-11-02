import os
from pypdf import PdfReader

reader = PdfReader("File_handeling_pdf/SQL.pdf")

print("PDF loaded successfully!")
x=len(reader.pages)

'''for i, page in enumerate(reader.pages,start=1):
  text=page.extract_text()

  if "DDL" in text:
    print("Found at: ",i)'''
  
lst=os.listdir("File_handeling_pdf/Documents")
print(lst)


pdf_dir = "File_handeling_pdf/Documents"

for filename in os.listdir(pdf_dir):

    if filename.lower().endswith(".pdf"):

        pdf_path = os.path.join(pdf_dir, filename)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        print("\nPDF NAME:", filename)
        print(text)