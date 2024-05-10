import customtkinter as ctk
from PIL import Image

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x600+350+20")
        self.master.title("Simulador de Abarrotes By Team 9")
        
        self.my_image = ctk.CTkImage(light_image=Image.open('images/Logo1.jpg'),
                                      dark_image=Image.open('images/Logo1.jpg'),
                                      size=(200, 200))
        self.my_label = ctk.CTkLabel(self.master, text='', image=self.my_image)
        self.my_label.pack(pady=10)
        self.my_label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        User = ["Salvador", "Israel", "Francisco"]
        self.my_box = ctk.CTkComboBox(self.master, values=User)
        self.my_box.pack(pady=20)
        self.my_box.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.my_label1 = ctk.CTkLabel(self.master, text='© Copyright by Kimi')
        self.my_label1.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

class Ventana_Simulador(ctk.CTkToplevel):
    def __init__(self, master=None, perfil=''):
        super().__init__(master)
        self.geometry("1000x800")
        self.title("Simulador de Abarrotes By Team 9")
        self.iconbitmap('images/Logo1.jpg')
        self.Label1 = ctk.CTkLabel(self, text=f'¡Bienvenido, {perfil}!')
        self.Label1.pack()

def login():
    perfil = app.my_box.get()  # Obtener el perfil seleccionado
    root.destroy()  
    Ventana_Simulador(perfil=perfil)  # Crear la nueva ventana

# Crear la ventana principal y la instancia de la clase VentanaPrincipal
root = ctk.CTk()
app = VentanaPrincipal(root)

button = ctk.CTkButton(master=root, text="Iniciar Simulacion", command=login, corner_radius=32, fg_color='#4158D0',
                       hover_color='#7f5af0')
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

root.mainloop()

#Prueba 1