from tkinter import *
import tkinter
from tkinter import messagebox, font
from tkcalendar import *

import re

import Image
import ImageTk

import mysql.connector

import smtplib

mydb = mysql.connector .connect (
    host = '127.0.0.1',
    user = 'root',
    password = 'dhruvab',
    database = 'rms'
)

my_cursor = mydb.cursor (buffered= True)

root = tkinter.Tk()


class Login :


    def __init__(self, root):

        self.root = root
        self.root.title ('railway management system')
        self.root.iconbitmap(r'C:\Users\deepa\OneDrive\Pictures\New folder\87877_naruto_129x129 (4).png')
        self.root.geometry('1270x720+320+150')
        self.root.resizable (False,False)
        self.background_root = ImageTk.PhotoImage(Image.open(r'C:\Users\deepa\OneDrive\Pictures\New folder\9-indian-railway-irctc.jpg'))
        background_root_label= Label(image = self.background_root).place(x = 350, y =0, relheight =1, relwidth =1 )

        login_frame = Frame (self.root, bg = 'white')
        login_frame.place(x= 0 , y = 0, height = 750, width = 490)

        login_label = Label (login_frame ,text = 'Login',font = ('Impact',35), bg = 'white', fg  = 'black')
        login_label.place(x= 180, y = 80)

        username_login = Label (login_frame, text = 'Username : ',font =('Calibri',18), bg = 'white', fg = 'black')
        username_login.place (x= 20, y = 220)
        self.username_check = Entry(login_frame, width = 45, bg = 'white' ,fg = 'red3', bd = 0 , borderwidth = 5)
        self.username_check.place(x= 160,y= 225)


        password_label = Label (login_frame, text= 'Password :', font = ('Calibri',18), bg= 'white', fg = 'black')
        password_label.place(x= 20 ,y= 300)
        self.password_check = Entry (login_frame , width = 45 , bg = 'white', fg  = 'red3', bd= 0 , borderwidth = 5)
        self.password_check.place (x = 160 , y = 305)



        login = Button(login_frame, text='→', bg='red3', fg='white', font=('Impact', 20), cursor='hand2',command = self.login_function)
        login.place(x=215, y=390)

        forget_pass = Button(login_frame, text='forgot password?',font = ('seoge UI', 10), bd=0, bg='white', fg='red3', cursor='hand2',command = self.forgot_password)
        forget_pass.place(x=25, y=480)

        signin_label = Label(login_frame, text='don\'t have an account? ', font=('seoge UI', 12), bg='white', fg='black')
        signin_label.place(x=25, y=540)
        signin_button = Button(login_frame, text='Sign in', bg='white', fg='red3', font=('seoge UI', 14),cursor='hand2',borderwidth = 0, command = self.sign_in_open)
        signin_button.place(x=210, y=535)


    def sign_in_open(self):

        self.root.withdraw()
        self.sign_in = Toplevel(bg = 'white')
        self.sign_in.title('sign in')
        self.sign_in.overrideredirect(True)
        self.sign_in.geometry('600x800+700+150')
        self.sign_in.resizable(False, False)

        sign_in_label = Label(self.sign_in, text='SIGN IN', font=('Impact', 27), bg='white', fg='black').place(x=245, y=50)


        username_label = Label(self.sign_in, text='Username ', font=('seoge UI', 12), bg='white',fg='black').place(x=65, y=150)
        self.username_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.username_entry.place(x=180, y=150, width=350, height=30)

        email_id_label = Label(self.sign_in, text='email id ', font=('seoge UI', 12), bg='white', fg='black').place(x=65, y=200)
        self.email_id_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.email_id_entry.place(x=180, y=200, width=350, height=30)

        firstname_label = Label (self.sign_in, text = 'First name', font = ('seoge UI', 12), bg='white',fg='black').place(x= 65, y = 250)
        self.firstname_entry = Entry (self.sign_in, width = 50 , bd = 0, bg = 'white', fg ='black', borderwidth = 3 )
        self.firstname_entry.place(x = 180 , y = 250 , width = 350, height = 30)

        lastname_label = Label(self.sign_in , text = 'Lastname', font = ('seoge UI', 12), bg='white',fg='black').place(x= 65, y = 300)
        self.lastname_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.lastname_entry.place(x=180, y=300, width=350, height=30)

        phone_no_label = Label(self.sign_in , text = 'Phone no.', font = ('seoge UI', 12), bg='white',fg='black').place(x= 65, y = 350)
        self.phone_no_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.phone_no_entry.place(x=180, y=350, width=350, height=30)

        address_label = Label (self.sign_in , text = 'address', font = ('seoge UI', 12), bg='white',fg='black').place(x= 65, y = 400)
        self.address_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.address_entry.place(x=180, y=400, width=350, height=30)

        gender_label = Label (self.sign_in, text = 'Gender', font = ('seoge UI', 12), bg='white',fg='black' ).place (x=65 , y = 450)
        self.gender_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.gender_entry.place(x=180, y=450, width=350, height=30)


        password_label = Label(self.sign_in, text='Password  ', font=('seoge UI', 12), bg="white",fg='black').place(x=65, y=500)
        self.password_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.password_entry.place(x=180, y=500, width=350, height=30)

        confirm_password = Label(self.sign_in, text='Confirm Password', font=('seoge UI', 12), bg="white",fg='black').place(x=40, y=550)
        self.confirm_password_entry = Entry(self.sign_in, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.confirm_password_entry.place(x=180, y=550, width=350, height=30)

        _lab = Label (self.sign_in, text = '*', fg = 'red3', bg = 'white', font =('seoge UI', 14) ).place(x = 29, y = 670)
        warning_label = Label(self.sign_in, text = 'please enter all details correctly.', fg = 'black', bg = 'white', font =('seoge UI', 12) ).place(x = 40 , y = 670)

        done_button = Button(self.sign_in, text='DONE', font=23, bg='red3', fg='white',command = self.sign_in_function)
        done_button.place(x=272, y=600)

        close_signin = Button(self.sign_in, text='x',font =('seoge UI', 14),  command=self.destroy_signin, bg='red3', fg='white',highlightthickness=0, cursor='hand2')
        close_signin.place(x=560, y=15)



    def destroy_signin(self):

        self.sign_in.destroy()
        self.root.deiconify()


    def sign_in_function(self):

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if self.username_entry.get() == '' or self.email_id_entry.get() =='' or self.password_entry.get == '' or\
        self.confirm_password_entry.get()== '' or self.firstname_entry.get()== '' or self.address_entry.get() == '' or\
        self.phone_no_entry.get== '' or self.lastname_entry.get() == '' or self.gender_entry.get()== '' :

            messagebox.showerror('incomplete details', 'please fill all the required feilds')

        elif not self.gender_entry.get() == 'M' or self.gender_entry.get()== 'F':
            messagebox.showerror('incorrect gender', 'enter either F for female or M for male')

        elif not (re.search(regex, self.email_id_entry.get())):
            messagebox.showwarning('invalid email', 'please eneter a valid email id')

        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror('password incorrect', 'passwords don\'t match')

        elif len(self.username_entry.get()) <= 8:
            messagebox.showerror('username too small', 'usmername must be at least 8 characters long')

        else:
            sqlsignin = 'INSERT INTO userinfo (Username, Firstname ,Surname,Phoneno,Email,UserPassword,Address) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            x1 = (self.username_entry.get(), self.firstname_entry.get(), self.lastname_entry.get(),
                  self.phone_no_entry.get(), self.email_id_entry.get(), self.password_entry.get(), self.address_entry.get())
            my_cursor.execute(sqlsignin, x1)
            mydb.commit()

            self.sign_in.destroy()
            self.root.deiconify()



    def login_function(self):

        user_check_sql = 'SELECT Username FROM userinfo'
        check_variable_user = True
        my_cursor.execute(user_check_sql)
        for ele1 in my_cursor:
            if ele1[0] == self.username_check.get():
                check_variable_user= True
                break
        else:
            check_variable_user= False

        password_check_sql = 'SELECT UserPassword FROM userinfo WHERE Username = %s'
        check_password_variable = True
        y3= (str(self.username_check.get()),)
        my_cursor.execute(password_check_sql,y3)

        for ele2 in my_cursor:
            if ele2[0] == self.password_check.get():
                check_password_variable = True
                break
        else:
            check_password_variable = False



        if self.username_check.get() == '' :
            messagebox.showerror('Invalid Credentials', 'All fields must be filled properly', parent = self.root)


        elif (check_variable_user== False):
            messagebox.showerror('Invalid username ', 'Username not in database')

        elif(check_password_variable == False):
            messagebox.showerror('Incorrect password','Please enter correct password' )

        else:
            self.root.withdraw()
            self.objmainscreen = Mainpage(root)

    def forgot_password(self):

        def passchk_2(self):

            pass_chk_2 = 'SELECT UserPassword FROM userinfo WHERE Username = %s  '
            y3 = (str(self.username_check.get()),)
            my_cursor.execute(pass_chk_2,y3)
            for checkpass in my_cursor:
                pass
            return checkpass[0]

        def userchk_2(self):

            usr_check_2 = 'SELECT Username FROM userinfo '
            check_variable_user = True
            my_cursor.execute(usr_check_2)

            for ele in my_cursor:
                if ele[0] == self.username_check.get():
                    check_variable_user = True
                    break
            else:
                check_variable_user = False

            return check_variable_user

        if (userchk_2(self) == True):

            user_email_id = 'SELECT Email FROM userinfo WHERE Username = %s '
            y2 = (str(self.username_check.get()),)
            my_cursor.execute(user_email_id,y2)

            for rec_email in my_cursor:
                pass

            sender_email = "testemailforprojects1234@gmail.com"
            password = "lrwazneksgdfzafb"

            message = " your password is " + str (passchk_2(self))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email[0], message)
            messagebox.showinfo('Email sent to '+ str(rec_email[0]), 'please check your spam emails if not found')

        else :
            messagebox.showerror('incorrect username', 'username not in database')


