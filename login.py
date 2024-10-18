from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')

    elif usernameEntry.get()=='shubh' and passwordEntry.get()=='1234':
        #messagebox.showinfo('Success','User Login')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid username or password')

root = CTk()

#window name and size
root.geometry("930x478")
root.title("My App")
root.resizable(0,0) #to diable minimize and mazimise button

#background image, its size, and functionality 
image = CTkImage(Image.open('6057485.jpg'),size=(930,478))
imageLabel = CTkLabel(root,image = image,text="")
imageLabel.place(x=0,y=0)

#Text on login page
heading = CTkLabel(root,text="Employee Managment System",text_color='white',bg_color="#070123",font=('Goudy old Style',20,'bold'))
heading.place(x=360,y=150)

#username and password
usernameEntry = CTkEntry(root,placeholder_text="Username",width=200)
usernameEntry.place(x=390,y=215)
passwordEntry = CTkEntry(root,placeholder_text="Password",width=200,show="*")
passwordEntry.place(x=390,y=265)

#login button
loginButton = CTkButton(root,text="LOGIN",cursor="hand2",command=login) #when hover over login btn cursor changes to hand, choose hand1/hand2
loginButton.place(x=423,y=320)

root.mainloop() #write everything before this main loop