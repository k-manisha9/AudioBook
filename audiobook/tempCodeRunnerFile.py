import PyPDF2

book=open('audioBook\\JavaNotesForProfessionals.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)

speaker=pyttsx3.init()
for num in range(28,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWa