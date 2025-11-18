import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog, QMessageBox,
    QHeaderView, QFrame, QScrollArea, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer

# 1. IMPORTACIÓN DEL ESTILO (Nuevo)
# Asume que views/styles.py existe y contiene la variable STYLE_SHEET
from views.styles import STYLE_SHEET 

ARCHIVO = "productos.json"

# --- Manejo de productos ---
def cargar_productos():
    try:
        with open(ARCHIVO, "r", encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def guardar_productos(productos):
    try:
        with open(ARCHIVO, "w", encoding='utf-8') as f:
            json.dump(productos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar productos: {e}")

# --- Ventana principal ---
class SistemaCosteo(QWidget):
    def __init__(self):
        super().__init__()
        self.productos = cargar_productos()
        self.costo_base = 0.0
        self.initUI()
        self.aplicar_estilos()

    def initUI(self):
        self.setWindowTitle("📊 Sistema de Costeo Profesional")
        self.resize(1200, 800)  # Aumentar tamaño de ventana
        self.setMinimumSize(1000, 700)

        # Scroll area principal para ventanas pequeñas
        # scroll = QScrollArea()
        # scroll.setWidgetResizable(True)
        # scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # Widget contenedor principal
        main_widget = QWidget()
        # scroll.setWidget(main_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(25)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Header mejorado
        header_frame = self.crear_header()
        main_layout.addWidget(header_frame)

        # Contenedor para la tabla con mejor espaciado
        tabla_frame = self.crear_seccion_tabla()
        main_layout.addWidget(tabla_frame)

        # Contenedor para botones con mejor organización
        buttons_frame = self.crear_seccion_botones()
        main_layout.addWidget(buttons_frame)

        # Resultado mejorado
        resultado_frame = self.crear_seccion_resultado()
        main_layout.addWidget(resultado_frame)

        # Layout principal de la ventana
        window_layout = QVBoxLayout()
        window_layout.setContentsMargins(0, 0, 0, 0)
        window_layout.addWidget(main_widget)  # Agrega el widget principal directamente
        # window_layout.addWidget(scroll)
        self.setLayout(window_layout)

        # Cargar datos iniciales
        self.cargar_tabla()

    def crear_header(self):
        """Crear header con mejor estructura"""
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_frame.setFixedHeight(120)
        header_layout = QVBoxLayout(header_frame)
        header_layout.setAlignment(Qt.AlignCenter)
        
        titulo = QLabel("Sistema de Costeo Profesional")
        titulo.setObjectName("mainTitle")
        titulo.setAlignment(Qt.AlignCenter)
        
        subtitulo = QLabel("Gestión inteligente de costos y productos")
        subtitulo.setObjectName("subtitle")
        subtitulo.setAlignment(Qt.AlignCenter)
        
        header_layout.addWidget(titulo)
        header_layout.addWidget(subtitulo)
        
        return header_frame

    def crear_seccion_tabla(self):
        """Crear sección de tabla con mejor estructura"""
        tabla_frame = QFrame()
        tabla_frame.setObjectName("tableFrame")
        tabla_layout = QVBoxLayout(tabla_frame)
        tabla_layout.setContentsMargins(20, 20, 20, 20)
        tabla_layout.setSpacing(15)

        tabla_label = QLabel("📋 Productos Registrados")
        tabla_label.setObjectName("sectionLabel")
        tabla_layout.addWidget(tabla_label)

        # Tabla mejorada con mejor configuración
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels([
            "Producto", "Precio Total ($)", "Peso (g)", "Peso (lb)", "Gramos a Usar", "Costo/Gramo ($)"
        ])
        self.tabla.setObjectName("productTable")
        self.tabla.setMinimumHeight(350)
        self.tabla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Configurar header para que todas las columnas se expandan
        header = self.tabla.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        # El resto de configuraciones de la tabla...
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setShowGrid(True)
        self.tabla.setGridStyle(Qt.SolidLine)
        self.tabla.verticalHeader().setDefaultSectionSize(78)  # <-- Aumenta el alto de las filas
        
        tabla_layout.addWidget(self.tabla)
        return tabla_frame

    def crear_seccion_botones(self):
        """Crear sección de botones con mejor organización"""
        buttons_frame = QFrame()
        buttons_frame.setObjectName("buttonsFrame")
        buttons_layout = QVBoxLayout(buttons_frame)
        buttons_layout.setContentsMargins(20, 20, 20, 20)
        buttons_layout.setSpacing(15)

        buttons_label = QLabel("⚡ Acciones Rápidas")
        buttons_label.setObjectName("sectionLabel")
        buttons_layout.addWidget(buttons_label)

        # Container para los botones con grid layout
        buttons_container = QWidget()
        buttons_grid = QVBoxLayout(buttons_container)
        buttons_grid.setSpacing(12)
        
        # Primera fila de botones en acciones rapidas ----------------------------------------
        btn_layout1 = QHBoxLayout()
        btn_layout1.setSpacing(15)
        
        self.btn_agregar = QPushButton("➕ Agregar Producto")
        self.btn_agregar.setObjectName("primaryButton")
        self.btn_agregar.setMinimumHeight(45)
        self.btn_agregar.clicked.connect(self.agregar_producto)
        
        self.btn_eliminar = QPushButton("🗑️ Eliminar Producto")
        self.btn_eliminar.setObjectName("dangerButton")
        self.btn_eliminar.setMinimumHeight(45)
        self.btn_eliminar.clicked.connect(self.eliminar_producto)
        
        btn_layout1.addWidget(self.btn_agregar)
        btn_layout1.addWidget(self.btn_eliminar)
        
        # Segunda fila de botones en acciones rapidas ----------------------------------------
        btn_layout2 = QHBoxLayout()
        btn_layout2.setSpacing(15)
        
        self.btn_ganancia = QPushButton("💰 Calcular Ganancia")
        self.btn_ganancia.setObjectName("successButton")
        self.btn_ganancia.setMinimumHeight(45)
        self.btn_ganancia.clicked.connect(self.aplicar_ganancia)
        
        self.btn_compuesto = QPushButton("🧩 Producto Compuesto")
        self.btn_compuesto.setObjectName("infoButton")
        self.btn_compuesto.setMinimumHeight(45)
        self.btn_compuesto.clicked.connect(self.crear_producto_compuesto)
        
        btn_layout2.addWidget(self.btn_ganancia)
        btn_layout2.addWidget(self.btn_compuesto)

        buttons_grid.addLayout(btn_layout1)
        buttons_grid.addLayout(btn_layout2)
        buttons_layout.addWidget(buttons_container)
        
        return buttons_frame

    def crear_seccion_resultado(self):
        """Crear sección de resultado con mejor diseño"""
        resultado_frame = QFrame()
        resultado_frame.setObjectName("resultFrame")
        resultado_frame.setFixedHeight(100)
        resultado_layout = QVBoxLayout(resultado_frame)
        resultado_layout.setContentsMargins(25, 20, 25, 20)
        resultado_layout.setAlignment(Qt.AlignCenter)

        self.resultado = QLabel("💲 Costo Total: $0.00")
        self.resultado.setObjectName("resultLabel")
        self.resultado.setAlignment(Qt.AlignCenter)
        self.resultado.setWordWrap(True)
        
        resultado_layout.addWidget(self.resultado)
        return resultado_frame


    # IMPORTACIÓN DE ESTILOS 
    def aplicar_estilos(self):
        """Aplica estilos CSS importados desde views/styles.py"""
        #USO DE LA VARIABLE IMPORTADA (Cambiado)
        self.setStyleSheet(STYLE_SHEET)



    # --- Funciones CRUD --------------------------------------LOGICA-----------------------------------------------
    def cargar_tabla(self):
        """Cargar tabla con manejo de errores"""
        try:
            self.tabla.setRowCount(len(self.productos))
            self.tabla.setEditTriggers(QTableWidget.AllEditTriggers)
            
            for fila, (nombre, datos) in enumerate(self.productos.items()):
                if not all(key in datos for key in ["precio", "peso", "costo_por_gramo"]):
                    continue
                
                # Nombre del producto
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(nombre)))
                
                # Precio
                precio_item = QTableWidgetItem(f"{datos['precio']:.2f}")
                self.tabla.setItem(fila, 1, precio_item)

                # Peso en gramos (editable) 
                peso_item = QTableWidgetItem(f"{datos['peso']:.2f}")
                peso_item.setFlags(peso_item.flags() | Qt.ItemIsEditable)
                self.tabla.setItem(fila, 2, peso_item)

                # Peso en libras (calculado)
                peso_lb = datos['peso'] / 454 if datos['peso'] else 0
                peso_lb_item = QTableWidgetItem(f"{peso_lb:.3f}")
                peso_lb_item.setFlags(peso_lb_item.flags() & ~Qt.ItemIsEditable)  # Solo lectura
                self.tabla.setItem(fila, 3, peso_lb_item)

                # Costo por gramo (calculo)
                costo_item = QTableWidgetItem(f"{datos['costo_por_gramo']:.5f}")
                self.tabla.setItem(fila, 5, costo_item)

                # Input para gramos a usar
                gramos_input = QLineEdit()
                gramos_input.setPlaceholderText("0.00")
                gramos_input.setStyleSheet("""
                    QLineEdit {
                        background-color: #494F55;
                        border: 2px solid #d1d5db;
                        border-radius: 6px;
                        padding: 8px 12px;
                        font-size: 12px;
                        font-weight: 500;
                        color: #000000;
                        min-height: 10px;
                    }
                    QLineEdit:focus {
                        border-color: #3b82f6;
                        background-color: #f8fafc;
                        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
                    }
                    QLineEdit:hover {
                        border-color: #6b7280;
                    }
                """)
                gramos_input.textChanged.connect(self.calcular_total)
                self.tabla.setCellWidget(fila, 4, gramos_input)

            # Conectar eventos
            self.tabla.itemChanged.connect(self.actualizar_costo_por_gramo)
            
            # Calcular total inicial
            QTimer.singleShot(100, self.calcular_total)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar la tabla: {str(e)}")


    # agregar producto --------------------------------------------------------------------------------------------------------------
    def agregar_producto(self):
        """Agregar producto permitiendo ingresar libras o gramos"""
        try:
            nombre, ok = QInputDialog.getText(self, "Agregar Producto", "Nombre del producto:")
            if not ok or not nombre.strip():
                return
            
            nombre = nombre.strip().lower()
            if nombre in self.productos:
                QMessageBox.warning(self, "Error", "El producto ya existe.")
                return

            precio, ok1 = QInputDialog.getDouble(self, "Agregar Producto", 
                                               "Precio total ($):", 0.0, 0.0, 999999.99, 2)
            if not ok1 or precio <= 0:
                QMessageBox.warning(self, "Error", "El precio debe ser mayor a cero.")
                return

            # Preguntar por libras y gramos, cualquiera puede quedar en 0
            peso_lb, ok_lb = QInputDialog.getDouble(self, "Agregar Producto", 
                                                    "Peso total (libras): o dejar en 0 si desea usar gramos", 0.0, 0.0, 999999.99, 3)
            peso_g, ok_g = QInputDialog.getDouble(self, "Agregar Producto", 
                                                  "Peso total (gramos): o dejar en 0 si usó libras", 0.0, 0.0, 999999.99, 2)

            # Si ambos en blanco o cero, error
            if (peso_lb <= 0 and peso_g <= 0):
                QMessageBox.warning(self, "Error", "Debe ingresar al menos libras o gramos.")
                return

            # Si solo libras, convertir a gramos
            if peso_lb > 0 and peso_g <= 0:
                peso = peso_lb * 454
            # Si solo gramos, usar gramos
            elif peso_g > 0 and peso_lb <= 0:
                peso = peso_g
            # Si ambos, sumar
            else:
                peso = peso_g + (peso_lb * 454)

            # Agregar producto
            self.productos[nombre] = {
                "precio": precio,
                "peso": peso,
                "costo_por_gramo": precio / peso
            }
            
            guardar_productos(self.productos)
            self.cargar_tabla()
            QMessageBox.information(
                self, "Éxito", 
                f"Producto '{nombre}' agregado correctamente.\nPeso total: {peso:.2f}g"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar producto: {str(e)}")


    # eliminar producto -------------------------------------------------------------------------------------------------------------
    def eliminar_producto(self):
        """Eliminar producto con confirmación"""
        try:
            fila = self.tabla.currentRow()
            if fila < 0:
                QMessageBox.warning(self, "Error", "Seleccione un producto para eliminar")
                return
            
            nombre_item = self.tabla.item(fila, 0)
            if not nombre_item:
                QMessageBox.warning(self, "Error", "No se puede obtener el nombre del producto")
                return
                
            nombre = nombre_item.text()
            
            # Confirmar eliminación
            respuesta = QMessageBox.question(self, "Confirmar", 
                                           f"¿Está seguro de eliminar el producto '{nombre}'?",
                                           QMessageBox.Yes | QMessageBox.No)
            
            if respuesta == QMessageBox.Yes and nombre in self.productos:
                del self.productos[nombre]
                guardar_productos(self.productos)
                self.cargar_tabla()
                QMessageBox.information(self, "Éxito", f"Producto '{nombre}' eliminado correctamente.")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar producto: {str(e)}")


    # crear producto compuesto -------------------------------------------------------------------------------------------------------------
    def crear_producto_compuesto(self):
        """Crear producto compuesto con mejor flujo"""
        try:
            if not self.productos:
                QMessageBox.warning(self, "Error", "No hay productos base para crear el compuesto.")
                return

            nombre_compuesto, ok = QInputDialog.getText(self, "Nombre del compuesto", 
                                                      "Nombre del producto compuesto:")
            if not ok or not nombre_compuesto.strip():
                return

            nombre_compuesto = nombre_compuesto.strip().lower()
            if nombre_compuesto in self.productos:
                QMessageBox.warning(self, "Error", "Ya existe un producto con ese nombre.")
                return

            ingredientes = []
            productos_disponibles = list(self.productos.keys())

            while True:
                ingrediente, ok = QInputDialog.getItem(self, "Ingrediente", 
                                                     "Selecciona un ingrediente:", 
                                                     productos_disponibles, editable=False)
                if not ok:
                    break
                    
                gramos, ok2 = QInputDialog.getDouble(self, "Cantidad", 
                                                   f"¿Cuántos gramos de '{ingrediente}'?", 
                                                   0.0, 0.01, 999999.99, 2)
                if not ok2 or gramos <= 0:
                    QMessageBox.warning(self, "Error", "La cantidad debe ser mayor a cero.")
                    continue
                    
                ingredientes.append((ingrediente, gramos))
                
                continuar = QMessageBox.question(self, "Agregar otro", 
                                               "¿Agregar otro ingrediente?", 
                                               QMessageBox.Yes | QMessageBox.No)
                if continuar == QMessageBox.No:
                    break

            if not ingredientes:
                QMessageBox.information(self, "Cancelado", "No se agregaron ingredientes.")
                return

            # Calcular costos y pesos totales ---------------------------------------------------------------------------------
            costo_total = 0
            peso_total = 0
            
            for nombre_ing, gramos in ingredientes:
                datos = self.productos.get(nombre_ing)
                if datos:
                    costo_total += gramos * datos["costo_por_gramo"]
                    peso_total += gramos

            if peso_total > 0:
                self.productos[nombre_compuesto] = {
                    "precio": costo_total,
                    "peso": peso_total,
                    "costo_por_gramo": costo_total / peso_total
                }
                guardar_productos(self.productos)
                self.cargar_tabla()
                
                # Mostrar resumen
                ingredientes_str = ", ".join([f"{ing}: {gr}g" for ing, gr in ingredientes])
                QMessageBox.information(self, "Éxito", 
                                      f"Producto compuesto '{nombre_compuesto}' creado!\n\n"
                                      f"Ingredientes: {ingredientes_str}\n"
                                      f"Costo total: ${costo_total:.2f}\n"
                                      f"Peso total: {peso_total}g")
                                      
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear producto compuesto: {str(e)}")


    # calcular total PARTE DE ABAJO -----------------------------------------------------------------------------------------------------
    def calcular_total(self):
        """Calcular total con mejor manejo de errores"""
        try:
            total = 0.0
            productos_usados = []
            
            for fila in range(self.tabla.rowCount()):
                nombre_item = self.tabla.item(fila, 0)
                if not nombre_item:
                    continue
                    
                nombre = nombre_item.text()
                if nombre not in self.productos:
                    continue
                
                # Obtener cantidad a usar ---------------------------------------------------------------------------------------------
                gramos_widget = self.tabla.cellWidget(fila, 4)
                gramos = 0.0
                
                if gramos_widget:
                    try:
                        texto = gramos_widget.text().strip()
                        gramos = float(texto) if texto else 0.0
                    except ValueError:
                        gramos = 0.0

                # Actualizar datos del producto si fueron editados ---------------------------------------------------------------------------------
                try:
                    precio_item = self.tabla.item(fila, 1)
                    peso_item = self.tabla.item(fila, 2)
                    
                    if precio_item and peso_item:
                        precio = float(precio_item.text())
                        peso = float(peso_item.text())
                        
                        if peso > 0 and precio >= 0:
                            datos = self.productos[nombre]
                            datos["precio"] = precio
                            datos["peso"] = peso
                            datos["costo_por_gramo"] = precio / peso
                            
                            # Actualizar costo por gramo en la tabla
                            costo_item = QTableWidgetItem(f"{datos['costo_por_gramo']:.5f}")
                            self.tabla.setItem(fila, 5, costo_item)
                            
                except (ValueError, ZeroDivisionError):
                    continue

                # Calcular costo parcial
                if gramos > 0:
                    costo_parcial = gramos * self.productos[nombre]["costo_por_gramo"]
                    total += costo_parcial
                    productos_usados.append(f"{nombre}: {gramos}g")

            self.costo_base = total
            self.resultado.setText(f"💲 Costo Total: ${total:.2f}")
            
            # Guardar cambios
            guardar_productos(self.productos)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al calcular total: {str(e)}")


    # calcular ganancia -----------------------------------------------------------------------------------------------------
    def aplicar_ganancia(self):
        """Aplicar ganancia con validación mejorada"""
        try:
            if not hasattr(self, "costo_base") or self.costo_base <= 0:
                QMessageBox.warning(self, "Error", "Primero debe calcular un costo base mayor a cero.")
                return
                
            porcentaje, ok = QInputDialog.getDouble(self, "Ganancia", 
                                                  "Ingrese % de ganancia:", 
                                                  20.0, 0.0, 1000.0, 2)
            if ok:
                precio_venta = self.costo_base * (1 + porcentaje / 100)
                ganancia_absoluta = precio_venta - self.costo_base
                
                self.resultado.setText(
                    f"💲 Costo: ${self.costo_base:.2f} | "
                    f"💵 Venta: ${precio_venta:.2f} | "
                    f"💰 Ganancia: ${ganancia_absoluta:.2f} ({porcentaje:.1f}%)"
                )
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al calcular ganancia: {str(e)}")

    # actualizar costo por gramo cuando se edita el peso -----------------------------------------------------------------------------------------
    def actualizar_costo_por_gramo(self, item):
        """Actualizar costo por gramo cuando se edita el peso"""
        try:
            if item.column() == 2:  # Columna de peso en gramos
                fila = item.row()
                nombre_item = self.tabla.item(fila, 0)
                precio_item = self.tabla.item(fila, 1)
                
                if nombre_item and precio_item:
                    nombre = nombre_item.text()
                    
                    try:
                        peso = float(item.text())
                        precio = float(precio_item.text())
                        
                        if peso <= 0:
                            QMessageBox.warning(self, "Error", "El peso debe ser mayor a cero.")
                            if nombre in self.productos:
                                item.setText(str(self.productos[nombre]["peso"]))
                            return
                        
                        if precio < 0:
                            QMessageBox.warning(self, "Error", "El precio no puede ser negativo.")
                            return
                        
                        # Actualizar producto -----------------------------------------------------------------------------------------------
                        if nombre in self.productos:
                            costo_por_gramo = precio / peso
                            self.productos[nombre]["peso"] = peso
                            self.productos[nombre]["precio"] = precio
                            self.productos[nombre]["costo_por_gramo"] = costo_por_gramo
                            
                            # Actualizar tabla
                            costo_item = QTableWidgetItem(f"{costo_por_gramo:.5f}")
                            self.tabla.setItem(fila, 5, costo_item)
                            # Actualizar columna de libras
                            peso_lb = peso / 454 if peso else 0
                            peso_lb_item = QTableWidgetItem(f"{peso_lb:.3f}")
                            peso_lb_item.setFlags(peso_lb_item.flags() & ~Qt.ItemIsEditable)
                            self.tabla.setItem(fila, 3, peso_lb_item)
                            
                            guardar_productos(self.productos)
                            self.calcular_total()
                            
                    except ValueError:
                        QMessageBox.warning(self, "Error", "Ingrese un valor numérico válido.")
                        if nombre in self.productos:
                            item.setText(str(self.productos[nombre]["peso"]))
                            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar producto: {str(e)}")

    def closeEvent(self, event):
        """Manejar cierre de aplicación"""
        try:
            guardar_productos(self.productos)
            event.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar datos: {str(e)}")
            event.accept()  # Cerrar de todas formas

# --- Ejecutar aplicación ------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setStyle('Fusion')  # Estilo más moderno
        
        # Configurar la aplicación
        app.setApplicationName("Sistema de Costeo Profesional")
        app.setApplicationVersion("2.0")
        app.setOrganizationName("Tu Empresa")
        
        ventana = SistemaCosteo()
        ventana.show()
        
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"Error crítico al iniciar la aplicación: {str(e)}")
        sys.exit(1)


