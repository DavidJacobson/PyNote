#!/usr/bin/env python3
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os.path
window=[]
to_open=[]# Store the files that are to be opened in an array
to_read=""
filename="note0.txt"
textboxes=[]
lastfound=0



if os.path.isfile("note0.txt")==True: #Make a new file if it already exists
	for i in range(256):
		if os.path.isfile("note"+str(i)+".txt")==False:
			filename="note"+str(i)+".txt"
			
		else:
			to_open.append("note"+str(i)+".txt")
			lastfound=i
	
	#Create an extra, new file
	create=open("note"+str(lastfound+1)+".txt","w")
	create.close()
	to_open.append("note"+str(lastfound+1)+".txt")
else:
	#Stupid hacky bug fix for when it's not the first file
	create=open("note0.txt","w")
	create.close()

for i in to_open:
	window.append(Tk()) #Create a new window for each note

for i in window:
	textbox=ScrolledText(i)
	#Set coloring
	i.configure(background="#FFFFA0")
	textbox.configure(background="#FFFFA0")
	
	textbox.pack()
	textboxes.append(textbox) #Make a list of all the textbook objects

for i in range(len(window)):
	window[i].wm_title("note "+str(i)) #Set the title
	to_open[i]
	with open(to_open[i],"r") as to_read:
		for iii in to_read:
			textbox.insert("0.0",iii)
def main():
	ii=0
	
	for i in window:
		textbox=textboxes[ii]
		
		if textbox.get("1.0",END)!="": #For some reason tkinter returns nothing sometimes, also doesn't bother saving if the person has typed nothing
			with open("note"+str(ii)+".txt","w") as textfile: #When the file is opened
				textfile.write(textbox.get("1.0",END)) #Write anything that's been written
				textfile.close() #Close the text file
		
		i.update()
		
		ii+=1

while 1==1: #Main loop
	main()