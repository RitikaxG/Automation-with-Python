# pip install py3-tts
# pip install PyPDF2
import pyttsx3
import PyPDF2
import os

book = open('Federated_Learning.pdf','rb')

filename = f"audiobook_{os.path.splitext(book.name)[0]}.mp3"  
# Read the book
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
# Initializing
speaker = pyttsx3.init('nsss')

for num in range(0,pages):
    page = pdfReader.pages[num]
    #Extract text from the page
    text = page.extract_text()

    speaker.save_to_file(text,filename)
    speaker.runAndWait()