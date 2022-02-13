# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:05:13 2022

@author: ARMAN
"""

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import PIL.ImageTk


import time
import datetime
import winsound
import pygame


#%% Ön Tanımlar
my_time = ""
current_time =""
#%%# Başlık ve Etiketler
fontStyle = ("cooper", 17, "bold")
little_fontStyle = ("cooper", 10, "bold")
buttonStyle = ("cooper", 12, "bold")
cnt = ("cooper", 50, "bold")

window = tk.Tk()
window.geometry("500x500")
window.resizable(0,0)
window.config(bg="gray80")  # arka plan rengi

# Başlık ve Etiket
window.title("COUNTING")  # form etiketi
baslik = tk.Label(text="COUNTING", fg="green", bg="gray80")
baslik.config(font="Bold 40")
baslik.pack()

#%% Logo ve ICO
im = PIL.Image.open("littlelion.png")
pht = PIL.ImageTk.PhotoImage(im)
afh = tk.Label(window,image=pht, bg="black")
afh.image = pht
afh.place(x=160, y=65)

window.iconbitmap("lion.ico")
#%% Close Button
def Close():      
    MsgBox = messagebox.askquestion(title = "Uyarı!", message = "Programı tamamen sonlandırmak istiyor musunuz?")
    
    if MsgBox == "yes":
        window.destroy()
    
closeButton = tk.Button(window, width=5, height=2, text='Close', fg='red', command = Close)
closeButton.pack(ipadx=1, ipady=1)  # buton paketle butonları sağ ortaya al buton çevre ölçüleri
closeButton.config(font=buttonStyle)
closeButton.place(x=420, y=400)

window.protocol("WM_DELETE_WINDOW", Close)
#%% UP or DOWN Seçimi

choose_label = tk.Label(text="UP or DOWN :",font= little_fontStyle, fg="black", bg="gray80")
choose_label.place(x = 10, y = 260)

select_one = ttk.Combobox(window, textvariable=StringVar(), width = 9, font=little_fontStyle, state='readonly') #readonly combobox klavyeden değer girmeyi engelleme
select_one["values"] = ["UP", "DOWN"]
select_one.place(x = 110, y = 260)
select_one.current(0)


#%%### Up Or Down ####

def UpDownSet():
    global situation

    selected_one = select_one.get()
    if selected_one == "UP":
        situation = Go_UP
    elif selected_one == "DOWN":
        situation = Go_DOWN
#%% Hour
label_hour = tk.Label(text='Hour: ', font= little_fontStyle, fg="black", bg="gray80")
label_hour.place(x = 10, y = 300)

label_entry_hour = tk.Entry(window, width = 13)
label_entry_hour.insert(string = "", index = 0)
label_entry_hour.place(x = 110,y = 300, height = 20) # Entry yükseklik ayarı bu şekilde yapılıyor.

this_hour = ""

def EnterHour():

    global this_hour
    
    this_hour = label_entry_hour.get()
    
    
    try:
        this_hour = int(this_hour)
        print("Hour: ",this_hour)
        
    except:
        this_hour = ""
        messagebox.showinfo(title = "Warning!", message = "Please enter information for hour as numbers only.")
        
#%%Minute

label_minute = tk.Label(text='Minute:', font= little_fontStyle, fg="black", bg="gray80")
label_minute.place(x = 10, y = 340)

label_entry_minute = tk.Entry(window, width = 13)
label_entry_minute.insert(string = "", index = 0)
label_entry_minute.place(x = 110, y = 340, height = 20)

this_minute = ""

def EnterMinute():

    global this_minute
    
    
    
    this_minute = label_entry_minute.get()
    
    try:
        
        this_minute = float(this_minute)
        

        print("Minute: ",this_minute)
        
    except:
        this_minute = ""
        messagebox.showinfo(title = "Uyarı!", message = "Please enter information for minute as numbers only.")
#%%SaveTime
    
def SaveTime():
    global my_time
    my_time = ((this_hour)*3600) + ((this_minute)*60)
    print("SaveTime:", my_time)    
    
#%%                       #### Birden çok fonksiyonu aynı anda çalıştırma ####
def combine_func(*funcs):
    def combined_func(*args,**kwargs):
        for f in funcs:
            f(*args,**kwargs)
    return combined_func
#%% Set Butonu
setButton = tk.Button(window, width=18, height=2, text='Set', fg='blue', command=combine_func(UpDownSet,EnterHour,EnterMinute,SaveTime))
setButton.pack(ipadx=5, ipady=1)  # buton paketle butonları sağ ortaya al buton çevre ölçüleri
setButton.config(font=buttonStyle)
setButton.place(x=10, y=370)
#%% Start Butonu
def Start():
    countdown(int(my_time))
    
startButton = tk.Button(window, width=18, height=2, text='Start', fg='green', command = Start)
startButton.pack(ipadx=5, ipady=1)  # buton paketle butonları sağ ortaya al buton çevre ölçüleri
startButton.config(font=buttonStyle)
startButton.place(x=10, y=430)
#%% Stop Butonu
def Stop():
    pass
    
stopButton = tk.Button(window, width=18, height=2, text='Stop', fg='red', command = Stop)
stopButton.pack(ipadx=5, ipady=1)  # buton paketle butonları sağ ortaya al buton çevre ölçüleri
stopButton.config(font=buttonStyle)
stopButton.place(x=200, y=430)
#%% Reset Butonu
def Reset():
    pass
    
resetButton = tk.Button(window, width=18, height=2, text='Reset', fg='blue', command = Reset)
resetButton.pack(ipadx=5, ipady=1)  # buton paketle butonları sağ ortaya al buton çevre ölçüleri
resetButton.config(font=buttonStyle)
resetButton.place(x=200, y=370)
#%%COUNTER
my_timer = ""
label_time = tk.Label(text = "" , fg="red", bg="gray80")
label_time.config(font="Bold 30")
label_time.place(x = 250, y = 290)
#%%TIME

def clock():
    clock_hour = time.strftime('%H')
    clock_minute = time.strftime('%M')
    clock_second = time.strftime('%S')
    clock_label.config(text = clock_hour + ":" + clock_minute + ":" + clock_second)
    clock_label.after(1000, clock)

clock_label = tk.Label(window, text = "", font= ("Helvetica", 15), bg = "gray80", fg = "black")
clock_label.place(x = 410, y = 10)


clock()

#%% PROGRAMMING FOR UP AND DOWN COUNTER
Go_UP = ""
Go_DOWN = ""

def countdown(my_time): 
    start_time = time.time()
    
    while my_time:   
        global my_timer
        
        mins, secs = divmod(my_time, 60) 
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)        
        # print(timer, end="\n" )
        time_before_sleep = time.time() - start_time
        time.sleep(1) 
        time_after_sleep = time.time() - start_time
        # print(timer, time_before_sleep, time_after_sleep)
        my_time -= 1
        my_timer = timer
        label_time.config(text = str(my_timer))
      
        window.update()
    print('TIME IS OVER')
    pygame.init()
    pygame.mixer.music.load("onepiece.mp3")
    pygame.mixer.music.play(-1)
    

window.mainloop()