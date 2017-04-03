from tkinter import *
import tkinter.filedialog
import sys, subprocess, os
import tkinter.messagebox
import time

from midiutil import MIDIFile
import random


class CoolMidi:
	def __init__(self, master):

		# main background frame
		frame = Frame(master, width=1800, height=800, bd=1, background="plum")
		frame.pack()

		# options for file
		self.file_opt = options = {}
		options['defaultextension'] = '.mid'
		options['filetypes'] = [('midi files', '.mid')]
		options['initialdir'] = 'C:\\'
		options['parent'] = root
		options['title'] = 'Cool-Midi 1.0'

		# variables
		self.bpm=IntVar()
		self.notelength=StringVar()
		self.keysignature=StringVar() 
		self.majorminor=StringVar() 
		self.mykey=StringVar()
		self.myfile=StringVar() 
		self.myrandomnote=IntVar()
		self.duration=IntVar() 

		# set up colors
		iframeA = Frame(frame, bd=2, relief=SUNKEN, bg="lavender")
		iframeB = Frame(frame, bd=2, relief=SUNKEN, bg="lavender")
		iframeC = Frame(frame, bd=2, relief=SUNKEN, bg="lavender")
		iframeD = Frame(frame, bd=2, relief=SUNKEN, bg="lavender")
		iframeE = Frame(frame, bd=2, relief=SUNKEN, bg="lavender")

		# key signature radio buttons
		self.RA1 = Radiobutton(iframeA, text="A", variable=self.keysignature, value="A", background="lavender")
		self.RA1.grid(row=0, column=0)
		self.RA2 = Radiobutton(iframeA, text="A#", variable=self.keysignature, value="ASharp", background="lavender")
		self.RA2.grid(row=0, column=1)
		self.RA3 = Radiobutton(iframeA, text="B", variable=self.keysignature, value="B", background="lavender")
		self.RA3.grid(row=1, column=0)	
		self.RA4 = Radiobutton(iframeA, text="B#", variable=self.keysignature, value="BSharp", background="lavender")
		self.RA4.grid(row=1, column=1)
		self.RA5 = Radiobutton(iframeA, text="C", variable=self.keysignature, value="C", background="lavender")
		self.RA5.grid(row=2, column=0)	
		self.RA6 = Radiobutton(iframeA, text="C#", variable=self.keysignature, value="CSharp", background="lavender")
		self.RA6.grid(row=2, column=1)
		self.RA7 = Radiobutton(iframeA, text="D", variable=self.keysignature, value="D", background="lavender")
		self.RA7.grid(row=3, column=0)	
		self.RA8 = Radiobutton(iframeA, text="D#", variable=self.keysignature, value="DSharp", background="lavender")
		self.RA8.grid(row=3, column=1)	
		self.RA9 = Radiobutton(iframeA, text="E", variable=self.keysignature, value="E", background="lavender")
		self.RA9.grid(row=4, column=0)	
		self.RA10 = Radiobutton(iframeA, text="E#", variable=self.keysignature, value="ESharp", background="lavender")
		self.RA10.grid(row=4, column=1)		
		self.RA11 = Radiobutton(iframeA, text="F", variable=self.keysignature, value="F", background="lavender")
		self.RA11.grid(row=5, column=0)	
		self.RA12 = Radiobutton(iframeA, text="F#", variable=self.keysignature, value="FSharp", background="lavender")
		self.RA12.grid(row=5, column=1)		
		self.RA13 = Radiobutton(iframeA, text="G", variable=self.keysignature, value="G", background="lavender")
		self.RA13.grid(row=6, column=0)		
		self.RA14 = Radiobutton(iframeA, text="G#", variable=self.keysignature, value="GSharp", background="lavender")
		self.RA14.grid(row=6, column=1)

		# major or minor radio buttons
		self.RB1 = Radiobutton(iframeB, text="MAJOR", variable=self.majorminor, value="Major", background="lavender")
		self.RB1.pack(side=TOP, anchor="w")		
		self.RB2 = Radiobutton(iframeB, text="MINOR", variable=self.majorminor, value="Minor", background="lavender")
		self.RB2.pack(side=TOP, anchor="w")
		
		# note duration buttons
		self.RC1 = Radiobutton(iframeC, text="WHOLE NOTES", variable=self.notelength, value="WholeNote", background="lavender")
		self.RC1.pack(side=TOP, anchor="w")		
		self.RC2 = Radiobutton(iframeC, text="QUARTER NOTES", variable=self.notelength, value="QuarterNote", background="lavender")
		self.RC2.pack(side=TOP, anchor="w")
		self.RC3 = Radiobutton(iframeC, text="EIGHTH NOTES", variable=self.notelength, value="EighthNote", background="lavender")
		self.RC3.pack(side=TOP, anchor="w")
		self.RC4 = Radiobutton(iframeC, text="SIXTEENTH NOTES", variable=self.notelength, value="SixteenthNote", background="lavender")
		self.RC4.pack(side=TOP, anchor="w")
		self.RC5 = Radiobutton(iframeC, text="RANDOMIZE", variable=self.notelength, value="RandomLength", background="lavender")
		self.RC5.pack(side=TOP, anchor="w")

		self.RD1 = Radiobutton(iframeD, text="60", variable=self.bpm, value=60, background="lavender")
		self.RD1.pack(side=TOP, anchor="w")		
		self.RD2 = Radiobutton(iframeD, text="80", variable=self.bpm, value=80, background="lavender")
		self.RD2.pack(side=TOP, anchor="w")
		self.RD3 = Radiobutton(iframeD, text="100", variable=self.bpm, value=100, background="lavender")
		self.RD3.pack(side=TOP, anchor="w")
		self.RD4 = Radiobutton(iframeD, text="120", variable=self.bpm, value=120, background="lavender")
		self.RD4.pack(side=TOP, anchor="w")
		self.RD5 = Radiobutton(iframeD, text="140", variable=self.bpm, value=140, background="lavender")
		self.RD5.pack(side=TOP, anchor="w")

		# default to c major whole notes
		self.RA5.select()
		self.RB1.select()
		self.RC1.select()
		self.RD4.select()

		# randomize
		Button(iframeE, text="RANDOMIZE", command=self.randomizesettings, width = 10, highlightbackground="lavender").pack(side=LEFT, padx=5)
		# save file
		Button(iframeE, text="CREATE MIDI", command=self.startprocess, width = 10, highlightbackground="lavender").pack(side=LEFT, padx=5)

		iframeA.pack(expand=1, fill=X, pady=10, padx=5)
		iframeA.columnconfigure(0, weight=3)
		iframeA.columnconfigure(1, weight=3)

		iframeB.pack(expand=1, fill=X, pady=10, padx=5)
		iframeC.pack(expand=1, fill=X, pady=10, padx=5)
		iframeD.pack(expand=1, fill=X, pady=10, padx=5)
		iframeE.pack(expand=1, fill=X, pady=10, padx=5)


	def makemidi(self, keysignature, majorminor, noteduration, bpm, outputfilename):
		# used for randomize.. allow you to pick a random note from a scale
		def quantizePitch(quantize_to_scale, input_note):
			new_note = min(quantize_to_scale, key=lambda x:abs(x-input_note))
			return new_note

		# fetch parameters
		scale_to_use=eval('keysignature+majorminor+"Scale"')

		def WholeNote():
			self.duration =  (10/self.bpm.get())
		def HalfNote():
			self.duration =  (20/self.bpm.get())
		def QuarterNote():
			self.duration =  (60/self.bpm.get())
		def EighthNote():
			self.duration =  (30/self.bpm.get())
		def SixteenthNote():
			self.duration =  (15/self.bpm.get())
		def SixteenthNote():
			self.duration =  (15/self.bpm.get())
		def RandomLength():						# needs to be changed
			self.duration =  (15/self.bpm.get())		
		setdurationvalue = {
			"WholeNote" 		: WholeNote,
			"HalfNote" 			: HalfNote,
			"QuarterNote" 		: QuarterNote,
			"EighthNote" 		: EighthNote, 
			"SixteenthNote" 	: SixteenthNote, 
			"RandomLength" 		: RandomLength,
		}

		

		# set up other variables to use
		basstrack 	= 0
		midtrack 	= 1
		hightrack 	= 2
		basschannel = 0
		midchannel 	= 1
		highchannel = 2
		time     	= 10    # In beats
		tempo    	= int(self.bpm.get())   # In BPM
		volume   	= 100  # 0-127, as per the MIDI standard
		setdurationvalue[self.notelength.get()]()


		# set up scales
		majorscale = [48, 50, 52, 53, 55, 57, 59, 60]
		minorscale = [48, 50, 51, 53, 55, 56, 58, 60]

		AMajorScale =[x-1 for x in majorscale]
		AMinorScale =[x-1 for x in minorscale]
		ASharpMajorScale =[x-1 for x in majorscale]
		ASharpMinorScale =[x-1 for x in minorscale]
		BMajorScale =[x-1 for x in majorscale]
		BMinorScale =[x-1 for x in minorscale]
		BSharpMajorScale =[x-1 for x in majorscale]
		BSharpMinorScale =[x-1 for x in minorscale]
		CMajorScale =[x+48 for x in majorscale]
		CMinorScale =[x+48 for x in minorscale]
		CSharpMajorScale =[x+1 for x in majorscale]
		CSharpMinorScale =[x+1 for x in minorscale]
		DMajorScale =[x+2 for x in majorscale]
		DMinorScale =[x+2 for x in minorscale]
		DSharpMajorScale =[x+3 for x in majorscale]
		DSharpMinorScale =[x+3 for x in minorscale]
		EMajorScale =[x+4 for x in majorscale]
		EMinorScale =[x+4 for x in minorscale]
		ESharpMajorScale =[x+5 for x in majorscale]
		ESharpMinorScale =[x+5 for x in minorscale]
		FMajorScale =[x+6 for x in majorscale]
		FMinorScale =[x+6 for x in minorscale]
		FSharpMajorScale =[x+7 for x in majorscale]
		FSharpMinorScale =[x+7 for x in minorscale]
		GMajorScale=[x+8 for x in majorscale]
		GMinorScale=[x+8 for x in minorscale]
		GSharpMajorScale=[x+9 for x in majorscale]
		GSharpMinorScale=[x+9 for x in minorscale]

		MyMIDI = MIDIFile(3)  # three tracks :)
		MyMIDI.addTempo(basstrack, time, tempo)
		MyMIDI.addTempo(midtrack, time, tempo)
		MyMIDI.addTempo(hightrack, time, tempo)

		MyMIDI.addProgramChange(basstrack, basschannel, time, 38) 		#	38 = Synth Bass
		MyMIDI.addProgramChange(midtrack, midchannel, time, 0) 		#	0 = Acoustic Grand Piano
		MyMIDI.addProgramChange(hightrack, highchannel, time, 75)		#	75 = Pan Flute


		for i, pitch in enumerate(eval(scale_to_use)):
			# go up through the notes
			# MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
			# pick a random note from the scale and add it to midi
			randomnote=random.choice(eval(scale_to_use))
			#MyMIDI.addNote(track, channel, quantizePitch(AMajorScale, randomnote), time + i, duration, volume)
			MyMIDI.addNote(basstrack, basschannel, randomnote-12, time+i, self.duration, volume)
			randomnote=random.choice(eval(scale_to_use))
			MyMIDI.addNote(midtrack, midchannel, randomnote, time+i, self.duration, volume)
			randomnote=random.choice(eval(scale_to_use))
			MyMIDI.addNote(hightrack, highchannel, randomnote+12, time+i, self.duration, volume)

		#	print("track", track, type(track))
		#	print("channel", channel, type(channel))
		#	print("random", randomnote, type(randomnote))
		#	print("time+i", time+i, type(time+i))
		#	print("duration", duration, type(duration))
		#	print("volume", volume, type(volume))

		#	MyMIDI.addNote(track, channel, randomnote, time + i, 10, volume)
			
			# making chords...
			#MyMIDI.addNote(track, channel, quantizePitch(cmajormid, randomnote+2), time + i, duration, volume)
			#MyMIDI.addNote(track, channel, quantizePitch(cmajormid, randomnote+5), time + i, duration, volume)

		with open(outputfilename, "wb") as output_file:
		    MyMIDI.writeFile(output_file)


	def randomizesettings(self):
		# put values into arrays
		scalearray=["A", "ASharp", "B", "BSharp", "C", "CSharp", "D", "DSharp", "E", "ESharp", "F", "FSharp", "G", "GSharp"]
		majorminorarray=["Major", "Minor"]
		durationarray=["WholeNote", "QuarterNote", "EighthNote", "SixteenthNote", "RandomLength"]
		bpmarray=["60", "80", "100", "120", "140"]
		# helper functions for switch style dictionary lookup
		def RA1SET():
			self.RA1.select()
		def RA2SET():
			self.RA2.select()
		def RA3SET():
			self.RA3.select()		
		def RA4SET():
			self.RA4.select()
		def RA5SET():
			self.RA5.select()
		def RA6SET():
			self.RA6.select()
		def RA7SET():
			self.RA7.select()
		def RA8SET():
			self.RA8.select()
		def RA9SET():
			self.RA9.select()
		def RA10SET():
			self.RA10.select()
		def RA11SET():
			self.RA11.select()
		def RA12SET():
			self.RA12.select()
		def RA13SET():
			self.RA13.select()
		def RA14SET():
			self.RA14.select()	
		def RB1SET():
			self.RB1.select()
		def RB2SET():
			self.RB2.select()
		def RC1SET():
			self.RC1.select()
		def RC2SET():
			self.RC2.select()
		def RC3SET():
			self.RC3.select()
		def RC4SET():
			self.RC4.select()
		def RC5SET():
			self.RC5.select()
		def RD1SET():
			self.RD1.select()
		def RD2SET():
			self.RD2.select()
		def RD3SET():
			self.RD3.select()
		def RD4SET():
			self.RD4.select()
		def RD5SET():
			self.RD5.select()							
		# define python "switch" statements
		setscale = {
			"A" 		: RA1SET,
			"ASharp" 	: RA2SET,
			"B" 		: RA3SET,
			"BSharp" 	: RA4SET,			
			"C" 		: RA5SET,
			"CSharp" 	: RA6SET,
			"D" 		: RA7SET,
			"DSharp" 	: RA8SET,
			"E" 		: RA9SET,
			"ESharp" 	: RA10SET,
			"F" 		: RA11SET,
			"FSharp" 	: RA12SET,
			"G" 		: RA13SET,
			"GSharp" 	: RA14SET,
		}
		setmajorminor = {
			"Major" 	: RB1SET,
			"Minor" 	: RB2SET,
		}
		setduration = {
			"WholeNote" 	: RC1SET, 
			"QuarterNote" 	: RC2SET,
			"EighthNote" 	: RC3SET, 
			"SixteenthNote" : RC4SET, 
			"RandomLength" 	: RC5SET,
		}
		setbpm = {
			"60" 		: RD1SET, 
			"80" 		: RD2SET,
			"100" 		: RD3SET, 
			"120" 		: RD4SET, 
			"140" 		: RD5SET,
		}
		# pick random values from arrays
		randomscale=random.choice(scalearray)
		randommajorminor=random.choice(majorminorarray)
		randomduration=random.choice(durationarray)
		randombpm=random.choice(bpmarray)
		# call switch statements to select values
		setscale[randomscale]()
		setmajorminor[randommajorminor]()
		setduration[randomduration]()
		setbpm[randombpm]()
		# pack the random values up to return
		# myrandomvalues=[randomscale,randommajorminor,randomduration,randombpm]
		# return myrandomvalues

	def startprocess(self):
		if (self.notelength.get() == "" or self.keysignature.get() == "" or self.majorminor.get() == ""):
			tkinter.messagebox.showinfo("ERROR", "please fill out all check boxes")
			return False
		else:
			self.myfile=self.keysignature.get()+self.majorminor.get()+self.notelength.get()+str(self.bpm.get())+"BPM.mid"
			myinitialfile=self.myfile
			outputfilename = tkinter.filedialog.asksaveasfilename(**self.file_opt, initialfile = self.myfile)
			print(outputfilename)
			# create midi file
			self.makemidi(self.keysignature.get(), self.majorminor.get(), self.notelength.get(), self.bpm.get(), outputfilename)

root = tkinter.Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
all = CoolMidi(root)
root.title('COOL MIDI')
root.mainloop()

