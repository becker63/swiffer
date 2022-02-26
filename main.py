import subprocess
import re
import webcolors


run = "sudo ampy --port /dev/ttyACM0 run sensor.py"

x = subprocess.check_output(run, shell=True)
print(x)
s = x[-17:]

g = re.search(r'\((.*?)\)',str(s)).group(1)
y = g.replace(" ","")
a,b,c = y.split(",")
print(a)

from colour import Color
a = Color(rgb=(int(a), int(b), int(c)) )
print(a)