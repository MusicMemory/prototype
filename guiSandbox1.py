from Tkinter import *

window = Tk()
window.title("Mein erstes GUI-Programm")
window.geometry("300x300")

myImage = PhotoImage(file="images/Sun.png")

def ausgabe():
    print "Mache was"

graphicalButton = Button(window, text="Klick mich!", command=ausgabe, image=myImage)
graphicalButton.pack()

inputField = Entry(window)
inputField.pack()

aLabel = Label(text="Initialer Text")
aLabel.pack()

def lesen():
    aLabel.configure(text=inputField.get())

standardButton = Button(window, text="Klick mich!", command=lesen)
standardButton.pack()

mainloop()