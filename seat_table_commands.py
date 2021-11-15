import mysql.connector

railwayconn = mysql.connector.connect(
    host="127.0.0.1", user="root", password="dhruvab", database="rms"
)

cursor = railwayconn.cursor()

seattable = "seat_table"

data = []
total_seats = 40
seats_per_compartment = 8

for i in range(1, total_seats + 1):
    if i % seats_per_compartment == 1:
        seattype = "LB"
    elif i % seats_per_compartment == 2:
        seattype = "MB"
    elif i % seats_per_compartment == 3:
        seattype = "UB"
    elif i % seats_per_compartment == 4:
        seattype = "LB"
    elif i % seats_per_compartment == 5:
        seattype = "MB"
    elif i % seats_per_compartment == 6:
        seattype = "UB"
    elif i % seats_per_compartment == 7:
        seattype = "LB"
    elif i % seats_per_compartment == 0:
        seattype = "UB"
    data.append((i, seattype))

# print(data)
# checking the contents of table

# cursor.execute(f'select * from {seattable}')
# print(cursor.fetchall())

query = f"insert into seat_table(seat_no,seat_type) values (%s,%s);"
cursor.executemany(query, data)
railwayconn.commit()


# cursor.execute(f'select * from {seattable}')
# print(cursor.fetchall())


railwayconn.close()
