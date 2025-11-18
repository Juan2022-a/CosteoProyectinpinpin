from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QLineEdit, QFrame, 
    QHeaderView, QSizePolicy
)
from PyQt5.QtCore import Qt
from .styles import STYLE_SHEET

# ---------------------------------------- diseño de la ventana principal ---------------------------------------- #

class MainWindow(QWidget):
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

        # Header cambiado
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
        
        # Primera fila de botones
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
        
        # Segunda fila de botones
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