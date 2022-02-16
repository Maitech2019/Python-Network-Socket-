#GUI-chat.py

from tkinter import *
from tkinter import ttk 
import tkinter.scrolledtext as st

GUI = Tk()
GUI.geometry('500x500+700+100')     #create box
GUI.title('Program Chat to May')

FONT1 = ('Angsana New', 22)
FONT2 = ('Angsana New', 22)
######################chatbox##########################
F1 = Frame(GUI)                     #create blackboard
F1.place(x=5,y=5)

allmsg = StringVar()

chatbox = st.ScrolledText(F1,width=38,heigh=9,font=FONT1)   #create blackboard to fill text with scroll
chatbox.pack(expand=True, fill='x')

######################message form#####################

v_msg = StringVar()

F2 = Frame(GUI)
F2.place(x=10,y=400)

E1 =ttk.Entry(F2,textvariable=v_msg,font=FONT2,width=34)
E1.pack(ipady=20)

######################botton############################

def SendMessage(event=None): #=None allow both (botton and Enter) coz Enter will to send 'event')
	msg = v_msg.get()
	allmsg.set(allmsg.get() + msg + '\n---\n')
	chatbox.delete(1.0,END)         #clear old msg
	chatbox.insert(INSERT,allmsg.get())  #insert new msg
	chatbox.yview(END)
	v_msg.set('')   #clear msg
	E1.focus() #go back to focus on Entry


F3 = Frame(GUI)
F3.place(x=360,y=400)
B1 = ttk.Button(F3,text='Send', command=SendMessage)
B1.pack(ipadx=15,ipady=30)

E1.bind('<Return>', SendMessage)


GUI.mainloop()