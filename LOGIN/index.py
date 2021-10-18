#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar Nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="image/LogoIcon.ico")

# CARREGAR IMAGENS

logo = PhotoImage(file="image/logo.png")

# WIDGETS 

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)
#
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)
#Botoes

LoginButton = ttk.Button(RightFrame, text="login", width=30)
LoginButton.place(x=150, y=225)
#
def Register():

    #Removendo WIdgets de Login
    LoginButton.place(x=99999)
    RegisterButton.place(x=99999)
    #Inserindo Widgets de Cadastro

    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=34)
    NomeEntry.place(x=125, y=15)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=34)
    EmailEntry.place(x=125, y=65)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        DataBaser.cursor.execute("""
        INSERT INTO User (Name, Email, User, Password) 
        VALUES (?, ?, ?, ?)
        """,(Name, Email, User, Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Account Created ")

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    Register.place(x=180, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadasdtro
        NomeLabel.place(x=99999)
        NomeEntry.place(x=99999)  
        EmailLabel.place(x=9999)     
        EmailEntry.place(x=99999)
        Register.place(x=9999)
        Back.place(x=9999)
        #Trazendo de Volta os Widgets de Login
        LoginButton.place(x=150)
        RegisterButton.place(x=180)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=180, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=180, y=260)

jan.mainloop()