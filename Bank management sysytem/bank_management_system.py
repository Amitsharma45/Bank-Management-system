
import datetime
import tkinter as t
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import os
import shelve

os.chdir('C:\\Users\\charm\\Desktop\\db')
r=t.Tk()
r.title('bank system')
def call_main():
    #disable window m
    m.state(['withdraw'])
    main()
def check_value():
    # creating new account
    print(gen.get())
    if  ent_phone.get().isdigit() ==False or len(ent_phone.get())!=10:
            messagebox.showinfo('Error','Please enter correct phone no. value')

            ent_phone.focus_set()
    

    elif  ent_file.get().isalpha()==False:
        messagebox.showinfo('Error','Please enter correct name value')
    try:
        if  (int(e_d.get())>31 or int(e_d.get())<1) or( int(e_m.get())<1 or int(e_m.get())>12) or len(e_y.get())!=4 :
            messagebox.showinfo('Error','Please enter correct Date of birth  value')
        else:
            creating_acc()
    except ValueError:
       messagebox.showinfo('Error','Please fill entrys enter')
    
    
            
def creating_acc():
    a=shelve.open('acclist')
    file_name='91'+ent_phone.get()
    k=a['list']
    k.append(file_name)
    a['list']=k
    a.close()
    
    file_name='91'+ent_phone.get()
    new_file=shelve.open(file_name)
    new_file['acc_num']='91'+ent_phone.get()
    new_file['user_name']=ent_file.get()
    new_file['address']=ent_add.get()
    new_file['phone']=ent_phone.get()
    new_file['acc_type']=acctype.get()
    new_file['email']=ent_mail.get()
    new_file['balance']=0
    new_file['statement']=[ ]
    new_file['index']=1
    new_file['dob']=e_d.get()+' / ' +e_m.get()+' /'+e_y.get()
    new_file.close()
    messagebox.showinfo('MESSAGE','''YOUR ACCOUNT IS SUCCESSFUL CREATE
AND YOUR ACC. NO. '''+file_name)
def new():
    # creating new window for new account
    global ent_file,   m ,  ent_add,  ent_phone,acctype,gen,ent_mail,e_d,e_m,e_y
    r.state(['withdraw'])
    
    m=t.Tk()
    m.title('New Acoount')
    lab_=Label(m,text="From ",font=("",20))
    lab_.place(x=180,y=10)
    lab_name=Label(m,text='NAME :',font=("",16),fg='red')
    lab_name.place(x=40,y=70)
    lab_messege=Label(m,text="  (name less than or equal to 16 alpha)",font=("",10),fg='grey')
    lab_messege.place(x=155,y=100)
    lab_add=Label(m,text='ADDRESS :',font=("",16),fg='red')
    lab_add.place(x=40,y=125)
    lab_phone=Label(m,text='PHONE NO :',font=("",16),fg='red')
    lab_phone.place(x=40,y=160)   
    lab_gender=Label(m,text='GENDER :',font=("",16),fg='red')
    lab_gender.place(x=40,y=190)
    lab_dob=Label(m,text='D. O. B :',font=("",16),fg='red')
    lab_dob.place(x=40,y=225)
    lab_mail=Label(m,text='E-MAIL :',font=("",16),fg='red')
    lab_mail.place(x=40,y=265)
    lab_acctype=Label(m,text='ACC. Type :',font=("",16),fg='red')
    lab_acctype.place(x=40,y=305)
    lab_d=Label(m,text='(dd/mm/yyyy)',fg='grey')
    lab_d.place(x=320,y=230)


    e_d=ttk.Entry(m,width=2,font=("",16))
    e_d.place(x=165,y=225)
    e_m=ttk.Entry(m,width=2,font=("",16))
    e_m.place(x=205,y=225)
    e_y=ttk.Entry(m,width=4,font=("",14))
    e_y.place(x=255,y=225)
    ent_phone=ttk.Entry(m,width=10,font=("",16))
    
    ent_phone.place(x=165,y=160)
    ent_file=ttk.Entry(m,width=25,font=("",16))
    ent_file.place(x=165,y=70)
    ent_add=ttk.Entry(m,width=25,font=("",16))
    ent_add.place(x=165,y=125)
    ent_mail=ttk.Entry(m,width=30,font=("",16))
    ent_mail.place(x=165,y=265)
 


    acctype=StringVar()
    ttk.Radiobutton(m,text='Saving',value='Male',variable=acctype).place(x=165,y=310)
    ttk.Radiobutton(m,text='Current',value='Female',variable=acctype).place(x=250,y=310)
    gen=StringVar()
    aaa=ttk.Radiobutton(m,text='Male',value='0',variable=gen)
    aaa.place(x=165,y=195)
    a=ttk.Radiobutton(m,text='Female',value='1',variable=gen)
    a.place(x=250,y=195)

    but_submit=ttk.Button(m,text="submit" ,command=check_value)
    but_submit.place(x=250,y=350)
    #ent_.insert(0,"less then or equal to 16 letters")
    but_back=ttk.Button(m,text="Back",width=10,command=call_main)
    #but_back.place(x=10,y=10)
   # but_back=ttk.Button(m,text="verifi email",width=10,command=call_main)
    #but_back.place(x=10,y=10)
     
    but_back.grid(row=300,column=10,padx=10,pady=10)   
