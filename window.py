from tkinter import *
from tkinter import messagebox
import json
#the window
window = Tk()
window.title("Scales and chords library")
window.geometry('800x600')

#functions
def info_display():
    messagebox.showinfo("Info", "This is a simple scales and chords library. Just a school project. We only support two modes (for now). The program will be slowly developed. Enjoy!")
def scale_display(scale, mode):
    scaleWindow = Toplevel(master=window)
    scaleWindow.title(scale + " " + mode)
    scaleLabel = Label(scaleWindow, text=scale + " " + mode, font=("Arial Bold", 20))
    scaleLabel.pack()
    with open("/home/infotech/Pulpit/Pythons/Projekt_koncowy/scales.json", "r") as scales:
        data = json.load(scales)
        scaleData = data[scale][mode]
        
        def notes_display():
            messagebox.showinfo("Notes", f"Notes in {scale} {mode}: {scaleData['notes']}")
        def chords_display():
            messagebox.showinfo("Chords", f"Chords in {scale} {mode}: {scaleData['chords']}")
        def scales_display():
            messagebox.showinfo("Scales", f"Scales in {scale} {mode}: {scaleData['scales']}")
        def chordnotes_display():
            messagebox.showinfo("Chord notes", f"Chord notes in {scale} {mode}: {scaleData['chord notes']}")
        def relativeChord_display():
            if mode == "major":
                messagebox.showinfo("Relative chord", f"Relative minor in {scale} {mode}: {scaleData['relative minor']}")
            else:
                messagebox.showinfo("Relative chord", f"Relative major in {scale} {mode}: {scaleData['relative major']}")
        notesButton = Button(scaleWindow, text="Notes", bg="white", fg="black", width=15, command=notes_display).pack()
        chordsButton = Button(scaleWindow, text="Chords", bg="white", fg="black", width=15, command=chords_display).pack()
        scalesButton = Button(scaleWindow, text="Scales", bg="white", fg="black", width=15, command=scales_display).pack()
        chordnotesButton = Button(scaleWindow, text="Chord notes", bg="white", fg="black", width=15, command= chordnotes_display).pack()
        relativeChordButton = Button(scaleWindow, text="Relative chord", bg="white", fg="black", width=15, command=relativeChord_display).pack()
#tkinter objects
headline = Label(window, text="Welcome to the scales and chords library!", font=("Arial Bold", 20))
cmajor = Button(window, text="C major", bg="white", fg="black", width=10, command=lambda: scale_display("C", "major"))
csharpmajor = Button(window, text="C#/Db major", bg="white", fg="black", width=10, command=lambda: scale_display("C#/Db", "major"))
dmajor = Button(window, text="D major", bg="white", fg="black", width=10, command=lambda: scale_display("D", "major"))
dsharpmajor = Button(window, text="D#/Eb major", bg="white", fg="black", width=10, command=lambda: scale_display("D#/Eb", "major"))
emajor = Button(window, text="E major", bg="white", fg="black", width=10, command=lambda: scale_display("E", "major"))
fmajor = Button(window, text="F major", bg="white", fg="black", width=10, command=lambda: scale_display("F", "major"))
fsharpmajor = Button(window, text="F#/Gb major", bg="white", fg="black", width=10, command=lambda: scale_display("F#/Gb", "major"))
gmajor = Button(window, text="G major", bg="white", fg="black", width=10, command=lambda: scale_display("G", "major"))
gsharpmajor = Button(window, text="G#/Ab major", bg="white", fg="black", width=10, command=lambda: scale_display("G#/Ab", "major"))
amajor = Button(window, text="A major", bg="white", fg="black", width=10, command=lambda: scale_display("A", "major"))
asharpmajor = Button(window, text="A#/Bb major", bg="white", fg="black", width=10, command=lambda: scale_display("A#/Bb", "major"))
bmajor = Button(window, text="B major", bg="white", fg="black", width=10, command=lambda: scale_display("B", "major"))
cminor = Button(window, text="C minor", bg="white", fg="black", width=10, command=lambda: scale_display("C", "minor"))
csharpminor = Button(window, text="C#/Db minor", bg="white", fg="black", width=10, command=lambda: scale_display("C#/Db", "minor"))
dminor = Button(window, text="D minor", bg="white", fg="black", width=10, command=lambda: scale_display("D", "minor"))
dsharpminor = Button(window, text="D#/Eb minor", bg="white", fg="black", width=10, command=lambda: scale_display("D#/Eb", "minor"))
eminor = Button(window, text="E minor", bg="white", fg="black", width=10, command=lambda: scale_display("E", "minor"))
fminor = Button(window, text="F minor", bg="white", fg="black", width=10, command=lambda: scale_display("F", "minor"))
fsharpminor = Button(window, text="F#/Gb minor", bg="white", fg="black", width=10, command=lambda: scale_display("F#/Gb", "minor"))
gminor = Button(window, text="G minor", bg="white", fg="black", width=10, command=lambda: scale_display("G", "minor"))
gsharpminor = Button(window, text="G#/Ab minor", bg="white", fg="black", width=10, command=lambda: scale_display("G#/Ab", "minor"))
aminor = Button(window, text="A minor", bg="white", fg="black", width=10, command=lambda: scale_display("A", "minor"))
asharpminor = Button(window, text="A#/Bb minor", bg="white", fg="black", width=10, command=lambda: scale_display("A#/Bb", "minor"))
bminor = Button(window, text="B minor", bg="white", fg="black", width=10, command=lambda: scale_display("B", "minor"))
info = Button(window, text="Info", bg="white", fg="red", width=10, command=info_display)


#pack the objects
headline.pack()


# place the major buttons in the left of the screen
cmajor.place(relx=0.25, y=50, anchor=CENTER)
csharpmajor.place(relx=0.25, y=95, anchor=CENTER)
dmajor.place(relx=0.25, y=140, anchor=CENTER)
dsharpmajor.place(relx=0.25, y=185, anchor=CENTER)
emajor.place(relx=0.25, y=230, anchor=CENTER)
fmajor.place(relx=0.25, y=275, anchor=CENTER)
fsharpmajor.place(relx=0.25, y=320, anchor=CENTER)
gmajor.place(relx=0.25, y=365, anchor=CENTER)
gsharpmajor.place(relx=0.25, y=410, anchor=CENTER)
amajor.place(relx=0.25, y=455, anchor=CENTER)
asharpmajor.place(relx=0.25, y=500, anchor=CENTER)
bmajor.place(relx=0.25, y=550, anchor=CENTER)

# place the minor buttons in the right of the screen
cminor.place(relx=0.75, y=50, anchor=CENTER)
csharpminor.place(relx=0.75, y=95, anchor=CENTER)
dminor.place(relx=0.75, y=140, anchor=CENTER)
dsharpminor.place(relx=0.75, y=185, anchor=CENTER)
eminor.place(relx=0.75, y=230, anchor=CENTER)
fminor.place(relx=0.75, y=275, anchor=CENTER)
fsharpminor.place(relx=0.75, y=320, anchor=CENTER)
gminor.place(relx=0.75, y=365, anchor=CENTER)
gsharpminor.place(relx=0.75, y=410, anchor=CENTER)
aminor.place(relx=0.75, y=455, anchor=CENTER)
asharpminor.place(relx=0.75, y=500, anchor=CENTER)
bminor.place(relx=0.75, y=550, anchor=CENTER)

# pack the info button
info.pack()

# functions for the buttons

window.mainloop()