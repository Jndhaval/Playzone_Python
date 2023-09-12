from tkinter import *
import pygame
import tkinter.messagebox
from PIL import Image, ImageTk
import os

# Setup display
# Creating widget
root = Tk()
root.geometry("1280x693+35+0")
root.title("TIC TAC TOE")

# Background image
pic = Image.open("img/ticbg.jpg")
open_img = ImageTk.PhotoImage(pic)
img = Label(root, image=open_img)
img.place(x=0, y=0)

# Sound
pygame.mixer.init()
pygame.mixer.music.load("sound/tic_theme.mp3")
pygame.mixer.music.play(loops=5)

# Label for title
Tops = Frame(root, bg='#000000', pady=2, width=1250, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)
lblTitle = Label(Tops, font=('jokerman', 50, 'bold'), text="tic tAc tOE", bd=15, fg='#8a0776', bg='#000000', justify=CENTER, relief=RIDGE)
lblTitle.grid(row=0, column=0)

# Board configurations
MainFrame = Frame(root, bg='#8a0776', pady=2, width=1250, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=450, pady=2, padx=10, bg='#8a0776', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=750, height=500, padx=10, pady=2, bg='#8a0776', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=600, height=200, padx=10, pady=2, bg='#000000', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=360, padx=10, pady=2, bg='#000000', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

# Player variables
PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

Player1 = StringVar()
Player2 = StringVar()
pa = StringVar()
pb = StringVar()
buttons = StringVar()

# For X
click = True
# Counter
flag = 0

# Label for X's & O's turn
Bottom = Frame(root, bg='#000000', pady=2, width=1250, height=100, relief=RIDGE)
Bottom.grid(row=2, column=0)
lblTitle = Label(Bottom, font=('jokerman', 20, 'bold'), text="X's turn", bd=5, fg='#FFFFFF', bg='#000000', justify=CENTER, relief=RIDGE)
lblTitle.grid(row=2, column=0)


# checker button function
def checker(buttons):
    global click, flag

    # For marking X
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        buttons.configure(background="#000000", fg='#FFFFFF')
        Bottom = Frame(root, bg='#000000', pady=2, width=1250, height=100, relief=RIDGE)
        Bottom.grid(row=2, column=0)
        lblTitle = Label(Bottom, font=('jokerman', 20, 'bold'), text="O's turn", bd=5, fg='#FF69B4', bg='#000000', justify=CENTER, relief=RIDGE)
        lblTitle.grid(row=2, column=0)
        click = False
        flag += 1
        scorekeeper()

    # For marking O
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        buttons.configure(background="#000000", fg='#FF69B4')
        Bottom = Frame(root, bg='#000000', pady=2, width=1250, height=100, relief=RIDGE)
        Bottom.grid(row=2, column=0)
        lblTitle = Label(Bottom, font=('jokerman', 20, 'bold'), text="X's turn", bd=5, fg='#FFFFFF', bg='#000000', justify=CENTER, relief=RIDGE)
        lblTitle.grid(row=2, column=0)
        click = True
        flag += 1
        scorekeeper()

    else:
        tkinter.messagebox.showerror("Tic Tac Toe", "Hey! that box has already been selected\nPick Another Box....")


# Label for Player X
lblPlayerX = Label(RightFrame1, font=('ravie', 30, 'bold'), text="Player X :", padx=2, pady=2, bg="#000000", fg="#FFFFFF")
lblPlayerX.grid(row=0, column=0, sticky=W)
# Player X name
nmPlayerX = Entry(RightFrame1, font=('ravie', 30, 'bold'), bd=3, fg="#000000", textvariable=Player1, width=6, justify=LEFT)
nmPlayerX.grid(row=0, column=1)
# Player X score
txtPlayerX = Button(RightFrame1, font=('ravie', 26, 'bold'), bd=2, fg="#FFFFFF", bg="#000000", textvariable=PlayerX, width=3, justify=LEFT)
txtPlayerX.grid(row=0, column=2)

# Label for Player O
lblPlayerO = Label(RightFrame1, font=('ravie', 30, 'bold'), text="Player O :", padx=2, pady=2, bg="#000000", fg="#FFFFFF")
lblPlayerO.grid(row=1, column=0, sticky=W)
# Player O name
nmPlayerO = Entry(RightFrame1, font=('ravie', 30, 'bold'), bd=3, fg="#000000", textvariable=Player2, width=6, justify=LEFT)
nmPlayerO.grid(row=1, column=1)
# Player O score
txtPlayerO = Button(RightFrame1, font=('ravie', 26, 'bold'), bd=2, fg="#FFFFFF", bg="#000000", textvariable=PlayerO, width=3, justify=LEFT)
txtPlayerO.grid(row=1, column=2)


# Winner decisive
def scorekeeper():
    global pa, pb, Player1, Player2, winner
    winner = False
    # Check for X
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.configure(background='#8a0776')
        button2.configure(background='#8a0776')
        button3.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button6.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.configure(background='#8a0776')
        button8.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.configure(background='#8a0776')
        button4.configure(background='#8a0776')
        button7.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button8.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.configure(background='#8a0776')
        button6.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button7.configure(background='#8a0776')
        winner = True
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        pa = Player1.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)
        reset()
    # Check for O
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.configure(background='#8a0776')
        button2.configure(background='#8a0776')
        button3.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button6.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.configure(background='#8a0776')
        button8.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.configure(background='#8a0776')
        button4.configure(background='#8a0776')
        button7.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button8.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.configure(background='#8a0776')
        button6.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button9.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    elif button5["text"] == "O" and button7["text"] == "O" and button3["text"] == "O":
        button3.configure(background='#8a0776')
        button5.configure(background='#8a0776')
        button7.configure(background='#8a0776')
        winner = True
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        pb = Player2.get() + " Won the Game!!"
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)
        reset()
    # Check if tie
    if flag == 9 and winner == False:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It is a tie!\nNo One Wins!")
        reset()


