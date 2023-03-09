import PyPDF2
from PyPDF2 import PdfReader, PdfFileReader
import re
import variable as v

#opens up the pdf file in order to use the parser 
def pdf_opener():
    reader = PdfReader(v.path)
    try:
        with open(v.file1, 'w') as f:
            for i in range(len(reader.pages)):
                pageobj = reader.pages[i]
                
                try:
                    text = pageobj.extract_text()
                    print(' '.center(100, '-'))
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

  
def extrap():
#checking for lumens
    x=0
    while len(v.data) != x:
        if v.data[x] in v.Lumens:
            v.table['lumen'].append(v.data[x])
        if v.data[x] in v.CCT:
            v.table['cct'].append(v.data[x])
        if v.data[x] in v.Volt:
            v.table['voltage'].append(v.data[x])
        v.data.pop(x)
        
       
            
        
        
         
    
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
    extrap()

    

if __name__ == "__main__":
    pdf_opener()
    text_parser()
    print(v.data)
    print(v.table)

   