class Mainpage:

    def __init__(self,root):

        self.page1= Toplevel(bg ='white')
        self.page1.title ('railway Management system')
        self.page1.attributes('-fullscreen', True)
        self.root = root
        self.background_mainpage = ImageTk.PhotoImage(Image.open(r'C:\Users\deepa\OneDrive\Pictures\New folder\indian-train-images-hd.jpg'))
        background_mainpage_lab = Label(self.page1,image=self.background_mainpage).place(x=0, y=68)

        page1_frame_1 = Frame(self.page1, bg='red3')
        page1_frame_1.place(x=0, y=0, height=70, width=2000)

        self.page_1_frame_2= Frame(self.page1, bg = 'linen')
        self.page_1_frame_2.place(x= 100, y= 160, height = 690, width = 890)


        logout = Button(page1_frame_1, text='LOGOUT', bg='red3', fg='white', font=('Impact', 22), cursor='hand2',bd=0, command=self.logout_func)
        logout.place(x=1800, y=4)

        rms_label = Label (page1_frame_1, text = 'Railway Management System' , font =('Impact', 22), fg = 'white', bg = 'red3').place(x= 765, y = 10)

        profile_button = Button(page1_frame_1,text = 'PROFILE', fg = 'white', bg = 'red3',font = ('Impact', 22), cursor = 'hand2', bd= 0, command = self.Profile )
        profile_button.place (x = 20, y = 4)

        book_ticket_lab = Label (self.page_1_frame_2, text = 'Book Ticket', bg = 'linen', fg = 'red3', font = ('Impact', 28)).place (x= 355, y = 50)


        sql_query_cityname = 'SELECT cityname FROM City'
        my_cursor.execute(sql_query_cityname)
        options_city = [x[0] for x in my_cursor]



        from_label = Label(self.page_1_frame_2, text='From:', bg='white', fg='Black', font=('seoge UI', 20)).place(x=100,y=180)
        self.from_menu = StringVar()
        self.from_menu.set("select city")
        drop_from = OptionMenu(self.page_1_frame_2, self.from_menu, *options_city)
        drop_from.place(x=520, y=183)
        self.from_entry= Entry(self.page_1_frame_2,bg = 'white', fg = 'Black', width= 25 , font= ('seoge UI', 16))
        self.from_entry.place(x= 197,y = 185)



        from_chose_button = Button(self.page_1_frame_2, text = 'Select', bg = 'red3', fg = 'white', font =('seoge UI', 12), command =self.from_show )
        from_chose_button.place (x=650 ,y= 182)


        to_label = Label(self.page_1_frame_2, text = 'To :', bg = 'white', fg = 'Black', font =('seoge UI', 20) ).place(x = 100 , y = 260)
        self.to_menu= StringVar()
        self.to_menu.set('Select city')
        drop_to= OptionMenu(self.page_1_frame_2,self.to_menu,*options_city)
        drop_to.place(x=520, y = 263)
        self.to_entry= Entry(self.page_1_frame_2,bg='white', fg ='Black', width = 25, font =('seoge UI', 16) )
        self.to_entry.place(x= 197, y = 265)


        to_chose_button = Button(self.page_1_frame_2, text='Select', bg='red3', fg='white', font=('seoge UI', 12),command=self.to_show)
        to_chose_button.place(x=650, y=262)


        date_label= Label(self.page_1_frame_2, text = 'Date :', bg = 'white', fg = 'Black', font =('seoge UI', 20) ).place(x = 100 , y = 340)
        self.date_entry = Entry(self.page_1_frame_2,bg='white', fg ='Black', width = 25, font =('seoge UI', 16))
        self.date_entry.place(x= 197, y = 342)
        date_chose_button = Button(self.page_1_frame_2, text='Select', bg='red3', fg='white', font=('seoge UI', 12),command=self.show_cal)
        date_chose_button.place(x=650, y=342)


        check_trains_button = Button(self.page_1_frame_2, text = 'Check Trains', bg = 'red3', fg = 'white', font =('Impact', 22),command= self.open_ticket_page)
        check_trains_button.place(x = 350, y = 500)

    def show_cal(self):

        self.cal = Calendar(self.page_1_frame_2, selectmode='day', year=2021, month=11, day=26, date_pattern='y/mm/dd')
        self.cal.place(x=200, y=380)

        self.get_date_button = Button(self.page_1_frame_2, text='get date', bg='red3', fg='white', font=('seoge UI', 12),command=self.getdate)
        self.get_date_button.place(x=525, y=342)

    def getdate(self):
        self.date_entry.delete(0, END)
        self.date_entry.insert(0, self.cal.get_date())
        self.cal.destroy()
        self.get_date_button.destroy()

    def from_show(self):
        self.from_entry.delete(0, END)
        self.from_entry.insert(0, self.from_menu.get())

    def to_show(self):
        self.to_entry.delete(0, END)
        self.to_entry.insert(0, self.to_menu.get())

    def open_ticket_page(self):

        if self.date_entry.get() == '' or self.from_entry.get == '' or self. to_entry.get() == '':
            messagebox.showerror('Incomplete details', 'All fields must be filled properly')

        elif self.from_entry.get() == 'select city' or self.to_entry.get()== 'select city':
            messagebox.showerror('Incorrect entry','Please select city names')

        else:
            self.page1.withdraw()
            objticketscreen = Ticketscreen(root)

    def Profile (self):

        self.page1.withdraw()
        self.profile_page = Toplevel(bg = 'white')
        self.profile_page.attributes('-fullscreen', True)
        profile_frame_1 = Frame (self.profile_page, bg = 'red3')
        profile_frame_1.place (x = 0 , y = 0 , height = 75 , width = 2000)
        self.background_profilepage = ImageTk.PhotoImage(Image.open(r'C:\Users\deepa\OneDrive\Pictures\New folder\indian-train-images-hd.jpg'))
        background_profile_lab = Label(self.profile_page, image=self.background_profilepage).place(x=0, y=68)

        profile_lab = Label (profile_frame_1, text = 'PROFILE', bg = 'red3',  font =('Impact', 22),fg = 'white').place (x= 900, y = 15)

        profile_back = Button(profile_frame_1, text = '←', bg = 'red3', fg = 'white', command = self.destroy_profile, font = ('Impact' , 22), bd = 0, cursor = 'hand2')
        profile_back.place (x = 20 , y = 10)

        profile_frame_2 = Frame(self.profile_page, bg = 'linen',highlightbackground="red3", highlightthickness=1 )
        profile_frame_2.place (x= 370, y= 255, height = 480, width = 1200)

        profile_frame_3 = Frame(profile_frame_2,bg = 'linen', highlightbackground = 'red3', highlightthickness = 1 )
        profile_frame_3.place(x= 0, y = 0 ,height = 479, width = 300)

        self.username= objLogin.username_check.get()


        firstname_p = 'SELECT Firstname FROM userinfo WHERE Username = %s'
        p1= (str(self.username),)
        my_cursor.execute(firstname_p,p1)
        for self.p1_1 in my_cursor:
            pass
        Pp_firstname_label = Label (profile_frame_3, text = 'Firstname', bg = 'linen', fg = 'black', font = ('seoge UI', 14)).place (x= 90, y = 55)
        Profile_firstname = Label (profile_frame_2, text = self.p1_1[0], fg = 'black', font= ('seoge UI', 12)).place(x=317, y=59)


        lastname_p = 'SELECT Surname FROM userinfo WHERE Username = %s'
        my_cursor.execute(lastname_p,p1)
        for self.p1_2 in my_cursor:
            pass
        Pp_lastname_label = Label (profile_frame_3, text = 'Lastname', bg = 'linen', fg = 'black', font =('seoge UI', 14)).place (x= 90, y= 100)
        Profile_lastname = Label(profile_frame_2, text = self.p1_2[0], fg = 'black', font= ('seoge UI', 12)).place(x=317, y=104)


        Pp_username_label = Label (profile_frame_3, text = 'Username', bg = 'linen', fg = 'black', font =('seoge UI', 14)).place (x= 90, y= 145)
        Profile_username = Label(profile_frame_2, text=p1, fg='black', font=('seoge UI', 12)).place(x=317, y=149)

        email_p = 'SELECT Email FROM userinfo WHERE Username= %s'
        my_cursor.execute(email_p,p1)
        for self.p1_3 in my_cursor:
            pass
        Pp_emailid_label= Label (profile_frame_3, text = 'Email Id', bg = 'linen', fg = 'black', font =('seoge UI', 14)).place (x= 90, y= 190)
        Profile_lastname = Label(profile_frame_2, text=self.p1_3[0], fg='black', font=('seoge UI', 12)).place(x=317, y=194)

        phoneno_p = 'SELECT Phoneno FROM userinfo WHERE Username = %s '
        my_cursor.execute(phoneno_p,p1)
        for self.p1_4 in my_cursor:
            pass
        Pp_phoneno_label= Label (profile_frame_3, text = 'Phone no', bg = 'linen', fg = 'black', font =('seoge UI', 14)).place (x= 90, y= 235)
        Profile_lastname = Label(profile_frame_2, text=self.p1_4[0], fg='black', font=('seoge UI', 12)).place(x=317, y=239)

        gender_p = 'SELECT Gender FROM userinfo WHERE Username = %s'
        my_cursor.execute (gender_p, p1)
        for p1_5 in my_cursor:
            pass
        Pp_gender_label = Label(profile_frame_3, text='Gender', bg='linen', fg='black', font=('seoge UI', 14)).place(x=90, y=280)
        Profile_lastname = Label(profile_frame_2, text=p1_5[0], fg='black', font=('seoge UI', 12)).place(x=317, y=284)

        address_p= 'SELECT Address FROM userinfo WHERE Username = %s'
        my_cursor.execute(address_p,p1)
        for self.p1_6 in my_cursor:
            pass
        Pp_address_label =Label(profile_frame_3, text='address', bg='linen', fg='black', font=('seoge UI', 14)).place(x=90, y=325)
        Profile_address = Label(profile_frame_2, text =self.p1_6[0] , font=('seoge UI', 12)).place(x=313, y=329)

        notice_label = Label (profile_frame_3, text = '*The above details will be displayed on your ticket', bg = 'linen', fg = 'black', font = ('seoge UI', 13)).place(x = 317 , y = 370 )

        Change_details_button = Button(self.profile_page, bg = 'red3', fg = 'white', text = 'Change Details', font = ('Impact' , 22) , command = self.change_profile)
        Change_details_button.place(x = 867, y = 830)


    def destroy_profile(self):

        self.page1.deiconify()
        self.profile_page.destroy()


    def change_profile(self):

        change_page = Toplevel(bg = 'white')
        change_page.attributes('-fullscreen', True)
        change_page_frame_1 = Frame(change_page, bg='red3')
        change_page_frame_1.place(x=0, y=0, height=75, width=2000)
        change_page__lab = Label(change_page_frame_1, text='CHANGE DETAILS', bg='red3', font=('Impact', 22), fg='white').place(x=880,y=15)

        profile_back = Button(change_page_frame_1, text='←', bg='red3', fg='white', command=change_page.destroy,font=('Impact', 22), bd=0, cursor='hand2')
        profile_back.place(x=20, y=10)

        change_profile_frame = Frame (change_page, bg = 'Linen')
        change_profile_frame.place (x = 680 , y = 200 , height = 700 , width = 600)

        user_change_label = Label(change_profile_frame, text='Username ', font=('seoge UI', 12), bg='white',fg='black').place(x=65, y=150)
        self.user_change_entry= Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.user_change_entry.place(x=180, y=150, width=350, height=30)
        self.user_change_entry.insert(0,str(self.username))

        firstname_change_label = Label(change_profile_frame, text='Firstname', font=('seoge UI', 12), bg='white',fg='black').place(x=65, y=200)
        self.firstname_change_entry = Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.firstname_change_entry.place(x=180, y=200, width=350, height=30)
        self.firstname_change_entry.insert(0, str(self.p1_1[0]))

        lastname_change_label = Label(change_profile_frame, text = 'Lastname', font = ('seoge UI',12), bg= 'white', fg= 'black'). place(x = 65, y = 250)
        self.lastname_change_entry = Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.lastname_change_entry.place(x=180, y=250, width=350, height=30)
        self.lastname_change_entry.insert(0, str(self.p1_2[0]))


        email_change_label = Label(change_profile_frame, text='Email', font=('seoge UI', 12), bg='white',fg='black').place(x= 65, y= 300)
        self.email_change_entry = Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.email_change_entry.place(x=180, y=300, width=350, height=30)
        self.email_change_entry.insert(0, str(self.p1_3[0]))

        phone_no_change_label = Label(change_profile_frame, text = 'Phone no', font = ('seoge UI', 12), bg = 'white', fg = 'black').place(x= 65, y =350)
        self.phone_no_change_entry = Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.phone_no_change_entry.place(x=180, y=350, width=350, height=30)
        self.phone_no_change_entry.insert(0, str(self.p1_4[0]))

        address_change_label = Label(change_profile_frame, text = 'Address', font = ('seoge UI', 12), bg = 'white', fg = 'black').place(x= 65, y =400)
        self.address_change_entry = Entry(change_profile_frame, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.address_change_entry.place(x=180, y=400, width=350, height=30)
        self.address_change_entry.insert(0, str(self.p1_6[0]))


        save_details_button = Button (change_profile_frame, text = 'save changes', bg = 'red3', fg = 'white', font = ('Impact', 20),command = self.change_function)
        save_details_button.place(x=220, y =500 )

        change_password_button = Button(change_profile_frame, text= 'change password', bg = 'red3',fg = 'white', font = ('Impact', 20), command = self.change_pass_func)
        change_password_button.place(x = 198, y = 600)



    def change_function(self):

        regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if(self.user_change_entry.get() == '' or self.firstname_change_entry.get() == '' or self.lastname_change_entry.get() == ''
                or self.email_change_entry.get() == '' or self.phone_no_change_entry.get() == '' or self.address_change_entry.get() == ''):
            messagebox.showerror('Incomplete details','ALl fields must be filled')

        elif len(self.user_change_entry.get()) <= 8:
            messagebox.showerror('username too small', 'usmername must be at least 8 characters long')

        elif not (re.search(regex2, self.email_change_entry.get())):
            messagebox.showwarning('invalid email', 'please eneter a valid email id')

        else:
            save_changes_ask=messagebox.askyesno('save changes', 'are you sure you want to save changes?')

            if save_changes_ask == 1:
                sql_query_change = 'UPDATE userinfo SET Username = %s ,Firstname = %s , Surname = %s, Email = %s, Phoneno = %s, Address = %s WHERE Username = %s'
                x2= (self.user_change_entry.get(), self.firstname_change_entry.get(), self.lastname_change_entry.get(), self.email_change_entry.get(),
                     self.phone_no_change_entry.get(), self.address_change_entry.get(), objLogin.username_check.get())
                my_cursor.execute(sql_query_change,x2)
                mydb.commit()
                messagebox.showinfo('details saved successfully','please restart the application to complete the procedure')
                root.destroy()

            else:
                pass


    def change_pass_func(self):

        pass_change = Toplevel (bg = 'white')
        pass_change.geometry('500x300+700+390')
        pass_change.resizable(False, False)

        username_pass_change_label = Label(pass_change,text = 'username', bg= 'white', fg = 'black', font =('seoge UI', 12)).place(x= 20, y= 50)
        self.username_pass_change_entry = Entry(pass_change,width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.username_pass_change_entry.place(x= 150,y=50)

        current_pass_label = Label(pass_change, text = 'current password', bg = 'white', fg = 'black',font = ('seoge UI', 12)).place (x = 20, y =100)
        self.current_pass_entry = Entry(pass_change, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.current_pass_entry.place(x=150, y=100)


        new_password_label= Label(pass_change, text = 'new password', bg= 'white',fg = 'black',font = ('seoge UI', 12)).place(x=20,y=150)
        self.new_password_pass_change_entry = Entry(pass_change, width=50, bd=0, bg='white', fg='black', borderwidth=3)
        self.new_password_pass_change_entry.place(x=150, y=150)


        save_changes = Button(pass_change,text = 'save_changes',bg = 'red3', fg = 'white', font = ('Impact,20'), command= self.change_pass_save)
        save_changes.place(x=200 , y= 220 )

    def change_pass_save(self):

        def userchk_3(self):

            usr_check_3 = 'SELECT Username FROM userinfo '
            check_variable_3 = True
            my_cursor.execute(usr_check_3)

            for ele9 in my_cursor:
                if ele9[0] == self.username_pass_change_entry.get():
                    check_variable_3 = True
                    break
            else:
                check_variable_3 = False
            return check_variable_3

        check_var_4 = True
        passcheck_3 = 'SELECT UserPassword FROM userinfo WHERE Username = %s'
        passvar = (str(self.username_pass_change_entry.get()),)
        my_cursor.execute(passcheck_3, passvar)

        for ele8 in my_cursor:
            if ele8[0] == self.current_pass_entry.get():
                check_var_4 = True
                break
        else:
            check_var_4 = False


        if userchk_3(self) == False:
            messagebox.showerror('Invalid Username', 'Username doesn\'t exist in database')

        elif check_var_4 == False:
            messagebox.showerror('Incorrect Password','Please enter the correct password' )

        else:
            sql_query_change_pass = 'UPDATE userinfo SET UserPassword = %s WHERE Username = %s'
            sql_var_10= (self.new_password_pass_change_entry.get(),self.username_pass_change_entry.get())
            my_cursor.execute(sql_query_change_pass,sql_var_10)
            mydb.commit()
            messagebox.showinfo('Password changed','Please restart the application to apply changes')


    def logout_func(self):
        logout_response = messagebox.askyesno('Logout', 'Are you sure you want to logout?')
        if logout_response == 1:
            self.root.destroy()
        else:
            pass

class Ticketscreen:

    def __init__(self,root):
        self.chktrains = Toplevel(bg = 'white')
        self.chktrains.attributes('-fullscreen', True)
        chktrain_f1 = Frame (self.chktrains, bg = 'red3')
        chktrain_f1.place (x = 0 , y = 0 , height = 75 , width = 2000)
        avail_lab = Label(chktrain_f1, text = 'Available trains',bg = 'red3', fg = 'white', font = ('Impact', 22)).place(x =850, y =15)

        back_butt = Button(chktrain_f1, text = '←' , bg = 'red3', fg = 'white',font = ('Impact', 20), command = self.back_tic_page)
        back_butt.place (x= 40, y = 10 )

        self.to_entry = objLogin.objmainscreen.to_entry.get()
        self.from_entry = objLogin.objmainscreen.from_entry.get()
        self.date_entry = objLogin.objmainscreen.date_entry.get()

        sql_query_date = 'SELECT Date_travel FROM Available_trains WHERE To_city = %s AND From_city = %s'
        date_exe = (self.to_entry, self.from_entry)
        my_cursor.execute(sql_query_date,date_exe)


        self.train_lst=[]

        sql_query_to_from= 'SELECT Train_name FROM Available_trains WHERE To_city = %s AND From_city = %s AND Date_travel = %s'
        to_from_exe= (self.to_entry, self.from_entry, self.date_entry)
        my_cursor.execute (sql_query_to_from,to_from_exe)

        for to_from in my_cursor:
            self.train_lst.append(to_from[0])
            pass

        sql_query_from_to_via = 'SELECT Train_name FROM Available_trains WHERE From_city = %s AND Via_city = %s AND Date_travel= %s'
        from_to_via_exe = (self.from_entry, self.to_entry, self.date_entry )
        my_cursor.execute(sql_query_from_to_via,from_to_via_exe)

        for from_via in my_cursor:
            self.train_lst.append(from_via[0])
            pass

        sql_query_via_to = 'SELECT Train_name FROM Available_trains WHERE Via_city = %s AND To_city = %s AND Date_travel= %s'
        via_to_exe = (self.from_entry,self.to_entry,self.date_entry)
        my_cursor.execute(sql_query_via_to,via_to_exe)

        for via_to in my_cursor:
            self.train_lst.append(via_to[0])

        if (len(self.train_lst)== 0):
            no_lab = Label(self.chktrains, text = 'NO TRAINS AVAILABLE ON THIS DATE', bg = 'white', fg = 'black', font= ('Impact', 23)).place (x = 740, y= 300)


        for fra in range (len(self.train_lst)):

            sql_query_lab_time = 'SELECT Time_travel FROM Available_trains WHERE Train_name = %s'
            sql_run_t= (str(self.train_lst[fra]),)
            my_cursor.execute(sql_query_lab_time,sql_run_t)
            tme= 0
            for tme in my_cursor:
                pass

            frames= Frame(self.chktrains, bg = 'lavender')
            frames.place(x=450, y=150+fra*60, height=45, width=1000)
            lab_train = Label(frames, text = self.train_lst[fra], bg = 'lavender',fg = 'black', font = ('Seoge UI',15)).place(x = 50, y = 7 )
            lab_date = Label (frames, text = self.date_entry, bg = 'lavender', fg = 'black', font = ('Seoge UI',15)).place (x= 360, y =7)
            lab_train_t= Label(frames, text = tme[0], bg = 'lavender', fg = 'black', font = ('Seoge UI',15)).place (x= 510, y =7)

            def book_pg(name):

                bookpg = Toplevel(bg='white')
                Labe = Label(bookpg, text=name, bg='white', fg='black').place(x=100, y=100)


            select_train_butt = Button(frames, text = 'select', bg = 'purple3', fg = 'white', font = ('seoge UI', 13),command=lambda:book_pg(self.train_lst[fra]))
            select_train_butt.place (x= 800, y= 5)

            if fra == self.train_lst.index('Mum-Pune-Hydrebad super'):
                break





    def back_tic_page (self):
        self.chktrains.destroy()
        objLogin.objmainscreen.page1.deiconify()












objLogin =  Login(root)

root.mainloop()