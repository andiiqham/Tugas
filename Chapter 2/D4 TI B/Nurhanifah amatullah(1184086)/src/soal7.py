# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:32:35 2019

@author: Lenovo
"""

i=0
NPM = input("npm : ")
while i<1:
    if len(NPM)<7:
        print("npm kurang dari 7!")
        NPM = input("Npm : ")
    elif len(NPM)>7:
        print("npm lebih dari 7!")
        NPM = input("npm : ")
    else:
        i=1
        
a=NPM[0]
b=NPM[1]
c=NPM[2]
d=NPM[3]
e=NPM[4]
f=NPM[5]
g=NPM[6]

X=1

for this in a,b,c,d,e,f,g:
    X*=int(this)
print(X)