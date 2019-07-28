from tkinter import *
import sys
import os
#import tkinter.messagebox
from PIL import ImageTk, Image
root=Tk()
root.title("Tic Tac Toe")
root.geometry("550x650+469+90")
root.resizable(width=False, height=False)
root.config(bg="Dimgray")

img = ImageTk.PhotoImage(Image.open("C:/Users/admin/Documents/Code/Python/Programs/img1.jpg"))
l=Label(image=img,width=549,height=564).place(x=-3, y=86)

op= 0
flag= 0
winflag = IntVar()

playerX = StringVar()
playerY = StringVar()
winplayX = StringVar()
winplayY = StringVar()

svar = StringVar()
deli = IntVar()


#winplayX= "asd"
#winplayY= "qwe"


winplayX= playerX.get()
winplayY= playerY.get()

#playerX=winplayX.set()
#playerY=winplayY.set()


u=Frame(root)
u.grid(row=1)

playerX_name = Label( u, text="Player X:", font='Times 25 bold', bg='white', fg='black', height=1, width=10)
playerX_name.grid(row=1, column=2)

playerX_name=Entry(u,textvariable=playerX,font="Times 25")
playerX_name.grid(row=1, column=3)



v=Frame(root)
v.grid(row=2)

playerO_name = Label( v, text="Player O:", font='Times 25 bold', bg='white', fg='black', height=1, width=10)
playerO_name.grid(row=2, column=0)

playerO_name = Entry(v,textvariable=playerY,font="Times 25")
playerO_name.grid(row=2, column=3)

#WELCOME_MSG = '''Names registered'''
#WELCOME_DURATION = 2000

#def welcome():
#    top = Toplevel()
#    top.title('Welcome')
#    top.title("")
#    top.geometry("140x30+614+339")
#    top.resizable(width=False, height=False)
#    top.attributes("-toolwindow",1)
#    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
#    top.after(WELCOME_DURATION, top.destroy)

#sub=Button(v, text="Submit", command=welcome)
#sub.grid(row=3,column=3)


#playerX=winplayX.set()
#playerY=winplayY.set()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def destroy():
    root.destroy()

def shif():
    global svar
    global deli
    deli=200
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)

def gameover(winflag):
    win= Toplevel()
    win.title("Game Over")
    win.geometry("260x260+614+339")
    win.resizable(width=False, height=False)
    #win.attributes("-toolwindow",1)
    global playerX
    global playerY
    global winplayX
    global winplayY
    global svar

    if  winflag==1:
        wLabel1=Label(win, text="%s Wins!"%winplayX,font='Times 20 bold').place(x=80, y=80)
    elif winflag==2:
        wLabel2=Label(win, text="%s Wins!"%winplayY,font='Times 20 bold').place(x=80, y=80)
    elif winflag==3:
        wLabel3=Label(win, text="It is a tie ¯\_(ツ)_/¯",font='Times 20 bold').place(x=15, y=80)        

    Button(win, text="RESTART",font='Times 10 bold', command=restart_program,width=12,height=3).place(x=80, y=150)    
    Button(win, text="QUIT",font='Times 10 bold',command=lambda:destroy(),width=12,height=3).place(x=80, y=200)
    Label(win, text="Tic-Tac-Toe",font='Times 35 bold').place(x=4, y=5)

    #label = Label(win, textvariable=svar,font='Times 35 bold', height=5 ).place(x=4, y=-110)
    #shif.msg= "Tic-Tac-Toe     "
    #shif()
    
def disable():
    a.config(state="disable")
    b.config(state="disable")
    c.config(state="disable")
    d.config(state="disable")
    e.config(state="disable")
    f.config(state="disable")
    g.config(state="disable")
    h.config(state="disable")
    i.config(state="disable")



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
        
        #tkinter.messagebox.showinfo("Tic-Tac-Toe")


        
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
         #tkinter.messagebox.showinfo("Tic-Tac-Toe")
         
    elif(flag == 8):
        disable()
        gameover(3)
        #tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        

def aa(q):
    global op
    global flag
    if q==1:
       if op==0:
           a.config(text="X")
           a.config(bg="dodgerblue")
           op=op+1
       else:
           a.config(text="O")
           a.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       a.config(state="disable")
       checkwin()
    elif q==2:
       if op==0:
           b.config(text="X")
           b.config(bg="dodgerblue")
           op=op+1
       else:
           b.config(text="O")
           b.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       b.config(state="disable")
       checkwin()
    elif q==3:
       if op==0:
           c.config(text="X")
           c.config(bg="dodgerblue")
           op=op+1
       else:
           c.config(text="O")
           c.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       c.config(state="disable")
       checkwin()
    elif q==4:
       if op==0:
           d.config(text="X")
           d.config(bg="dodgerblue")
           op=op+1
       else:
           d.config(text="O")
           d.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       d.config(state="disable")
       checkwin()
    elif q==5:
       if op==0:
           e.config(text="X")
           e.config(bg="dodgerblue")
           op=op+1
       else:
           e.config(text="O")
           e.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       e.config(state="disable")
       checkwin()
    elif q==6:
       if op==0:
           f.config(text="X")
           f.config(bg="dodgerblue")
           op=op+1
       else:
           f.config(text="O")
           f.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       f.config(state="disable")
       checkwin()
    elif q==7:
       if op==0:
           g.config(text="X")
           g.config(bg="dodgerblue")
           op=op+1
       else:
           g.config(text="O")
           g.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       g.config(state="disable")
       checkwin()
    elif q==8:
       if op==0:
           h.config(text="X")
           h.config(bg="dodgerblue")
           op=op+1
       else:
           h.config(text="O")
           h.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       h.config(state="disable")
       checkwin()
    elif q==9:
       if op==0:
           i.config(text="X")
           i.config(bg="dodgerblue")
           op=op+1
       else:
           i.config(text="O")
           i.config(bg="dodgerblue")
           op=op-1
       flag= flag+1
       i.config(state="disable")
       checkwin()

#frame= Frame(root, width=400, height=400,bg='sky blue').place(x=50, y=160)

a=Button(root,text='',command=lambda:aa(1),font='Times 20 bold', bg='white', fg='blue',width=5,height=3)#X=90 , Y=116
a.place(x=140, y=193)

b=Button(root,text="",command=lambda:aa(2),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
b.place(x=230, y=193)

c=Button(root,text="",command=lambda:aa(3),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
c.place(x=320, y=193)

d=Button(root,text="",command=lambda:aa(4),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
d.place(x=140, y=309)

e=Button(root,text="",command=lambda:aa(5),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
e.place(x=230, y=309)

f=Button(root,text="",command=lambda:aa(6),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
f.place(x=320, y=309)

g=Button(root,text="",command=lambda:aa(7),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
g.place(x=140, y=425)

h=Button(root,text="",command=lambda:aa(8),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
h.place(x=230, y=425)

i=Button(root,text="",command=lambda:aa(9),font='Times 20 bold', bg='white', fg='white',width=5,height=3)
i.place(x=320, y=425)

z=Button(root, text="RESTART",font='Times 17 bold', command=restart_program,width=10,height=3).place(x=210, y=555)

mainloop()
