from tkinter import *
from tkinter import messagebox
import sqlite3


banco = sqlite3.connect('base_dados.db') #inserindo intens no banco

cursor  = banco.cursor()

#cursor.execute("CREATE TABLE alunos (nome text,idade integer, media integer)")

#cursor.execute("INSERT INTO alunos VALUES('Matias',17,15)")

banco.commit()

cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

def validar_acesso():
    professor = prof_name.get()
    card_number   = card.get()

    if (professor== 'Neusa' and card_number == '2424'):

        screen = Toplevel(tela)
        screen.title('Sistema de Controle de Notas')

        screen.geometry('800x500')
        screen.iconbitmap('imagens/book.ico')

        screen['bg'] = '#8A2BE2'

        meuMenu = Menu(screen,)

        FileMenu = Menu(meuMenu, tearoff=0)
        FileMenu.add_command(label='Novo Aluno')
        FileMenu.add_command(label='Excluir Aluno')
        meuMenu.add_cascade(label='Alunos | ', menu=FileMenu)

        EditMenu = Menu(meuMenu, tearoff=0)
        EditMenu.add_command(label='Ver mini-pauta')
        meuMenu.add_cascade(label='Mini Pauta | ', menu=EditMenu)

        EditMenu = Menu(meuMenu, tearoff=0)
        EditMenu.add_command(label='Sala nº ')
        EditMenu.add_command(label='Turma : ')
        EditMenu.add_command(label='Turno: ')
        EditMenu.add_command(label='Classe: ')
        meuMenu.add_cascade(label='Mais Informação | ', menu=EditMenu)

        EditMenu = Menu(meuMenu, tearoff=0)
        EditMenu.add_command(label='Professor')
        EditMenu.add_command(label='Total de Alunos')
        meuMenu.add_cascade(label='Definições | ', menu=EditMenu)

        screen.config(menu=meuMenu)

        
        
        screen.mainloop()
    else:
        messagebox.showerror('SCNA - Erro de Acesso*', 'Sem Permissão de Acesso!')
#..


tela = Tk()
tela.title('SCNA - Controlo de Notas de Alunos')

tela.geometry('1000x700')
tela.iconbitmap('imagens/livro.ico')
tela['bg'] = '#8A2BE2'

tela.resizable(False, False)


img = PhotoImage(file='Imagens/gggg.png')
Label(tela, image=img,bg='#8A2BE2').place(x=50, y=50)

frame = Frame(tela,
    width=350,
    height=350,
    bg='#8A2BE2',
    )
frame.place(x=550, y=50)
#.......................Titulo do login................
heading = Label(tela,
    text='Controlo de Notas',
    fg='white',
    bg='#8A2BE2',
    font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(x=600, y=100)
#----------------------------------------------------

prof_name = Entry(tela,
    fg='white',
    bg='#8A2BE2',
    font='Tahoma 12 normal',
    border=0,
    width=25)
prof_name.place(x=600, y=160)
prof_name.insert(0, 'Nome de Professor')

frame = Frame(tela,
    width=295,
    height=1,
    bg='white'
    ).place(x=600, y=185)
#-----------------------++++++++++++++++++++++++

card = Entry(tela,
    fg='white',
    bg='#8A2BE2',
    font='Tahoma 12 normal',
    border=0,
    width=25)
card.place(x=600, y=230)
card.insert(0, 'Número de Cartão')



frame = Frame(tela,
    width=295,
    height=1,
    bg='white'
    ).place(x=600, y=260)
Button(frame,
    width=20,
    pady=7,
    text='Conectar-me',
    bg='#D2691E',
    fg='white',
    border=0,
    font='Calibri 12 bold',
    cursor="mouse",
    command=validar_acesso).place(x=600, y=280)
#........................................

tela.mainloop()




