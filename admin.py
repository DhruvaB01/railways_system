from tkinter import *
import tkinter
from tkinter import messagebox, font
from tkcalendar import *

import mysql.connector

mydb = mysql.connector .connect (
    host = '127.0.0.1',
    user = 'root',
    password = 'dhruvab',
    database = 'rms'
)

my_cursor = mydb.cursor (buffered= True)

admin = tkinter.Tk()

class Mainpage:

    def __init__(self,admin):

        self.admin= admin
        self.admin.state('zoomed')
        self.admin.geometry('1270x720+320+150')
        self.admin.title('RMS admin')

        sql_query_cityname = 'SELECT cityname FROM City'
        my_cursor.execute(sql_query_cityname)
        options_city = [x[0] for x in my_cursor]

        select_lab = Label(self.admin, text='train type', bg='white', fg='black', font=('seoge UI', 14)).place(x=68, y=50)
        self.select_train_entry = Entry(self.admin,bg= 'white', fg = 'black', font = ('seoge UI', 13))
        self.select_train_entry.place(x = 169, y = 47)
        select_lab_2 = Label(self.admin, text = 'Enter \'D\' for direct train and \'I\' for Indirect train',bg = 'white', fg = 'black', font = ('seoge UI', 13)).place(x= 20,y = 10)


        self.from_menu= StringVar()
        self.from_menu.set("select city")
        from_lab = Label(self.admin, text='From :', bg='white', fg='black', font=('seoge UI', 14)).place(x=68, y=110)
        drop_from= OptionMenu(self.admin, self.from_menu, *options_city)
        drop_from.place(x = 450, y = 110)
        self.from_entry = Entry(self.admin,bg = 'white', fg = 'Black', width= 25 , font= ('seoge UI', 16))
        self.from_entry.place(x= 140,y = 112)


        from_chose_button = Button(self.admin, text='Select', bg='red3', fg='white', font=('seoge UI', 12),command=self.from_show)
        from_chose_button.place(x=560, y=110)


        to_lab = Label(self.admin, text = 'To :', bg = "white", fg = 'black', font= ('seoge UI',14)).place(x = 68, y = 210)
        self.to_menu = StringVar()
        self.to_menu.set('select city')
        drop_to= OptionMenu(self.admin,self.to_menu,*options_city)
        drop_to.place(x= 450, y = 196)

        self.to_entry = Entry(self.admin, bg='white', fg='Black', width=25, font=('seoge UI', 16))
        self.to_entry.place(x=140, y=212)


        to_chose_button = Button(self.admin, text='Select', bg='red3', fg='white', font=('seoge UI', 12),command=self.to_show)
        to_chose_button.place(x=560, y=209)


        date_journey_label = Label(self.admin,text = 'Date : ',fg = 'black', bg = 'white', font = ('seoge UI',14)).place(x = 68, y = 260)

        self.date_entry = Entry(self.admin, bg='white', fg='Black', width=25, font=('seoge UI', 16))
        self.date_entry.place(x=157, y=263)
        date_chose_button = Button(self.admin, text='Select', bg='blue', fg='white', font=('seoge UI', 12),command=self.show_cal)
        date_chose_button.place(x=570, y=263)

        via_label = Label (self.admin,text = 'via: ', fg= 'black', bg = 'white',  font=('seoge UI', 14)).place(x = 68, y = 160)
        self.via_menu = StringVar()
        self.via_menu.set('select city')
        drop_via = OptionMenu(self.admin, self.via_menu, *options_city)
        drop_via.place(x=451, y=158)
        self.via_entry = Entry(self.admin, bg='white', fg='Black', width=25, font=('seoge UI', 16))
        self.via_entry.place(x=140, y=162)


        via_chose_button = Button(self.admin, text='Select', bg='red3', fg='white', font=('seoge UI', 12),command=self.via_show)
        via_chose_button.place(x=560, y=160)

        time_label = Label(self.admin,text ='Time: ' ,bg = 'white', fg = 'black',font = ('seoge UI', 14)).place(x = 68, y = 320)
        self.time_entry = Entry(self.admin, bg='white', fg='Black', width=25, font=('seoge UI', 16))
        self.time_entry.place(x=157, y=323)

        Train_name = Label(self.admin,text = 'train name: ', bg = 'white', fg = 'black', font = ('seoge UI', 14)).place(x=68 ,y = 370)
        self.train_name_entry = Entry(self.admin, bg='white', fg='Black', width=25, font=('seoge UI', 16))
        self.train_name_entry.place(x=187, y=373)

        button_enter = Button(self.admin, text='enter', bg='blue', fg='white', font=('seoge UI', 14),command=self.enter)
        button_enter.place(x=280, y=460)

    def from_show(self):
        self.from_entry.delete(0, END)
        self.from_entry.insert(0, self.from_menu.get())

    def to_show(self):
        self.to_entry.delete(0, END)
        self.to_entry.insert(0, self.to_menu.get())

    def via_show(self):
        self.via_entry.delete(0, END)
        self.via_entry.insert(0, self.via_menu.get())

    def show_cal(self):

        self.cal = Calendar(self.admin, selectmode='day', year=2021, month=11, day=26, date_pattern= 'y/mm/dd')
        self.cal.place(x=180, y=295)

        self.get_date_button = Button(self.admin, text='get date', bg='blue', fg='white', font=('seoge UI', 12),command=self.getdate)
        self.get_date_button.place(x=490, y=263)

        destroy_cal_button = Button(self.admin,text = 'x', bg= 'red3', fg= 'white', font = ('seoge UI', 13), command = self.cal.destroy)
        destroy_cal_button.place (x = 640, y = 263)

    def getdate(self):
        self.date_entry.delete(0, END)
        self.date_entry.insert(0, self.cal.get_date())
        self.cal.destroy()
        self.get_date_button.destroy()



    def enter (self):

        if self.select_train_entry.get()=='D':

            if self.from_entry.get() == 'select city' or self.to_entry.get() == 'select city' or self.to_entry.get()== '' or self.from_entry.get() == '':
                messagebox.showerror('Invalid city','please check the cities selected')

            elif self.train_name_entry.get == '':
                messagebox.showerror('No train name', 'Please enter name of train')

            else :
                sql_query_avail_1= 'INSERT INTO Available_trains (Train_name , From_city, To_city, Date_travel, Time_travel) VALUES (%s,%s,%s,%s,%s)'
                query_input_1 = (self.train_name_entry.get(), self.from_entry.get(), self.to_entry.get(), self.date_entry.get(), self.time_entry.get())
                my_cursor.execute(sql_query_avail_1,query_input_1)
                mydb.commit()

        elif self.select_train_entry.get()== 'I':

            if self.from_entry.get() == 'select city' or self.to_entry.get() == 'select city' or self.via_entry.get()== 'select city':
                messagebox.showerror('Invalid city','please check the cities selected')

            elif self.train_name_entry.get()== '':
                messagebox.showerror('No train name', 'Please enter name of train')

            else:
                sql_query_avail_2 = 'INSERT INTO Available_trains (Train_name , From_city,via_city, To_city, Date_travel, Time_travel) VALUES (%s,%s,%s,%s,%s,%s)'
                query_input_2 = (self.train_name_entry.get(),self.from_entry.get(),self.via_entry.get(), self.to_entry.get(), self.date_entry.get(), self.time_entry.get())
                my_cursor.execute(sql_query_avail_2,query_input_2)
                mydb.commit()












objAdmin =  Mainpage(admin)
admin.mainloop()