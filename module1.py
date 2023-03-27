from struct import pack
from tkinter import *
from tkinter import font
from turtle import colormode # vajalik teksti fondi muutmiseks
from PIL import ImageGrab
import io
from math import *
from random import *
from time import *
#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")

#x0=0
#y0=0
#x1=600
#y1=600
#a=300
#r=(a**2+a**2)**(1/2)
#p=(a-r)

#for i in range(12):  
#    x0+=p
#    y0+=p
#    x1-=p
#    y1-=p
#    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="red")
#    tahvel.create_oval(x0,y0,x1,y1, width=1, outline="blue", fill="yellow")
#    p=r-a
#    r=r-p
#    a=((r)*sqrt(2))/2
#tahvel.grid()


colors = ["black",
           "cyan",
           "magenta",
           "red",
           "blue",
           "gray",
           "yellow"
           "green",
           "lightblue",
           "pink",
           "gold"]
raam2 = Tk()
raam2.title("Ringid")
tahvel2 = Canvas(raam2, width=600, height=600, background="white")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):  
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))


tahvel2.grid()

raam2.mainloop()
