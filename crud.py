#creating database
'''
import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',password='12345678')
mycur=mycon.cursor()
nod=input("Enter name of database that you want to create : ")
q="create database %s"%nod
mycur.execute(q)
print("Database has been created successfully!!!")
'''

# creating table in database
import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',password='12345678',database='rizwan')
mycur=mycon.cursor()
q="create table new (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
a="create table new1 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
b="create table new2 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
c="create table new3 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
d="create table new4 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
e="create table new5 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
f="create table new6 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
g="create table new7 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
h="create table new8 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
i="create table new9 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
j="create table new10 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
k="create table new11 (pid varchar(10) primary key, pname varchar(50), pmanager varchar(50),psdate date, pedate date)"
mycur.execute(a)
mycur.execute(b)
mycur.execute(c)
mycur.execute(d)
mycur.execute(e)
mycur.execute(f)
mycur.execute(g)
mycur.execute(h)
mycur.execute(i)
mycur.execute(j)
mycur.execute(k)
mycur.execute(l)
mycur.execute(m)

print("Table created")