#check_value


    m.geometry('600x600')
    m.mainloop()
def aa():
    print()
    print(gen.get())
def open(a):
    global s
    op=shelve.open('acclist')
    o=op['list']
    name=ent.get()
    if name in op['list']:
            r.state(['withdraw'])
            s=t.Tk()
            s.title('HDB BANK')
            def withdraw():
                global e_withdraw
                l_withdraw=ttk.Label(s,text='Enter Amount to withdraw :',font=('',16)).place(x=45,y=230)
                e_withdraw=ttk.Entry(s,width=10,font=('',14))
                e_withdraw.focus_set()
                e_withdraw.bind('<Return>',sub_wid)
                e_withdraw.place(x=300,y=230)
                b_withdraw=ttk.Button(s,text='Click',command=sub_wid).place(x=150,y=270)
            def deposit():
                global e_deposit
                l_deposit=ttk.Label(s,text='Enter Amount to Deposit :',font=('',16)).place(x=45,y=230)
                e_deposit=ttk.Entry(s,width=10,font=('',14))
                e_deposit.focus_set()
                e_deposit.bind('<Return>',add_dep)
                e_deposit.place(x=300,y=230)
                b_deposit=ttk.Button(s,text='Click',command=add_dep).place(x=150,y=270)
            def sub_wid(a):
                if e_withdraw.get().isdigit()== True:
                    detail=shelve.open(name)
                    if detail['balance']>2000:
                        detail['balance']-=int(e_withdraw.get())
                        lab_balance.config(text='Balance :'+str(detail['balance']))
                        k=detail['statement']
                        tj.config(state='normal')
                        d=datetime.datetime.now()
                    
                        tj.delete('1.0', END)
                        tj.insert(INSERT,'Your   '+e_withdraw.get()+'\trupees successfull withdraw\n')
                        
                        tj.config(state='disabled')
                        
                        k.append(str(str(detail['index'])+'    '+str(d.year)+ ','+str(d.month)+','+str(d.day)+'                   ' + e_withdraw.get()+'dr.     '+str(detail['balance'])))
                        detail['index']+=1
                        #print(detail['statement'])
                        detail['statement']=k
                        #print(str(d))
                        detail.close()
                        e_withdraw.delete(0,t.END)
                        #messagebox.showinfo('With draw',e_withdraw.get()+' rupess successfully withdraw')
                    else:
                        messagebox.showinfo('Error','Low Balance')
                else:
                    messagebox.showinfo('Error','Enter correct value')
            def add_dep(a):
                if e_deposit.get().isdigit()== True:
                    detail=shelve.open(name)
                    detail['balance']+=int(e_deposit.get())
                    k=detail['statement']
                    tj.config(state='normal')
                    d=datetime.datetime.now()
                    
                    tj.delete('1.0', END)
                    lab_balance.config(text='Balance :'+str(detail['balance']))
                    tj.insert(INSERT,'Your   '+e_deposit.get()+'\trupees successfull deposit\n')
                    tj.config(state='disabled')
                    k.append(str(str(detail['index'])+'    '+str(d.year)+ ','+str(d.month)+','+str(d.day)+'     '+e_deposit.get()+'cr.     '+'              ' +str(detail['balance'])))
                    detail['index']+=1
                        #print(detail['statement'])
                    detail['statement']=k
                        #print(str(d))
                    detail.close()

                    detail.close()
                    e_deposit.delete(0,t.END)
                    #messagebox.showinfo('Deposit',e_deposit.get()+' rupess successfully deposit')
                else:
                    messagebox.showinfo('Error','Enter correct value')
            def sat():
                detail=shelve.open(name)
               
                tj.config(state='normal')
                tj.delete('1.0', END)
                tj.insert(INSERT,'So.no.   Date     Deposit      Withdraw    Balance \n')
                
                #t.insert(INSERT,str(str(detail['index'])+'\t' + e_withdraw.get()+'dr.\t'+str(detail['balance'])))
                for i in  detail['statement']:
                    #print(i,end='\n')
                    tj.insert(INSERT,i+'\n')
                
                tj.config(yscrollcommand=scroll.set)
                tj.config(state='disabled')
                
            tj=Text(s,width=60,height=12,wrap='word')
             
            tj.grid(row=1,column=0,pady=300,padx=50)
            scroll=Scrollbar(s,orient=VERTICAL,command=tj.yview)
            scroll.grid(row=1,column=1,pady=300,sticky=N+S)
        # scroll.place(x=460,y=230)
            #tj.place(x=30,y=300)    
            tj.config(state='disabled')
            #tj.config(state='disabled')
            global lab_balance
            detail=shelve.open(name) 
            lab_=ttk.Label(s,text='ACCOUNT DETAIL',font=('',20)).place(x=130,y=18)
            lab_name3=ttk.Label(s,    text='Name    :'+ detail['user_name'],font=('',13)).place(x=90,y=50)
            lab_phone2=ttk.Label(s,   text='Phone   :'+ detail['phone'],font=('',13)).place(x=90,y=70)
            lab_email3=ttk.Label(s,    text='Email    :'+ detail['email'],font=('',13)).place(x=90,y=90)
            lab_dob=ttk.Label(s,text='D. O. B. :'+ detail['dob'],font=('',13)).place(x=90,y=110)
            lab_phone25=ttk.Label(s, text='Address :'+ detail['address'],font=('',13)).place(x=90,y=130)
            lab_email33=ttk.Label(s,  text='Acc. No. :'+ detail['acc_num'],font=('',13)).place(x=90,y=150)
            lab_balance=ttk.Label(s,text='Balance :'+ str(detail['balance']),font=('',13))
            lab_balance.place(x=90,y=170)
            b=ttk.Button(s,text='Deposit',command=deposit).place(x=70,y=190)
            b1=ttk.Button(s,text='With draw',command=withdraw).place(x=190,y=190)
            b11=ttk.Button(s,text='statement',command=sat).place(x=310,y=190)
            b_back=ttk.Button(s,text='Back',width=10,command=back_main).place(x=10,y=10)
            s.geometry('600x500')
            s.mainloop()
    else:
        messagebox.showinfo('ERROR','Acc. No. Not Found')
def back_main():
    s.state(['withdraw'])
    r.state(['normal'])
def main():
    # main starting of program
    r.state(['normal'])
    global ent
    
    lab=Label(r,text='HDB Bank',font=("",30))
    lab1=Label(r,text='ACCOUNT ::',font=('',16),fg='red')
    ent=ttk.Entry(r,width=20,font=("",14))
    but =ttk.Button(r,text='Click',command=open)
    but1=ttk.Button(r,text='create new account',command=new)
    lab.place(x=170,y=50)   
    lab1.place(x=90,y=120)
    ent.place(x=220,y=125)
    but.place(x=210,y=180)
    but1.place(x=375,y=5)
    ent.focus_set()
    ent.bind('<Return>',open)
    r.geometry('500x400+100+50')
    
main()
r.mainloop()
                
