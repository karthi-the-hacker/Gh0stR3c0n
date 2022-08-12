import sqlite3
import os
from datetime import date

today = str(date.today())
cwd = os.getcwd()

conn = sqlite3.connect("recon.db")

c = conn.cursor()
data=""
#c.execute("INSERT INTO recon VALUES('"+cname+"','"+reporturl+"','"+today+"');")
c.execute('''CREATE TABLE recon (company_name TEXT, report_url TEXT, created_date TEXT);''')
#c.execute('''INSERT INTO recon VALUES('cappriciosec','security@cappriciosec.com','10-7-3');''')
#c.execute('''SELECT * from recon ;''')
#c.execute('DELETE from recon;')
conn.commit()

conn.close()
print(str(data))
