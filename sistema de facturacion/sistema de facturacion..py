""" Proyecto de programacion Gr-1"""
""" Sistema de facturacion para una tienda de barrio"""
""" Autor: Cristian Eras"""
""" Docente: Victor Hidalgo"""

### 1. Importar librerias.
import tkinter as tk
from tkinter import ttk

### 2. Desarrollo.
class SistemaFacturacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Facturación")

        self.productos = {
            "Arroz 10lb": 5,
            "Aceite": 3,
            "Azucar 1kg": 1.5,
            "Atun 180gr": 1.55,
            "leche 1l": 0.95,
            "pollo 1kg": 2.8,
            "salchicha 6 unidades": 1,
            "nectar de durazno 1lt": 1.25,
            # Puedes agregar más productos aquí en el formato "Nombre del producto": Precio
        }

        self.carrito = {}
        self.total = 0
        self.subtotal = 0
        self.iva = 0

        self.lbl_producto = tk.Label(root, text="Producto:")
        self.lbl_producto.pack()

        self.producto_var = tk.StringVar()
        self.producto_combobox = ttk.Combobox(root, textvariable=self.producto_var, values=list(self.productos.keys()))
        self.producto_combobox.pack()

        self.lbl_cantidad = tk.Label(root, text="Cantidad:")
        self.lbl_cantidad.pack()

        self.cantidad_entry = tk.Entry(root)
        self.cantidad_entry.pack()

        self.btn_agregar = tk.Button(root, text="Agregar al carrito", command=self.agregar_al_carrito)
        self.btn_agregar.pack()

        self.lbl_carrito = tk.Label(root, text="Carrito:")
        self.lbl_carrito.pack()

        self.carrito_listbox = tk.Listbox(root)
        self.carrito_listbox.pack()

        self.lbl_total_unitario = tk.Label(root, text="Total Unitario: $0")
        self.lbl_total_unitario.pack()

        self.lbl_subtotal = tk.Label(root, text="Subtotal: $0")
        self.lbl_subtotal.pack()

        self.lbl_iva = tk.Label(root, text="IVA (12%): $0")
        self.lbl_iva.pack()

        self.lbl_total = tk.Label(root, text="Total: $0")
        self.lbl_total.pack()

    def agregar_al_carrito(self):
        producto = self.producto_var.get()
        cantidad = int(self.cantidad_entry.get())

        if cantidad <= 0:
            return

        precio_unitario = self.productos[producto]
        total_unitario = precio_unitario * cantidad
        subtotal_anterior = self.subtotal

        if producto in self.carrito:
            self.carrito[producto] += cantidad
        else:
            self.carrito[producto] = cantidad

        self.subtotal += total_unitario
        self.total = self.subtotal + self.iva

        self.actualizar_carrito()
        self.actualizar_total_unitario(producto, total_unitario)
        self.actualizar_subtotal(subtotal_anterior)
        self.actualizar_iva()
        self.actualizar_total()

    def actualizar_carrito(self):
        self.carrito_listbox.delete(0, tk.END)
        for producto, cantidad in self.carrito.items():
            self.carrito_listbox.insert(tk.END, f"{producto} x {cantidad}")

    def actualizar_total_unitario(self, producto, total_unitario):
        self.lbl_total_unitario.config(text=f"Total Unitario: ${total_unitario:.2f} ({producto})")

    def actualizar_subtotal(self, subtotal_anterior):
        self.lbl_subtotal.config(text=f"Subtotal: ${self.subtotal:.2f}")
        if self.subtotal > subtotal_anterior:
            self.actualizar_iva()

    def actualizar_iva(self):
        self.iva = self.subtotal * 0.12
        self.lbl_iva.config(text=f"IVA (12%): ${self.iva:.2f}")

    def actualizar_total(self):
        self.total = self.subtotal + self.iva
        self.lbl_total.config(text=f"Total: ${self.total:.2f}")


### 3. Impresion de resultados.
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaFacturacion(root)
    root.mainloop()

