import mysql.connector

con=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="learn")
cur=con.cursor()
cur.execute("select * from fdcal")
for row in cur:
    print(row[0], row[1], row[2], row[3],row[4])
con.close()