#Proyecto hecho por Salvador, Israel y Francisco

import customtkinter as ctk
from abarrrotes import *
from PIL import Image

class VentanaPrincipal:
    def __init__(self, master):
        print(f"Ventana_Principal: store is {store}") 
        self.master = master
        self.store = store
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

        button = ctk.CTkButton(master=self.master, text="Administrador", command=self.login, corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button.place(relx=0.5, rely=0.67, anchor=ctk.CENTER)

        button2 = ctk.CTkButton(master=self.master, text="Ventas", command=self.login2 ,corner_radius=32,
                               fg_color='#4158D0', hover_color='#7f5af0')
        button2.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

    def login(self):
        print(f"login: store is {store}") 
        perfil = self.my_box.get()  
        self.master.destroy()  
        Ventana_Simulador(perfil=perfil)  
    
    def login2(self):
        perfil = self.my_box.get()  
        self.master.destroy()  
        Ventana_Simulador2(perfil=perfil, store=self.store)  

class Ventana_Simulador(ctk.CTkToplevel):
    def __init__(self, master=None, perfil=''):
        super().__init__(master)
        print(f"Ventana_Simulador: store is {store}") 
        self.geometry("1000x800")
        self.title("Simulador de Abarrotes By Team 9")
        self.iconbitmap('images/Logo1.jpg')
        self.perfil = perfil
        self.store = store
        self.Label1 = ctk.CTkLabel(self, text=f'¡Bienvenido, {perfil}!')
        self.Label1.pack()

        self.id_entry = None
        self.name_entry = None
        self.price_entry = None
        self.stock_entry = None
        self.category_entry = None
        self.description_entry = None
        self.supplier_entry = None
        self.delete_entry = None

        # Botones para abrir las ventanas
        button1 = ctk.CTkButton(self, text="Agregar Producto", command=self.open_add_product_window, corner_radius=32,
                                fg_color='#4158D0', hover_color='#7f5af0')
        button1.pack(pady=5)
        button1.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        button2 = ctk.CTkButton(self, text="Ver productos", command=self.open_view_products_window, corner_radius=32,
                                fg_color='#4158D0', hover_color='#7f5af0')
        button2.pack(pady=5)
        button2.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)

        button3 = ctk.CTkButton(self, text="Información del Producto", command=self.open_product_info_window, corner_radius=32,
                                fg_color='#4158D0', hover_color='#7f5af0')
        button3.pack(pady=5)
        button3.place(relx=0.5, rely=0.20, anchor=ctk.CENTER)

        button4 = ctk.CTkButton(self, text="Eliminar Producto", command=self.open_delete_product_window, corner_radius=32,
                                fg_color='#4158D0', hover_color='#7f5af0')
        button4.pack(pady=5)
        button4.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)


    def open_add_product_window(self):
        # Cerrar la ventana actual
        self.destroy()

        # Abrir una nueva ventana
        new_window = ctk.CTkToplevel(self.master)
        new_window.title("Agregar Producto")
        new_window.geometry("500x600")

        ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
        ctk.CTkLabel(new_window, text="Ingresa los detalles del producto").pack(pady=10)

        self.id_entry = ctk.CTkEntry(new_window)
        self.id_entry.pack()
        self.id_entry.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="ID:").place(relx=0.3, rely=0.15, anchor=ctk.CENTER)

        self.name_entry = ctk.CTkEntry(new_window)
        self.name_entry.pack()
        self.name_entry.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Name:").place(relx=0.3, rely=0.25, anchor=ctk.CENTER)

        self.price_entry = ctk.CTkEntry(new_window)
        self.price_entry.pack()
        self.price_entry.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Price:").place(relx=0.3, rely=0.35, anchor=ctk.CENTER)

        self.stock_entry = ctk.CTkEntry(new_window)
        self.stock_entry.pack()
        self.stock_entry.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Stock:").place(relx=0.3, rely=0.45, anchor=ctk.CENTER)

        self.category_entry = ctk.CTkEntry(new_window)
        self.category_entry.pack()
        self.category_entry.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Category:").place(relx=0.3, rely=0.55, anchor=ctk.CENTER)

        self.description_entry = ctk.CTkEntry(new_window)
        self.description_entry.pack()
        self.description_entry.place(relx=0.50, rely=0.65, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Description:").place(relx=0.28, rely=0.65, anchor=ctk.CENTER)

        self.supplier_entry = ctk.CTkEntry(new_window)
        self.supplier_entry.pack()
        self.supplier_entry.place(relx=0.50, rely=0.75, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="Supplier:").place(relx=0.30, rely=0.75, anchor=ctk.CENTER)

        back_button1 = ctk.CTkButton(new_window, text="Guardar",command= self.add_product)
        back_button1.pack(pady=5)
        back_button1.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

        back_button = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
        back_button.pack(pady=5)
        back_button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

    def add_product(self):
        id_val = self.id_entry.get()
        name_val = self.name_entry.get()
        price_val = self.price_entry.get()
        stock_val = self.stock_entry.get()
        category_val = self.category_entry.get()
        description_val = self.description_entry.get()
        supplier_val = self.supplier_entry.get()

        product = Product(id_val, name_val, price_val, stock_val, category_val, description_val, supplier=supplier_val)

        self.store.add_product(product)        

        # Limpiar los campos de entrada después de agregar el producto
        self.id_entry.delete(0, ctk.END)
        self.name_entry.delete(0, ctk.END)
        self.price_entry.delete(0, ctk.END)
        self.stock_entry.delete(0, ctk.END)
        self.category_entry.delete(0, ctk.END)
        self.description_entry.delete(0, ctk.END)
        self.supplier_entry.delete(0, ctk.END)

        
    def open_view_products_window(self):
        
        self.destroy()

        new_window = ctk.CTkToplevel(self.master)
        new_window.title("Ver Productos")
        new_window.geometry("500x600")
        ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()            
        ctk.CTkLabel(new_window, text="Lista de productos").pack(pady=10)

        products_info = store.show_products() 
        products_label = ctk.CTkLabel(new_window, text=products_info)
        product_names = "\n".join([product.get_name() for product in store.products]) 

        products_label = ctk.CTkLabel(new_window, text=product_names)
        products_label.pack()

        back_button2 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
        back_button2.pack(pady=5)
        back_button2.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    def open_product_info_window(self):

        self.destroy()

        new_window = ctk.CTkToplevel(self.master)
        new_window.title("Información del Producto")
        new_window.geometry("500x600")
        ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
        ctk.CTkLabel(new_window, text="Detalles del producto seleccionado").pack(pady=10)

        back_button3 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
        back_button3.pack(pady=5)
        back_button3.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)           

    def open_delete_product_window(self):

        self.destroy()

        new_window = ctk.CTkToplevel(self.master)
        new_window.title("Eliminar Producto")
        new_window.geometry("500x600")
        ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
        ctk.CTkLabel(new_window, text="Eliminar un producto").pack(pady=10)

        self.delete_entry = ctk.CTkEntry(new_window)
        self.delete_entry.pack()
        self.delete_entry.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)
        ctk.CTkLabel(new_window, text="ID:").place(relx=0.3, rely=0.15, anchor=ctk.CENTER)

        back_button1 = ctk.CTkButton(new_window, text="Eliminar",command= self.delete_product)
        back_button1.pack(pady=5)
        back_button1.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

        back_button4 = ctk.CTkButton(new_window, text="Regresar al Menu", command=lambda: self.show_simulador(new_window))
        back_button4.pack(pady=5)    
        back_button4.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    def delete_product(self):
        delete_entry = self.delete_entry.get()

        self.store.remove_product(delete_entry)

        self.delete_entry.delete(0, ctk.END)

    def show_simulador(self, window_to_close):
        window_to_close.destroy()  
        Ventana_Simulador(self.master, perfil=self.perfil)  # Mostrar Ventana_Simulador nuevamente

