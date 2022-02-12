
import os;
from urllib.request import urlopen
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
    
