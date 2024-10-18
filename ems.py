from customtkinter import *
from PIL import Image

window = CTk()
#window name and size
window.geometry('930x580')
window.resizable(0,0)
window.title("Employee Managment System")

#background image, its size, and functionality 
image = CTkImage(Image.open('ems-bg.jpg'),size=(930,170))
imageLabel = CTkLabel(window,image = image,text="")
imageLabel.grid(row=0,column=0)

window.mainloop()