class Ventana_Simulador2(ctk.CTkToplevel):
    def __init__(self, master=None, perfil='', store=None):
        super().__init__(master)
        self.geometry("1000x800")
        self.title("Simulador de Abarrotes By Team 9")
        self.iconbitmap('images/Logo1.jpg')
        self.perfil = perfil
        self.store = store
        self.Label1 = ctk.CTkLabel(self, text=f'¡Bienvenido, {perfil}!')
        self.Label1.pack()

        self.destroy()

        # Abrir una nueva ventana
        new_window = ctk.CTkToplevel(self.master)
        new_window.title("Agregar Producto")
        new_window.geometry("500x600")

        ctk.CTkLabel(new_window, text=f'¡Bienvenido, {self.perfil}!').pack()
        ctk.CTkLabel(new_window, text="Ingresa los productos del cliente").pack(pady=10)

        self.displaySale = ctk.CTkCanvas(self.master, bg = 'white', width=300, height=400)
        self.displaySale.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.displaySale.create_text(200, 200, text = "Este es un cuadro blanco con texto", fill="black", font=("aria"))

        self.entry = ctk.CTkEntry(self.master)
        self.entry.place(relx=0.55, rely=0.1, relwidth=0.3)

        self.button = ctk.CTkButton(self.master, text="Agregar")
        self.button.place(relx=0.55, rely=0.2, relwidth=0.3)

store = Store()
root = ctk.CTk()
app = VentanaPrincipal(root)

root.mainloop()


# ID - NAME - PREC