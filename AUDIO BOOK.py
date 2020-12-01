# her the pyttsx3 is modulo for the speech reader
import pyttsx3
# pypdf2 is to read the pdf file which we are given in the code 
import PyPDF2

book = open('oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
# here this will shows the how many numbers of pages in the given pdf file
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(10)
text = page.extractText()
#her this will gives the output by using this to speech
speaker.say(text)
speaker.runAndWait()
