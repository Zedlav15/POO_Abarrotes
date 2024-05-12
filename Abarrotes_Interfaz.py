#Proyecto hecho por Salvador, Israel y Francisco

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

        button = ctk.CTkButton(master=self.master, text="Iniciar Simulacion", command=self.login, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

    def login(self):
        perfil = self.my_box.get()  # Obtener el perfil seleccionado
        self.master.destroy()  
        Ventana_Simulador(perfil=perfil)  # Crear la nueva ventana

class Ventana_Simulador(ctk.CTkToplevel):
    def __init__(self, master=None, perfil=''):
        super().__init__(master)
        self.geometry("1000x800")
        self.title("Simulador de Abarrotes By Team 9")
        self.iconbitmap('images/Logo1.jpg')
        self.perfil = perfil
        self.Label1 = ctk.CTkLabel(self, text=f'¡Bienvenido, {perfil}!')
        self.Label1.pack()

        def open_add_product_window():
            # Cerrar la ventana actual
            self.destroy()

            # Abrir una nueva ventana
            new_window = ctk.CTkToplevel(self.master)
            new_window.title("Agregar Producto")
            new_window.geometry("500x600")

            ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
            ctk.CTkLabel(new_window, text="Ingresa los detalles del producto").pack(pady=10)

            id_entry = ctk.CTkEntry(new_window)
            id_entry.pack()
            id_entry.place(relx=0.5, rely=0.20, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="ID:").place(relx=0.3, rely=0.20, anchor=ctk.CENTER)

            name_entry = ctk.CTkEntry(new_window)
            name_entry.pack()
            name_entry.place(relx=0.5, rely=0.30, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="Name:").place(relx=0.3, rely=0.30, anchor=ctk.CENTER)

            price_entry = ctk.CTkEntry(new_window)
            price_entry.pack()
            price_entry.place(relx=0.5, rely=0.40, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="Price:").place(relx=0.3, rely=0.40, anchor=ctk.CENTER)

            stock_entry = ctk.CTkEntry(new_window)
            stock_entry.pack()
            stock_entry.place(relx=0.5, rely=0.50, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="Stock:").place(relx=0.3, rely=0.50, anchor=ctk.CENTER)

            category_entry = ctk.CTkEntry(new_window)
            category_entry.pack()
            category_entry.place(relx=0.5, rely=0.60, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="Category:").place(relx=0.3, rely=0.60, anchor=ctk.CENTER)

            description_entry = ctk.CTkEntry(new_window)
            description_entry.pack()
            description_entry.place(relx=0.50, rely=0.70, anchor=ctk.CENTER)
            ctk.CTkLabel(new_window, text="Description:").place(relx=0.28, rely=0.70, anchor=ctk.CENTER)

            back_button = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
            back_button.pack(pady=5)
            back_button.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

            
        def open_view_products_window():

            self.destroy()

            new_window = ctk.CTkToplevel(self.master)
            new_window.title("Ver Productos")
            new_window.geometry("500x600")
            ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()            
            ctk.CTkLabel(new_window, text="Lista de productos").pack(pady=10)

            back_button2 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
            back_button2.pack(pady=5)
            back_button2.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        def open_product_info_window():

            self.destroy()

            new_window = ctk.CTkToplevel(self.master)
            new_window.title("Información del Producto")
            new_window.geometry("500x600")
            ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
            ctk.CTkLabel(new_window, text="Detalles del producto seleccionado").pack(pady=10)

            back_button3 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
            back_button3.pack(pady=5)
            back_button3.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)           

        def open_delete_product_window():

            self.destroy()

            new_window = ctk.CTkToplevel(self.master)
            new_window.title("Eliminar Producto")
            new_window.geometry("500x600")
            ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
            ctk.CTkLabel(new_window, text="Eliminar un producto").pack(pady=10)

            back_button4 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
            back_button4.pack(pady=5)    
            back_button4.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)        

        # Botones para abrir las ventanas
        button1 = ctk.CTkButton(self, text="Agregar Producto", command=open_add_product_window, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button1.pack(pady=5)
        button1.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        button2 = ctk.CTkButton(self, text="Ver productos", command=open_view_products_window, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button2.pack(pady=5)
        button2.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)

        button3 = ctk.CTkButton(self, text="Información del Producto", command=open_product_info_window, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button3.pack(pady=5)
        button3.place(relx=0.5, rely=0.20, anchor=ctk.CENTER)

        button4 = ctk.CTkButton(self, text="Eliminar Producto", command=open_delete_product_window, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button4.pack(pady=5)
        button4.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

    def show_simulador(self, window_to_close):
        window_to_close.destroy()  
        Ventana_Simulador(self.master, perfil=self.perfil)  # Mostrar Ventana_Simulador nuevamente

root = ctk.CTk()
app = VentanaPrincipal(root)

root.mainloop()
