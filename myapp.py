from math import log10
import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import keyboard as kb
from time import sleep as stop , time
from  os import system
from tkinter.messagebox import askokcancel,  WARNING


def hourmodify(*_):
    x = int(h.get())
    if x > 0 :
        h.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
    else :
        h.set("00")

def write(e):
    ele = e.widget
    #print(ele,dir(ele))

def minmodify(*_):
    x = int(m.get())
    if x > 0 :
        m.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
    else :
        m.set("00")

def secmodify(*_):
    x = int(s.get())
    #print(s.get())
    if x > 0 :
        s.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
    else :
        s.set("00")

def extract():
    x = 60*int(h.get())
    x = (int(m.get())+x)*60
    x += int(s.get())
    return x

def sleepfun():
    kb.press("left windows")
    kb.press("x")
    kb.release("left windows")
    kb.release("x")
    stop(0.5)
    kb.press("u")
    kb.release("u")
    kb.press("s")
    kb.release("s")


def shutfun():
    #system("shutdown /s")
    pass


def restartfun():
    #system("shutdown /s")
    pass


def warning():
    top = Toplevel()
    top.title('Warning')
    top.iconbitmap("warning.ico")
    seconds = 5
    box = Message(top, text="Your Computer is going to "+modename.getting()+" in "+str(seconds), padx=20, pady=20).pack()
    top.after(5000, top.destroy)
    end = time()+5
    while end-time()>0:
        seconds = int(end-time())
        box.configure(text="Your Computer is going to "+modename.getting()+" in "+str(seconds))
        #top.update()

def main():
    if modename.getting() != "" :
        seconds = extract()
        for el in timearea.winfo_children()[0::2]:
            el.destroy()

        for el in app.winfo_children()[2::2]:
            el.destroy()
        
        hour = Label(timearea,font=arfont,width=2,textvariable=h,background=yellow,border="0")
        hour.grid(row=0,column=2)

        min = Label(timearea,font=arfont,width=2,textvariable=m,background=yellow,border="0")
        min.grid(row=0,column=4)

        sec = Label(timearea,font=arfont,width=2,textvariable=s,background=yellow,border="0")
        sec.grid(row=0,column=6)

        end = time()+seconds

        while seconds > 0:
            #stop(0.8)
            seconds = int(end-time())
            print(seconds)
            
            x = seconds//3600
            print("hours:",x)

            if x != 0:
                h.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
            else:
                h.set("00")

            x = (seconds-(x*3600))//60

            if x != 0:
                m.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
            else:
                m.set("00")

            x = seconds%60
            print("seconds:",x)

            if x != 0:
                s.set(('0'*(2-int(log10(x)+1))+str(x))[0:2])
            else:
                s.set("00")

            app.update()

        
        seconds = 5
        #msg = askokcancel(title="Warning", message="Your Computer is going to "+modename.getting()+" in "+ str(seconds),icon=WARNING)
        warning()

        app.destroy()
        #print(msg)
        #while seconds > 1:
        #    stop(1)
        #    seconds -= 1
        #exec(modename.getting()+"fun()")
    
    
        
    


def on_enter(e):
    ele = e.widget
    ele["background"]="white"
    ele["foreground"]="black"

def on_leave(e):
    ele = e.widget
    ele["background"]=yellow
    ele["foreground"]="black"


def change(x):
    #exec(x+".configure(image="+x+"c)")
    #exec(x+"bc = 'black'")
    #exec("print("+x+"bc)")
    mode.configure(text=x.upper())
    modename.changing(x)


class moding:

    def __init__(self):
        self.__value = str()

    def changing(self,value):
        self.__value = value
    
    def getting(self):
        return self.__value


app = Tk()




modename = moding()

yellow = "#D6B731"
app.configure(bg=yellow)

shutbc = yellow
sleepbc = yellow
restartbc = yellow

#shutc = PhotoImage(file="shutclicked.png")
#restartc = PhotoImage(file="restartclicked.png")
#sleepc = PhotoImage(file="sleepclicked.png")

app.title("Countdown Sleep")
app.iconbitmap("logo.ico")
height = app.winfo_screenheight()
width = app.winfo_screenwidth()


xfont = font.Font(family='Qatar2022 Arabic Heavy',size=10)
arfont = font.Font(family='Qatar2022 Arabic Heavy',size=14)

app.geometry(str(int(width*(2/8)))+"x"+str(int(height*(7/9)))+"+"+str(3*(width//8))+"+"+str((height//9)-30))
app.minsize(int(width*(2/8)),int(height*(7/9)))
app.maxsize(int(width*(2/8)),int(height*(7/9)))


Label(app,text="Time:",background=yellow,font=arfont).pack(pady=(100,0))
ttk.Style(app).configure("TFrame",background=yellow)


h = StringVar(app)
h.set("00")
h.trace('w', hourmodify)

timearea = ttk.Frame(app,style="TFrame")
hour = Entry(timearea,font=arfont,width=2,textvariable=h,background=yellow,border="0")
hour.grid(row=0,column=2)
hour.bind("<1>",write)

Label(timearea,text=":",background=yellow).grid(row=0,column=3)

m = StringVar(app)
m.set("00")
m.trace('w', minmodify)

min = Entry(timearea,font=arfont,width=2,textvariable=m,background=yellow,border="0")
min.grid(row=0,column=4)
min.bind("<1>",write)

Label(timearea,text=":",background=yellow).grid(row=0,column=5)

s = StringVar(app)
s.set("00")
s.trace('w', secmodify)
sec = Entry(timearea,font=arfont,width=2,textvariable=s,background=yellow,border="0")
sec.grid(row=0,column=6)
sec.bind("<1>",write)

timearea.pack(padx=20,pady=(10))


icons = Frame(app)

mode = Label(app,text="",background=yellow,font=xfont)

shutphoto = PhotoImage(file="shut.png")
shut = Button(icons, image=shutphoto,background=shutbc,border="0",activebackground="black",command=lambda:change("shut"))

sleephoto = PhotoImage(file="sleep.png")
sleep = Button(icons, image=sleephoto,background=sleepbc,border="0",activebackground="black",command=lambda:change("sleep"))

restartphoto = PhotoImage(file="restart.png")
restart = Button(icons, image=restartphoto,background=restartbc,border="0",activebackground="black",command=lambda:change("restart"))

mode.pack(pady=(50,10))

shut.grid(row=3,column=1,padx=30)
restart.grid(row=3,column=2)
sleep.grid(row=3,column=3,padx=30)



icons.configure(background=yellow)
icons.pack(pady=(0,50))

sub = Button(app,text="SET",font=arfont,foreground="black",background=yellow,activebackground="black",activeforeground=yellow,width=10,relief="solid",command=main)

sub.pack(pady=20)


app.update()

for item in app.winfo_children():
    if "Frame" in str(type(item)):
        for subele in item.winfo_children():
            if not "label" in  str(subele):
                subele.bind("<Enter>",on_enter)
                subele.bind("<Leave>",on_leave)
    else :
        if not "label" in  str(item):
            item.bind("<Enter>",on_enter)
            item.bind("<Leave>",on_leave)




app.mainloop()