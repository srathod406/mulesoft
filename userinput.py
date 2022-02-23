import sqlite3
con=sqlite3.connect('movie.db')

class Demo:
    def __init__(self):
       pass

    def insertdata():
         nm=input("Enter Movie Name :")
         actor=input("Enter Actor Nmae :")
         actress=input("Enter Actress Name :")
         year=int(input("Enter Released Year:"))
         director= input("Enter Director Nmae :")
         con.execute("insert into movie(name,actor,actress,released,director) values(?,?,?,?,?)",(nm,actor,actress,year,director))
         con.commit()

    def display():
        data=con.execute('select * from movie')

        for row in data:
            print("Name:{}".format(row[0]))
            print("Actor:{}".format(row[1]))
            print("Actress:{}".format(row[2]))
            print("Year:{}".format(row[3]))
            print("Director:{}".format(row[4]))
d1=Demo
d1.insertdata()
d1.display()
