
from sys import platform
if platform == "linux" or platform == "linux2":
  execfile('linux_proc.py');
   #linux
elif platform == "darwin":
  execfile('mac_proc.py');
   #macos
elif platform == "win32":
  execfile('win_proc.py');
   #windows
    
