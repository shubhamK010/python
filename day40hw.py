#HW 

#### RUN THE SAME CODE WITH DIFFERENT ATTRIBUTES OF BUTTON AND ENTRY WIDGETS AND SHARE THE OUTPUT !!!





import tkinter
window = tkinter.Tk()
window.title("Simple Calculator")

# working inside the window

# making Input/Entry box 
e = tkinter.Entry(window, width=60, borderwidth=10,bg="grey")
e.grid(row=0 , column=0, columnspan=3 , padx=10 ,pady=25)
# e.pack()
# creating buttons inside the calc
# Step 1 Definig the buttons numeric and function

button1 = tkinter.Button(window, text=" 1 ",borderwidth=8.5, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button2 = tkinter.Button(window, text=" 2 ",borderwidth=8, padx=42 ,pady=20,bg="blue",fg="white",font="Helvetica")
button3 = tkinter.Button(window, text=" 3 ",borderwidth=8, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button4 = tkinter.Button(window, text=" 4 ",borderwidth=8.5, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button5 = tkinter.Button(window, text=" 5 ",borderwidth=8, padx=42 ,pady=20,bg="blue",fg="white",font="Helvetica")
button6 = tkinter.Button(window, text=" 6 ",borderwidth=8, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button7 = tkinter.Button(window, text=" 7 ",borderwidth=8.5, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button8 = tkinter.Button(window, text=" 8 ",borderwidth=8, padx=42 ,pady=20,bg="blue",fg="white",font="Helvetica")
button9 = tkinter.Button(window, text=" 9 ",borderwidth=8, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button0 = tkinter.Button(window, text=" 0 ",borderwidth=10.5,padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")

# creating function button 

button_add = tkinter.Button(window, text=" + ",borderwidth=10, padx=40 ,pady=20,bg="blue",fg="white",font="Helvetica")
button_equal = tkinter.Button(window, text=" = ",borderwidth=10, padx=103 ,pady=20,bg="grey",fg="white",font="Helvetica")
button_clear = tkinter.Button(window, text=" C ",borderwidth=10, padx=103 ,pady=20,bg="grey",fg="white",font="Helvetica")

# Step 2 Placing the buttons 

# 3rd row
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
# 2nd row

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
# 1st row

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

# 4th row 

button_add.grid(row=5,column=0)
button_equal.grid(row=4, column=1,columnspan=2)
button_clear.grid(row=5, column=1,columnspan=2)

button0.grid(row=4, column=0)








window.mainloop()