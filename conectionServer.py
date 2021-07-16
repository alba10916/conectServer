import pymysql
db = pymysql.connect(host="192.168.1.78",    # your host, usually localhost
                     user="userchat",         # your username
                     passwd="FsmN.pml4Fv@",  # your password
                     db="chatdb")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("insert into usuarios (nombre) values ('Fernando');")

# print all the first cell of all the rows
#for row in cur.fetchall():
 #   print row

db.close()
#def sendMessage