import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


Janela = customtkinter.CTk()
#Tamanho da Janela 
Janela.geometry("500x300")

#Função Click
def clique():
  print("clicando")

texto = customtkinter.CTkLabel(Janela, text="fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(Janela, placeholder_text="Seu email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(Janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(Janela, text="lembrar login")
checkbox.pack(padx= 10 , pady = 10)


botao = customtkinter.CTkButton(Janela, text="login", command=clique)
botao.pack(padx=10, pady=10)

Janela.mainloop()

