import os
from server import *

def readFile(path):
    file=open(path, "r")
    content=file.read()
    file.close()
    return content

def writeFile(path,content):
    file=open(path,"w")
    file.write(content)
    file.close()

#runs programs from scripts
def runFile(path):
    os.system(path)

def object(pasos):
    publish(3,pasos)

def move(pasos):
    return (pasos)

def vibration(n):
    return (n)

def inclination(n):
    return (n)

def temperature(n):
    return (n)

def brightnes(n):
    return (n)

def sound(n):
    return (n)

def inc(var, valor):
    var=var+valor
    return var

def dec(var, valor):
    var=var-valor
    return var