# New Game function
def Newgame():
    global pa, pb, Player1, Player2, flag
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    Player1 = StringVar()
    Player2 = StringVar()

    # Player X name
    nmPlayerX = Entry(RightFrame1, font=('ravie', 30, 'bold'), bd=3, fg="#000000", textvariable=Player1, width=6, justify=LEFT)
    nmPlayerX.grid(row=0, column=1)
    # Player O name
    nmPlayerO = Entry(RightFrame1, font=('ravie', 30, 'bold'), bd=3, fg="#000000", textvariable=Player2, width=6, justify=LEFT)
    nmPlayerO.grid(row=1, column=1)


# Newgame button
btnNewGame = Button(RightFrame2, text="New  Game", font=('ravie', 30, 'bold'), height=1, width=15, fg='#FFFFFF', bg='#8a0776', command=Newgame)
btnNewGame.grid(row=1, column=0, padx=1, pady=11)

# Building buttons
button1 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button1))
button2 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button2))
button3 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button3))

button4 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button4))
button5 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button5))
button6 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button6))

button7 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button7))
button8 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button8))
button9 = Button(LeftFrame, text=" ", font=('ravie', 20, 'bold'), height=3, width=8, bg='#FFFFFF', command=lambda: checker(button9))


# Start the game over!
# Reset function
def reset():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global click, flag
    flag = 0

    # Configuring and Griding the buttons to the screen
    button1["text"] = " "
    button1.configure(background='#000000')
    button1.grid(row=1, column=0, sticky=S + N + E + W)
    button2["text"] = " "
    button2.configure(background='#000000')
    button2.grid(row=1, column=1, sticky=S + N + E + W)
    button3["text"] = " "
    button3.configure(background='#000000')
    button3.grid(row=1, column=2, sticky=S + N + E + W)

    button4["text"] = " "
    button4.configure(background='#000000')
    button4.grid(row=2, column=0, sticky=S + N + E + W)
    button5["text"] = " "
    button5.configure(background='#000000')
    button5.grid(row=2, column=1, sticky=S + N + E + W)
    button6["text"] = " "
    button6.configure(background='#000000')
    button6.grid(row=2, column=2, sticky=S + N + E + W)

    button7["text"] = " "
    button7.configure(background='#000000')
    button7.grid(row=3, column=0, sticky=S + N + E + W)
    button8["text"] = " "
    button8.configure(background='#000000')
    button8.grid(row=3, column=1, sticky=S + N + E + W)
    button9["text"] = " "
    button9.configure(background='#000000')
    button9.grid(row=3, column=2, sticky=S + N + E + W)


# Exit function
def exit1():
    pygame.quit()
    root.destroy()
    os.system('menu.py')


# Exit button
btnExit = Button(RightFrame2, text="Exit", font=('ravie', 30, 'bold'), height=1, width=15, fg='#FFFFFF', bg='#8a0776', command=exit1)
btnExit.grid(row=3, column=0, padx=1, pady=11)

# Create Menu
my_menu = Menu(root)
root.configure(menu=my_menu)

# Create Options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="OPTIONS", menu=options_menu)
options_menu.add_command(label="New Game", command=Newgame)
options_menu.add_separator()
options_menu.add_command(label="Reset Grid", command=reset)
options_menu.add_separator()
options_menu.add_command(label="Exit", command=exit1)

reset()
root.mainloop()