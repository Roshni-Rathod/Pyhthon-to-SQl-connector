import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'August2001',database = 'pyhton')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
# val = ('John','it', 54)

# if user wantot create multiple value than you can creaate list 

val = [('John','it',54),('mike','cse', 7),('Ira','chem',34)]
#mycursor.execut(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')