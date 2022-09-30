# HW
######################
# using tinker library 
# window title should be 
# "My hobby "
# label
# " I LOVE PYTHOON "
import tkinter
window = tkinter.Tk() # this should be the 1st line 
window.title("My hobby")
label1 = tkinter.Label(window,text="I LOVE PYTHON") # defining the label 
label1.grid(column=0 , row= 0) # displaying the label using grid()
window.mainloop()