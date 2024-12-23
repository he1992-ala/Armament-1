import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Armamet")
ventana.geometry("400x300")

class Arma:
    def __init__(self, tipo, numero_inventario, estado):
        self.tipo = tipo
        self.numero_inventario = numero_inventario
        self.estado = estado

class ArmaDeFuego(Arma):
    def __init__(self, tipo, numero_inventario, estado, calibre, tiene_cargador, cantidad_balas, alcance_maximo, longitud_canon):
        super().__init__(tipo, numero_inventario, estado)
        self.calibre = calibre
        self.tiene_cargador = tiene_cargador
        self.cantidad_balas = cantidad_balas
        self.alcance_maximo = alcance_maximo
        self.longitud_canon = longitud_canon

    def calcular_peso_perdida(self):
        return self.cantidad_balas * self.calibre

    def calcular_utilidad(self):
        return self.longitud_canon * self.alcance_maximo * 1.5

class ArmaBlanca(Arma):
    def __init__(self, tipo, numero_inventario, estado, material, valor_material, peligrosidad):
        super().__init__(tipo, numero_inventario, estado)
        self.material = material
        self.valor_material = valor_material
        self.peligrosidad = peligrosidad

    def calcular_peso_perdida(self):
        return self.valor_material * self.peligrosidad

    def calcular_utilidad(self):
        return self.peligrosidad * 1.7

class Inventario:
    def __init__(self):
        self.armas = []

    def agregar_arma(self, arma):
        self.armas.append(arma)

    def buscar_arma(self, numero_inventario):
        for arma in self.armas:
            if arma.numero_inventario == numero_inventario:
                return arma
        return None

    def listar_armas(self):
        return [str(arma) for arma in self.armas]

inventario = Inventario()

def agregar_arma():
    tipo = tipo_var.get()
    numero_inventario = numero_inventario_var.get()
    estado = estado_var.get()
    if tipo == "Arma de Fuego":
        calibre = float(calibre_var.get())
        tiene_cargador = tiene_cargador_var.get() == "Sí"
        cantidad_balas = int(cantidad_balas_var.get())
        alcance_maximo = float(alcance_maximo_var.get())
        longitud_canon = float(longitud_canon_var.get())
        arma = ArmaDeFuego(tipo, numero_inventario, estado, calibre, tiene_cargador, cantidad_balas, alcance_maximo, longitud_canon)
    else:
        material = material_var.get()
        valor_material = float(valor_material_var.get())
        peligrosidad = float(peligrosidad_var.get())
        arma = ArmaBlanca(tipo, numero_inventario, estado, material, valor_material, peligrosidad)
    inventario.agregar_arma(arma)
    print(f"Arma agregada: {arma}")

# Crear widgets para ingresar datos
tipo_var = tk.StringVar()
numero_inventario_var = tk.StringVar()
estado_var = tk.StringVar()
calibre_var = tk.StringVar()
tiene_cargador_var = tk.StringVar()
cantidad_balas_var = tk.StringVar()
alcance_maximo_var = tk.StringVar()
longitud_canon_var = tk.StringVar()
material_var = tk.StringVar()
valor_material_var = tk.StringVar()
peligrosidad_var = tk.StringVar()

ttk.Label(ventana, text="Tipo de Arma").grid(column=0, row=0)
ttk.Combobox(ventana, textvariable=tipo_var, values=["Arma de Fuego", "Arma Blanca"]).grid(column=1, row=0)

ttk.Label(ventana, text="Número de Inventario").grid(column=0, row=1)
ttk.Entry(ventana, textvariable=numero_inventario_var).grid(column=1, row=1)

ttk.Label(ventana, text="Estado").grid(column=0, row=2)
ttk.Entry(ventana, textvariable=estado_var).grid(column=1, row=2)

ttk.Label(ventana, text="Calibre").grid(column=0, row=3)
ttk.Entry(ventana, textvariable=calibre_var).grid(column=1, row=3)

ttk.Label(ventana, text="Tiene Cargador").grid(column=0, row=4)
ttk.Combobox(ventana, textvariable=tiene_cargador_var, values=["Sí", "No"]).grid(column=1, row=4)

ttk.Label(ventana, text="Cantidad de Balas").grid(column=0, row=5)
ttk.Entry(ventana, textvariable=cantidad_balas_var).grid(column=1, row=5)

ttk.Label(ventana, text="Alcance Máximo").grid(column=0, row=6)
ttk.Entry(ventana, textvariable=alcance_maximo_var).grid(column=1, row=6)

ttk.Label(ventana, text="Longitud del Cañón").grid(column=0, row=7)
ttk.Entry(ventana, textvariable=longitud_canon_var).grid(column=1, row=7)

ttk.Label(ventana, text="Material").grid(column=0, row=8)
ttk.Entry(ventana, textvariable=material_var).grid(column=1, row=8)

ttk.Label(ventana, text="Valor del Material").grid(column=0, row=9)
ttk.Entry(ventana, textvariable=valor_material_var).grid(column=1, row=9)

ttk.Label(ventana, text="Peligrosidad").grid(column=0, row=10)
ttk.Entry(ventana, textvariable=peligrosidad_var).grid(column=1, row=10)

ttk.Button(ventana, text="Agregar Arma", command=agregar_arma).grid(column=0, row=11, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
