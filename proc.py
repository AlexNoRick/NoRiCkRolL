
import os;
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/AlexNoRick/NoRiCkRolL/main/CnctWeb/ver';
output = urlopen(url).read();
f = open("CnctWeb/ver", "r")
o = f.read())
if output == o:
from sys import platform
if platform == "linux" or platform == "linux2":
 os.startfile('linux_proc.py');
   #linux
elif platform == "darwin":
  os.startfile('mac_proc.py');
   #macos
elif platform == "win32":
  os.startfile("win_proc.py");
   #windows
else: 
 print("the NoRickRoll Has been update.");
    
