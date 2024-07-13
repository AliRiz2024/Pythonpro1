# **************************************************#
#           -----------------------------           #
#           |Database management system |           #
#           -----------------------------           #
#( CRUD OPERATION :INSERT RECORD INSIDE DATABASE(C) #
#                  READ DATA FROM DATABASE (R)      #
#                  UPDATE DATA IN DATABASE (U)      #
#                  DELETE DATA IN DATABASE (D)      #
# RIZWAN STUDENT MANAGEMENT SYSTEM [ CRUD - OPERATION


import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',password='12345678',database='rizwan')
mycur=mycon.cursor()
print("\t\t--------------------------------------------------------------------------------------")
print("\t\t\t\t Welcome to the student database made by Rizwan")
print("\t\t--------------------------------------------------------------------------------------")
ch=int(input("\t\t\t\t Press 1 for login and 2 for Sign up : "))
if ch==1:
    print("\n\t\t\t\t user login : ")
    uid=input("\t\t\t\t Enter user Id : ")
    pas=input("\t\t\t\t Enter password : ")
    q="select userid,password from users where userid='{}' and password='{}'".format(uid,pas)
    mycur.execute(q)
    data=mycur.fetchall()
    if data==[]:
        print("Login fail because invalid user id or password")
    else :
        print("\t\t--------------------------------------------------------------------------------------")
        print("\t\t\t\t Welcome to the student Management system")
        print("\t\t--------------------------------------------------------------------------------------")
        print("\t\t\t Press 1 New Entry of Student : ")
        print("\t\t\t Press 2 fro Student verification : ")
        print("\t\t\t Press 3 to update Student Details : ")
        print("\t\t\t Press 4 to Delete student record : ")
        print("\t\t\t Press 5 to close the Application : ")
        chh=int(input("\t\t\t Enter your choice : "))
        if chh==1: 
            sid=input("Enter student id : ")
            sname=input("Enter student name : ")
            dob=input("Enter student date of birth : ")
            phone=input("Enter student ph no  : ")
            doa=input("Enter student date of admission : ")
            cid=input("Enter student course id : ")
            q="insert into student values('{}','{}','{}','{}','{}','{}'".format(sid,sname,dob,phone,doa,cid)
            mycur.execute(q)
            mycon.commit()
            print("Record saved successfully")
        elif chh==2:
            sid=input("Enter student Id : ")
            q="select * from student"
            mycur.execute(q)
            data=mycur.fetchall()
            if data==[]:
                print("Data not found")
            else :
                print("Record found \n\t",data)
        elif ch==3:
            pass
        elif ch==4:
            pass
        else :
            pass
elif ch==2:
    print("\n\t\t\t\t User Sign up")
    uid=input("Enter user id : ")
    pas=input("Enter password : ")
    q="insert into users values('{}','{}')".format(uid,pas)
    mycur.execute(q)
    mycon.commit()
        
        
