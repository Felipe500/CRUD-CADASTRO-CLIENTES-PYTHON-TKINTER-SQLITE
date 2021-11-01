from tkinter import *
from tkinter import ttk
root = Tk()


class funcoes():
	def limpar_campos(self):
		self.entry_codigo.delete(0,END)
		self.entry_nome.delete(0,END)
		self.entry_telfone.delete(0,END)
		self.entry_cidade.delete(0,END)


class Aplication(funcoes):
	def __init__(self):
		self.root = root
		self.tela()
		self.frames_tela()
		self.grid_cliente()
		self.widgets_frame1()
		root.mainloop()

	def tela(self):
		self.root.title("Cadastro de Clientes")
		self.root.configure(background='#6a50c9')
		self.root.geometry("800x600")
		self.root.resizable(True,True)
		self.root.maxsize(width=850,height=700)
		self.root.minsize(width=400,height=300)
	def frames_tela(self):
		self.frame1= Frame(self.root, bd=4, bg="#fff",
		 highlightbackground="#b471f8",highlightthickness=3)
		self.frame1.place(relx=0.02, rely=0.02,relwidth=0.96,relheight=0.46)

		self.frame2= Frame(self.root, bd=4, bg="#fff",
		 highlightbackground="#b471f8",highlightthickness=3)
		self.frame2.place(relx=0.02, rely=0.5,relwidth=0.96,relheight=0.46)

	def widgets_frame1(self):
		#botão limpar
		self.bt_limpar = Button(self.frame1, text="Limpar",
			bg="#583bbf",fg="white", font=('verdana',8,'bold'),command=self.limpar_campos)
		self.bt_limpar.place(relx=0.2, rely=0.1,relwidth=0.1,relheight=0.15)

		#botão Buscar
		self.bt_buscar = Button(self.frame1, text="Buscar",
			bg="#583bbf",fg="white", font=('verdana',8,'bold'))
		self.bt_buscar.place(relx=0.3, rely=0.1,relwidth=0.1,relheight=0.15)

		#botão Novo	
		self.bt_buscar = Button(self.frame1, text="Novo",
			bg="#583bbf",fg="white", font=('verdana',8,'bold'))
		self.bt_buscar.place(relx=0.6, rely=0.1,relwidth=0.1,relheight=0.15)

		#Botão Altera
		self.bt_buscar = Button(self.frame1, text="Alterar",
			bg="#583bbf",fg="white", font=('verdana',8,'bold'))
		self.bt_buscar.place(relx=0.7, rely=0.1,relwidth=0.1,relheight=0.15)

		#Botão Apagar
		self.bt_buscar = Button(self.frame1, text="Apagar",
			bg="#583bbf",fg="white", font=('verdana',8,'bold'))
		self.bt_buscar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.15)

		
		#label e entry - codigo -----------------------------
		self.lb_codigo = Label(self.frame1,text="Codigo",
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.lb_codigo.place(relx=0.05, rely=0.05)

		self.entry_codigo = Entry(self.frame1,text="Codigo",
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.entry_codigo.place(relx=0.05, rely=0.15, relwidth=0.08)

		#label e entry - nome ----------------------------------
		self.lb_nome = Label(self.frame1,text="Nome",
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.lb_nome.place(relx=0.05, rely=0.35)

		self.entry_nome	 = Entry(self.frame1,
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.7)

		#label e entry - Telfone--------------------------
		self.lb_telfone = Label(self.frame1,text="Telfone",
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.lb_telfone.place(relx=0.05, rely=0.6)

		self.entry_telfone	 = Entry(self.frame1,
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.entry_telfone.place(relx=0.05, rely=0.7, relwidth=0.4)

		#label e entry - Cidade -----------------------
		self.lb_cidade = Label(self.frame1,text="Cidade",
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.lb_cidade.place(relx=0.5, rely=0.6)

		self.entry_cidade	 = Entry(self.frame1,
			bg="white",fg="#583bbf",font=('verdana',10,'bold'))
		self.entry_cidade.place(relx=0.5, rely=0.7, relwidth=0.5)

	def grid_cliente(self):
		self.lista_grid = ttk.Treeview(self.frame2, height=3,
			column=('col1','col2','col3','col4')) 
		self.lista_grid.heading("#0",text='')
		self.lista_grid.heading("#1",text='CODIGO')
		self.lista_grid.heading("#2",text='NOME')
		self.lista_grid.heading("#3",text='TELEFONE')
		self.lista_grid.heading("#4",text='CIDADE')

		self.lista_grid.column("#0",width=1)
		self.lista_grid.column("#1",width=25)
		self.lista_grid.column("#2",width=200)
		self.lista_grid.column("#3",width=125)
		self.lista_grid.column("#4",width=125)
		self.lista_grid.place(relx=0.005, rely=0.1, relwidth=0.95, relheight=0.86)

		self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
		self.lista_grid.configure(yscroll=self.scrol_lista.set)
		self.scrol_lista.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.88)








Aplication()