# very important to run this pip install gTTS, tkinter, playsound(or dont, )

#very very important libraries to run the GUI and Voice. There are tons and tons of these, use one that you like.

from tkinter import *
from gtts import gTTS
from playsound import playsound

#a Simple Gui window with random parameters, im sure with more effort i can set adjustible pixels, but................
root = Tk() #Calls the tkinter library to do its magic on the downlow.
root.geometry('550x350') #those random numbers
root.resizable(0,0) #More of these
root.config(bg = 'Dark olive green') #go to http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter for complete list of colors(not HTML)
root.title('Say what i type')#Still thinking of a catchy name

#This here incorporates the heading into the Gui
Label(root, text = 'Catchy name' , font='arial 20 bold' , bg ='light cyan').pack()
Label(root, text ='terrible app' , font ='arial 15 bold', bg = 'light cyan').pack(side = BOTTOM)


#Self explaining
Label(root, text ='Enter what you want to hear', font ='arial 15 bold', bg ='light cyan').place(x=20,y=60)


#Input text variable
Msg = StringVar()


#Data entry text box
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

#The function that reads the text then converts it into sound, save the sound file into MP3, then play the sound. MAGIC


def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('motebang.mp3')
    playsound('motebang.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Buttons with basic functionality to play the sound, reset the text or exit the app
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
#need to know how to program sounds that match certain themes, like, Spooky sound would envoke a bla theme, but i have a job so.............
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'red').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)


#If the exit button is not pressed, the program will keep running. 
root.mainloop()
