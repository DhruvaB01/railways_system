import mysql.connector


mydb = mysql.connector .connect (
    host = '127.0.0.1',
    user = 'root',
    password = 'dhruvab',
    database = 'rms'
)

my_cursor = mydb.cursor (buffered= True)

final_seat_list = []
n = int (input('n = '))
for i in range(n):
    inp = input()
    final_seat_list.append (inp)

print (final_seat_list)
f_tuple = tuple(final_seat_list)
print (f_tuple)

print (len(f_tuple))
print(f_tuple[0])