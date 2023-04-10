import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
choice=st.sidebar.selectbox('MY MENU',("Home","Student Login","Librarian Login"))
st.title("LIBRARY MANAGEMENT SYSTEM")
if(choice=="Home"):
    st.header('WELCOME')
    st.subheader('👉​There is no friend as loyal as 📚book 👈')
    st.image("https://www.pngkit.com/png/detail/443-4433043_library-management-system-library-management-system-png.png")
    st.markdown("This is Management Application- **developed for the purpose of project**.")
#-----------------------------------Student Login------------------------------------

elif(choice=="Student Login"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    sid=st.text_input("Enter Student ID")
    pwd=st.text_input("Enter Password")
    btn=st.button('Login')
    btn2=st.button("Logout")
    if btn2:
        st.session_state['login']=False
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
        c=mydb.cursor()
        c.execute("select * from student")
        for r in c:
            if(r[0]==sid and r[1]==pwd):
                st.session_state['login']=True
                break
        if(st.session_state['login']==False):
            #st.header("Incorrect ID or Password")
            e = RuntimeError('RuntimeError-Incorrect ID or Password❌')
            st.exception(e)
    if(st.session_state['login']==True):
        #st.header("Login Successful")
        st.success('Login Successful!', icon="✅")
        st.balloons()
#---------------------------------------Search Book-----------------------------------
        choice2=st.selectbox("Features",("None","Search Book","Issue Book","CHECK BOOK RETURN","BOOK REQUIREMENT"))
        if(choice2=="Search Book"):
            choice3=st.selectbox("Branches",('','EE','EC','CS'))
            if(choice3=='EE'):
                #bookname=st.text_input("enter name")
                mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                c=mydb.cursor()
                c.execute("select * from EEbooks")
                l=[]
                for r in c:
                    l.append(r)
                    books=st.selectbox("search books name 📚​",l)       
                df=pd.DataFrame(data=l,columns=['Book ID','Book Name','Author Name'])
                st.dataframe(df)
            elif(choice3=='EC'):
                #bookname=st.text_input("enter name")
                mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                c=mydb.cursor()
                c.execute("select * from ECbooks")
                l=[]
                for r in c:
                    l.append(r)
                    books=st.selectbox("search books name 📚​",l)    
                df=pd.DataFrame(data=l,columns=['Book ID','Book Name','Author Name'])
                st.dataframe(df)
            elif(choice3=='CS'):
                #bookname=st.text_input("enter name")
                mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                c=mydb.cursor()
                c.execute("select * from CSbooks")
                l=[]
                for r in c:
                    l.append(r)
                    books=st.selectbox("search books name 📚​",l)     
                df=pd.DataFrame(data=l,columns=['Book ID','Book Name','Author Name'])
                st.dataframe(df)


                                                                                       
#--------------------------------------------Issue Book-----------------------------------------------
        elif(choice2=='Issue Book'):
            bid=st.text_input("Enter Book ID")
            stid=st.text_input("Enter Your ID")
            agree = st.checkbox('check detail again')
            if agree:
                btn3=st.button("Issue Book")
                if btn3:
                    doi=str(datetime.datetime.now())     
                    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                    c=mydb.cursor()
                    c.execute("insert into issue values(%s,%s,%s)",(doi,bid,stid))
                    mydb.commit()
                    st.success('Book Issued Successfully!', icon="✅")
                    #st.header("Book Issued Successfully")

#-----------------------------------------------BOOK REQUIREMENT----------------------------------------------
        elif(choice2=='BOOK REQUIREMENT'):
            bid=st.text_input("Enter Book ID")
            bookname=st.text_input("Enter book name")
            authorname=st.text_input("Enter author name")
            agree = st.checkbox('check detail again')
            if agree:
                btn4=st.button("request send")
                if btn4:
                    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                    c=mydb.cursor()
                    c.execute("insert into bookrequirements values(%s,%s,%s)",(bid,bookname,authorname))
                    mydb.commit()
                    st.success('request send successfully!', icon="✅")
                    #st.header("request send successfully")

#--------------------------------------------CHECK BOOK RETURN------------------------------------------
        elif(choice2=="CHECK BOOK RETURN"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
            c=mydb.cursor()
            c.execute("select * from returned")
            k=[]
            for r in c:
                k.append(r)  
            df=pd.DataFrame(data=k,columns=['DIO','Book ID','SID'])
            st.dataframe(df)





        


          
        
#--------------------------------------------Librarian Login-------------------------------------------------   
    

elif(choice=="Librarian Login"):
    if 'login2' not in st.session_state:
        st.session_state['login2']=False
    sid=st.text_input("Enter Librarian ID")
    pwd=st.text_input("Enter Password")
    btn=st.button('Login')
    btn2=st.button("Logout")
    if btn2:
        st.session_state['login2']=False
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
        c=mydb.cursor()
        c.execute("select * from librarian")
        for r in c:
            if(r[0]==sid and r[1]==pwd):
                st.session_state['login2']=True
                break
        if(st.session_state['login2']==False):
            #st.header("Incorrect ID or Password")
            e = RuntimeError('RuntimeError-Incorrect ID or Password❌')
            st.exception(e)
    if(st.session_state['login2']==True):
        #st.header("Login Successful")
        st.success('Login Successful!', icon="✅")
        st.balloons()
#--------------------------------------------Check Issue Book---------------------------------
        choice2=st.selectbox("Features",("None","Add pdfbooks","Check Issue Book","Add new Book","BOOK RETURN","REMOVE BOOK","CHECK BOOK REQUIREMENT","Penalty"))
        if(choice2=="Check Issue Book"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
            c=mydb.cursor()
            c.execute("select * from issue")
            l=[]
            for r in c:
                l.append(r)  
            df=pd.DataFrame(data=l,columns=['DOI','Book ID','Student ID'])
            st.dataframe(df)

 #-------------------------------------------CHECK BOOK REQUIREMENT--------------------------------------------
        elif(choice2=="CHECK BOOK REQUIREMENT"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
            c=mydb.cursor()
            c.execute("select * from bookrequirements")
            k=[]
            for r in c:
                k.append(r)  
            df=pd.DataFrame(data=k,columns=['Book ID','Book name','Author name'])
            st.dataframe(df)
#-----------------------------------------------Add new Book-------------------------------------------------
        elif(choice2=='Add new Book'):
            choice3=st.selectbox("Branches",('','EE','EC','CS'))
            result=("search Branches name",choice3)
            if(choice3=='EE'):
                bid=st.text_input("Enter Book ID")
                bname=st.text_input("Enter Book Name")
                aname=st.text_input("Enter Author Name")
                agree = st.checkbox('check detail again')
                if agree:
                    btn3=st.button("Add new Book")
                    if btn3:                
                        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                        c=mydb.cursor()
                        c.execute("insert into EEbooks values(%s,%s,%s)",(bid,bname,aname))
                        mydb.commit()
                        st.success('Book Added Successfully!', icon="✅")
                        #st.header("Book Added Successfully")
            if(choice3=='CS'):
                bid=st.text_input("Enter Book ID")
                bname=st.text_input("Enter Book Name")
                aname=st.text_input("Enter Author Name")
                agree = st.checkbox('check detail again')
                if agree:
                    btn3=st.button("Add new Book")
                    if btn3:                
                        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                        c=mydb.cursor()
                        c.execute("insert into CSbooks values(%s,%s,%s)",(bid,bname,aname))
                        mydb.commit()
                        st.success('Book Added Successfully!', icon="✅")
        
 #--------------------------------------------REMOVE BOOK-----------------------------------------------------               

        elif(choice2=="REMOVE BOOK"):
            choice3=st.selectbox("Branches",('','EE','EC','CS'))
            result=("search Branches name",choice3)
            if(choice3=='EE'):
                bid=st.text_input("Enter BOOK ID")
                agree = st.checkbox('check detail again')
                if agree:
                    btn4=st.button("Book removed")
                    if btn4:                
                        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                        c=mydb.cursor()
                        c.execute("delete from EEbooks where bookid=%s",(bid,))
                        mydb.commit()
                        #st.header("book Delete Successfully")
                        st.success('Book Delete Successfully!', icon="✅")
                
            if(choice3=='EC'):
                bid=st.text_input("Enter BOOK ID")
                agree = st.checkbox('check detail again')
                if agree:
                    btn4=st.button("Book removed")
                    if btn4:                
                        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                        c=mydb.cursor()
                        c.execute("delete from ECbooks where bookid=%s",(bid,))
                        mydb.commit()
                        #st.header("book Delete Successfully")
                        st.success('Book Delete Successfully!', icon="✅")
            
               

#--------------------------------------------BOOK RETURN------------------------------------------
        elif(choice2=="BOOK RETURN"):
            bookid=st.text_input("Enter Book ID")
            sid=st.text_input("Enter student ID")
            agree = st.checkbox('check detail again')
            if agree:
                btn5=st.button("Book returned")
                if btn5:
                    DIO=str(datetime.datetime.now())
                    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                    c=mydb.cursor()
                    c.execute("insert into returned values(%s,%s,%s)",(DIO,bookid,sid))
                    mydb.commit()
                    #st.header("Book returned Successfully")
                    st.success('Book returned Successfully!', icon="✅")

#----------------------------------------add pdf book-------------------------------------------
        elif(choice2=="Add pdfbooks"):
            pdf_file =st.file_uploader("Uploade DOC",type=['pdf'])
            btn3=st.button("Add new pdf")
            if btn3:
                mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                c=mydb.cursor()
                c.execute("insert into pdf values(%s,)",(pdf_file,))
                mydb.commit()
                st.subheader('Pdf File')
                if uploaded_file is not None:
                    file_details={"filename":pdf_file.name}
                    st.write(file_details)
'''
        elif(choice7=="Penalty"):
            bid=st.text_input("Enter Book ID")
            sid=st.text_input("Enter student ID")
            btn5=st.button("request send")
            if btn5:
                mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
                c=mydb.cursor()
                c.execute("select*from issue;")
                k=[]
                for r in c:
                    k.append(r)
                df=pd.DataFrame(data=k,columns=['DOI','bookid','sid'])
        
                c.execute("select*from returned")
                l=[]
                for i in c:
                    l.append(i)
                di=pd.DataFrame(data=k,columns=['DOI','bookid','sid'])
                if k[1]==l[1]:
                    st.dataframe(df)
                    st.dataframe(di)
            
'''
        
                
                   

#------------------------------------Self Analysis-------------------------------------------------------
choice6=st.sidebar.selectbox("Self Analysis",('','self analysis','Check Record'))
if(choice6=='self analysis'): 
    totalhour=st.number_input("enter study hours")
    btn3=st.button("recorded")
    if btn3:
        doi=str(datetime.datetime.now())
        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
        c=mydb.cursor()
        c.execute("insert into self_analysis values(%s,%s)",(doi,totalhour))
        mydb.commit()
        st.header("record recorded")


elif(choice6=="Check Record"):
    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='lms')
    c=mydb.cursor()
    c.execute("select * from self_analysis")
    k=[]
    for r in c:
        k.append(r)  
    df=pd.DataFrame(data=k,columns=['DOI','Total study hours'])
    st.dataframe(df)



            
            

                        
                        

         
        






     

                

            


