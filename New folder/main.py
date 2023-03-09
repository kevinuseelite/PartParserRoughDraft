import PyPDF2
from PyPDF2 import PdfReader, PdfFileReader
import re, csv
from csv import DictWriter
import pandas as pd
import tabula
import openpyxl #pip install xlwt
from openpyxl import load_workbook
from tabula.io import read_pdf
#files to be working with in order to edit the columns 
import variable as v
import editor as e
from editor import excel_edit
from mergedeep import merge

#opens up the pdf file in order to use the parser 
def pdf_opener():
    reader = PdfReader(v.pdf_path)
    try:
        with open(v.file1, 'w') as f:
            for i in range(len(reader.pages)):
                pageobj = reader.pages[i]
                
                try:
                    text = pageobj.extract_text()
                except:
                    pass
                else:
                    f.write("Page {0}\n".format(i + 1))
                    f.write(''.center(100, '-'))
                    for x in text:
                       f.write((x[0].replace('\u274f', '\n*') + x[1:] ))
#this part is the loader for the second part of the parser
        load = open(v.parser, 'w+')
        try:
            for line in open(v.file1, 'r'):
                if '*' in line[0]:
                    load.write(line.replace('*', ''))
                    
        except OSError as err:
                print("OSError:", err)
                                                  
        f.close()
        load.close()
        
    except OSError as err:
        print("OSError:", err)

def text_parser():
    try:
        x = open(v.parser, 'r')
        lines = x.readlines()
        for int in lines:
            v.data.append(int.replace('\n', ''))
            
        x.close()
    except OSError as err:
        print("OSError: ", err)
    for int in range(len(v.data)):
        v.data[int] = v.data[int].replace(' ', '')


def pdf_to_excel():
    try:
        data = tabula.read_pdf(v.pdf_path, encoding='utf-8', pages='2', stream = True)
        df = data[0]
        v.first_ext = df.astype('str').to_dict()
        basic_edit()
        df2 = pd.DataFrame.from_dict(v.first_ext)
        newfile = df2.to_csv(v.raw_output)
    except OSError as err:
         print("OSError:", err)
         
    
def basic_edit():
    for x in v.first_ext:
        for y in v.first_ext[x]:
            #REMOVING TRAILING SPACES
            v.first_ext[x][y] = v.first_ext[x][y].replace('*', '')
            v.first_ext[x][y] = v.first_ext[x][y].replace('\u274f', '') 
            v.first_ext[x][y] = v.first_ext[x][y].replace('nan',  '')
            e.space_check(x,y)
   
    e.excel_edit()
    e.cleaner()


 
if __name__ == '__main__':
    pdf_opener()
    text_parser()
    pdf_to_excel()
       

    
        



