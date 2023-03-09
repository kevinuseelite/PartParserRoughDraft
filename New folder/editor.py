import main as m
import variable as v
import xlsxwriter
import pandas as pd
import variable as v
from mergedeep import merge

#THE PUPOSE OF THIS PART IS TO GET RID OF THE TRAILING TABLES AND ADD THEM TO THE 
#NEW ONES

def excel_edit():   
    counter = 0
    temp = ''
    lists = []
    for i in v.first_ext.keys():
        for j in v.first_ext[i].keys():
            
            
            #to find the vals such as optics and such
            if temp in v.cat and counter == len(v.first_ext["SERIES"])-1:
                add_value(temp, lists)
                temp =  ''
                lists.clear()
            elif temp in v.cat and counter <= len(v.first_ext["SERIES"]) -1 :
                lists.append(v.first_ext[i][j])
                v.first_ext[i][j] = ''
            elif v.first_ext[i][j] in v.cat:
                temp = v.first_ext[i][j]
                v.first_ext[i][j] = ''
                
            counter+=1
        counter = 0
    
    merge(v.first_ext, v.dic_to_add)
#takes in the old value and adds them to the dictionary
def add_value(temp, lists):    
    length = len(v.first_ext["SERIES"])
    for int in range(len(lists), length):
        lists.append('')   
    temp_dic = {temp: {}}
    
    
    for int in range(length):
        temp_dic[temp][int] = lists[int]
    x = sorted(lists, reverse = True)
    merge(v.dic_to_add, temp_dic )
    
    
'''
the point of this code is to take any fleeting characters from 
each of the respective categories, and make the necessary changes to them
'''

def option_check(x,y):
    head, sep, tail = v.first_ext[x][y].partition(' ')
    v.first_ext[x][y] = head
    
    '''some characters in this one might contain more than one space due to the way the partition
    functions on this particular check'''
def space_check(x, y):
    while v.first_ext[x][y].startswith(' ') == True:
        if v.first_ext[x][y] != '':
            temp = v.first_ext[x][y][1:]
            v.first_ext[x][y] = temp
        else:
            break
        
def driver_check(x,y):
    head, sep, tail = v.first_ext[x][y]. partition(' ')
    v.first_ext[x][y] = head
        
def trim_type(x, y):
    if '-' not in v.first_ext[x][y]:
        v.first_ext[x][y] = ''

def lumen_check(x, y):
    head, sep, tail = v.first_ext[x][y].partition('L')
    v.first_ext[x][y] = head + sep

def refl_check(x, y):
    if '-' not in v.first_ext[x][y]:
        v.first_ext[x][y] = ''

def volt_check(x, y):
    try:
        temp = int(v.first_ext[x][y])
    except:
        v.first_ext[x][y] = ''
        
def CRI_check(x,y):
    if v.first_ext[x][y].endswith("+") == False and v.first_ext[x][y]!='':
        head, sep, tail = v.first_ext[x][y].partition("+") 
        v.first_ext[x][y] = head + sep

def EMG_check(x, y):
    if v.first_ext[x][y].startswith("EMG") == False:
        v.first_ext[x][y] = ''


def cct_check(x, y):
    if v.first_ext[x][y].endswith("K") == False and v.first_ext[x][y]!='':
        head, sep, tail = v.first_ext[x][y].partition("K") 
        v.first_ext[x][y] = head + sep

def cleaner():
    for x in v.first_ext:
        for y in v.first_ext[x]: 
            #attempt to run every check for here
            if x.startswith('EM'):
                EMG_check(x, y)
            if x.startswith("CCT"):
                cct_check(x, y)
            if x.startswith("CRI"):
                CRI_check(x, y)
            if x.startswith("VOLT"):
                volt_check(x,y)
            if x.startswith("REF"):
                refl_check(x,y)
            if x.startswith("LUMENS"):
                lumen_check(x,y)
                    
            #trim and trimless use the same sub variables
            if x.startswith('TRIM'):
                trim_type(x,y)
                
            if x.startswith('DRIVER'):
                driver_check(x,y)
            
            if x.startswith('OPTION'):
                option_check(x,y)