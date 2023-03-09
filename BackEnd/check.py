import variable as v 
import main as m
from openpyxl import workbook, worksheet, load_workbook
import openpyxl
import pandas as pd
import xlrd, xlwt, openpyxl, xlsxwriter
import csv
import pandas

def open_to_edit():
    #this part will open up the worksheet in order to conduct the 
    #necessary edits
    df = pd.read_excel(v.raw_output)
    
    
    df = df.apply(lambda x: pd.Series(x.dropna().values)).fillna('')
    temp = []
    
    for int in df:
        if int.startswith('Unnamed'):
            temp.append(int)   
            
    if len(temp) > 0:
        for int in range(len(temp)):
            df.drop(temp[int], inplace=True,axis=1)
    newfile = df.to_excel(v.finished_product)
    
    
#pdf_path = 'hh6ic-led.pdf'