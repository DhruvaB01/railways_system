
import mysql.connector
import sys
import re

usertable = 'user_table'
seattable = 'seat_table'


class User_Actions() :

    def __init__(self,username):
        self.username = username
         
        # self.check_password(passwd)

        self.userdata = {

            'firstname' : None,
            'lastname' : None,
            'username' : None,
            'email' : None,
            'phoneno' : 0,
            'gender' : None,
            'address' : None,
            'booked seats' : []
            
        }
        self.get_data()

    def check_password(self,login_passwd):
        cursor.execute(f'select password from {usertable} where username = "{self.username}"',)
        # print(login_passwd := cursor.fetchall()[0][0])
        passwd = cursor.fetchall()
        print(passwd)
        if not passwd :
            print('NO SUCH USER FOUND ! ')
            return False
        else :
            passwd = passwd[0][0]

        if passwd == login_passwd:
            print('PASSWORD CORRECT')
            return True
        else :
            print('INCORRECT PASSWORD')
            return False

    def get_data(self) :

        #extracting the data
        query = f'select firstname,lastname,username,email,phone_no,gender,address from {usertable} where username = "{self.username}"'
        cursor.execute(query)
        
        output = cursor.fetchall()
        print(output)
        if not output == []:
            output = output[0]
        else :
            print('NO RECORD FOUND !')


        # parseing data into a dictionary
        self.userdata['firstname'] = output[0]
        self.userdata['lastname'] = output[1]
        self.userdata['username'] = output[2]
        self.userdata['email'] = output[3]
        self.userdata['phoneno'] = output[4]
        self.userdata['gender'] = output[5]
        self.userdata['address'] = output[6]
        # self.userdata['password'] = output[7]

        # print(self.userdata)
        return self.userdata

    def sign_up(self):
        
        userdata_dict = {
        'firstname' : 'testname',
        'lastname' : 'testlastname',
        'username' : self.username,
        'email' : 'xylo3@gmail.com',
        'phoneno' : 9921098761,
        'gender' : 'F',
        'address' : 'D-201 , Alcove Society , Pimple Saudagar , Pune , Maharashtra',
        'password' : '444'

        }

        data = userdata_dict.values()
        data = tuple(data)
        print(data)

        try :
            query = f'insert into {usertable} values (%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(query,data)
            railwayconn.commit()
            print('Success')
        except mysql.connector.errors.IntegrityError as exc:
            # print(str(exc))
            if re.search(r'email',str(exc)) : print('EMAIL ALREADY EXIST')
            if re.search(r'phone_no',str(exc)) : print('PHONE NUMBER ALREADY EXIST')
            if re.search(r'PRIMARY',str(exc)) : print('USERNAME ALREADY EXIST')
            
            # print('DUPLICATE VALUE')


    def book_tickets(self) :
        # print(self.userdata)
        # no_of_tickets = 1  

        cursor.execute('select seat_no,seat_type from seat_table where username is null')
        output = cursor.fetchall()
        # print(output)
        no_available_tickets = int(len(output))

        if 0 >=  no_available_tickets : 
            print('NOT ENOUGH TICKETS LEFT')       

        else :          
            print(f'{no_available_tickets} TICKETS ARE AVAILABLE')
            availableseats = {seatno for seatno,seattype in output}
 
            bookseats = set(map(int,input(f"Enter seatno to book from {availableseats}--> ").rstrip().split()))
            print(bookseats)

            # print(f'{no_available_tickets} TICKETS ARE AVAILABLE')

            for seat in availableseats.intersection(bookseats):
                # seat = output[i][0]
                query = f'''update {seattable} set username = "{self.userdata['username']}" where seat_no = {seat}'''
                cursor.execute(query)
                print(f"BOOKED {seat} for {self.username}")
                
                # self.userdata['booked seats'].append(seat)

            railwayconn.commit()
            
            # print('TICKETS BOOKED --> ',self.userdata['booked seats'])

    def cancel_tickets(self) : 
        print(self.userdata)

        cancelation_options = ['all','custom']
        # cancel_ans = 'all'
        cancel_ans = 'custom'

        if cancel_ans == cancelation_options[0]:
            # seat = output[i][0]
            query = f'''update {seattable} set username = null 
            where username = "{self.userdata['username']}";'''
            print(query)
            cursor.execute(query)

            railwayconn.commit()
            self.userdata['booked seats'] = []
            print('ALL TICKETS CANCELLED !')

        else :
            query = f"select seat_no,username from seat_table where username = '{self.username}';"
            print(query)
            cursor.execute(query)
            output = cursor.fetchall()

            bookedseats = {seatno for seatno , _  in output}
            print("BOOKED SEATS = ",bookedseats)

            cancelseats = set(map(int,input(f'Enter seats to cancel from {bookedseats} -->').rstrip().split()))      
            # print(cancelseats.intersection(bookedseats))
            
            for seat in cancelseats.intersection(bookedseats) :
                query = f'update seat_table set username = null where seat_no = {seat}; '
                cursor.execute(query)
                print(f"CANCELLED {seat} for {self.username}")

            railwayconn.commit()




if __name__ == "__main__" :


    railwayconn= mysql.connector.connect(host = 'localhost',user= 'root', passwd = 'rudu101519',database = 'railway')
    cursor = railwayconn.cursor()


    # checking the table
    try :
        cursor.execute(f'select * from {usertable}')
        output = cursor.fetchall()[0]
        # print(output)


         
    except IndexError :  
        print('TABLE IS EMPTY, NO DATA TO FETCH')
        sys.exit(1)

    #testcase 1
    username1 = 'deathgrad'
    passwd1 = '234'
    # / testcase 1

    #testcase 2
    username2 = 'ha5hkat'
    passwd2 = '123'
    # / testcase 2

    #testcase 3
    username3 = 'void'
    passwd3 = '333'
    # / testcase 3

    #testcase4
    username = 'xlyo3'
    passwd = '444'


    username = username2
    passwd = passwd2

    ua = User_Actions(username)
    # ua.sign_up()
    # query = 'select * from user_table where username'
    # cursor.execute()

    if not ua.check_password(passwd) : 
        print('RETRY')
        del ua
    else :
    
    # ua = User_Actions(username)
        # print(ua.get_data())
        ua.book_tickets()
        # ua.cancel_tickets()
    # ua.book_tickets()

    # ua = User_Actions(username)
    # ua.sign_up()

    railwayconn.close()