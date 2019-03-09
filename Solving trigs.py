import numpy
import numpy as np
import math


def menu():
    rangeval = []
    option = str(input("Which trig function is you θ enclosed into (sin/cos/tan)???: "))
    value = float(input("Wut is the value of the product?"))
    st = int(input("wut's the value that you want to start the range of the solutions with"))
    fin = int(input("wut's the value that you want to end the range of the solutions with"))
    rangeval.append(st)
    rangeval.append(fin)
    if option == "sin":
        sine(value,rangeval)
        
    if option == "cos":
        cosine(value,rangeval)
        
    if option == "tan":
        tangent(value,rangeval)


def sine(val,rangeval):
    ans = []
    thet = np.arcsin(val)
    thet = np.rad2deg(thet)
    if thet >= min(rangeval) and thet <= max(rangeval):
        ans.append(thet)
        print(ans)
    #val = str(val)
    #if val[0] == "-":

def cosine(val):
    
    thet = np.arccos(val)
    thet = np.rad2deg(thet)
    if thet < 180:
        thet2 = 180-thet
        print(thet,thet2)
    #val = str(val)
    #if val[0] == "-":
        
def tangent(val):
    
    thet = np.arctan(val)
    thet = np.rad2deg(thet)
    if thet < 180:
        thet2 = 180-thet
        print(thet,thet2)
    #val = str(val)
    #if val[0] == "-":
        



menu()
