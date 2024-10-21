from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database

#Define Functions

def delete_all():
    result = messagebox.askyesno('Confirm','Do you really want to DELETE ALL data?')
    if result:
        database.delete_all_records()
        treeview_data()
        clear_entries() 
        messagebox.showinfo('Success','All data deleted successfully')

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Select Option')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Select Option':
        messagebox.showerror('Error','Select an option to search')
    else:
        searched_data=database.search (searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END , values=employee)

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select an employee to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear_entries()
        messagebox.showinfo('Success','Employee deleted successfully')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select an employee to update')
    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear_entries()
        messagebox.showinfo('Success','Employee Data updated successfully')

def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear_entries()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear_entries(value=False):
    if value :
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    salaryEntry.delete(0,END)
    roleBox.set('Select Option')
    genderBox.set('Select Option')

#display data in side treeview
def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END , values=employee)

#Define Function of ADD button
def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear_entries()
        messagebox.showinfo('Success','Employee added successfully')


#The only_numbers function checks whether the input in phone & salary field is numeric.
def only_numbers(char):
    return char.isdigit()

window = CTk()
#window name and size
window.geometry('930x580+100+100')
window.resizable(0,0)
window.title("Employee Managment System")

#background image, its size, and functionality 
image = CTkImage(Image.open('ems-bg.jpg'),size=(930,158))
imageLabel = CTkLabel(window,image = image,text="")
imageLabel.grid(row=0,column=0,columnspan=2)

#frame creation
leftFrame = CTkFrame(window)
leftFrame.grid(row=1,column=0)

#id_label
idLabel = CTkLabel(leftFrame, text='Id', font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,sticky='w',padx=20)
idEntry = CTkEntry(leftFrame, font=('arial',16,'bold'), width=160)
idEntry.grid(row=0,column=1,padx=13,pady=15)

#Name_label
nameLabel = CTkLabel(leftFrame, text='Name', font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,sticky='w',padx=20)
nameEntry = CTkEntry(leftFrame, font=('arial',16,'bold'), width=160)
nameEntry.grid(row=1,column=1,padx=13,pady=15)

#Phone_label
phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,sticky='w',padx=20)
#to make sure only numerical values are added
vcmd = (leftFrame.register(only_numbers), '%S')
#The validate="key" and validatecommand=vcmd parameters are applied to restrict the input to only digits.
phoneEntry = CTkEntry(leftFrame, font=('arial',16,'bold'), width=160, validate="key", validatecommand=vcmd)
phoneEntry.grid(row=2,column=1,padx=13,pady=15)

#Role_label
roleLabel = CTkLabel(leftFrame, text='Role', font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,sticky='w',padx=20)
role_options = ['Web Developer','Software Developer','App Developer','Cloud Architect','HR',
                'Network Engineer','Data Analyst','Data Scientist','Project Manager','Sales Manager']
roleBox = CTkComboBox(leftFrame, values=role_options, width=160,state='readonly')
roleBox.grid(row=3,column=1,padx=13,pady=15)
roleBox.set('Select Option')

#gender_label
genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,sticky='w',padx=20)
gender_options = ['Male','Female','Other']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=160,state='readonly')
genderBox.grid(row=4,column=1,padx=13,pady=15)
genderBox.set('Select Option')

#salary_label
salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,sticky='w',padx=20)
#to make sure only numerical values are added
# vcmd = (leftFrame.register(only_numbers), '%S')
#The validate="key" and validatecommand=vcmd parameters are applied to restrict the input to only digits.
salaryEntry = CTkEntry(leftFrame, font=('arial',16,'bold'), width=160)
salaryEntry.grid(row=5,column=1,padx=13,pady=15)


rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1) 

#search options
search_options=['Select Option','Id','Name','Phone','Role','Gender','Salary']
searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Select Option')

#search bar
searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

#search button
searchButton = CTkButton(rightFrame, text='SEARCH',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

#Show All Button
showallButton = CTkButton(rightFrame, text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

#Treeview
tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns'] = ('Id','Name','Phone','Role','Gender','Salary')
#headings of column
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=130)
tree.column('Role',width=160)
tree.column('Gender',width=100)
tree.column('Salary',width=130)

#scrollbar
scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL)
scrollbar.grid(row=1,column=4,sticky='ns')
 
#styling the heading
style = ttk.Style()
style.configure('Treeview.Heading', font=('arial',12,'bold'))
style.configure('Treeview', font=('arial',15,'bold'), rowheight=30)

#Button on lower side
buttonFrame = CTkFrame(window)
buttonFrame.grid(row=2,column=0,columnspan=2)

#New button
NewButton = CTkButton(buttonFrame, text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear_entries(True))
NewButton.grid(row=0,column=0,padx=13,pady=10)

#add button
addButton = CTkButton(buttonFrame, text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,padx=13,pady=10)

#update button
updateButton = CTkButton(buttonFrame, text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,padx=13,pady=10)

#delete button
deleteButton = CTkButton(buttonFrame, text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=13,pady=10)

#Delete ALL button
deleteallButton = CTkButton(buttonFrame, text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,padx=13,pady=10)

treeview_data()

window.bind('<ButtonRelease>', selection)

window.mainloop() 