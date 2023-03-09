import PyPDF2
from PyPDF2 import PdfReader, PdfFileReader, PdfFileWriter
import re, csv
from csv import DictWriter
import pandas as pd
import tabula
import openpyxl #pip install xlwt
from openpyxl import load_workbook
from tabula.io import read_pdf

#files to be working with in order to edit the columns 
from mergedeep import merge
import check as c
import variable as v
import dict_parse as e
from dict_parse import first
import camelot as cam
import pymysql
import warnings

db_creds = ''

with open('creds.txt', 'r') as infile:
    db_creds = [line for line in infile]
           
with open('creds.txt', 'r') as infile:
    db_creds = [line.rstrip() for line in infile]


with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    

db = pymysql.connect(
    host =      'partnumbers.cz7haxuvz9yz.us-west-2.rds.amazonaws.com',
    user =      'partusername',
    password =  'part123part123',
    port=       3306,

    )
cur = db.cursor()
cur.execute('USE partnumbers')



#opens up the pdf file in order to use the parser 
def pdf_opener():
    reader = PdfReader(v.pdf_path)
    try:
        with open(v.file1, 'wb') as f:
            for i in range(len(reader.pages)):
                pageobj = reader.pages[i]
                
                try:
                    text = pageobj.extract_text()
                except:
                    pass
                else:
                    f.write("Page {0}\n".format(i + 1))
                    f.write(''.center(100, '-'))
                    f.write(text)
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



def pdf_opener():
    pdf = PdfFileWriter(v.pdf_path)
    with open(v.file1, 'w') as f:
        for int in range(len(pdf.pages)):
            print('---------working---------')
            pageobj = pdf.getPage(int)
            
            try:
                text = pageobj.extract_text()
            except:
                pass
            else:
                f.write(text)
        f.close()
def pdf_to_excel():
    try:
        data = tabula.read_pdf(v.pdf_path, pages = '2')
        df = data[0]
        print(df)
        v.first_ext = df.astype('str').to_dict()

        basic_edit()
        df2 = pd.DataFrame.from_dict(v.first_ext)
        newfile = df2.to_excel(v.raw_output, index = False)
    except OSError as err:
         print("OSError:", err)         
    
def basic_edit():
    for x in v.first_ext:
        for y in v.first_ext[x]:
            #REMOVING TRAILING SPACES
            v.first_ext[x][y] = v.first_ext[x][y].replace('*', chr(32))
            v.first_ext[x][y] = v.first_ext[x][y].replace('\u274f',  chr(32)) 
            v.first_ext[x][y] = v.first_ext[x][y].replace('nan',  chr(32))
            e.space_check(x,y)
    e.cleaner()
    e.first()
 
if __name__ == '__main__':
    pdf_opener()
    pdf_to_excel()
    c.open_to_edit()