from customtkinter import *
from PIL import Image

#The only_numbers function checks whether the input is numeric.
def only_numbers(char):
    return char.isdigit()

window = CTk()
#window name and size
window.geometry('930x580')
window.resizable(0,0)
window.title("Employee Managment System")

#background image, its size, and functionality 
image = CTkImage(Image.open('ems-bg.jpg'),size=(930,170))
imageLabel = CTkLabel(window,image = image,text="")
imageLabel.grid(row=0,column=0,columnspan=2)

#frame creation
leftFrame = CTkFrame(window)
leftFrame.grid(row=1,column=0)

#id_label
idLabel = CTkLabel(leftFrame, text='Id', font=('arial',18,'bold'))
idLabel.grid(row=0,column=0)
idEntry = CTkEntry(leftFrame, font=('arial',12,'bold'), width=180)
idEntry.grid(row=0,column=1,padx=20,pady=10)

#Name_label
nameLabel = CTkLabel(leftFrame, text='Name', font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0)
nameEntry = CTkEntry(leftFrame, font=('arial',12,'bold'), width=180)
nameEntry.grid(row=1,column=1,)

#Phone_label
phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0)
phoneEntry = CTkEntry(leftFrame, font=('arial',12,'bold'), width=180)
phoneEntry.grid(row=2,column=1,padx=20,pady=10)

#Role_label
roleLabel = CTkLabel(leftFrame, text='Role', font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0)
role_options = ['Web Developer','SOftware Developer','App Developer','Cloud Architect','HR',
                'Network Engineer','Data Analyst','Data Scientist','Project Manager','Sales Manager']
roleBox = CTkComboBox(leftFrame, values=role_options, width=180,state='readonly')
roleBox.grid(row=3,column=1,padx=20,pady=10)
roleBox.set('Select Option')

#gender_label
genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0)
gender_options = ['Male','Female','Transgender']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180,state='readonly')
genderBox.grid(row=4,column=1,padx=20,pady=10)
genderBox.set('Select Option')

#salary_label
salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0)
#to make sure only numerical values are added
vcmd = (leftFrame.register(only_numbers), '%S')
#The validate="key" and validatecommand=vcmd parameters are applied to restrict the input to only digits.
salaryEntry = CTkEntry(leftFrame, font=('arial',12,'bold'), width=180, validate="key", validatecommand=vcmd)
salaryEntry.grid(row=5,column=1,padx=20,pady=10)

rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1) 

window.mainloop()