#! /usr/bin/env python3


import sys
from denoise import denoiser_m 
from rotate import rotate
from model import Models
from noise_adder import noise
from resizer import resize
from tkinter import messagebox
import cv2

try:
    import Tkinter as tk
    import tkMessageBox
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import runner_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    img_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
	    try:
		    '''This class configures and populates the toplevel window.
		       top is the toplevel containing window.'''
		    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		    _fgcolor = '#000000'  # X11 color: 'black'
		    _compcolor = '#d9d9d9' # X11 color: 'gray85'
		    _ana1color = '#d9d9d9' # X11 color: 'gray85'
		    _ana2color = '#ececec' # Closest X11 color: 'gray92'

		    top.geometry("600x450+713+322")
		    top.minsize(1, 1)
		    top.maxsize(1905, 1050)
		    top.resizable(1,  1)
		    top.title("Image Processing")
		    top.configure(background="#000000")
		    top.configure(highlightcolor="black")

		    self.Label1 = tk.Label(top)
		    self.Label1.place(relx=0.333, rely=0.044, height=51, width=189)
		    self.Label1.configure(activebackground="#333333")
		    self.Label1.configure(background="#FDD700")
		    self.Label1.configure(font="-family {DejaVu Sans} -size 16")
		    self.Label1.configure(foreground="#333333")
		    self.Label1.configure(text='''D-Process''')
		    
		    def rotated(i,a):
			    ang=a.get()
			    if ang=="":
			    	messagebox.showerror("error","Angle is not define")
			    
			    else:
			    	rotate(i,ang)
			    	self.ang.delete(0,'end')
			    	messagebox.showinfo("Done","image is save")
			    return
		    
		    def resz(i,s1,s2):
			    si1=s1.get()
			    si2=s2.get()
			    if si1=="":
			    	messagebox.showerror("error","Size is not properly define")
			    elif si2=="":
		    		messagebox.showerror("error","Size is not properly define")
			    else:
		    		resize(i,si1,si2)
		    		self.s1.delete(0,'end')
		    		self.s2.delete(0,'end')
		    		messagebox.showinfo("Done","image is save")
			    return	
				    

		    	
  
		    n=noise()
		    m=Models(240,240,3)
		    def upload(i):
			    i=i.get()
			    if i=="":
			    	messagebox.showerror("error","No Image is Chosen")
			    else:
			    	img=str(cv2.imread(i,1))
			    	if img == "None":
			        	messagebox.showerror("error","Image is not found")
			    	else:
			    		messagebox.showinfo("Done","image is uploaded")
			    	
			    		a = tk.StringVar()
			    		self.ang = tk.Entry(top,textvariable=a)
			    		self.ang.place(relx=0.383, rely=0.444, height=33, relwidth=0.093)
			    		self.ang.configure(background="#FFD700")
			    		self.ang.configure(font="TkFixedFont")
			    		self.ang.configure(foreground="#333333")
			    		self.ang.configure(selectbackground="blue")
			    		self.ang.configure(selectforeground="white")
			    	
			    		s1 = tk.StringVar()
			    		self.s1 = tk.Entry(top,textvariable=s1)
			    		self.s1.place(relx=0.383, rely=0.578, height=33, relwidth=0.093)
			    		self.s1.configure(background="#FFD700")
			    		self.s1.configure(font="TkFixedFont")
			    		self.s1.configure(foreground="#333333")
			    		self.s1.configure(selectbackground="blue")
			    		self.s1.configure(selectforeground="white")
			    	
			    		s2 = tk.StringVar()
			    		self.s2 = tk.Entry(top,textvariable=s2)
			    		self.s2.place(relx=0.5, rely=0.578, height=33, relwidth=0.093)
			    		self.s2.configure(background="#FFD700")
			    		self.s2.configure(font="TkFixedFont")
			    		self.s2.configure(foreground="#333333")
			    		self.s2.configure(selectbackground="blue")
			    		self.s2.configure(selectforeground="white")
				    	 	
			    		self.Button1 = tk.Button(top)
			    		self.Button1.place(relx=0.117, rely=0.444, height=31, width=141)
			    		self.Button1.configure(activebackground="#333333")
			    		self.Button1.configure(background="#FFD700")
			    		self.Button1.configure(foreground="#333333")
			    		self.Button1.configure(text='''Rotate''')
			    		self.Button1.configure(command=lambda:rotated(i,a))
			    		
			    		self.Button2 = tk.Button(top)
			    		self.Button2.place(relx=0.117, rely=0.689, height=31, width=141)
			    		self.Button2.configure(activebackground="#333333")
			    		self.Button2.configure(background="#FFD700")
			    		self.Button2.configure(font="-family {DejaVu Sans} -size 12")
			    		self.Button2.configure(foreground="#333333")
			    		self.Button2.configure(text='''denoise''')
			    		self.Button2.configure(command=lambda:[denoiser_m(i,n,m),messagebox.showinfo("Done","image is save")])
			    		
			    		self.Button3 = tk.Button(top)
			    		self.Button3.place(relx=0.117, rely=0.578, height=31, width=141)
			    		self.Button3.configure(activebackground="#333333")
			    		self.Button3.configure(background="#FFD700")
			    		self.Button3.configure(foreground="#333333")
			    		self.Button3.configure(text='''Resize''')
			    		self.Button3.configure(command=lambda:resz(i,s1,s2))
			    		
			    		self.Button6 = tk.Button(top)
			    		self.Button6.place(relx=0.50, rely=0.911, height=31, width=141)
			    		self.Button6.configure(activebackground="#333333")
			    		self.Button6.configure(background="#FFD700")
			    		self.Button6.configure(foreground="#333333")
			    		self.Button6.configure(text='''Restart''')
			    		self.Button6.configure(command=lambda:[top.destroy(),vp_start_gui()])
			    		
			    	
		    	
		    
		    self.Button5 = tk.Button(top)
		    self.Button5.place(relx=0.117, rely=0.333, height=31, width=141)
		    self.Button5.configure(activebackground="#333333")
		    self.Button5.configure(background="#FFD700")
		    self.Button5.configure(foreground="#333333")
		    self.Button5.configure(text='''Upload''')
		    self.Button5.configure(command=lambda:upload(i))
		    
		    i = tk.StringVar()
		    self.img = tk.Entry(top,textvariable=i)
		    self.img.place(relx=0.383, rely=0.333, height=33, relwidth=0.26)
		    self.img.configure(background="#FFD700")
		    self.img.configure(font="TkFixedFont")
		    self.img.configure(foreground="#333333")
		    self.img.configure(selectbackground="blue")
		    self.img.configure(selectforeground="white")
		    
		    

		    self.Button4 = tk.Button(top)
		    self.Button4.place(relx=0.75, rely=0.911, height=31, width=141)
		    self.Button4.configure(activebackground="#333333")
		    self.Button4.configure(background="#FFD700")
		    self.Button4.configure(foreground="#333333")
		    self.Button4.configure(text='''Exit''')
		    self.Button4.configure(command=top.destroy)
		    
		    

	    except Exception as e:
		    print(e)

		
if __name__ == '__main__':
	vp_start_gui()





