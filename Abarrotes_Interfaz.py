import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Primera Ventana
root = ctk.CTk()
root.geometry("500x600+350+20")
root.title("Simulador de Abarrotes By Team 9")

my_image = ctk.CTkImage(light_image=Image.open('images/Logo1.jpg'),
                        dark_image=Image.open('images/Logo1.jpg'),
                        size=(200, 200))
my_label = ctk.CTkLabel(root, text='', image=my_image)
my_label.pack(pady=10)
my_label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

User = ["Salvador", "Israel", "Francisco"]
my_box = ctk.CTkComboBox(root, values=User)
my_box.pack(pady=20)
my_box.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

my_label1 = ctk.CTkLabel(root, text='© Copyright by Kimi')
my_label1.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)


class Ventana_Simulador(ctk.CTkToplevel):
    def __init__(self, master=None, perfil=''):
        super().__init__(master)
        self.geometry("1000x800")
        self.title("Simulador de Abarrotes By Team 9")
        self.iconbitmap('images/Logo1.jpg')
        self.Label1 = ctk.CTkLabel(self, text=f'¡Bienvenido, {perfil}!')
        self.Label1.pack()


def login():
    perfil = my_box.get()  # Obtener el perfil seleccionado
    root.destroy()  # Cerrar la ventana actual
    Ventana_Simulador(perfil=perfil)  # Crear la nueva ventana


button = ctk.CTkButton(master=root, text="Iniciar Simulacion", command=login, corner_radius=32, fg_color='#4158D0',
                       hover_color='#7f5af0')
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

root.mainloop()


#Prueba 1