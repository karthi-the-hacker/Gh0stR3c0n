from fastapi import *
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import sqlite3
from datetime import date

today = str(date.today())

global dbdata
dbdata = ""
cwd = os.getcwd()
app = FastAPI()
templates = Jinja2Templates(directory=cwd+"/web/")
@app.get('/company')
def landing(request: Request):
    return templates.TemplateResponse("company.html", {"request": request})


@app.get('/report')
def landing(request: Request):
    data = ""
    conn = sqlite3.connect("recon.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('''SELECT * from recon ;''')
    conn.commit()
    for i in c:
        print(i[1])
        data += "<tr><td>"+i[0]+"</td><td>" +i[1]+"</td><td>"+i[2]+"</td></tr>"
    conn.close()
    dbdata = data
   
    return templates.TemplateResponse("report.html", {"request": request, "dbdata": dbdata})

@app.get('/finish')
def landing(request: Request):
    os.system("python ~/tools/Gh0stR3con/back-end/d3vnull.py "+company+ " &")
    return templates.TemplateResponse("finish.html", {"request": request})

@app.post('/create')
def adddata(request: Request, cname: str = Form(...), reporturl: str = Form(...), domain: str = Form(...)):
    conn = sqlite3.connect("recon.db", check_same_thread=False)
    c = conn.cursor()   
    os.system("mkdir ~/recon/gh0str3c0n/"+cname)
    c.execute("INSERT INTO recon VALUES('"+cname+"','"+reporturl+"','"+today+"');")
    conn.commit()
    conn.close()
    global company 
    company = str(cname)
    os.system("echo "+domain +" >> ~/recon/gh0str3c0n/"+cname+"/scope.txt")
    return templates.TemplateResponse("addscope.html",{"request": request , "cname":cname})


@app.post('/add')
def adddata(request: Request, cname: str = Form(...), cdomain: str = Form(...)):
    os.system("echo "+cdomain + " >> ~/recon/gh0str3c0n/"+cname+"/scope.txt")
    return templates.TemplateResponse("addscope.html", {"request": request, "cname": cname})
