import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rajs727571@",
    database="db1"
    )
cursor=con.cursor()
while True:
    def insert():
        roll_no=int(input("enter roll_no:"))
        name=input("enter name:")
        branch=input("enter branch:")
        c=eval(input("enter c marks:"))
        cplus=eval(input("enter c++ marks:"))
        python=eval(input("enter python marks:"))
        total=c+cplus+python
        per=total/3
        sql="INSERT INTO record3(roll_no,name,branch,c,cplus,python,total,per) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(roll_no,name,branch,c,cplus,python,total,per)
        cursor.execute(sql,values)
        con.commit()
        print("✅ data successfully inserted into table record3")
        
    def download():
        roll_no=input("enter roll_no:")
        query="select * from record3 where roll_no=%s"
        cursor.execute(query,(roll_no,))
        row=cursor.fetchone()
        if row:
            print(row)
            file=open("result.txt","w")
            file.write(str(row))
            file.close()
        else:
            print("record not found") 
               
    k=int(input('''press 1 for insert
     2 for download:'''))  
    if k==1:
        insert()
    elif k==2:
        download()
        
    else:
        print("wrong choice")          
    con.close()
    cursor.close()    