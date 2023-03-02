import pyttsx3
import PyPDF2


pdf_reader = PyPDF2.PdfReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()


for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[0].extract_text()
    clean_text = text.strip()
    final_text = clean_text.replace('\n', ' ')

speaker.save_to_file(final_text, 'book.mp3')
speaker.runAndWait()

speaker.stop()
