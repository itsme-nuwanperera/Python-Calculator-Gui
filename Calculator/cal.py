from tkinter import *  
from tkinter import messagebox
import webbrowser
import pygame

# Window Setup
window = Tk()
window.geometry("460x640+400+200")
window.resizable(0,0)
window.title("Calculator")
window.iconbitmap(r"C:\Users\nuwan\Developer\Simple Projects\Calculator\calculator.ico")

#setting the values
var = ""
A = 0
operator = ""
His = []
count =1
temp_1 = 0
temp_2 = 1

# Initialize mixer module in pygame
pygame.mixer.init()

#func for button click sound
def play_sound():
   pygame.mixer.music.load(r"C:\Users\nuwan\Developer\Simple Projects\Calculator\Click_Sound.mp3")
   pygame.mixer.music.play()

def play_sound2():
   pygame.mixer.music.load("Simple Projects/Calculator/flying_kiss.mp3")
   pygame.mixer.music.play()

def play_sound3():
   pygame.mixer.music.load("Simple Projects/Calculator/wtf.mp3")
   pygame.mixer.music.play()

#func for Link
def callback(url):
   webbrowser.open_new_tab(url)

def close_win(e):
    window.destroy()


def key_response(event):
    if (event.char) == "1":
        b1_Pressed()

    elif (event.char) == "2":
        b2_Pressed()

    elif (event.char) == "3":
        b3_Pressed()

    elif (event.char) == "4":
        b4_Pressed()

    elif (event.char) == "5":
        b5_Pressed()

    elif (event.char) == "6":
        b6_Pressed()

    elif (event.char) == "7":
        b7_Pressed()

    elif (event.char) == "8":
        b8_Pressed()

    elif (event.char) == "9":
        b9_Pressed()

    elif (event.char) == "0":
        b0_Pressed()

    elif (event.char) == "c":
        bCLEAR_pressed()

    elif (event.char) == "+":
        bADD_presed()

    elif (event.char) == "*":
        bMULTIPLIED_presed()

    elif (event.char) == "-":
        BSubtracted()

    elif (event.char) == "/":
        bDIVIDE_presed()

    elif (event.char) == ".":
        bDOT_Pressed()


# funcs for buttons

def history_Pressed():
    global var, His, count, temp_1, temp_2, msg
    play_sound()
    count =1
    temp_1 = 0
    temp_2 = 1
    msg = "(" + str(count) + ") " + str(His[temp_1]) + str(His[temp_2])
    data.set(msg)
    

def up_pressed():
    global count, temp_2, temp_1, msg
    play_sound()
    count = count + 1
    temp_1 =temp_1 + 2
    temp_2 =temp_2 + 2
    msg = "(" + str(count) + ") " + str(His[temp_1]) + str(His[temp_2])
    data.set(msg)

def down_pressed():
    global count, temp_2, temp_1, msg
    play_sound()
    count = count - 1
    temp_1 =temp_1 - 2
    temp_2 =temp_2 - 2
    msg = "(" + str(count) + ") " + str(His[temp_1]) + str(His[temp_2])
    data.set(msg)

def b0_Pressed():
    global var
    play_sound()
    var = var + "0"
    data.set(var)

def b1_Pressed():
    global var
    play_sound()
    var = var + "1"
    data.set(var)

def b2_Pressed():
    global var
    play_sound()
    var = var + "2"
    data.set(var)

def b3_Pressed():
    global var
    play_sound()
    var = var + "3"
    data.set(var)

def b4_Pressed():
    global var
    play_sound()
    var = var + "4"
    data.set(var)

def b5_Pressed():
    global var
    play_sound()
    var = var + "5"
    data.set(var)

def b6_Pressed():
    global var
    play_sound()
    var = var + "6"
    data.set(var)

def b7_Pressed():
    global var
    play_sound()
    var = var + "7"
    data.set(var)

def b8_Pressed():
    global var
    play_sound()
    var = var + "8"
    data.set(var)

def b9_Pressed():
    global var
    play_sound()
    var = var + "9"
    data.set(var)

def bDOT_Pressed():
    global var
    play_sound()
    var = var + "."
    data.set(var)

def bADD_presed ():
    global A, var, operator  
    play_sound()
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    data.set(var)  

def BSubtracted ():
    global A, var, operator  
    play_sound()
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    data.set(var)  

def bMULTIPLIED_presed ():
    global A, var, operator  
    play_sound()
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    data.set(var)  

def bDIVIDE_presed ():
    global A, var, operator  
    play_sound()
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    data.set(var)  

def bEQUAL_pressed():
    play_sound()
    global A  
    global operator  
    global var  
    

    var2 = var 
    var = var + "="
    His.append(var)
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:    
            messagebox.showerror(title= "Undefined", message="Division by 0 Not Allowed.")
            A == ""  
            var = ""  
            data.set(var)  
        else:  
            x = float(A/a)  
            data.set(x)  
            var = str(x)  
    His.append(x)

def bCLEAR_pressed():  
    global A , temp_1, temp_2, count 
    global var  
    global operator  
    play_sound()
    var = ""  
    A = 0   
    operator = ""  
    data.set(var)  

