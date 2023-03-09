import main as m
import main 


#path and setup external files
pdf_path = 'hh6ic-led.pdf'
raw_output = "F:\\BackEnd\\file1.xlsx"
finished_product = 'F:\\BackEnd\\' + pdf_path[:-4] + '.xlsx'
xxiax = 'creds.txt'
db_creds = []

#variables in regard for the reading
first_ext = ''
dic_to_add = dict()
res = ''
size = 0

file1 = 'text.txt'
parser = 'parse.txt'

text = ''
part = ''
data = []

#PRESET VALUES WILL BE SET HERE
table = dict()
table["lumen"] = []
table["driver"] = []
table["voltage"] = []
table["cct"] = []
table["emg"] = []
table["trim"] = []
table["flange"] = []
table["cri"] = []
table["optic"] = []
   
cat = ['SERIES', 'LUMENS', 'VOLAGE', 'CCT', 'EMERGENCY', 
       'TRIM TYPE', 'REFLECTOR/FLANGE COLORS', 'OPTICS', 'CRI', 'OPTIONS', 'TRIMLESS' ]
Lumens = ('900L', '1200L', '1500L')
Volt = ('120', '277', 'MVOLT', '347')
CCT = ('22K', '27K', '30K', '35K', '40K', '50K')
driver = ('DIM10', 'DIMTR', 'LUTH', 'LUT2W', 'LUTFTB', 'ELDODALI-.1', 
          'ELDODMX-.1', 'ELDO10-.1')