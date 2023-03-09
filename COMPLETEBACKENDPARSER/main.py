import zipfile
import xml.etree.ElementTree as ET
from docx import Document
import asposecells 
import loading
import jpype
import aspose.pdf as ap

pdf_path = 'hh6ic-led.pdf'
output = pdf_path[:-4] + '.xlsx'

document = ap.Document(pdf_path)
save_option = ap.ExcelSaveOptions()
document.save(output, save_option)