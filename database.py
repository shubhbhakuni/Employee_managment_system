import pymysql
from tkinter import messagebox

#connecting database
def connect_database():
    try:
        conn = pymysql.connect(host='localhost',user='root',password='0211')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong')
        return 

    #creating database
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20) PRIMARY KEY, Name VARCHAR(50), Phone VARCHAR(12), Role VARCHAR(50), Gender VARCHAR(10), Salary DECIMAL(10,2))')

def insert(id, name, phone, role, gender, salary):
    print(id, name, phone, role, gender, salary)

connect_database()