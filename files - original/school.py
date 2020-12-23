import mysql.connector as sql
import webbrowser as www
import numpy as np
import matplotlib.pyplot as p
import tkinter as tk
from tkinter import ttk
from os import system


def sign_up(event5):
     global class3,name1,password3,cpassword1,answer,sq,tkvar,class2,tkvar2
     global root,root6
     global root2
     root6.withdraw()
     class2=tkvar.get()
     if class2=='11' or class2=='12':
          pass
     else:
          global class3,name1,password3,cpassword1,answer,sq
          root2=tk.Tk()
          root2.iconbitmap('signup.ico')
          root2['bg'] = 'white'
          root2.title('Sign up')
          name=tk.Label(root2,text='Name: ',bg = 'white',font = ('Times New Roman',20,'bold'))
          name.grid(row=3,column=2)
          password2=tk.Label(root2,text='Password: ',bg = 'white',font = ('Times New Roman',20,'bold'))
          password2.grid(row=5,column=2)
          name1=tk.Entry(root2,font = ('Times New Roman',20))
          name1.grid(row=3,column=3)
          password3=tk.Entry(root2,show='*',font = ('Times New Roman',20))
          password3.grid(row=5,column=3)
          cpassword=tk.Label(root2,text='Confirm Password: ',bg = 'white',font = ('Times New Roman',20,'bold'))
          cpassword.grid(row=6,column=2)
          cpassword1=tk.Entry(root2,show='*',font = ('Times New Roman',20))
          cpassword1.grid(row=6,column=3)
          secuques=tk.Label(root2,text='Security Question:',font=('Times New Roman',20,'bold'),bg='white')
          secuques.grid(row=7,column=2)
          questions=['What is your favourite colour?','Which is your favourite animal?','What is your favourite food?','A random word']
          sq=ttk.Combobox(root2,values=questions,font = ('Times New Roman',19),state='readonly')#creates a drop down in which text cannot be edited
          sq.current(0)
          sq.grid(row=7,column=3,sticky='we')
          ans=tk.Label(root2,text='Answer:',font=('Times New Roman',20,'bold'),bg='white')
          ans.grid(row=8,column=2)
          answer=tk.Entry(root2,font=('Times New Roman',20,'bold'))
          answer.grid(row=8,column=3)
          submit=tk.Button(root2,text='Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
          submit.bind('<Button-1>',sqlreg)
          submit.grid(row=9,column=2)
          back=tk.Button(root2,text='Back',fg = 'black',bg = 'red',font = ('Lucida Calligraphy',15))
          back.bind('<Button-1>',back2)
          back.grid(row=9,column=3)
          rClickbindersig(root2)#binds the window for right click
     

# To withdraw login page

def back1(event):
     root1.withdraw()#Hides the window
     main()

def back111(event):
     root11.withdraw()
     login1('x')
     
#To ask for daily attendance when button is clicked
     
def dailyattendance(x):
     global col,month,result,root9
     root9.withdraw()
     demo = sql.connect(user = 'root',host = 'localhost',password = 'tiger',database = result)
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM {}_ATTENDANCE'.format(month))
     rj = mycursor.fetchall()
     if rj != []:
          demo = sql.connect(user = 'root',host = 'localhost',password = 'tiger',database = result)
          mycursor = demo.cursor()
          f = open('names/templates/daily_attendance.html','w')
          m = '<html>\n<body bgcolor = "orange">\n<form action = "#" method = "POST"> \n {%csrf_token%}'
          mycursor.execute('SELECT NAME FROM {}_ATTENDANCE'.format(month))
          r123 = mycursor.fetchall()
          for i in range(len(r123)):
               m += '{}<br> P:<input type = "radio" name = "{}" value  = "p"><br>A:<input type = "radio" name = "{}" value  = "a"><br><hr><br>'.format(r123[i][0],r123[i][0],r123[i][0])
          m+="<button type = 'Submit'>Submit</button>\n</form>\n<input type='button' value='Close' onclick='parent.close()'>\n</body>\n</html>"
          f.write(m)          
          f.close()
          f = open('names/stuattend.csv','w')
          f.write(' ')
          f.close()
          f = 'attendance1.html'
          www.open_new_tab(f)
          system('cd names && manage.py runserver &')
          f = open('names/stuattend.csv')
          l = []
          for i in f.readlines():
               if i == '\n' or i[0:5] == ' csrf' or i[0:4] == 'csrf':
                    pass #empty statement does nothing
               else:
                    if i[-1] == '\n':
                         l.append(i[:-1])
          l1 = []
          mycursor.execute('SELECT COUNT(NAME) FROM {}_ATTENDANCE'.format(month))
          r0 = mycursor.fetchone()
          for i in range(0,len(l),r0[0]):
               y = []
               for j in range(r0[0]):
                    y.append(l[j])
               l1.append(y)
          for z in l1:
               d = {}
               for i in z:
                    x = i.index(',')#to get the index of ',' or any character if specified
                    d[i[:x]] = i[x+1:]
          for i in d.keys():
               if d[i] == 'a':
                    mycursor.execute('UPDATE {}_ATTENDANCE SET {} = "A" WHERE NAME LIKE "{}"'.format(month,col,i))
                    demo.commit()
               else:
                    mycursor.execute('UPDATE {}_ATTENDANCE SET {} = "P" WHERE NAME LIKE "{}"'.format(month,col,i))
                    demo.commit()
          open_form(result)

     else:
          tk.messagebox.showinfo('Name','There are no students in class')
          open_form('x')
          
#Right click options

def rClickersig(e):
     def rClick_Copy(e):
          e.widget.event_generate('<Control-c>')#does the function of ctrl+c(copy)

     def rClick_Cut(e):
          e.widget.event_generate('<Control-x>')#does the function of ctrl+x(cut)

     def rClick_Paste(e):
          e.widget.event_generate('<Control-v>')#does the function of ctrl+v(paste)

     def rClick_Clear(e):
          e.widget.event_generate('<Control-a>')#does the function of ctrl+a(select all)
          e.widget.event_generate('<Delete>')#does the function of delete button

     e.widget.focus()

     nclst=[
            (' Cut', lambda e: rClick_Cut(e)),
            (' Copy', lambda e: rClick_Copy(e)),
            (' Paste', lambda e: rClick_Paste(e)),
            (' Clear', lambda e: rClick_Clear(e))
            ]

     rmenu=tk.Menu()

     for (txt, cmd) in nclst:
          rmenu.add_command(label=txt, command=cmd)

     rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

def rClickerlog(e):
     global class1,root1
     def rClick_Copy(e):
          e.widget.event_generate('<Control-c>')

     def rClick_Cut(e):
          e.widget.event_generate('<Control-x>')

     def rClick_Paste(e):
          e.widget.event_generate('<Control-v>')

     def rClick_Clear(e):
          e.widget.event_generate('<Control-a>')
          e.widget.event_generate('<Delete>')

     def sub456(event):
          global cp1,np1,class1,root12
          if cp1.get() == np1.get():
               demo=sql.connect(user='root',password='tiger',host='localhost',database='teacher')
               mycursor=demo.cursor()
               mycursor.execute('UPDATE TEACHERTAB SET PASSWORD = "{}" WHERE CLASS LIKE "{}"'.format(str(cp1.get()),str(class1.get())))
               demo.commit()
               root12.withdraw()
               tk.messagebox.showinfo(' ','Password Successfully changed')
               main()
          else:
               tk.messagebox.showerror('password','Passwords do not match')# show error message

     def ans(event):
          global answer1,class1,result23,root11,cp1,np1,root12
          root11.withdraw()
          demo=sql.connect(user='root',password='tiger',host='localhost',database='teacher')
          mycursor=demo.cursor()
          ans2=answer1.get()
          if ans2==result23[0][1]:
               root12=tk.Tk()
               np=tk.Label(root12,text='New password',font = ('Times New Roman',20,'bold'))
               np.grid(row = 1,column = 1)
               np1 = tk.Entry(root12,show = '*',font = ('Times New Roman',20))
               np1.grid(row = 1,column = 2)
               cp=tk.Label(root12,text='Confirm password',font = ('Times New Roman',20,'bold'))
               cp.grid(row = 2,column = 1)
               cp1 = tk.Entry(root12,show = '*',font = ('Times New Roman',20))# show * instead of text entered
               cp1.grid(row = 2,column = 2)
               s = tk.Button(root12,text = 'Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
               s.grid(row = 3,column = 1)
               s.bind('<Button-1>',sub456)
          else:
               tk.messagebox.showerror('wrong answer','Wrong Answer')
               main()
               
     def forgot_password(e):
          global answer1,class1,result23,root11
          demo=sql.connect(user='root',password='tiger',host='localhost',database='teacher')
          mycursor=demo.cursor()
          root1.withdraw()
          mycursor.execute('SELECT QUESTION,ANSWER FROM TEACHERTAB WHERE CLASS LIKE "{}"'.format(str(class1.get())))
          result23=mycursor.fetchall()
          if result23 != []:
               root11=tk.Tk()
               root11.title('Forgot Password')
               ques1=tk.Label(root11,text=str(result23[0][0]),font = ('Times New Roman',20))
               ques1.grid(row=1,column=1)
               answer1=tk.Entry(root11,font = ('Times New Roman',20))
               answer1.grid(row=1,column=2,sticky='we')#we stands for west and east respectively
               submit11=tk.Button(root11,text='Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
               submit11.grid(row=3,column=1)
               submit11.bind('<Button-1>',ans)
               back11=tk.Button(root11,text='Back',fg = 'black',bg = 'red',font = ('Lucida Calligraphy',15))
               back11.grid(row=3,column=2)
               back11.bind('<Button-1>',back111)
          else:
               tk.messagebox.showerror('Registration Error','You are not Registered')
               login1('x')
     e.widget.focus()

     nclst=[(' Cut', lambda e=e: rClick_Cut(e)),
            (' Copy', lambda e=e: rClick_Copy(e)),
            (' Paste', lambda e=e: rClick_Paste(e)),
            ('Clear', lambda e=e: rClick_Clear(e)),
            ('Forgot/Change password', lambda e=e: forgot_password(e))
            ]

     rmenu=tk.Menu()

     for (txt, cmd) in nclst:
          rmenu.add_command(label=txt, command=cmd)

     rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

def rClickbindersig(r):
   for b in ['Text', 'Entry']: 
       r.bind_class(b, sequence='<Button-3>',func=rClickersig, add='')

def rClickbinderlog(r):
   for b in ['Tk','Text','Entry']: 
       r.bind_class(b, sequence='<Button-3>',func=rClickerlog, add='')#binds the window/text/entry and runs when right clicked

# To withdraw signup page 
     
def back2(event):
     root2.withdraw()
     
# To open the frame without adding values

def skp(event):
     global root9
     marks2(result)
     attendance1()
     exec('{}'.format('octo(result)'))
     exec('{}'.format('jan(result)'))
     exec('{}'.format('feb(result)'))
     exec('{}'.format('mar(result)'))
     exec('{}'.format('jun(result)'))
     exec('{}'.format('jul(result)'))
     exec('{}'.format('aug(result)'))
     exec('{}'.format('sep(result)'))
     exec('{}'.format('nov(result)'))
     exec('{}'.format('dec(result)'))
     report(result)
     reportcard1_10(result)
     avg_mark(result)
     root9.withdraw()
     html('x')

def delname(event):
     global na1,month,result
     demo=sql.connect(user='root',password='tiger',host='localhost',database=result)
     mycursor=demo.cursor()
     mycursor.execute("DELETE FROM {}_ATTENDANCE WHERE NAME LIKE '{}'".format(month,na1.get()))#delete the entry of student
     mycursor.execute("DELETE FROM MARKS WHERE NAME LIKE '{}'".format(na1.get()))
     demo.commit()
     tk.messagebox.showinfo('delete','Student name deleted')
     
def delnamew(event):
     global na1,root13
     root13=tk.Tk()
     na=tk.Label(root13,text='Name:',font=('Times New Roman',20,'bold'))
     na.grid(row=1,column=1)
     na1=tk.Entry(root13,font=('Times New Roman',20))
     na1.grid(row=1,column=2,sticky='we')
     sub13=tk.Button(root13,text='Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
     sub13.grid(row=2,column=1,sticky='we')
     back=tk.Button(root13,text='Back',fg = 'black',bg = 'red',font = ('Lucida Calligraphy',15),command = root13.destroy)
     back.grid(row = 2,column = 2)
     sub13.bind('<Button-1>',delname)
# To update the marks

def upmar1(event):
     global root9,root7,result
     root9.withdraw()
     file = open('names/stumarks.csv','w+')
     file.write(' ')
     file.close()
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = result)
     mycursor = demo.cursor()
     f = 'marks1.html'
     www.open_new_tab(f)#using the web browser module it is used to open a html file
     system('cd names && manage.py runserver &')#opens command prompt with the address till the django apps and run a html file using django and save the values
     file = open('names/stumarks.csv')
     l = []
     for i in file.readlines():
          if i == '\n' or i[0:5] == ' csrf' or i[0:4] == 'csrf':
               pass #empty statement does nothing
          else:
               if i[-1] == '\n':
                    l.append(i[:-1])
     l1 = []
     for i in range(0,len(l),8):
          y = [l[i],l[i+1],l[i+2],l[i+3],l[i+4],l[i+5],l[i+6],l[i+7]]
          l1.append(y)
     #print(l1)
     for z in l1:
          d = {}
          for i in z:
               x = i.index(',')#to get the index of ',' or any character if specified
               d[i[:x]] = i[x+1:]
          mycursor.execute('UPDATE MARKS SET COMPUTER = {} WHERE NAME LIKE "{}"'.format(d['comp'],d['nname']))
          mycursor.execute('UPDATE MARKS SET L3 = {} WHERE NAME LIKE "{}"'.format(d['l3'],d['nname']))
          mycursor.execute('UPDATE MARKS SET L2 = {} WHERE NAME LIKE "{}"'.format(d['l2'],d['nname']))
          mycursor.execute('UPDATE MARKS SET MATHEMATICS = {} WHERE NAME LIKE "{}"'.format(d['maths'],d['nname']))
          mycursor.execute('UPDATE MARKS SET ENGLISH = {} WHERE NAME LIKE "{}"'.format(d['eng'],d['nname']))
          mycursor.execute('UPDATE MARKS SET SOCIAL = {} WHERE NAME LIKE "{}"'.format(d['soc'],d['nname']))
          mycursor.execute('UPDATE MARKS SET SCIENCE = {} WHERE NAME LIKE "{}"'.format(d['sci'],d['nname']))
          demo.commit()
     open_form('x')
     
def form(event):
     global root9,root7,result,col,month,d
     root9.withdraw()
     file = open('names/studata.csv','w+')
     file.write(' ')
     file.close()
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = result)
     mycursor = demo.cursor()
     f = 'name.html'
     www.open_new_tab(f)
     system("cd names && manage.py runserver &")
     file = open('names/studata.csv')
     l = []
     for i in file.readlines():
          if i == '\n' or i[0:5] == ' csrf' or i[0:4] == 'csrf':
               pass
          else:
               if i[-1] == '\n':
                    l.append(i[:-1])
     l1 = []
     for i in range(0,len(l),3):
          y = [l[i],l[i+1],l[i+2]]
          l1.append(y)
     for z in l1:
          d = {}
          for i in z:
               x = i.index(',')
               d[i[:x]] = i[x+1:]
          mycursor.execute('INSERT INTO {}_ATTENDANCE (NAME,{}) VALUES ("{}","P")'.format(month,col,d['nname']))
          mycursor.execute('INSERT INTO MARKS VALUES ({},"{}","0","0","0","0","0","0","0")'.format(int(d['rollno']),d['nname']))
          demo.commit()
     open_form('x')
# To ask to add values or not

def open_form(event):
     global root9,result,root7
     try:
          root7.withdraw()
          pass
     except NameError:
          pass
     root9 = tk.Toplevel()
     root9['bg'] = 'white' #adds background colour to the window
     root9.title(' ')
     root9.state('zoomed')#Opens the window in maximize view
     add = tk.Label(root9,text = 'Do you want to ...',bg = 'white',font = ('Times New Roman',30,'bold'))
     add.grid(row = 0,column = 4,padx = 50)
     addpic=tk.PhotoImage(file='add_name.png')
     val = tk.Button(root9,image=addpic)
     val.grid(row = 2,column = 2,padx=40)
     val.bind('<Button-1>',form)
     a123 = tk.Label(root9,text = 'Add Name',bg = 'white',font = ('Times New Roman',15))
     a123.grid(row = 3,column = 2)
     val.image=addpic
     demo = sql.connect(user = 'root',host = 'localhost',password = 'tiger',database = result)
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM {}_ATTENDANCE'.format(month))
     rj = mycursor.fetchall()
     if rj != []:
          delpic=tk.PhotoImage(file='delete_name.png')
          dels = tk.Button(root9,image=delpic)
          dels.grid(row = 2,column = 4)
          abc = tk.Label(root9,text = 'Delete Name',bg = 'white',font = ('Times New Roman',15))
          abc.grid(row = 3,column = 4)
          dels.bind('<Button-1>',delnamew)
          dels.image=delpic
          att = tk.PhotoImage(file = 'attendance.png')
          dayat = tk.Button(root9,image = att)
          dayat.grid(row = 2,column = 8)
          day1 = tk.Label(root9,text = 'Update Attendance',bg = 'white',font = ('Times New Roman',15))
          dayat.bind('<Button-1>',dailyattendance)
          dayat.image=att
          day1.grid(row = 3,column = 8)
          upmarpic=tk.PhotoImage(file='up_marks.png')
          upmar = tk.Button(root9,image=upmarpic)
          upmar.grid(row = 4,column = 3)
          upmar.bind('<Button-1>',upmar1)
          upmar.image=upmarpic
          upmar3= tk.Label(root9,text = 'Update Marks',bg = 'white',font = ('Times New Roman',15))
          upmar3.grid(row=5,column=3)
          skippic=tk.PhotoImage(file='skip.png')
          skip3 = tk.Button(root9,image=skippic)
          skip3.grid(row = 4,column = 6,pady = 60,padx = 40)
          skip3.bind('<Button-1>',skp)
          skip3.image=skippic
     
# To plot the graph of marks for each student

def marks2(event):
     demo = sql.connect(user = 'root',
                       password = 'tiger',
                       host = 'localhost',
                       database = event)
     mycursor = demo.cursor()
     mycursor.execute("SELECT * FROM MARKS")
     l = []
     result = list(mycursor.fetchall())
     mar = []
     
     for i in result:     
         l.append(i[1])
         mar.append(i[2:])
      
     for i in range(len(l)): 
         x = np.arange(len(result[0]))
         p.ylabel('Marks')
         p.xlabel('Subjects')
         p.title(l[i].upper())
         r = []
         p.ylim(0,100)
         for z in mar:
             l1 = []
             for y in z:
                 l1.append(int(y))
             r.append(l1)
         a = [32,32,32,32,32,32,32] 
         p.figure()
         p.ylim(0,100)
         y = ['COMPUTER','ENGLISH','MATHS','SCIENCE','SOCIAL','L2','L3']
         p.plot(y,a,'r') 
         p.plot(y,r[i])
         
         p.plot(y,r[i],'ko')
         p.savefig('folder\marks'+l[i]+'.png')
         
     f = open('folder/marks.html','w')
     m = '<html>\n<body>'
     
     for i in range(len(l)):
          m = m + "<a href = '{}'>{}</a><br><br>".format('marks'+l[i]+'.png',l[i])
     m = m + '</body>\n</html>'
     f.write(m)
     f.close()

# To create a html file attendance.html of monthwise attendance

def attendance1():
     f = open('folder/attendance.html','w')
     message = '''<html>
     <body bgcolor = 'orange'>
     <a href = "jun.html" target = "c">June</a><br><br>
     <a href = "jul.html" target = "c">July</a><br><br>
     <a href = "aug.html" target = "c">August</a><br><br>
     <a href = "sep.html" target = "c">September</a><br><br>
     <a href = "octo.html" target = "c">October</a><br><br>
     <a href = "nov.html" target = "c">November</a><br><br>
     <a href = "dec.html" target = "c">December</a><br><br>
     <a href = "jan.html" target = "c">January</a><br><br>
     <a href = "feb.html" target = "c">February</a><br><br>
     <a href = "mar.html" target = "c">March</a><br><br>
     </body>
     </html>'''
     f.write(message)
     f.close()

# To add january's attendance
     
def jan(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/jan.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM jan_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<32:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add october's attendance

def octo(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/octo.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM oct_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border
     color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<32:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add july's attendance

def jul(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/jul.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM jul_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<32:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add june's attendance

def jun(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/jun.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM jun_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<31:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add march's attendance
     
def mar(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/mar.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM mar_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<32:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add august's attendance
     
def aug(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/aug.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM aug_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<32:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add september's attendance

def sep(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/sep.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM sep_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<31:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add november's attendance

def nov(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/nov.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM nov_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     <th> Name </th>'''
     i = 1
     s = ''
     while i<31:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''               
     f.write(m)
     f.close()     

# To add february's attendance

def feb(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/feb.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM feb_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     
     <th> Name </th>'''
     i = 1
     s = ''
     while i<29:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To add december's attendance

def dec(x):
     global month
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     f = open('folder/dec.html','w')
     mycursor = demo.cursor()
     mycursor.execute('SELECT * FROM dec_attendance')
     r = mycursor.fetchall()
     m = '''<html>
     <body>
     <table border = 1 border color = 'black'>
     <tr>
     
     <th> Name </th>'''
     i = 1
     s = ''
     while i<31:
          s = s + '<th> {} </th>\n'.format(i)
          i+=1
     m = m + s + '</tr>'
     for i in range(len(r)):
          roll = r[i][0]
          name10 = r[i][1]
          m = m + '''<tr>
          <td> {} </td>'''.format(name10)
          for j in range(len(r[i][2:])):
               date = r[i][2:][j]
               m = m + '<td> {} </td>'.format(date)
     m = m + '''</tr>
     </table>
     </body>
     </html>'''
     f.write(m)
     f.close()

# To open each student's report card

def report(x):
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     mycursor = demo.cursor()
     mycursor.execute('SELECT NAME FROM MARKS')
     r4 = mycursor.fetchall()
     l = []
     f = open('folder/reportcard.html','w')
     m = '<html>\n<body>'
     for i in range(len(r4)):
          l.append(r4[i][0])
     for k in range(len(l)):
          m += '<a href = "{}">{}</a><br><br>'.format(l[k]+'.html',l[k])
     m += '</body>\n</html>'
     f.write(m)
     f.close()

# The report card's main page
     
def reportcard1_10(x):
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     mycursor = demo.cursor()
     mycursor.execute('SELECT ROLLNO,NAME,COMPUTER,ENGLISH,SOCIAL,MATHEMATICS,SCIENCE,L2,L3,COMPUTER+MATHEMATICS+ENGLISH+SOCIAL+SCIENCE+L2+L3 "TOTAL",ROUND(((COMPUTER+MATHEMATICS+ENGLISH+SOCIAL+SCIENCE+L2+L3)/7),2) "PER" FROM MARKS ORDER BY PER DESC')
     r3 = mycursor.fetchall()
     name17 = []
     rol = []
     comp = []
     eng = []
     soc = []
     sci = []
     mat = []
     l2 = []
     l3 = []
     tot = []
     per = []
     
     for i in range(len(r3)):
          name17.append(r3[i][1])
          rol.append(r3[i][0])
          comp.append(r3[i][2])
          eng.append(r3[i][3])
          soc.append(r3[i][4])
          mat.append(r3[i][5])
          sci.append(r3[i][6])
          l2.append(r3[i][7])
          l3.append(r3[i][8])
          tot.append(r3[i][9])
          per.append(r3[i][10])
          
     for j in range(len(r3)):
          f = open("folder/"+name17[j]+'.html','w')
          m = '''<html>
          <body>
          <h2><center>Marks report</center></h2>
          <br><br>
          <font>
          <b>Name:</b> {}<br>
          <b>Class:</b> {}<br>
          <b>Roll No:</b> {}<br>
          <b>Computer:</b> {}<br>
          <b>L2:</b> {}<br>
          <b>English:</b> {}<br>
          <b>L3:</b> {}<br>
          <b>Social Studies:</b> {}<br>
          <b>Mathematics:</b> {}<br>
          <b>Science:</b> {}<br>
          <br>
          <b><u>Total:</b></u>{}<br>
          <b><u>Percentage:</b></u>{}<br>
          <b><u>Rank:</b></u>{}<br>
          </font>
          <img src = "{}">
          <br>
          <br>
          <br>
          <font>
          <b>Signature of Class teacher:
          <br>
          <br>
          <br>
          Signature of Parent:
          <br>
          <br>
          <br>
          Signature of Principal:
          </body>
          <html>'''.format(name17[j],x,rol[j],comp[j],l2[j],eng[j],l3[j],soc[j],mat[j],sci[j],tot[j],per[j],j+1,'marks'+name17[j]+'.png')
          f.write(m)
          f.close()
          
# To open the html file frame.html 
     
def html(event):
     f='frame.html'
     www.open(f,new=0)
     main()
     
# To plot the subjectwise class average 

def avg_mark(x):
     global course1
     demo = sql.connect(user = 'root',
                        password = 'tiger',
                        host = 'localhost',
                        database = x)
     mycursor = demo.cursor()
     p.figure()
     p.title('Class average of class '+x+' in each subject')
     p.xlabel('Subjects')
     p.ylabel('Marks')
     
     if '11' not in x and '12' not in x:
          mycursor.execute('SELECT AVG(COMPUTER),AVG(ENGLISH),AVG(MATHEMATICS),AVG(SCIENCE),AVG(SOCIAL),AVG(L2),AVG(L3) FROM MARKS')
          r1 = mycursor.fetchall()
          y = ['COMPUTER','ENGLISH','MATHS','SCIENCE','SOCIAL','L2','L3']

     else:
          tk.messagebox.showerror('class error','Only until class 10')
          
     p.plot(y,r1[0],'k-o')
     p.savefig('folder/avg.png')
     f = open('folder/avg.html','w')
     m = '''<html>
     <body>
     <a href = 'avg.png'>Click here to see the graph</a>
     </body>
     </html>'''
     f.write(m)
     f.close()

# Automatically adds 5 values when button skip is clicked
          
def skip1(event):
      global result1,class1,col,root7,month
      root7.withdraw()
      demo=sql.connect(user='root',password='tiger',host='localhost',database='teacher')
      mycursor=demo.cursor()
      mycursor.execute('SELECT CLASS FROM TEACHERTAB WHERE CLASS LIKE "{}" AND PASSWORD LIKE "{}"'.format(class1.get(),password1.get()))
      result1=mycursor.fetchall()
      result=result1[0][0]
      demo=sql.connect(user='root',password='tiger',host='localhost',database='{}'.format(result))
      mycursor=demo.cursor()
      mycursor.execute('INSERT INTO {}_attendance (NAME,{}) VALUES("Abhinav","P")'.format(month,col))
      mycursor.execute('INSERT INTO {}_attendance (NAME,{}) VALUES("Abhay","P")'.format(month,col))
      mycursor.execute('INSERT INTO {}_attendance (NAME,{}) VALUES("Bhumi","P")'.format(month,col))
      mycursor.execute('INSERT INTO {}_attendance (NAME,{}) VALUES("Rahul","A")'.format(month,col))
      mycursor.execute('INSERT INTO {}_attendance (NAME,{}) VALUES("Vivek","P")'.format(month,col))
      
      if '11' not in result and '12' not in result:
           mycursor.execute('INSERT INTO MARKS VALUES (1,"Abhinav",56,59,68,49,68,70,58)')
           mycursor.execute('INSERT INTO MARKS VALUES (2,"Abhay",78,89,85,75,96,79,75)')
           mycursor.execute('INSERT INTO MARKS VALUES (3,"Bhumi",62,59,24,15,36,58,68)')
           mycursor.execute('INSERT INTO MARKS VALUES (4,"Rahul",98,96,95,91,89,96,99)')
           mycursor.execute('INSERT INTO MARKS VALUES (5,"Vivek",69,58,47,36,59,68,32)')
      demo.commit()
      marks2(result)
      attendance1()
      mycursor.execute('SELECT MONTH(CURDATE())')
      R5 = mycursor.fetchone()
      exec('{}'.format('octo(result)'))
      exec('{}'.format('jan(result)'))
      exec('{}'.format('feb(result)'))
      exec('{}'.format('mar(result)'))
      exec('{}'.format('jun(result)'))
      exec('{}'.format('jul(result)'))
      exec('{}'.format('aug(result)'))
      exec('{}'.format('sep(result)'))
      exec('{}'.format('nov(result)'))
      exec('{}'.format('dec(result)'))
      report(result)
      reportcard1_10(result)
      avg_mark(result)
      html('x')

# When the user clicks login      
      
def sqllogin(event):
     global class1,password1,root1,root7
     if class1.get()=='' or password1.get()=='':
          tk.messagebox.showerror('Input Error','All fields are required')
     else:
          demo=sql.connect(user='root',password='tiger',host='localhost',database='teacher')
          mycursor=demo.cursor()
          mycursor.execute('SELECT * FROM TEACHERTAB WHERE CLASS LIKE "{}" AND PASSWORD LIKE "{}"'.format(class1.get(),password1.get()))

          if mycursor.fetchall()==[]:
               tk.messagebox.showerror('Registration error','You are not registered')
               root1.withdraw()
               selectclass('anything')
               demo.commit()
               
          else:
               global result,col,result1
               mycursor.execute('SELECT CLASS FROM TEACHERTAB WHERE CLASS LIKE "{}" AND PASSWORD LIKE "{}"'.format(class1.get(),password1.get()))
               result1=mycursor.fetchall()
               result=result1[0][0]
               demo=sql.connect(user='root',password='tiger',host='localhost',database='{}'.format(result))
               mycursor=demo.cursor()
               mycursor.execute('SHOW TABLES')
               s=''
               
               for i in result:
                    if i.isdigit()==True:
                          s+=i
                          
               if int(s)<=10 and int(s)>0:
                    global month
                    demo=sql.connect(user='root',password='tiger',host='localhost',database='{}'.format(result))
                    mycursor=demo.cursor()
                    mycursor.execute('SELECT CURDATE()')
                    result1=mycursor.fetchone()
                    date=str(result1[0])
                    mycursor.execute('SELECT MONTH("{}")'.format(date))
                    month1=mycursor.fetchone()
                    date=date.replace('-','_')
                    month2=month1[0]-1
                    months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
                    month=months[month2]
                    col=str(month)+str(date)
                    mycursor.execute('CREATE TABLE IF NOT EXISTS jan_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS feb_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS mar_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS jun_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS jul_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS aug_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS sep_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS oct_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS nov_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('CREATE TABLE IF NOT EXISTS dec_attendance(ROLLNO INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30))')
                    mycursor.execute('DESC {}_attendance'.format(month))
                    result2=mycursor.fetchall()
                    l=[]
                    
                    for i in range(0,len(result2)):
                         l.append(result2[i][0])
                         
                    mycursor.execute('SELECT CURDATE()')
                    result1=mycursor.fetchone()
                    date=str(result1[0])
                    mycursor.execute('SELECT MONTH("{}")'.format(date))
                    month1=mycursor.fetchone()
                    date=date.replace('-','_')
                    month2=month1[0]-1
                    months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
                    month=months[month2]
                    col=str(month)+str(date)
                    mycursor.execute('DESC {}_attendance'.format(month))
                    result15 = mycursor.fetchall()
                    l1 = []
                    
                    for i in result15:
                         l1.append(i[0])
                         
                    mycursor.execute('SELECT DAYOFMONTH(CURDATE())')
                    result13=mycursor.fetchone()[0]
                    for k in range(result13-1,0,-1):
                         mycursor.execute('SELECT DATE_SUB(CURDATE(), INTERVAL {} DAY)'.format(k))
                         result14=str(mycursor.fetchone()[0])
                         result16=result14.replace('-','_')
                         result16=str(month)+result16
                         if result16 not in l1:
                              mycursor.execute('ALTER TABLE %s_attendance ADD %s VARCHAR(20)'%(month,result16))
                    mycursor.execute('SELECT * FROM {}_attendance'.format(month))
                    result18 = mycursor.fetchall()
                    l12 = []
                    for i in result18:
                         l12.append(i[0])
                    for k in range(result13-1,0,-1):
                         mycursor.execute('SELECT DATE_SUB(CURDATE(), INTERVAL {} DAY)'.format(k))
                         result14=str(mycursor.fetchone()[0])
                         result16=result14.replace('-','_')
                         result16=str(month)+result16
                         for o in l12:
                              mycursor.execute('UPDATE %s_attendance IFNULL SET %s="HL" WHERE ROLLNO=%i'%(month,result16,o))
                              demo.commit()
                         
                    if col not in l1:
                         demo=sql.connect(user='root',password='tiger',host='localhost',database='{}'.format(result))
                         mycursor=demo.cursor()
                         mycursor.execute('ALTER TABLE %s_attendance ADD %s VARCHAR(20)'%(month,str(month)+str(date)))
                         demo.commit()
                    mycursor.execute('SELECT * FROM {}_attendance'.format(month))
                    result5 = mycursor.fetchall()
                    root1.withdraw()
                    mycursor.execute('SELECT MONTH(CURDATE())')
                    R5 = mycursor.fetchone()
                    
                    if result5 == []:
                          root7=tk.Tk()
                          root7['bg'] = 'white'
                          root7.title('Adding values')
                          n=tk.Label(root7,text='Click Open Form to add values',bg = 'white',font = ('Times New Roman',20,'bold'))
                          n.grid(row=0,column=2)
                          addname=tk.Button(root7,text='Open form',font = ('Lucida Calligraphy',15))
                          addname.grid(row=1,column=1)
                          addname.bind('<Button-1>',open_form)
                          skip=tk.Button(root7,text='Skip--->',font = ('Lucida Calligraphy',15))
                          skip.bind('<Button-1>',skip1)
                          skip.grid(row=1,column=3)
                          mycursor.execute('CREATE TABLE IF NOT EXISTS MARKS(ROLLNO INT,NAME VARCHAR(20),COMPUTER VARCHAR(3),ENGLISH VARCHAR(3),MATHEMATICS VARCHAR(3),SCIENCE VARCHAR(3),SOCIAL VARCHAR(3),L2 VARCHAR(3),L3 VARCHAR(3))')
                          demo.commit()
                          rClickbinderlog(root7)
                                
                    else:
                          open_form(result)

# When the user sign's up
          
def sqlreg(event):
     global class3,name1,password3,cpassword1,root2,ques,answer,sq,tkvar,tkvar1
     if name1.get()=='' or tkvar.get()=='' or password3.get()=='' or cpassword1.get()=='' or answer.get()=='':
          tk.messagebox.showerror('Input Error','All fields are required')#shows a error message if any one of the fiels is not entered
     else:
          demo=sql.connect(user='root',password='tiger',host='localhost')
          mycursor=demo.cursor()
          mycursor.execute('CREATE DATABASE IF NOT EXISTS TEACHER')
          mycursor.execute('USE TEACHER')
          mycursor.execute('CREATE TABLE IF NOT EXISTS TEACHERTAB(NAME VARCHAR(50),CLASS CHAR(4),PASSWORD VARCHAR(12),QUESTION VARCHAR(80),ANSWER VARCHAR(30))')
          demo.commit()
          
          if password3.get()==cpassword1.get():
               mycursor.execute('SELECT CLASS FROM TEACHERTAB')
               result=mycursor.fetchall()
               l=[]
               
               for i in result:
                    for j in i:
                         l.append(j)
               
               if tkvar.get()+tkvar1.get() not in l:
                    global title
                    mycursor.execute('INSERT INTO TEACHERTAB VALUES("{}","{}","{}","{}","{}")'.format(str(name1.get()),str(tkvar.get()+tkvar1.get()),str(cpassword1.get()),str(sq.get()),str(answer.get())))
                    mycursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(str(tkvar.get()+tkvar1.get())))
                    tk.messagebox.showinfo('register','You have successfully registered')
                    root2.withdraw()
                    demo.commit()
                    
               else:
                    tk.messagebox.showerror('Class','Class already Exists')
                    root2.withdraw()
                    selectclass('x')
                    demo.commit()
                    
          else:
               tk.messagebox.showerror('password','Passwords do not match')

# When the user clicks sign up     
#step2
def selectclass(event):
     global class3,name1,password3,cpassword1,answer,sq,tkvar,tkvar1
     global root,root6
     global root2
     root6=tk.Tk()
     tkvar=tk.StringVar(root6)
     tkvar.set(1)
     tkvar1=tk.StringVar(root6)
     tkvar1.set('A')
     class5=tk.Label(root6,text="Select class: ",bg = 'white',font = ('Times New Roman',20,'bold'))
     class5.grid(row=1,column=1)
     class1=tk.OptionMenu(root6,tkvar,*[i for i in range(1,13)])
     class1.grid(row=1,column=2)
     section1=tk.Label(root6,text="Select Section: ",bg = 'white',font = ('Times New Roman',20,'bold'))
     section1.grid(row=2,column=1)
     section2=tk.OptionMenu(root6,tkvar1,*['A','B','C','D'])
     section2.grid(row=2,column=2)
     submit=tk.Button(root6,text='Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
     submit.bind("<Button-1>",sign_up)
     submit.grid(row=3,column=1)

# When the user clicks login
#step2
def login1(event):
     global root
     global root1,class1,password1
     root.withdraw()
     root1=tk.Tk()
     root1.iconbitmap('login.ico')
     root1['bg'] = 'white'
     root1.title('Login')
     class2=tk.Label(root1,text='Class: ',font = ('Times New Roman',20,'bold'),bg = 'white')
     class2.grid(row=3,column=2)
     password=tk.Label(root1,text='Password: ',font = ('Times New Roman',20,'bold'),bg = 'white')
     password.grid(row=4,column=2)
     class1=tk.Entry(root1,font = ('Times New Roman',20))
     class1.focus()
     class1.grid(row=3,column=3)
     password1=tk.Entry(root1,textvariable=password,show='*',font = ('Times New Roman',20))
     password1.grid(row=4,column=3)
     submit=tk.Button(root1,text='Submit',fg = 'black',bg = 'lime',font = ('Lucida Calligraphy',15))
     submit.bind('<Button-1>',sqllogin)
     submit.grid(row=5,column=2,padx = 50)
     back=tk.Button(root1,text='Back',fg = 'black',bg = 'red',font = ('Lucida Calligraphy',15))
     back.bind('<Button-1>',back1)
     back.grid(row=5,column=3)
     rClickbinderlog(root1)

# To ask for login or sign up
#step 1

def main():
     global root
     ro=tk.Tk()#Creates a window
     ro.withdraw()#hides the created window
     root =tk.Toplevel()#Is required to run widgets with pics otherwise if we click back it raises error
     root.state('zoomed')#Makes the window full screened
     root.iconbitmap('book.ico')#adds a icon to the window
     root.title('Ever Scholar ')#give title to the window
     root['bg'] = 'white'#add background to the window
     title1=tk.Label(root,fg = 'purple',bg = 'white',text='Welcome to Ever Scholar',font=('Algerian',45 ))
     title1.grid(row=0,column=3)
     logpic=tk.PhotoImage(file='login.png')
     login=tk.Button(root,image=logpic)
     login.bind("<Button-1>",login1)
     login.grid(row=4,column=2,padx=15)
     login.image = logpic
     signpic=tk.PhotoImage(file='signup.png')#link to the image
     reg=tk.Button(root,image=signpic)
     reg.bind("<Button-1>",selectclass)
     reg.grid(row=4,column=4)
     reg.image = signpic#adding image to button
     tk.Button(root, text="Quit",fg = 'white',bg = '#E41B17',command=root.destroy,width = 5,height = 2,font = ('Lucida Calligraphy',25)).grid(row=5,column=3,pady=200)
     #root defines where to place the object
     #Other arguments are optional

  
main()
