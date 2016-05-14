from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(10, 10, 'Hello, python!', textAncho = 'midle')
d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')
