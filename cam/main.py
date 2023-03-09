import pandas as pd
#from camelot.io import read_pdf #pip install 'PyPDF2<3.0'
import sys, locale
import camelot
#temporary function declarations
import PyPDF2
import ghostscript
import tabula
from tabula.io import read_pdf
import pymysql
import warnings

coordinate = []

db = pymysql.connect(
    host =      'partnumbers.cz7haxuvz9yz.us-west-2.rds.amazonaws.com',
    user =      'partusername',
    password =  'part123part123',
    port=       3306,

    )
cur = db.cursor()
cur.execute('USE partnumbers')




def read_camelot():
    coordinate = []
    try:
        with warnings.catch_warnings():
            warnings.simplefilter(action='ignore', category=FutureWarning)
        
            table = camelot.read_pdf('F:\cam\hh5-led.pdf', flavor = 'lattice', pages = '7' )
            tables = table[0].df
            #first_dict = tables.astype('str').to_dict()
        newfile = tables.to_excel('answer.xlsx', sheet_name = 'sheet2')
    except PermissionError as err:
        print('not working due to CSV file open')

if __name__ == '__main__':
    read_camelot()
    
    