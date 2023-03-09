import main as m
import editor as e

#needed variables
pdf_path = 'hh4adj-ic-led.pdf'
raw_output = "F:\\New folder\\file.csv"
first_ext = ''
size = 0

dic_to_add = {}
file1 = 'text.txt'
parser = 'parse.txt'

text = ''
part = ''
data = []
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