# creating the label for the window  
data = StringVar()  
CALLabel = Label(  
    window,  
    text = "Label",  
    anchor = SE,  
    font = ("Digital-7", 30),  
    textvariable = data,
    background = "#192431",  
    fg = "#e9eaec"  
)  
# using the pack() method  
CALLabel.pack(expand = True, fill = "both")  

# creating the frames for the buttons 

f0 = Frame(window, bg = "#192431")
f0.pack(expand = True, fill = "both")
f1 = Frame(window, bg = "#192431")  
f1.pack(expand = True, fill = "both") 
 
f2 = Frame(window, bg = "#192431")  
f2.pack(expand = True, fill = "both")  
 
f3 = Frame(window, bg = "#192431")  
f3.pack(expand = True, fill = "both")  
 
f4 = Frame(window, bg = "#192431")  
f4.pack(expand = True, fill = "both")  

border_color = Frame(window, background="red")
#creating Buttons
button7 = Button(  
    f1,  
    text = "7",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0,  
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec',
    command = b7_Pressed
    
)  
button7.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button8 = Button(  
    f1,  
    text = "8",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = b8_Pressed
)   
button8.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button9 = Button(  
    f1,  
    text = "9",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0,  
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec',
    command = b9_Pressed
)    
button9.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

buttonADD = Button(  
    f1,  
    text = "+",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4, 
    bg='#1c2938',
    fg='#e9eaec',
    command = bADD_presed  
)  
buttonADD.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button4 = Button(  
    f2,  
    text = "4",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = b4_Pressed  
)   
button4.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button5 = Button(  
    f2,  
    text = "5",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0,
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec',  
    command = b5_Pressed
)  
button5.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button6 = Button(  
    f2,  
    text = "6",  
    font = ("Impact", 22), 
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4, 
    bg='#1c2938',
    fg='#e9eaec',
    command = b6_Pressed  
)  
button6.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonSUBSTRACT = Button(  
    f2,  
    text = "-",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4, 
    bg='#1c2938',
    fg='#e9eaec',
    command = BSubtracted
)  
buttonSUBSTRACT.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3)  

button1 = Button(  
    f3,  
    text = "1",  
    font = ("Impact", 22), 
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = b1_Pressed 
)  
button1.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

button2 = Button(  
    f3,  
    text = "2",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0,  
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec',
    command = b2_Pressed  
)  
button2.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

button3 = Button(  
    f3,  
    text = "3",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = b3_Pressed  
)  
button3.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonMULTIPY = Button(  
    f3,  
    text = "×",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = bMULTIPLIED_presed
)  
buttonMULTIPY.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

button0 = Button(  
    f4,  
    text = "0",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 2, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = b0_Pressed
)  
button0.pack(side = LEFT, expand = True, fill = "both", padx=2, pady=2) 

buttonDOT = Button(  
    f4,  
    text = ".",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = bDOT_Pressed  
)  
buttonDOT.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonEQUAL = Button(  
    f4,  
    text = "=",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4, 
    bg='#1c2938',
    fg='#e9eaec',
    command = bEQUAL_pressed
)  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonC = Button(  
    f0,  
    text = "C",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0,  
    height= 1, width=32,
    bg='#1c2938',
    fg='#b70000',
    command = bCLEAR_pressed
)  
buttonC.place(x=3, y=3)
#buttonC.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonDIVIDE = Button(  
    f4,  
    text = "÷",  
    font = ("Impact", 22),  
    relief = GROOVE,  
    border = 0, 
    height= 1, width=4,
    bg='#1c2938',
    fg='#e9eaec', 
    command = bDIVIDE_presed  
)  
buttonDIVIDE.pack(side = LEFT, expand = True, fill = "both", padx=3, pady=3) 

buttonhis = Button(  
    window,  
    text = "↺",  
    font = ("Impact", 12),  
    relief = GROOVE,  
    border = 0,  
    height= 1, width=2,
    bg='#1c2938',
    fg='#e9eaec',
    command = history_Pressed  
)  
buttonhis.place(x=4, y=35)

buttonup = Button(  
    window,  
    text = "↑",  
    font = ("Impact", 6),  
    relief = GROOVE,  
    border = 0,  
    height= 2, width=4,
    bg='#1c2938',
    fg='#e9eaec',
    command = up_pressed 
)  
buttonup.place(x=4, y=6 )

buttondown = Button(  
    window,  
    text = "↓",  
    font = ("Impact", 6),  
    relief = GROOVE,  
    border = 0,  
    height= 2, width=4,
    bg='#1c2938',
    fg='#e9eaec',
    command = down_pressed 
)  
buttondown.place(x=4, y=69)


window.config(background="#192431")

link = Label(window, 
    text="@NuOne Perera",
    font=('Freestyle Script', 10),
    background = "#192431",  
    fg = "#e9eaec" , 
    cursor="hand2")
link.pack(side=RIGHT, fill=X )
link.bind("<Button-1>", lambda e:
callback("https://web.facebook.com/itsme.nuwanperera"))

#key bindings
window.bind('<Key>', lambda e : key_response(e))
window.bind('<Return>', lambda e: bEQUAL_pressed())
window.bind('<Escape>', lambda e: close_win(e))

window.mainloop()
