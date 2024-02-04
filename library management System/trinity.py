from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import sqlite3
image1='library.png'
image2='image2.png'
image3='finance.png'
class menu:

    def __init__(self):
        self.root=Tk()
        self.root.title('Menu')
        self.root.attributes('-zoomed', True)
        conn=sqlite3.connect('press.db')
        conn.commit()
       
        conn.close()
        self.a=self.canvases(image1)
        self.x1=self.entry()
        self.root.mainloop()
    def canvases(self,images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        
        photo=Image.open(images)
        photo1 = photo.resize((w, h), Image.LANCZOS)
        photo2=ImageTk.PhotoImage(photo1)

       
        self.canvas = Canvas(self.root, width='%d'%w, height='%d'%h)
        self.canvas.grid(row = 0, column = 0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor = NW, image=photo2)
        self.canvas.image=photo2
        return self.canvas
    
    def entry(self):
        self.a.destroy()
        self.a = self.canvases(image2)

        welcome_button = Button(
        self.a,
        text='Welcome to Library',
        font='Arial 24 bold',
        fg='wheat1',
        bg='salmon4',
        width=25,
        pady=10,
        state=DISABLED  # Disable the button if needed
    )
        welcome_button.place(x=self.root.winfo_screenwidth() // 2 - 200, y=50)
    
        button_positions = [
            ('Add Books', 180),
            ('Generate Report', 280),
            ('All Books', 380),
            ('EXIT', 480)
         ]

        for text, offset_y  in button_positions:
            Button(
                self.a,
                text=text,
                font='Arial 22 bold',
                fg='wheat1',
                bg='salmon4',
                width=15,
                padx=10,
                command=self.addentry if text == 'Add Books' else
                    self.search if text == 'Generate Report' else
                    self.all if text == 'All Books' else
                    self.mainmenu
        ).place(x=self.root.winfo_screenwidth() // 2 - 100, y=offset_y)

        return self.a





    def addentry(self):
        self.aid=StringVar()
        self.title=StringVar()
        self.client=StringVar()
        self.acopies=IntVar()
        self.price=StringVar()
        self.comment=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='salmon4')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.aid).place(x=200,y=50)
        l2=Label(self.f1,text='Title : ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.client).place(x=200,y=100)
        l3=Label(self.f1,text='Student Name : ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.title).place(x=200,y=150)
        l4=Label(self.f1,text='Date of issuance : ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=200)
        e2=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.price).place(x=200,y=200)
        l4=Label(self.f1,text='Quantity: ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=250)
        e2=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.acopies).place(x=200,y=250)
        l5=Label(self.f1,text='Comment : ',font='Arial 12 bold',fg='salmon4',bg='wheat1',pady=1).place(x=50,y=300)
        e3=Entry(self.f1,width=30,bg='wheat1',font='Arial 12 bold',fg='black',textvariable=self.comment).place(x=200,y=300)
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Arial 10 bold',fg='salmon4',bg='wheat1',width=15,bd=3,command=self.adddata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Arial 10 bold',fg='salmon4',bg='wheat1',width=15,bd=3,command=self.rm).place(x=350,y=400)

    def rm(self):
        self.f1.destroy()
    def mainmenu(self):
        self.root.destroy()
        

    def adddata(self):
        a=self.aid.get()
        b=self.client.get()
        c=self.title.get()
        d=self.price.get()
        e=self.acopies.get()
        f=self.comment.get()
        conn=sqlite3.connect('press.db')
        try:
            if (a and b and c and d  and f)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                conn.execute("insert into entries \
                values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e,f.capitalize(),));
                conn.commit()
                messagebox.showinfo("Success","Task added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error","Task is already present.")


        conn.close()

    def search(self):
        
        self.sid=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='salmon4')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID/Title/Student Name:',font=('Arial 10 bold'),bd=2, fg='salmon4',bg='wheat1').place(x=20,y=40)
        e1=Entry(self.f1,width=25,bd=5,bg='wheat1',fg='salmon4',textvariable=self.sid).place(x=260,y=40)
        b1=Button(self.f1,text='Search',bg='wheat1',font='Arial 10 bold',fg='salmon4',width=9,bd=2,command=self.serch1).place(x=500,y=37)
        b1=Button(self.f1,text='Back',bg='wheat1',font='Arial 10 bold',fg='salmon4',width=10,bd=2,command=self.rm).place(x=250,y=450)

    def create_tree(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree


    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("Book ID","TITLE","Student Name","Date of issuance","Quantity","COMMENT")
            self.trees=self.create_tree(self.f1,self.list4)
            self.trees.place(x=25,y=150)
            conn=sqlite3.connect('press.db')

            
            c = conn.execute("select * from entries where id=? OR TITLE=? OR `Student Name`=?", (k.capitalize(), k.capitalize(), k.capitalize(),))

            a=c.fetchall()
            if len(a)!=0:
                for row in a:

                    self.trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                self.variable.set("Select Action:")


                self.cm =ttk.Combobox(self.f1,textvariable=self.variable ,state='readonly',font='Arial 15 bold',height=50,width=15,)
                self.cm.config(values =('Add Quantity', 'Delete Quantity', 'Delete Task'))

                self.cm.place(x=50,y=100)
                self.cm.pack_propagate(0)


                self.cm.bind("<<ComboboxSelected>>",self.combo)
                self.cm.selection_clear()
            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")


    def combo(self,event):
        self.var_Selected = self.cm.current()
        
        if self.var_Selected==0:
            self.copies(self.var_Selected)
        elif self.var_Selected==1:
            self.copies(self.var_Selected)
        elif self.var_Selected==2:
            self.deleteitem()
    def deleteitem(self):
        try:
            self.curItem = self.trees.focus()

            self.c1=self.trees.item(self.curItem,"values")[0]
            b1=Button(self.f1,text='Update',font='Arial 10 bold',width=9,bd=3,command=self.delete2).place(x=500,y=97)

        except:
            messagebox.showinfo("Empty","Please select something.")
    def delete2(self):
        conn=sqlite3.connect('press.db')
        cd=conn.execute("select * from entries where id=?",(self.c1,))
        ab=cd.fetchall()
        if ab!=0:
            conn.execute("DELETE FROM entries where id=?",(self.c1,))
            conn.commit()
            messagebox.showinfo("Successful","entry Deleted sucessfully.")
            self.trees.delete(self.curItem)
        else:
            messagebox.showinfo("Error","entry cannot be deleted.")
        conn.commit()
        conn.close()


    def copies(self,varr):
        try:
            curItem = self.trees.focus()
            self.c1=self.trees.item(curItem,"values")[0]
            self.c2=self.trees.item(curItem,"values")[4]
            self.scop=IntVar()
            self.e5=Entry(self.f1,width=20,textvariable=self.scop)
            self.e5.place(x=310,y=100)
            if varr==0:
                b5=Button(self.f1,text='Update',font='Arial 10 bold',bg='wheat1',fg='salmon4',width=9,bd=3,command=self.copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(self.f1,text='Update',font='Arial 10 bold',bg='wheat1',fg='salmon4',width=9,bd=3,command=self.copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")

    def copiesadd(self):
        no=self.e5.get()
        if int(no)>=0:

            conn=sqlite3.connect('press.db')

            conn.execute("update entries set COPIES=COPIES+? where ID=?",(no,self.c1,))
            conn.commit()

            messagebox.showinfo("Updated","Quantity added sucessfully.")
            self.serch1()
            conn.close()

        else:
            messagebox.showinfo("Error","Quantitycannot be negative.")

    def copiesdelete(self):
        no1=self.e5.get()
        if int(no1)>=0:
            if int(no1)<=int(self.c2):
                conn=sqlite3.connect('press.db')

                conn.execute("update entries set COPIES=COPIES-? where ID=?",(no1,self.c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated","Deleted sucessfully")
                self.serch1()

            else:
                messagebox.showinfo("Maximum","Quantityto delete exceed available copies.")
        else:
            messagebox.showinfo("Error","Quantitycannot be negative.")

    def all(self):
        self.f1=Frame(self.a,height=500,width=650,bg='salmon4')
        self.f1.place(x=500,y=100)
        b1=Button(self.f1,text='Back',bg='wheat1' ,fg='salmon4',width=10,bd=3,command=self.rm).place(x=250,y=400)
        conn=sqlite3.connect('press.db')
        self.list3=("Book ID","TITLE","Student Name","Date of issuance ","Quantity","Comment")
        self.treess=self.create_tree(self.f1,self.list3)
        self.treess.place(x=25,y=50)
        c=conn.execute("select * from entries")
        g=c.fetchall()
        if len(g)!=0:
            for row in g:
                self.treess.insert('',END,values=row)
        conn.commit()
        conn.close()

   
#===================START=======================
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize((w,h),Image.LANCZOS)
    photo2=ImageTk.PhotoImage(photo1)

    canvas = Canvas(root, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas
root = Tk()
root.title("LOGIN")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas=canvases(image3,w,h)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("python1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'sidra'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `login` (username, password) VALUES('admin', 'sidra')")
        conn.commit()

def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.destroy()
            a=menu()
        else:
            messagebox.showinfo("Error","Invalid username or password.")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
#==============================LABELS=========================================
lbl_title = Label(canvas, text = "Library Management  Sysem", font=('Arial', 30,'bold', ),bg='PeachPuff4', fg='black')
lbl_title.place(x=500,y=150)
lbl_username = Label(canvas, text = "Username:", font=('Arial', 20,'bold'),bd=5,bg='PeachPuff4', fg='black')
lbl_username.place(x=500,y=240)
lbl_password = Label(canvas, text = "Password :", font=('Arial', 20,'bold'),bd=3,bg='PeachPuff4', fg='black')
lbl_password.place(x=500, y=330)
lbl_text = Label(canvas)
lbl_text.place(x=450,y=500)
lbl_text.grid_propagate(0)
#==============================ENTRY WIDGETS==================================
username = Entry(canvas, textvariable=USERNAME, font=(20),bg='PeachPuff4', fg='black',bd=6,width=33)
username.place(x=670, y=250,)
password = Entry(canvas, textvariable=PASSWORD, show="*", font=(20),bg='PeachPuff4', fg='black',bd=6,width=33)
password.place(x=670, y=330)
#==============================BUTTON WIDGETS=================================
btn_login = Button(canvas, text="LOGIN", font=('Arial 20 bold'),width=25,command=Login,bg='PeachPuff4', fg='black')
btn_login.place(x=530,y=400)
btn_login.bind('<Return>', Login)
root.mainloop()
