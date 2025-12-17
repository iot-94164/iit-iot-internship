import math

radius = float(input("Enter radius: "))

area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

print("Area of circle:", area)
print("Circumference of circle:", circumference)

num=int(input("enter a number: "))

sin=math.sin(math.pi/2)   # 1.0
cos=math.cos(0)
radian=math.radians(90)
log=math.log(num) 
factorial=math.factorial(num)   # 120
gcd=math.gcd(num)    # 12
lcm=math.lcm(num) 

print(sin)
print(cos)
print(radian)
print(log)
print(factorial)
print(gcd)
print(lcm)

import os

#import shutil
folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")
else:
    os.rmdir(folder)
    print("Folder deleted")

