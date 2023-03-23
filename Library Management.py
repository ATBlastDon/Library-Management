# Starting Of Program

from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime

b1,b2,b3,b4,cur,con,e1,e2,e3,e4,e5,i,ps=None,None,None,None,None,None,None,None,None,None,None,None,None
window,win=None,None
com1d,com1m,com1y,com2d,com2m,com2y=None,None,None,None,None,None
stdid = None
serial = None

month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2020, 2040))
d = list(range(1,31))

# After Login Things

#login
def loginlibr():
    global window, stdid
    connectdb()
    for i in range(cur.rowcount):
        data=cur.fetchone()
        if e1.get().strip()==str(data[1]) and e2.get().strip()==str(data[2]):
            stdid = int(e1.get())
            closedb()
            libr()
            break
    else:
        messagebox.showerror("Login", "ID or Password is Wrong!!")
        closedb()


# Main Window After login
def libr():
    global window
    window.withdraw()
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("500x450")
    win.configure(bg='lightyellow')
    b8=Label(win, text=' Main Menu ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    b1=Button(win, height=2,width=25,text=' Donate Book ',command=addbook, font='cosmicsansms 11 italic', bg='skyblue')
    b2=Button(win, height=2,width=25,text=' Apply Book ',command=issuebook, font='cosmicsansms 11 italic', bg='skyblue')
    b3=Button(win, height=2,width=25,text=' Return Book ',command=returnbook, font='cosmicsansms 11 italic', bg='skyblue')
    b4=Button(win, height=2,width=25,text=' View Books ',command=viewbook, font='cosmicsansms 11 italic', bg='skyblue')
    b5=Button(win, height=2,width=25,text=' Applied Books ',command=issuedbook, font='cosmicsansms 11 italic', bg='skyblue')
    b7=Button(win, height=2,width=25,text=' LogOut ',command=logout, font='cosmicsansms 11 italic', bg='orange')
    b8.place(x=160,y=10)
    b1.place(x=120,y=60)
    b2.place(x=120,y=120)
    b3.place(x=120,y=180)
    b4.place(x=120,y=240)
    b5.place(x=120,y=300)
    b7.place(x=120,y=360)
    win.mainloop()


# Add Books interface
def addbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Donate Book')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    b8=Label(win, text=' Donate A BOOK ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    sub=Label(win,text='SUBJECT', font='cosmicsansms 13 italic', bg='lightyellow')
    tit=Label(win,text='TITLE', font='cosmicsansms 13 italic', bg='lightyellow')
    auth=Label(win,text='AUTHOR', font='cosmicsansms 13 italic', bg='lightyellow')
    ser=Label(win,text='SERIAL NO', font='cosmicsansms 13 italic', bg='lightyellow')
    global e1,b,b1
    e1=Entry(win,width=60)
    global e2
    e2=Entry(win,width=60)
    global e3
    e3=Entry(win,width=60)
    global e4
    e4=Entry(win,width=60)
    b=Button(win, height=2,width=20,text=' ADD ',command=addbooks, bg='skyblue', font='cosmicsansms 10')
    b1=Button(win, height=2,width=20,text=' CLOSE ',command=closebooks, bg='orange', font='cosmicsansms 10')
    sub.place(x=70,y=60)
    tit.place(x=70,y=100)
    auth.place(x=70,y=140)
    ser.place(x=70,y=180)
    e1.place(x=180,y=60)
    e2.place(x=180,y=100)
    e3.place(x=180,y=140)
    e4.place(x=180,y=180)
    b.place(x=180,y=220)
    b1.place(x=360,y=220)
    b8.place(x=220,y=5)
    win.mainloop()
  
# Addbook Button
def addbooks():
    connectdb()
    global cur,con
    qq="SELECT * FROM book WHERE serial = '%i'"
    
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '':
        messagebox.showerror("Book", "Fill All Details")
        return None
        
    cur.execute(qq%(int(e4.get())))
    iddd = cur.fetchone()
    
    if iddd is None:
        q='INSERT INTO Book VALUE("%s","%s","%s","%i")'
        cur.execute(q%(e1.get(),e2.get(),e3.get(),int(e4.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Book", "Book Added")
        closedb()
        libr()
    else:
        messagebox.showerror("Delete","ID Already Taken.")
        closedb()
   

# Closebook Button
def closebooks():
    global win
    win.destroy()
    libr()

# Issue Book interface
def issuebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Apply Book')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    b8=Label(win, text=' APPLY A BOOK ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    sid=Label(win,text='STUDENT ID', font='cosmicsansms 13 italic', bg='lightyellow')
    no=Label(win,text='BOOK NO', font='cosmicsansms 13 italic', bg='lightyellow')
    issue=Label(win,text='APPLY DATE', font='cosmicsansms 13 italic', bg='lightyellow')
    exp=Label(win,text='RETURN DATE', font='cosmicsansms 13 italic', bg='lightyellow')
    global e1,b,b1
    e1=Entry(win,width=50)
    global e4
    e4=Entry(win,width=50)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    com2y=Combobox(win,value=y,width=5)
    com2m=Combobox(win,value=month,width=5)
    com2d=Combobox(win,value=d,width=5)
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    com2y.set(now.year)
    com2m.set(month[now.month-1])
    com2d.set(now.day)
    b=Button(win, height=2,width=20,text=' APPLY BOOK ',command=issuebooks, font='cosmicsansms 10', bg='skyblue')
    b1=Button(win, height=2,width=20,text=' CLOSE ',command=closebooks, font='cosmicsansms 10', bg='orange')
    sid.place(x=50,y=60)
    no.place(x=50,y=100)
    issue.place(x=50,y=140)
    exp.place(x=50,y=180)
    e1.place(x=180,y=60)
    e4.place(x=180,y=100)
    com1y.place(x=180,y=140)
    com1m.place(x=230,y=140)
    com1d.place(x=280,y=140)
    com2y.place(x=180,y=180)
    com2m.place(x=230,y=180)
    com2d.place(x=280,y=180)
    b.place(x=120,y=225)
    b1.place(x=300,y=225)
    b8.place(x=210,y=10)
    win.mainloop()


# Issuebook Button
def issuebooks():
    global stdid
    connectdb()
    
    qq="SELECT * FROM book WHERE serial = '%i'"
    i=datetime.datetime(int(com1y.get()),month.index(com1m.get())+1,int(com1d.get()))
    e=datetime.datetime(int(com2y.get()),month.index(com2m.get())+1,int(com2d.get()))
    i=i.isoformat()
    e=e.isoformat()
    
    if e1.get() == '' or e4.get() == '':
            messagebox.showerror("ApplyBook", "Enter All Details")
            return None
            
    cur.execute(qq%(int(e4.get())))
    bkid = cur.fetchone()
    qqq="SELECT userid FROM login WHERE userid = '%i'"
    cur.execute(qqq%(int(e1.get())))
    result = cur.fetchone()
    usdi = (int(e1.get()))
    
    if usdi == stdid:
        messagebox.showinfo("ApplyBook","ID Matched")
        if bkid is None:
            messagebox.showerror("ApplyBook","Book Not Found.")
            closedb()
        else:
            qqqq='SELECT serial FROM bookissue where serial="%i"'
            cur.execute(qqqq%(int(e4.get())))
            chkk = cur.fetchone()
            print(chkk)
            
            if chkk is None:
                q='INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
                cur.execute(q%(e1.get(),(int(e4.get())), i, e))
                con.commit()
                win.destroy()
                messagebox.showinfo("ApplyBook", "Book Applied")
                closedb()
                libr()
            else:
                messagebox.showerror("ApplyBook", "Book Already Applied")
                
    else:
        messagebox.showerror("ApplyBook","ID Not Matched")
        
   
# Return Book interface
def returnbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Return Request')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    no=Label(win,text='BOOK NO', font='cosmicsansms 13 italic', bg='lightyellow')
    date=Label(win,text='RETURN DATE', font='cosmicsansms 13 italic', bg='lightyellow')
    b8=Label(win, text=' RETURN A BOOK ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    global b,b1
    global e4
    e4=Entry(win,width=60)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    b=Button(win, height=2,width=20,text=' RETURN BOOK ',command=returnbooks, font='cosmicsansms 10', bg='lightblue')
    b1=Button(win, height=2,width=20,text=' CLOSE ',command=closebooks, font='cosmicsansms 10', bg='orange')
    no.place(x=50,y=70)
    date.place(x=50,y=130)
    e4.place(x=190,y=70)
    com1y.place(x=190,y=130)
    com1m.place(x=240,y=130)
    com1d.place(x=290,y=130)
    b.place(x=160,y=200)
    b8.place(x=200,y=10)
    b1.place(x=340,y=200)
    win.mainloop()

# ReturnBook Button
def returnbooks():
    connectdb()
    q='SELECT exp FROM bookissue WHERE serial="%s"'
    
    if e4.get() == '':
            messagebox.showerror("ApplyBook", "Enter Book ID")
            return None

    cur.execute(q%(e4.get()))
    e=cur.fetchone()       
    if e is None:
        messagebox.showerror("Return", "Book not found")
        return None
    e=str(e[0])
    i=datetime.date.today()
    e=datetime.date(int(e[:4]),int(e[5:7]),int(e[8:10]))

    if i<=e:
        a='DELETE FROM bookissue WHERE serial="%s"'
        messagebox.showinfo("Return",' Book Returned ')
        cur.execute(a%e4.get())
        con.commit()
    else:
        e=str((i-e)*10)
        d='DELETE FROM bookissue WHERE serial="%s"'
        cur.execute(d%e4.get())
        messagebox.showinfo("Return",t[:4]+' Book Returned with ')
        con.commit()
    win.destroy()
    closedb()
    libr()
    

# View All Book Queries
def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("900x300+270+180")
    win.configure(bg='lightyellow')    
    treeview=Treeview(win,columns=("Subject","Title","Author","Serial No"),show='headings')
    treeview.heading("Subject", text="Subject")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Serial No", text="Serial No")
    treeview.column("Subject", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Serial No", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

# Issued Book Queries
def issuedbook():
    global stdid
    connectdb()
    q='SELECT * FROM BookIssue WHERE stdid = %s'
    cur.execute(q%(stdid))
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('Applied Books')
        win.geometry("900x300+270+180")
        win.configure(bg='lightyellow')
        treeview=Treeview(win,columns=("Student ID","Serial No","Issue Date","Expiry Date"),show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Serial No", text="Serial No")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Serial No", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Books","No Book Issued")
    closedb()
   
   
# Delete book interface
def deletebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Book')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    b8=Label(win, text=' DELETE A BOOK ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    usid=Label(win,text='SERIAL NO', font='cosmicsansms 13 italic', bg='lightyellow')
    paswrd=Label(win,text='PASSWORD', font='cosmicsansms 13 italic', bg='lightyellow')
    global e1
    e1=Entry(win,width=60)
    global e2,b2
    e2=Entry(win,width=60)
    b1=Button(win, height=2,width=17,text=' DELETE ',command=deletebooks, font='cosmicsansms 10 italic', bg='lightblue')
    b2=Button(win, height=2,width=17,text=' CLOSE ',command=adminclose, font='cosmicsansms 10 italic', bg='orange')
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    b8.place(x=180,y=10)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=360,y=180)
    win.mainloop()


# Deletebooks Button
def deletebooks():
    connectdb()
    if e2.get()=='admin':
        q="SELECT * FROM book WHERE serial = '%i'"
        
        if e1.get() == '':
            messagebox.showerror("Delete", "Enter Correct ID")
            return None
            
        cur.execute(q%(int(e1.get())))
        book = cur.fetchone()
        
        if book is None:
            messagebox.showerror("Delete","Book Not Found.")
            closedb()
        else:
            qq="DELETE FROM book WHERE serial = '%i'"
            cur.execute(qq%(int(e1.get())))
            con.commit()
            win.destroy()
            messagebox.showinfo("Delete","Book Deleted Successfully.")
            closedb()
            admin()
            
    else:
        messagebox.showerror("Delete","Password is Wrong.")
        closedb()

# LOGIN as ADMIN   


#ADDITIONS

def adminbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Book')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    b8=Label(win, text=' Add A BOOK ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    sub=Label(win,text='SUBJECT', font='cosmicsansms 13 italic', bg='lightyellow')
    tit=Label(win,text='TITLE', font='cosmicsansms 13 italic', bg='lightyellow')
    auth=Label(win,text='AUTHOR', font='cosmicsansms 13 italic', bg='lightyellow')
    ser=Label(win,text='SERIAL NO', font='cosmicsansms 13 italic', bg='lightyellow')
    global e1,b,b1
    e1=Entry(win,width=60)
    global e2
    e2=Entry(win,width=60)
    global e3
    e3=Entry(win,width=60)
    global e4
    e4=Entry(win,width=60)
    b=Button(win, height=2,width=20,text=' ADD ',command=adminbooks, bg='skyblue', font='cosmicsansms 10')
    b1=Button(win, height=2,width=20,text=' CLOSE ',command=adminclose, bg='orange', font='cosmicsansms 10')
    sub.place(x=70,y=60)
    tit.place(x=70,y=100)
    auth.place(x=70,y=140)
    ser.place(x=70,y=180)
    e1.place(x=180,y=60)
    e2.place(x=180,y=100)
    e3.place(x=180,y=140)
    e4.place(x=180,y=180)
    b.place(x=180,y=220)
    b1.place(x=360,y=220)
    b8.place(x=220,y=5)
    win.mainloop()

# Addbook Button
def adminbooks():
    connectdb()
    global cur,con
    qq="SELECT * FROM book WHERE serial = '%i'"
    
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '':
        messagebox.showerror("Book", "Fill All Details")
        return None
        
    cur.execute(qq%(int(e4.get())))
    iddd = cur.fetchone()
    
    if iddd is None:
        q='INSERT INTO Book VALUE("%s","%s","%s","%i")'
        cur.execute(q%(e1.get(),e2.get(),e3.get(),int(e4.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Book", "Book Added")
        closedb()
        admin()
    else:
        messagebox.showerror("Delete","ID Already Taken.")
        closedb()

   
# Closebook Button
def adminclose():
    global win
    win.destroy()
    admin()

# End Of Additions For Admin   



# Admin Password
def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin();
    else:
        messagebox.showerror("Login", "Wrong ID or Password!!!")


# Admin interface
def admin():
    window.withdraw()
    global win,b1,b2,b3,b4,cur,con
    win=Tk()
    win.title('Admin')
    win.geometry("600x350")
    win.configure(bg='lightyellow')
    b1=Button(win, height=2,width=20,text=' Add Student ',command=addstudent, font='cosmicsansms 11 italic', bg='skyblue')
    b2=Button(win, height=2,width=20,text=' View Students ',command=viewstudent, font='cosmicsansms 11 italic', bg='skyblue')
    b3=Button(win, height=2,width=20,text=' Delete Student ',command=deletestudent, font='cosmicsansms 11 italic', bg='skyblue')
    b4=Button(win, height=2,width=20,text=' LogOut ',command=logout, font='cosmicsansms 11 italic', bg='orange')
    b6=Button(win, height=2,width=20,text=' Add Book ',command=adminbook, font='cosmicsansms 11 italic', bg='skyblue')
    b7=Button(win, height=2,width=20,text=' View Books ',command=viewbook, font='cosmicsansms 11 italic', bg='skyblue')
    b8=Button(win, height=2,width=20,text=' Delete Book ',command=deletebook, font='cosmicsansms 11 italic', bg='skyblue')
    b5=Label(win, text=' Main Menu ', font='cosmicsansms 26 bold underline', fg='green', bg='lightyellow')
    b1.place(x=60,y=70)
    b2.place(x=60,y=130)
    b3.place(x=60,y=190)
    b4.place(x=200,y=250)
    b6.place(x=340,y=70)
    b7.place(x=340,y=130)
    b8.place(x=340,y=190)
    b5.place(x=200, y=10)
    win.mainloop()
    
# logout button
def logout():    
    win.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()

# Close Button
def closedb():
    global con,cur
    cur.close()
    con.close()


# Add User interface
def addstudent():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Student')
    win.geometry("600x300")
    win.configure(bg='lightyellow')
    b5=Label(win, text=' Enter Your Details ', font='cosmicsansms 20 bold underline', fg='green', bg='lightyellow')
    name=Label(win,text=' NAME ', font='cosmicsansms 11 italic bold', fg='black', bg='lightyellow')
    usid=Label(win,text='STUDENT ID', font='cosmicsansms 11 italic bold', fg='black', bg='lightyellow')
    password=Label(win, text='PASSWORD', font='cosmicsansms 11 italic bold', fg='black', bg='lightyellow')
    branch=Label(win,text='BRANCH', font='cosmicsansms 11 italic bold', fg='black', bg='lightyellow')
    mob=Label(win,text='MOBILE NO', font='cosmicsansms 11 italic bold', fg='black', bg='lightyellow')
    global e1,b
    e1=Entry(win,width=55)
    global e2
    e2=Entry(win,width=55)
    global e3
    e3=Entry(win,width=55)
    global e4
    e4=Entry(win,width=55)
    global e5
    e5=Entry(win,width=55)
    b=Button(win, height=2,width=21,text=' ADD STUDENT ',command=addstudents, font='cosmicsansms 9', bg='skyblue')
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closestudent, font='cosmicsansms 9', bg='orange')
    name.place(x=70,y=60)
    usid.place(x=70,y=100)
    password.place(x=70,y=140)
    branch.place(x=70,y=180)
    mob.place(x=70,y=220)
    e1.place(x=180,y=60)
    e2.place(x=180,y=100)
    e3.place(x=180,y=140)
    e4.place(x=180,y=180)
    e5.place(x=180,y=220)
    b.place(x=180,y=250)
    b1.place(x=360,y=250)
    b5.place(x=200,y=10)
    win.mainloop()


# Addstudents button
def addstudents():
    global con,cur
    connectdb()
    q="SELECT * FROM login WHERE userid = '%i'"
    
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '' or e5.get() == '':
        messagebox.showerror("Student", "Fill All Details")
        return None
        
    cur.execute(q%(int(e2.get())))
    student = cur.fetchone()
    
    if student is None:
        qq='INSERT INTO Login VALUE("%s","%i","%i","%s","%i")' 
        try:
            pas = int(e3.get())
        except ValueError:
            messagebox.showerror("Student", "Password Must be in Numbers")
            return None
        cur.execute(qq%(e1.get(),int(e2.get()),int(e3.get()),e4.get(),int(e5.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Student", "Student Added")
        closedb()
        admin()
    else:
        messagebox.showerror("Student","ID Already Taken.")
        closedb()


# Closestudent button
def closestudent():
    global win
    win.destroy()
    admin()

# Viewstudent Interface
def viewstudent():
    win=Tk()
    win.title('View Students')
    win.geometry("1100x250+270+180")
    win.configure(bg='lightyellow')
    treeview=Treeview(win,columns=("Name","User ID","Password","Branch","Mobile No"),show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("User ID", text="User ID")
    treeview.heading("Branch", text="Branch")
    treeview.heading("Password", text="Password")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("Name", anchor='center')
    treeview.column("User ID", anchor='center')
    treeview.column("Branch", anchor='center')
    treeview.column("Password", anchor='center')    
    treeview.column("Mobile No", anchor='center')
    index=0
    iid=0
    connectdb()
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()
    admin()


# Deletestudent Interface
def deletestudent():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Student')
    win.geometry("600x300")
    win.resizable(False,False)
    win.configure(bg='lightyellow')
    b5=Label(win, text=' Delete Student ', font='cosmicsansms 26 bold underline', fg='green', bg='lightyellow')
    usid=Label(win,text='STUDENT ID', font='cosmicsansms 11 italic', fg='black', bg='lightyellow')
    paswrd=Label(win,text='ADMIN \n PASSWORD', font='cosmicsansms 11 italic', fg='black', bg='lightyellow')
    global e1
    e1=Entry(win, width=50)
    global e2,b2
    e2=Entry(win, width=50)
    b1=Button(win, height=2,width=17,text=' DELETE ',command=deletestudents, font='cosmicsansms 10 bold', bg='skyblue')
    b2=Button(win, height=2,width=17,text=' CLOSE ',command=closestudent, font='cosmicsansms 10 ', bg='orange' )
    usid.place(x=80,y=80)
    paswrd.place(x=70,y=120)
    e1.place(x=180,y=80)
    e2.place(x=180,y=130)
    b1.place(x=180,y=180)
    b2.place(x=340,y=180)
    b5.place(x=200,y=20)
    win.mainloop()


# Deletestudents query
def deletestudents():
    connectdb()
    if e2.get()=='admin':
        q="SELECT * FROM login WHERE userid = '%i'"
        
        if e1.get() == '':
            messagebox.showerror("Delete", "Enter Correct ID")
            return None
            
        cur.execute(q%(int(e1.get())))
        book = cur.fetchone()
        
        if book is None:
            messagebox.showerror("Delete","Student Not Found.")
            closedb()
        else:
            qq="DELETE FROM login WHERE userid = '%i'"
            cur.execute(qq%(int(e1.get())))
            con.commit()
            win.destroy()
            messagebox.showinfo("Delete","Student Deleted Successfully.")
            closedb()
            admin()
            
    else:
        messagebox.showerror("Delete","Password is Wrong.")
        closedb()



# MySQL Connection
def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    global enter
    if enter==1:
        l='CREATE TABLE IF NOT EXISTS Login(name varchar(20),userid varchar(10),password int(10), branch varchar(20),mobile int(10))'
        b='CREATE TABLE IF NOT EXISTS Book(subject varchar(20),title varchar(20),author varchar(20),serial int(5))'
        i='CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20),serial varchar(10),issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter=enter+1
    query='SELECT * FROM Login'
    cur.execute(query)

# HomePage interface
def home():
    try:
        global window,b1,b2,e1,e2,con,cur,win
        window=Tk()
        window.title('Library')
        window.geometry("600x300")
        window.resizable(False,False)
        window.configure(bg='skyblue')
        wel=Label(window,text='LIBRARY',font='cosmicsansms 26 bold', fg='red', bg="lightyellow")
        lib=Label(window,text='MANAGEMENT',font='cosmicsansms 26 bold', fg='blue', bg='lightyellow')
        usid=Label(window,text='USER ID', font='cosmicsansms 10 italic', bg='skyblue')
        paswrd=Label(window,text='PASSWORD', font='cosmicsansms 10 italic', bg='skyblue')
        wel.pack(fill=X)
        lib.pack(fill=X)
        e1=Entry(window,width=40)
        e2=Entry(window,width=40)
        b1=Button(window,text=' LOGIN AS STUDENT' ,height=2,width=30,command=loginlibr, font='cosmicsansms 10 italic', bg="lightyellow")
        b2=Button(window,text=' LOGIN AS ADMIN ', height=2,width=30,command=loginadmin,font='cosmicsansms 10 italic', bg="lightyellow")
        usid.place(x=70,y=100)
        paswrd.place(x=70,y=140)
        e1.place(x=200,y=100)
        e2.place(x=200,y=140)
        b1.place(x=200,y=230)
        b2.place(x=200,y=180)
        window.mainloop()
    except Exception:
        window.destroy()
enter=1
home()