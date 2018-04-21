import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#set page reference (zero-based index)
pageObj = pdfReader.getPage(0)

#print page content
print(pageObj.extractText())
