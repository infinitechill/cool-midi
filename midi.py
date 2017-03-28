#!/usr/bin/env python

from midiutil import MIDIFile
import random

cmajorbass = [0, 2, 4, 5, 7, 9, 11, 12]
cmajormid = [x+48 for x in cmajorbass]

def quantizePitch(scale_to_use, input_note):
	new_note = min(scale_to_use, key=lambda x:abs(x-input_note))
	return new_note

track    = 0
channel  = 0
time     = 10    # In beats
duration = 1    # duration of note
tempo    = 160   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(cmajormid):
	#MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
	rootnote=random.choice(cmajormid)
	MyMIDI.addNote(track, channel, quantizePitch(cmajormid, rootnote), time + i, duration, volume)
	MyMIDI.addNote(track, channel, quantizePitch(cmajormid, rootnote+2), time + i, duration, volume)
	MyMIDI.addNote(track, channel, quantizePitch(cmajormid, rootnote+5), time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)