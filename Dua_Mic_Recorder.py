import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
import pyaudio
from scipy.io.wavfile import read as scipy_wave_read
import time
import csv
import timeit
import wave
import os
import cv2


root = tk.Tk()
root.geometry("800x600")
root.title("Python Dual Mic Recorder")

render = PhotoImage(file = 'bgk.png')
img = Label(root, image = render)
img.place(x=0,y=0)

root.configure(background='')

global file_info
global duration_


heading = Label(text="Python Dual Mic Recorder",fg="white",bg="blue",width="500",height="2",font="10")
heading.pack()



def resize():
	w = width_entry.get()
	h = 800
	root.geometry(f"{w}x{h}")



def save_audio(args):
	file_info = filename.get()
	duration_=duration.get()
	if file_info and duration_:
		if val == 2:
			CHUNK = 4
			FORMAT = pyaudio.paInt16
			CHANNELS = 2
			RATE = 16000
			
			WAVE_OUTPUT_FILENAME = file_info
			stream_list=[]
		

			p = pyaudio.PyAudio()

			def makeStream(FORMAT, CHANNELS, RATE, INDEX, CHUNK):
				stream = p.open(format=FORMAT,
				                channels=CHANNELS,
				                rate=RATE,
				                input=True,
				                input_device_index = INDEX,
				                frames_per_buffer=CHUNK)
				return stream

			number_of_mics = 2
			index_of_mics = []
			for i in range(number_of_mics):
				index_of_mics.append(i)
				stream_list.append(makeStream(FORMAT, CHANNELS, RATE, index_of_mics[-1],CHUNK))

			frames = []

			time.sleep(0.2)

			frames = [ [] for _ in range(len(stream_list))]
			start = timeit.default_timer()

			for i in range(0, int(RATE / CHUNK * duration_)):
				for j in range(len(stream_list)):
					data = stream_list[j].read(CHUNK, exception_on_overflow = False)
					frames[j].append(data)
					
					
		

			
			for i in range(len(stream_list)):
				wf = wave.open(os.path.join(WAVE_OUTPUT_FILENAME), 'w')
				wf.setnchannels(CHANNELS)
				wf.setsampwidth(p.get_sample_size(FORMAT))
				wf.setframerate(RATE)
				wf.writeframes(b''.join(frames[i]))
				wf.close()
			

		else:
			messagebox.showinfo("Alert","Please Connect Both USB Mic ...")

	else:
		messagebox.showinfo("Alert","Please Enter File Name First...")



def Mic_One():
	save_audio(4)



def onclick(args):

	if args == 1:
		Mic_One()
	if args == 2:
		root.destroy()


val = 0
def clicked():
	global val
	if (val < 2):
		val=val+1
		var.set(val)
		if (val == 1):
			my_image = my_canvas.create_image(40,10, anchor=NW, image=img2)
			lbl.config(fg="black", text="Mic Conencted "+str(val)+" Out of Two")
		if (val == 2):
			my_image = my_canvas.create_image(200,10, anchor=NW, image=img)
			lbl.config(fg="black", text="Mic Conencted "+str(val)+" Out of Two")

	else:
		messagebox.showinfo("Alert","both of the mics are connected successfully...")





filename_text = Label(text="FileName :")
filename = StringVar()
filename_text.pack()
filename_text.place(x=10, y=50)
width_entry = Entry(root)

file_entry = Entry(textvariable=filename,width="20")
file_entry.pack()
file_entry.place(x=80, y=50)
width_entry = Entry(root)




duration_text = Label(text="Duration :")
duration=IntVar()
duration_text.pack()
duration_text.place(x=10, y=100)
width_entry = Entry(root)

duration_entry = Entry(textvariable=duration,width="20")
duration_entry.pack()
duration_entry.place(x=80, y=100)
width_entry = Entry(root)




var = IntVar()
my_canvas = Canvas(root, width=300, heigh=200,bg=None)
my_canvas.pack(pady=15)

img = PhotoImage(file="img10.png")
img2 = PhotoImage(file="img20.png")





lbl = Label(
	root,
	font = ("consolas",16)
	)
lbl.pack(pady=15)
width_entry = Entry(root)
lbl.config(fg="black", text="Mic Conencted "+str(val)+" Out of Two")

btn = Button(
	root,
	text= "Connect Mic",
	command = clicked,
	)
btn.pack(pady=20)
width_entry = Entry(root)





button = Button(root,text="Start Recrording",command=lambda:onclick(1),width="20",height="2",bg="grey")
button.pack(pady=22)
width_entry = Entry(root)


button = Button(root,text="Save",command=lambda:onclick(2),width="10",height="2",bg="grey")
button.pack()
width_entry = Entry(root)




root.mainloop()