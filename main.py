#import tkinter
from tkinter import *
from tkinter import ttk

#colors
black = '#3b3b3b'
white = '#fff'
blue = '#38576b'
gray = '#d3d3d3'
orange = '#ffab40'

screen = Tk()
screen.title("Calculadora Simples PY")
screen.geometry("235x310")
screen.config(bg=black)

#frames
frame_screen = Frame(screen, width=235, height=50, bg=blue)
frame_screen.grid(row=0, column=0)

frame_body = Frame(screen, width=235, height=268)
frame_body.grid(row=1, column=0)

#variable all_values (concatena os valores)
all_values = ''
value_text = StringVar()

#functions
def input_value(event):

    global all_values
    all_values = all_values + str(event)
    #passando valor para tela
    value_text.set(all_values)

#calculate 
def calculate():
    global all_values
    result = eval(all_values)
    value_text.set(str(result))
    all_values = str("")

#clean screen
def clean_screen():
    global all_values
    all_values = ""
    value_text.set("")

#label
app_label = Label(frame_screen, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=blue, fg=white)
app_label.place(x=0, y=0)

#buttons
#1 line
b1 = Button(frame_body, command = clean_screen, text="C", width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_body, command=lambda:input_value('%'), text="%", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)

b3 = Button(frame_body, command=lambda:input_value('/'), text="/", width=5, height=2, bg= orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

#2 line
b4 = Button(frame_body, command=lambda:input_value('7'), text="7", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)

b5 = Button(frame_body, command=lambda:input_value('8'), text="8", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)

b6 = Button(frame_body, command=lambda:input_value('9'), text="9", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)

b7 = Button(frame_body, command=lambda:input_value('*'), text="*", width=5, height=2, bg= orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

#3 line

b8 = Button(frame_body, command=lambda:input_value('4'), text="4", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)

b9 = Button(frame_body, command=lambda:input_value('5'), text="5", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)

b10 = Button(frame_body, command=lambda:input_value('6'), text="6", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)

b11 = Button(frame_body, command=lambda:input_value('-'), text="-", width=5, height=2, bg= orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

#4 line

b12 = Button(frame_body, command=lambda:input_value('1'), text="1", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)

b13 = Button(frame_body, command=lambda:input_value('2'), text="2", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)

b14 = Button(frame_body, command=lambda:input_value('3'), text="3", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)

b15 = Button(frame_body, command=lambda:input_value('+'), text="+", width=5, height=2, bg= orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

#5 line
b16 = Button(frame_body, command=lambda:input_value('0'), text="0", width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)

b17 = Button(frame_body, command=lambda:input_value('.'), text=".", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)

b18 = Button(frame_body, command = calculate, text="=", width=5, height=2, bg= orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)


screen.mainloop()