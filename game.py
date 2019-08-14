import os
import sys
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Tic Tac Toe")
root.geometry("550x650+469+90")
root.resizable(width = False, height = False)
root.config(bg = "Dimgray")
#root.attributes("-alpha",-1)

img  =  ImageTk.PhotoImage(Image.open("C:/Users/navee/Documents/Code/Python/Programs/xoxo.jpg"))
l = Label(image = img,width = 549,height = 564).place(x = -3, y = 86)

op =  0
flag =  0
winflag  =  IntVar()

playerX = StringVar()
playerO = StringVar()

u = Frame(root)
u.grid(row = 1)
playerX_name = Label( u, text = "Player X:", font = 'Times 25 bold', bg = 'white', fg = 'black', height = 1, width = 10)
playerX_name.grid(row = 1, column = 2)
playerX_name =  Entry(u,textvariable = playerX,font = "Times 25")
playerX_name.grid(row = 1, column = 3)

v = Frame(root)
v.grid(row = 2)
playerO_name  =  Label( v, text = "Player O:", font = 'Times 25 bold', bg = 'white', fg = 'black', height = 1, width = 10)
playerO_name.grid(row = 2, column = 0)
playerO_name  =  Entry(v,textvariable = playerO,font = "Times 25")
playerO_name.grid(row = 2, column = 3)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def destroy():
    root.destroy()

def gameover(winflag):
    win = Toplevel()
    win.title("Game Over")
    win.geometry("260x260+614+339")
    win.resizable(width = False, height = False)
    #win.attributes("-toolwindow",1)
    global playerX, playerO, playerX_name, playerO_name

    playerX = playerX_name.get()
    playerO = playerO_name.get()

    if playerX == "":
        playerX = "Player X"
    if playerO == "":
        playerO = "Player O"

    if  winflag == 1:
        wLabel1 = Label(win, text = "%s Wins!"%playerX,font = 'Times 20 bold').place(x = 50, y = 80)
    elif winflag == 2:
        wLabel2 = Label(win, text = "%s Wins!"%playerO,font = 'Times 20 bold').place(x = 50, y = 80)
    elif winflag == 3:
        wLabel3 = Label(win, text = "It is a tie ¯\_(ツ)_/¯",font = 'Times 20 bold').place(x = 15, y = 80)   
    Button(win, text = "RESTART",font = 'Times 10 bold', command = restart_program,width = 12,height = 3).place(x = 80, y = 150)    
    Button(win, text = "QUIT",font = 'Times 10 bold',command = lambda:destroy(),width = 12,height = 3).place(x = 80, y = 200)
    Label(win, text = "Tic-Tac-Toe",font = 'Times 35 bold').place(x = 4, y = 5)

def disable():
    a.config(state = "disable")
    b.config(state = "disable")
    c.config(state = "disable")
    d.config(state = "disable")
    e.config(state = "disable")
    f.config(state = "disable")
    g.config(state = "disable")
    h.config(state = "disable")
    i.config(state = "disable")

def checkwin():
    if (a['text'] == 'X' and b['text'] == 'X' and c['text'] == 'X' or
        d['text'] == 'X' and e['text'] == 'X' and f['text'] == 'X' or
        g['text'] =='X' and h['text'] == 'X' and i['text'] == 'X' or
        a['text'] == 'X' and e['text'] == 'X' and i['text'] == 'X' or
        c['text'] == 'X' and e['text'] == 'X' and g['text'] == 'X' or
        a['text'] == 'X' and b['text'] == 'X' and c['text'] == 'X' or
        a['text'] == 'X' and d['text'] == 'X' and g['text'] == 'X' or
        b['text'] == 'X' and e['text'] == 'X' and h['text'] == 'X' or
        g['text'] == 'X' and f['text'] == 'X' and i['text'] == 'X'):
        disable()
        gameover(1)
        
    elif(a['text'] == 'O' and b['text'] == 'O' and c['text'] == 'O' or
         d['text'] == 'O' and e['text'] == 'O' and f['text'] == 'O' or
         g['text'] =='O' and h['text'] == 'O' and i['text'] == 'O' or
         a['text'] == 'O' and e['text'] == 'O' and i['text'] == 'O' or
         c['text'] == 'O' and e['text'] == 'O' and g['text'] == 'O' or
         a['text'] == 'O' and b['text'] == 'O' and c['text'] == 'O' or
         a['text'] == 'O' and d['text'] == 'O' and g['text'] == 'O' or
         b['text'] == 'O' and e['text'] == 'O' and h['text'] == 'O' or
         g['text'] == 'O' and f['text'] == 'O' and i['text'] == 'O'):
         disable()
         gameover(2)
         
    elif(flag == 8):
        disable()
        gameover(3)

def aa(q):
    global op, flag
    if q == 1:
       if op == 0:
           a.config(text = "X",bg = "dodgerblue",fg= "red")
           op = op+1
       else:
           a.config(text = "O",bg = "dodgerblue",fg= "red")
           op = op-1
       flag= flag+1
       a.config(state="disable")
       checkwin()
    elif q == 2:
       if op == 0:
           b.config(text="X",bg = "dodgerblue",fg= "yellow")
           op=op+1
       else:
           b.config(text="O",bg = "dodgerblue",fg= "yellow")
           op=op-1
       flag= flag+1
       b.config(state="disable")
       checkwin()
    elif q == 3:
       if op == 0:
           c.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           c.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       c.config(state="disable")
       checkwin()
    elif q == 4:
       if op == 0:
           d.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           d.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       d.config(state="disable")
       checkwin()
    elif q == 5:
       if op == 0:
           e.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           e.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       e.config(state="disable")
       checkwin()
    elif q == 6:
       if op == 0:
           f.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           f.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       f.config(state="disable")
       checkwin()
    elif q == 7:
       if op == 0:
           g.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           g.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       g.config(state="disable")
       checkwin()
    elif q == 8:
       if op == 0:
           h.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           h.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       h.config(state="disable")
       checkwin()
    elif q == 9:
       if op == 0:
           i.config(text="X",bg = "dodgerblue",fg= "white")
           op=op+1
       else:
           i.config(text="O",bg = "dodgerblue",fg= "white")
           op=op-1
       flag= flag+1
       i.config(state="disable")
       checkwin()

a=Button(root,text="", font='Times 20 bold', bg='white',width=5,height=3,command=lambda:aa(1))#X=90 , Y=116
a.place(x=140, y=193)

b=Button(root,text="", font='Times 20 bold', bg='white',width=5,height=3,command=lambda:aa(2))
b.place(x=230, y=193)

c=Button(root,text="", font='Times 20 bold', bg='white',width=5,height=3,command=lambda:aa(3))
c.place(x=320, y=193)

d=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3 ,command=lambda:aa(4))
d.place(x=140, y=309)

e=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3,command=lambda:aa(5))
e.place(x=230, y=309)

f=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3,command=lambda:aa(6))
f.place(x=320, y=309)

g=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3,command=lambda:aa(7))
g.place(x=140, y=425)

h=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3,command=lambda:aa(8))
h.place(x=230, y=425)

i=Button(root,text="",font='Times 20 bold', bg='white', width=5,height=3,command=lambda:aa(9))
i.place(x=320, y=425)

z=Button(root, text="RESTART",font='Times 17 bold', command=restart_program,width=10,height=3).place(x=210, y=555)
mainloop()
