import sqlite3
con=sqlite3.connect('movie.db')
#con.execute('''create table movie (name text,actor text,actress text, released int,director text)''')
print("Created")

con.execute("insert into movie values('PK','Aamir Khan','Anushaka Sharma',2018,'abcd')")
con.commit()
print("inserted Sucessfully")

data=con.execute('select * from movie')

for row in data:
    print("Name{},Actor:{},Actress:{},Released:{},Director:{}".format(row[0],row[1],row[2],row[3],row[4]))


