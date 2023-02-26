import os
import sys
from subprocess import Popen, PIPE, STDOUT
import re
from win32gui import GetWindowText, GetForegroundWindow
import win32com.client
from time import sleep

path = input(r"Enter the path of point cloud: ")
while(os.path.exists(path) == False):
    path = input("Path entered does not exists, please enter again: ")
f = open('path_file.txt', 'w')
f.write(path)
f.close()

shell = win32com.client.Dispatch("WScript.Shell")

p = Popen([sys.executable, '-u', 'pick_points.py'], stdout = PIPE, stderr = STDOUT, bufsize = 1)

with p.stdout:
    for line in iter(p.stdout.readline, b''):
        temp = str(line)
        if 'Picked point' in temp:            
            temp = re.findall(r"[-+]?(?:\d*\.*\d+)", temp)
            temp = [float(i) for i in temp]
            print("Point Selected: ", temp[1], "&", "Position: ", temp[2], ",", temp[3], ",", temp[4])
            pos = '#' + str(temp[2]) + ',' + str(temp[3]) + ',' + str(temp[4]) + '{Enter}'
            #shell.AppActivate('Test Digitizer - Floradig')#if you want to check keyboard digitiser remove this comment and comment line 22 to 32           
            flag = shell.AppActivate('Digitize Node - Floradig')
            if flag == True:
                shell.SendKeys(pos)
            else:
                shell.AppActivate('Hierarchy')
                shell.SendKeys(pos)
        else:
            print("This point was not sent, you can click again on the last point again:", temp)
p.wait()
