import json

# ---------------------------------------- modelo de datos del PRODUCTO ---------------------------------------- #

class ProductoModel:
    def __init__(self):
        self.productos = {}
        self.archivo = "productos.json"

    def cargar_productos(self):
        try:
            with open(self.archivo, "r", encoding='utf-8') as f:
                self.productos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}
        return self.productos

    def guardar_productos(self):
        with open(self.archivo, "w", encoding='utf-8') as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def agregar_producto(self, nombre, precio, peso):
        self.productos[nombre] = {
            "precio": precio,
            "peso": peso,
            "costo_por_gramo": precio / peso
        }
        self.guardar_productos()

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_productos()

    def actualizar_producto(self, nombre, precio, peso):
        if nombre in self.productos:
            self.productos[nombre].update({
                "precio": precio,
                "peso": peso,
                "costo_por_gramo": precio / peso
            })
            self.guardar_productos()