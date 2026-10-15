
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desarrollado por: 👉 Cristian M. Veliz Cano ✔
Versión del Soft: 👉 V-03
Nombre del Soft: ✨ JXL Image Converter ✨
Lenguaje: 👉 Python 3.8.3
Interfaz Gráfica: 👉 PyQt5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ CONVERSOR DE IMÁGENES JPEG-XL ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Este Software ha sido desarrollado como una
herramienta sencilla, minimalista y práctica para
trabajar con imágenes en formato JPEG-XL (.JXL).

El programa permite visualizar imágenes y realizar
conversiones entre JPEG-XL y diferentes formatos
de imagen convencionales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 FORMATOS COMPATIBLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software permite ingresar imágenes en los
siguientes formatos:

    • PNG
    • JPG
    • JPEG
    • BMP
    • TIFF
    • WEBP
    • GIF
    • JXL / JPEG-XL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ➡️ CONVERSIÓN HACIA JXL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software permite convertir una imagen cargada
a formato JPEG-XL (.JXL).

Formatos de entrada:

    • PNG
    • JPG
    • JPEG
    • BMP
    • TIFF
    • WEBP
    • GIF

La conversión hacia JPEG-XL se realiza utilizando
compresión LOSSLESS (sin pérdida).

Esto permite conservar los datos de imagen sin
aplicar una pérdida de calidad intencional durante
la conversión.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ⬅️ CONVERSIÓN DESDE JXL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Las imágenes JPEG-XL (.JXL) pueden ser abiertas
y posteriormente convertidas a:

    • PNG
    • JPEG / JPG
    • BMP
    • TIFF

El usuario puede seleccionar el formato de salida
desde el cuadro de diálogo de guardado.

┌─────────────────────────────────────────────────────────┐
│  Usuario presiona "JXL → PNG/JPG"                       │
└────────────────┬────────────────────────────────────────┘
                 │
    ┌────────────▼────────────┐
    │ ¿Hay JXL cargado?       │
    └────────────┬────────────┘
         Sí │          │ No
           ▼          ▼
    ┌──────────┐   ┌──────────────────┐
    │ Modo     │   │ Selector múltiple│
    │ Single   │   │ de archivos .jxl │
    └──────────┘   └────────┬───────────┘
                            │
                   ┌────────▼────────┐
                   │ Selector formato │
                   │ (PNG/JPG/BMP/TIFF)│
                   └────────┬────────┘
                            │
                   ┌────────▼────────┐
                   │ Selector carpeta│
                   │ de salida       │
                   └────────┬────────┘
                            │
                   ┌────────▼────────┐
                   │ QThread Worker  │
                   │ + ProgressDialog│
                   │ "X de XX"       │
                   └─────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       🖼️ VISUALIZADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software incorpora un visor integrado que permite
mostrar la imagen cargada directamente dentro de la
ventana principal.

En el caso de JPEG-XL, el archivo es decodificado
mediante el módulo especializado:

    pillow_jxl

Los datos de imagen JPEG-XL son convertidos en una
imagen compatible con Pillow y posteriormente son
enviados al sistema gráfico de Qt para su
visualización.

El proceso de visualización se realiza en memoria,
sin necesidad de crear un archivo PNG temporal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔧 MOTOR DE PROCESAMIENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El procesamiento de imágenes se realiza mediante:

    • Python
    • Pillow
    • pillow-jxl
    • PyQt5

Pillow se utiliza para trabajar con los formatos
de imagen convencionales.

JPEG-XL utiliza el Decoder proporcionado por
pillow_jxl para realizar la decodificación del
formato JXL.

La imagen resultante es posteriormente transformada
para ser mostrada mediante QImage y QPixmap.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📐 INFORMACIÓN DE IMAGEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Al cargar una imagen, el Software muestra
información básica sobre ella:

    • Ancho de la imagen
    • Alto de la imagen
    • Modo de color
    • Formato de imagen

Ejemplo:

    📐 1280 × 1024 px
    🎨 Modo: RGB
    📦 Formato: JXL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        📌 LICENCIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita, a cualquier
persona que obtenga una copia de este software y de
los archivos de documentación asociados, para utilizar
el Software sin restricción, incluyendo sin limitación
los derechos de uso, copia, modificación, fusión,
publicación, distribución, sublicencia y/o venta de
copias del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              🖼️ JXL Image Converter 🖼️

      Una herramienta sencilla para trabajar
             con imágenes JPEG-XL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Alojado en Mega:
https://mega.nz/file/Hptz0TzY#0n2Pq9lILpdINhrJEVRVvweoNoB9xYSXOpG8E6eCF40
'''
##=========================================================================================
import sys, os
from io import BytesIO

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QFileDialog,
    QVBoxLayout, QHBoxLayout, QMessageBox, QDialog, QShortcut, QTextEdit, QPlainTextEdit, QProgressDialog)

from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QKeySequence, QPixmap, QImage, QIcon, QFont

from PIL import Image
import glob
# ============================================================
# IMPORTANTE:
# Registra el soporte JPEG-XL en Pillow
# ============================================================
import pillow_jxl
from pillow_jxl import Decoder

##====================================================================================
# --- Clase para manejo de rutas de recursos (Sin cambios) ---
##====================================================================================
class Path():

    # =========================
    # ✨ Debuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================
    def resource_path(relative_path):    ## Forma #1 resource_path(relative_path)
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # =========================
    # ✨ Debuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================
    def resource_path_app():    ## Forma #2 resource_path_app()

        try:
            path_app = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

        except Exception as e:
            print(e)

        except IOError as error:
            print( error )

        return path_app

# ============================================================
# WORKERS PARA THREADS (Anti-congelamiento)
# ============================================================
class ConvertirAJXLWorker(QThread):
    """Worker para convertir imágenes a JXL sin bloquear la UI"""
    progreso = pyqtSignal(int, int)      # (actual, total)
    completado = pyqtSignal(list)        # [rutas_convertidas]
    error = pyqtSignal(str)              # mensaje_error
    cancelado = pyqtSignal()
    
    def __init__(self, rutas_imagenes, carpeta_salida=None):
        super().__init__()
        self.rutas_imagenes = rutas_imagenes if isinstance(rutas_imagenes, list) else [rutas_imagenes]
        self.carpeta_salida = carpeta_salida
        self._cancelar = False
        
    def cancelar(self):
        self._cancelar = True
        
    def run(self):
        rutas_convertidas = []
        total = len(self.rutas_imagenes)
        
        for idx, ruta in enumerate(self.rutas_imagenes):
            if self._cancelar:
                self.cancelado.emit()
                return
                
            try:
                # Determinar ruta de salida
                if self.carpeta_salida:
                    nombre = os.path.splitext(os.path.basename(ruta))[0] + ".jxl"
                    ruta_salida = os.path.join(self.carpeta_salida, nombre)
                else:
                    ruta_salida = os.path.splitext(ruta)[0] + ".jxl"
                
                # Abrir y convertir
                with Image.open(ruta) as img:
                    img.load()
                    if img.mode not in ("RGB", "RGBA"):
                        img = img.convert("RGBA")

                    img.save(ruta_salida, format="JXL", lossless=True)
                    
                rutas_convertidas.append(ruta_salida)
                self.progreso.emit(idx + 1, total)
                
            except Exception as e:
                self.error.emit(f"Error en {os.path.basename(ruta)}: {str(e)}")
                return
                
        self.completado.emit(rutas_convertidas)

# ============================================================
# QWorker: ConvertirDesdeJXLWorker - Worker para convertir JXL a otros formatos sin bloquear la UI
# ============================================================
class ConvertirDesdeJXLWorker(QThread):
    """Worker para convertir JXL a otros formatos sin bloquear la UI"""
    progreso = pyqtSignal(int, int)      # (actual, total)
    completado = pyqtSignal(list)        # [rutas_convertidas]
    error = pyqtSignal(str)              # mensaje_error
    cancelado = pyqtSignal()
    
    def __init__(self, rutas_jxl, formato_salida="png", carpeta_salida=None):
        super().__init__()
        self.rutas_jxl = rutas_jxl if isinstance(rutas_jxl, list) else [rutas_jxl]
        self.formato_salida = formato_salida.lower().replace(".", "")
        self.carpeta_salida = carpeta_salida
        self._cancelar = False
        
    def cancelar(self):
        self._cancelar = True
        
    def run(self):
        rutas_convertidas = []
        total = len(self.rutas_jxl)
        decoder = Decoder(parallel=True)
        
        for idx, ruta in enumerate(self.rutas_jxl):
            if self._cancelar:
                self.cancelado.emit()
                return
                
            try:
                # Determinar ruta de salida
                if self.carpeta_salida:
                    nombre = os.path.splitext(os.path.basename(ruta))[0] + f".{self.formato_salida}"
                    ruta_salida = os.path.join(self.carpeta_salida, nombre)
                else:
                    ruta_salida = os.path.splitext(ruta)[0] + f".{self.formato_salida}"
                
                # Leer JXL
                with open(ruta, "rb") as f:
                    datos_jxl = f.read()
                    
                # Decodificar
                info, pixels = decoder(datos_jxl)
                imagen = Image.frombytes(info.mode, (info.width, info.height), pixels)
                
                # Convertir según formato de salida
                if self.formato_salida in ("jpg", "jpeg"):
                    if imagen.mode == "RGBA":
                        fondo = Image.new("RGB", imagen.size, "white")
                        fondo.paste(imagen, mask=imagen.getchannel("A"))
                        imagen = fondo
                    elif imagen.mode != "RGB":
                        imagen = imagen.convert("RGB")
                    imagen.save(ruta_salida, format="JPEG", quality=95, optimize=True)
                else:
                    imagen.save(ruta_salida, format=self.formato_salida.upper())
                    
                rutas_convertidas.append(ruta_salida)
                self.progreso.emit(idx + 1, total)
                
            except Exception as e:
                self.error.emit(f"Error en {os.path.basename(ruta)}: {str(e)}")
                return
                
        self.completado.emit(rutas_convertidas)

# ============================================================
# VENTANA PRINCIPAL
# ============================================================
class JXLConverter(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🖼️ JXL Image Converter - PyQt5")
        self.center_on_screen()

               # Icono
        icon_path = Path.resource_path("Ico\\1.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # ----------------------------------------------------
        # ESTADO INTERNO
        # ----------------------------------------------------
        self.ruta_imagen = None
        self.imagen_pil = None
        self.formato_imagen = None
        self.expand = False
        self.images = []
        self.current_index = 0

        # ----------------------------------------------------
        # FRONT-END
        # ----------------------------------------------------
        self.crear_interfaz()
        self.aplicar_estilo()
        
        # Atajos de teclado
        QShortcut(QKeySequence('F1'), self).activated.connect(self.show_app_info)
        # ESC para cerrar
        QtWidgets.QShortcut(QtGui.QKeySequence(Qt.Key_Escape), self, activated=self.close)

        self.show_app_info()

    ##=========================================================================================

    ## ➜ Metodo para Centrar la App.
    def center_on_screen(self):

        screen = QApplication.primaryScreen().availableGeometry()
        w, h = 900, 700
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2 + 10
        self.setGeometry(x, y, w, h)
    
    ##=========================================================================================

    def show_app_info(self):
        dialog = app_info(self)
        dialog.exec_()
    
    # ========================================================
    # INTERFAZ
    # ========================================================
    def crear_interfaz(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QVBoxLayout(central)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(15)

        # ----------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------

        titulo = QLabel("🖼️ CONVERSOR JPEG-XL")
        titulo.setAlignment(Qt.AlignCenter)

        subtitulo = QLabel(
            "PNG / JPG / JPEG / BMP / TIFF / WEBP  ↔  JXL"
        )
        subtitulo.setAlignment(Qt.AlignCenter)

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(subtitulo)

        # ----------------------------------------------------
        # VISOR
        # ----------------------------------------------------
        self.lbl_imagen = QLabel()

        self.lbl_imagen.setAlignment(Qt.AlignCenter)
        self.lbl_imagen.setMinimumSize(600, 400)

        self.lbl_imagen.setText("🖼️\n\n" "Seleccione una imagen para comenzar")

        layout_principal.addWidget(self.lbl_imagen, 1)

        # ----------------------------------------------------
        # INFORMACIÓN
        # ----------------------------------------------------
        self.lbl_info = QLabel("Sin imagen cargada")
        self.lbl_info.setAlignment( Qt.AlignCenter)

        layout_principal.addWidget(self.lbl_info)

        # ----------------------------------------------------
        # BOTONES
        # ----------------------------------------------------
        botones = QHBoxLayout()

        self.btn_abrir = QPushButton("📂 Abrir Imagen")
        self.btn_a_jxl = QPushButton("➡️ Convertir a JXL")
        self.btn_desde_jxl = QPushButton("⬅️ JXL → PNG/JPG")
        self.btn_limpiar = QPushButton("🗑️ Limpiar")
        
        # Botones navegación
        self.left_button = QPushButton('<', self)
        self.left_button.setStyleSheet("background-color: rgba(0, 0, 0, 150); color: white; border-radius: 25px;")
        self.left_button.setFont(QFont('Arial', 20, QFont.Bold))
        self.left_button.clicked.connect(self.previous_image)
        self.left_button.setFixedSize(50, 50)
        
        self.right_button = QPushButton('>', self)
        self.right_button.setStyleSheet("background-color: rgba(0, 0, 0, 150); color: white; border-radius: 25px;")
        self.right_button.setFont(QFont('Arial', 20, QFont.Bold))
        self.right_button.clicked.connect(self.next_image)
        self.right_button.setFixedSize(50, 50)

        # Botón adicional para modo carpeta
        self.btn_carpeta = QPushButton("📁 Carpeta → JXL")      

        botones.addWidget(self.btn_abrir)
        botones.addWidget(self.btn_a_jxl)
        botones.addWidget(self.btn_carpeta)
        botones.addWidget(self.btn_desde_jxl)
        botones.addWidget(self.btn_limpiar)

        layout_principal.addLayout(botones)

        # ----------------------------------------------------
        # CONEXIONES
        # ----------------------------------------------------
        self.btn_abrir.clicked.connect(self.abrir_imagen)
        self.btn_a_jxl.clicked.connect(self.convertir_a_jxl)
        self.btn_carpeta.clicked.connect(self.convertir_carpeta_a_jxl)
        self.btn_desde_jxl.clicked.connect(self.convertir_desde_jxl)
        self.btn_limpiar.clicked.connect(self.limpiar)

        self.cargar_Banner()

    # ========================================================
    # ABRIR CUALQUIER IMAGEN
    # ========================================================
    def abrir_imagen(self):

        self.expand = False
        self.expand_lbl()
        self.current_index = 0
        self.images.clear()

        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", (
                "Imágenes (*.png *.jpg *.jpeg *.bmp " "*.tif *.tiff *.webp *.gif *.jxl);;"
                "Todos los archivos (*)"))

        fpath, fname = os.path.split(ruta)
        if fpath:
            for f in os.listdir(fpath):
                self.images.append(fpath+'/'+f)

        if not ruta:
            return

        try:
            ruta = self.images[0]
            extension = os.path.splitext(
                ruta
            )[1].lower()

            # ------------------------------------------------
            # JXL
            # ------------------------------------------------
            if extension == ".jxl":

                self.cargar_jxl(ruta)

            # ------------------------------------------------
            # IMÁGENES NORMALES
            # ------------------------------------------------
            else:

                self.cargar_imagen_normal(ruta)

        except Exception as e:

            JXLConverter.show_error(self, "Error", ("No se pudo abrir la imagen:\n\n" f"{e}"))

    # ========================================================
    # CARGAR IMAGEN NORMAL
    #
    # Punto central de entrada para TODAS las imágenes.
    #
    # Pillow se encarga de decodificar:
    #
    # PNG, JPG, JPEG, BMP, TIFF, WEBP, GIF, JXL
	# ========================================================
    def cargar_imagen_normal(self, ruta):

	    with Image.open(ruta) as imagen:
	        imagen.load()

	        if imagen.mode not in ("RGB", "RGBA"):
	            imagen = imagen.convert("RGBA")

	        self.imagen_pil = imagen.copy()

	    self.ruta_imagen = ruta

	    self.formato_imagen = (self.obtener_formato_por_extension(ruta))
	    self.mostrar_imagen(self.imagen_pil)

	    self.actualizar_info()
	    self.mostrar_referencias(ruta, es_jxl=False)

    def convertir_carpeta_a_jxl(self):
        """Convierte todas las imágenes de una carpeta"""
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta con imágenes")
        if not carpeta:
            return
            
        # Buscar imágenes
        extensiones = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.tif", "*.tiff", "*.webp", "*.gif"]
        rutas = []
        for ext in extensiones:
            ### rutas.extend(glob.glob(os.path.join(carpeta, ext)))
            rutas.extend(glob.glob(os.path.join(carpeta, ext.upper())))
            
        if not rutas:
            JXLConverter.show_info(self, "Info", "No se encontraron imágenes en la carpeta")
            return
            
        # Preguntar carpeta de salida
        carpeta_salida = QFileDialog.getExistingDirectory(
            self,
            "Carpeta de salida (Cancelar para misma ubicación)"
        )
        if not carpeta_salida:
            carpeta_salida = None
            
        self._iniciar_conversion_jxl(rutas, carpeta_salida)

	# ========================================================
	# CARGAR JXL
	#
	# IMPORTANTE:
	#
	# NO utilizamos:
	#
	#     Image.open(ruta)
	#
	# porque la versión 1.0.1 del plugin presenta
	# el problema "can't set attribute".
	#
	# Utilizamos directamente:
	#
	#     pillow_jxl.Decoder
	#
	# ========================================================
    def cargar_jxl(self, ruta):

        try:

            print("=" * 60)
            print("CARGANDO JPEG-XL")
            print("=" * 60)

            # ------------------------------------------------
            # Leer archivo JXL
            # ------------------------------------------------
            with open(ruta,"rb") as archivo:
                datos_jxl = archivo.read()

            print("Archivo:", ruta)
            print("Bytes JXL:", len(datos_jxl))

            # ------------------------------------------------
            # Crear decoder
            # ------------------------------------------------
            decoder = Decoder(parallel=True)

            # ------------------------------------------------
            # Decodificar
            #
            # Resultado:
            #
            # info
            # pixels
            # ------------------------------------------------

            info, pixels = decoder(datos_jxl)

            print("JXL decodificado correctamente")
            print("Width:", info.width)
            print("Height:", info.height)
            print("Mode:", info.mode)
            print("Channels:", info.num_channels)
            print("Alpha:", info.has_alpha_channel)
            print("Pixel bytes:", len(pixels))

            # ------------------------------------------------
            # Crear imagen PIL directamente desde RAW
            # ------------------------------------------------

            if info.mode not in ("RGB", "RGBA", "L", "LA"):

                raise ValueError("Modo JXL no soportado: " f"{info.mode}")

            self.imagen_pil = Image.frombytes(info.mode, (info.width, info.height), pixels)

            # ------------------------------------------------
            # Guardar estado
            # ------------------------------------------------
            self.ruta_imagen = ruta
            self.formato_imagen = "JXL"

            # ------------------------------------------------
            # Mostrar
            # ------------------------------------------------
            self.mostrar_imagen(self.imagen_pil)

            # ------------------------------------------------
            # Información
            # ------------------------------------------------
            self.actualizar_info()

            print("Imagen JXL creada correctamente")
            print("=" * 60)

            # Guardamos en Temporales...
            self.mostrar_referencias(ruta, es_jxl=True, datos_jxl=datos_jxl, info_jxl=info)

        except Exception as e:

            print("=" * 60)
            print("ERROR CARGANDO JXL")
            print("=" * 60)

            print(type(e).__name__)
            print(str(e))
            print("=" * 60)

            raise

	# ========================================================
	# OBTENER FORMATO POR EXTENSIÓN
	# ========================================================
    def obtener_formato_por_extension(self, ruta):

	    extension = os.path.splitext(ruta)[1].lower()

	    formatos = {
	        ".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG", ".bmp": "BMP", ".tif": "TIFF",
	        ".tiff": "TIFF", ".webp": "WEBP", ".gif": "GIF", ".jxl": "JXL"}

	    return formatos.get(extension, "Desconocido")

	# ========================================================
	# CONVERTIR A JXL (POR LOTES + THREAD)
    # ========================================================
    def convertir_a_jxl(self):
        """Abre diálogo para seleccionar múltiples imágenes y convertirlas a JXL"""
        if self.imagen_pil is None:
            # Modo por lotes - seleccionar archivos
            rutas, _ = QFileDialog.getOpenFileNames(
                self, 
                "Seleccionar imágenes para convertir a JXL", 
                "", 
                "Imágenes (*.png *.jpg *.jpeg *.bmp *.tif *.tiff *.webp *.gif);;Todos los archivos (*)"
            )
            
            if not rutas:
                return
                
            # Preguntar carpeta de salida
            carpeta_salida = QFileDialog.getExistingDirectory(
                self,
                "Seleccionar carpeta de salida (Cancelar para misma ubicación)"
            )
            if not carpeta_salida:
                carpeta_salida = None  # Misma ubicación que origen
                
            self._iniciar_conversion_jxl(rutas, carpeta_salida)
        else:
            # Modo single - usar imagen cargada
            ruta, _ = QFileDialog.getSaveFileName(
                self, 
                "Guardar imagen JXL", 
                "", 
                "JPEG XL (*.jxl)"
            )
            if not ruta:
                return

            if not ruta.lower().endswith(".jxl"):
                ruta += ".jxl"
            self._iniciar_conversion_jxl([self.ruta_imagen], None, ruta_salida_unica=ruta)
    
    def _iniciar_conversion_jxl(self, rutas, carpeta_salida, ruta_salida_unica=None):
        """Inicia el thread de conversión con diálogo de progreso"""
        total = len(rutas)
        
        # Crear diálogo de progreso
        self.progress_dialog = QProgressDialog(
            f"Convirtiendo imagen 0 de {total}...",
            "Cancelar",
            0,
            total,
            self
        )
        
        # === OCULTAR EL % DE LA BARRA ===
        # Buscar el QProgressBar interno y desactivar texto
        for child in self.progress_dialog.children():
            if isinstance(child, QtWidgets.QProgressBar):
                child.setTextVisible(False)  # <-- SIN PORCENTAJE
                break

        self.progress_dialog.setWindowTitle("🔄 Convirtiendo a JXL...")
        self.progress_dialog.setStyleSheet("""
            QProgressDialog {
                background-color: #1a1a2e;
                border: 2px solid #00c3ff;
                border-radius: 10px;
            }
            
            QProgressDialog QLabel {
                color: #00eaff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                background-color: transparent;
            }
            
            QProgressBar {
                border: 2px solid #00c3ff;
                border-radius: 5px;
                background-color: #0a0a0f;
                text-align: center;
                font-weight: bold;
                font-size: 12px;
                color: #ff0040 !important;  /* <-- Esto fuerza el color del % */
            }
            
            QProgressBar::chunk {
                background-color: qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007c99, 
                    stop:1 #00eaff
                );
                border-radius: 3px;
            }
            
            QPushButton {
                background-color: #101820;
                color: #00eaff;
                border: 2px solid #00c3ff;
                border-radius: 7px;
                padding: 8px 20px;
                font-weight: bold;
                min-width: 80px;
            }
            
            QPushButton:hover {
                background-color: #00c3ff;
                color: #071018;
            }
            
            QPushButton:pressed {
                background-color: #007c99;
            }
        """)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setValue(0)
        
        # Ajustar tamaño mínimo para que se vea mejor
        self.progress_dialog.setMinimumWidth(400)
        self.progress_dialog.setMinimumHeight(150)
        self.progress_dialog.show()
        
        # Crear y configurar worker
        self.worker_jxl = ConvertirAJXLWorker(rutas, carpeta_salida)
        self.worker_jxl.progreso.connect(self._actualizar_progreso)
        self.worker_jxl.completado.connect(self._conversion_completada)
        self.worker_jxl.error.connect(self._conversion_error)
        self.worker_jxl.cancelado.connect(self._conversion_cancelada)
        self.progress_dialog.canceled.connect(self.worker_jxl.cancelar)
        
        # Iniciar
        self.worker_jxl.start()
    
    def _actualizar_progreso(self, actual, total):
        """Actualiza el diálogo de progreso"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.setValue(actual)
            self.progress_dialog.setLabelText(f"Convirtiendo imagen {actual} de {total}...")
            QApplication.processEvents()
    
    def _conversion_completada(self, rutas_convertidas):
        """Maneja la finalización exitosa"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
            
        cantidad = len(rutas_convertidas)
        fpath, fname = os.path.split(rutas_convertidas[0])
        JXLConverter.show_info(
            self, 
            "✅ Conversión completada", 
            f"📌 Se convirtieron {cantidad} imagen(es) correctamente.\n\n"
            f"• Almacendas Exitosamente En: → \n{fpath if fpath else 'N/A'}"
        )

        self.limpiar()
        
    def _conversion_error(self, mensaje):
        """Maneja errores durante la conversión"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
        JXLConverter.show_error(self, "❌ Error de conversión", mensaje)
        
    def _conversion_cancelada(self):
        """Maneja cancelación por el usuario"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
        JXLConverter.show_info(self, "Cancelado", "La conversión fue cancelada.")      

    # ========================================================
    # CONVERTIR DESDE JXL (JXL → PNG/JPG/BMP/TIFF) - POR LOTES + THREAD    #
    # Este método:
    #
    # 1. Abre JXL con Pillow.
    # 2. Lo muestra en el visor.
    # 3. Pregunta dónde guardar.
    # 4. Exporta al formato seleccionado.
	# ========================================================
    def convertir_desde_jxl(self):
        """
        Modo por lotes: Selecciona múltiples JXL y los convierte.
        Mantiene compatibilidad con modo single si hay imagen cargada.
        """
        self.expand = False
        self.expand_lbl()

        # Si hay una imagen JXL cargada, modo single
        if self.imagen_pil is not None and self.formato_imagen == "JXL":
            self._convertir_single_desde_jxl()
            return
            
        # Modo por lotes - seleccionar múltiples archivos
        rutas, _ = QFileDialog.getOpenFileNames(
            self, 
            "Seleccionar imágenes JXL para convertir", 
            "", 
            "JPEG XL (*.jxl)"
        )

        if not rutas:
            return

        # Seleccionar formato de salida con diálogo personalizado
        formato = self._seleccionar_formato_salida()
        if not formato:
            return

        # Preguntar carpeta de salida
        carpeta_salida = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar carpeta de salida (Cancelar para misma ubicación que origen)"
        )
        if not carpeta_salida:
            carpeta_salida = None

        # Iniciar conversión por lotes con thread
        self._iniciar_desconversion_jxl(lista, formato, carpeta_salida)
    
    def _seleccionar_formato_salida(self):
        """Diálogo para seleccionar formato de salida"""
        from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton, QLabel, QPushButton
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Seleccionar formato de salida")
        dialog.setMinimumWidth(300)
        
        # === STYLESheet PARA EL DIÁLOGO ===
        dialog.setStyleSheet("""
            QDialog {
                background-color: #1a1a2e;
                border: 2px solid #00c3ff;
            }
            
            QLabel {
                color: #00eaff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            
            QRadioButton {
                color: white;
                font-size: 13px;
                spacing: 8px;
                padding: 5px;
            }
            
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #00c3ff;
                background-color: #0a0a0f;
            }
            
            QRadioButton::indicator:checked {
                background-color: #00eaff;
                border: 2px solid #00eaff;
            }
            
            QPushButton {
                background-color: #101820;
                color: #00eaff;
                border: 2px solid #00c3ff;
                border-radius: 7px;
                padding: 10px 25px;
                font-weight: bold;
                min-width: 90px;
            }
            
            QPushButton:hover {
                background-color: #00c3ff;
                color: #071018;
            }
            
            QPushButton:pressed {
                background-color: #007c99;                
                color: transparent;  /* <-- EL PORCENTAJE DESAPARECE */
            }
        """)
        
        layout = QVBoxLayout(dialog)
        
        layout.addWidget(QLabel("¿A qué formato deseas convertir?"))
        
        # Grupo de botones
        grupo = QButtonGroup(dialog)
        
        formatos = [
            ("PNG", "png"),
            ("JPEG", "jpg"),
            ("BMP", "bmp"),
            ("TIFF", "tiff")
        ]
        
        seleccion = {"formato": None}
        
        for nombre, ext in formatos:
            rb = QRadioButton(nombre)
            rb.setChecked(ext == "png")  # PNG por defecto
            rb.ext = ext
            grupo.addButton(rb)
            layout.addWidget(rb)
        
        # Botones
        btn_layout = QHBoxLayout()
        btn_aceptar = QPushButton("Aceptar")
        btn_cancelar = QPushButton("Cancelar")
        
        btn_layout.addWidget(btn_aceptar)
        btn_layout.addWidget(btn_cancelar)
        layout.addLayout(btn_layout)
        
        # Conexiones
        def aceptar():
            btn = grupo.checkedButton()
            if btn:
                seleccion["formato"] = btn.ext
            dialog.accept()
            
        def cancelar():
            dialog.reject()
            
        btn_aceptar.clicked.connect(aceptar)
        btn_cancelar.clicked.connect(cancelar)
        
        if dialog.exec_() == QDialog.Accepted:
            return seleccion["formato"]
        return None
    
    def _convertir_single_desde_jxl(self):
        """Modo single: Convierte solo la imagen JXL cargada actualmente"""
        salida, filtro = QFileDialog.getSaveFileName(
            self, 
            "Guardar imagen convertida", 
            "",
            "PNG (*.png);;JPEG (*.jpg *.jpeg);;BMP (*.bmp);;TIFF (*.tiff)"
        )

        if not salida:
            return

        try:
            extension = os.path.splitext(salida)[1].lower()

            # Si el usuario no puso extensión
            if not extension:
                if "PNG" in filtro:
                    salida += ".png"
                    extension = ".png"
                elif "JPEG" in filtro:
                    salida += ".jpg"
                    extension = ".jpg"
                elif "BMP" in filtro:
                    salida += ".bmp"
                    extension = ".bmp"
                elif "TIFF" in filtro:
                    salida += ".tiff"
                    extension = ".tiff"

            imagen_salida = self.imagen_pil

            # JPEG
            if extension in (".jpg", ".jpeg"):
                if imagen_salida.mode == "RGBA":
                    fondo = Image.new("RGB", imagen_salida.size, "white")
                    fondo.paste(imagen_salida, mask=imagen_salida.getchannel("A"))
                    imagen_salida = fondo
                elif imagen_salida.mode != "RGB":
                    imagen_salida = imagen_salida.convert("RGB")
                imagen_salida.save(salida, format="JPEG", quality=95, optimize=True)

            # PNG
            elif extension == ".png":
                imagen_salida.save(salida, format="PNG")

            # BMP
            elif extension == ".bmp":
                if imagen_salida.mode not in ("RGB", "RGBA"):
                    imagen_salida = imagen_salida.convert("RGB")
                imagen_salida.save(salida, format="BMP")

            # TIFF
            elif extension in (".tif", ".tiff"):
                imagen_salida.save(salida, format="TIFF")

            else:
                raise ValueError("Formato de salida no soportado.")

            JXLConverter.show_info(
                self, 
                "✅ Conversión completada",
                f"JXL convertido correctamente.\n\nArchivo:\n{salida}"
            )

        except Exception as e:
            JXLConverter.show_error(
                self, 
                "❌ Error de conversión",
                f"No se pudo guardar la imagen:\n\n{e}"
            )
    
    def _iniciar_desconversion_jxl(self, rutas, formato, carpeta_salida):
        """Inicia el thread de desconversión con diálogo de progreso"""
        total = len(rutas)
        
        # Crear diálogo de progreso
        self.progress_dialog = QProgressDialog(
            f"Desconvirtiendo imagen 0 de {total}...",
            "Cancelar",
            0,
            total,
            self
        )
        
        # === OCULTAR EL % DE LA BARRA ===
        # Buscar el QProgressBar interno y desactivar texto
        for child in self.progress_dialog.children():
            if isinstance(child, QtWidgets.QProgressBar):
                child.setTextVisible(False)  # <-- SIN PORCENTAJE
                break

        self.progress_dialog.setWindowTitle(f"🔄 JXL → {formato.upper()}...")
        self.progress_dialog.setStyleSheet("""
            QProgressDialog {
                background-color: #1a1a2e;
                border: 2px solid #00c3ff;
                border-radius: 10px;
            }
            
            QProgressDialog QLabel {
                color: #00eaff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                background-color: transparent;
            }
            
            QProgressBar {
                border: 2px solid #00c3ff;
                border-radius: 5px;
                background-color: #0a0a0f;
                text-align: center;
                font-weight: bold;
                font-size: 12px;
                color: white;  /* <-- Esto fuerza el color del % */
            }
            
            QProgressBar::chunk {
                background-color: qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007c99, 
                    stop:1 #00eaff
                );
                border-radius: 3px;
            }
            
            QPushButton {
                background-color: #101820;
                color: #00eaff;
                border: 2px solid #00c3ff;
                border-radius: 7px;
                padding: 8px 20px;
                font-weight: bold;
                min-width: 80px;
            }
            
            QPushButton:hover {
                background-color: #00c3ff;
                color: #071018;
            }
            
            QPushButton:pressed {
                background-color: #007c99;
            }
        """)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setValue(0)
        
        # Ajustar tamaño mínimo para que se vea mejor
        self.progress_dialog.setMinimumWidth(400)
        self.progress_dialog.setMinimumHeight(150)
        self.progress_dialog.show()
        
        # Crear y configurar worker
        self.worker_des = ConvertirDesdeJXLWorker(rutas, formato, carpeta_salida)
        self.worker_des.progreso.connect(self._actualizar_progreso_desconversion)
        self.worker_des.completado.connect(self._desconversion_completada)
        self.worker_des.error.connect(self._desconversion_error)
        self.worker_des.cancelado.connect(self._desconversion_cancelada)
        self.progress_dialog.canceled.connect(self.worker_des.cancelar)
        
        # Iniciar
        self.worker_des.start()
    
    def _actualizar_progreso_desconversion(self, actual, total):
        """Actualiza el diálogo de progreso de desconversión"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.setValue(actual)
            self.progress_dialog.setLabelText(
                f"Desconvirtiendo imagen {actual} de {total}..."
            )
            QApplication.processEvents()
    
    def _desconversion_completada(self, rutas_convertidas):
        """Maneja la finalización exitosa de desconversión"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
            
        cantidad = len(rutas_convertidas)
        
        # Mostrar resumen
        mensaje = f"✅ Se desconvirtieron {cantidad} imagen(es) JXL correctamente.\n\n"
        if cantidad <= 3:
            mensaje += "Archivos:\n" + "\n".join(rutas_convertidas)
        else:
            mensaje += f"Primeros 3 archivos:\n"
            mensaje += "\n".join(rutas_convertidas[:3])
            mensaje += f"\n... y {cantidad - 3} más"
            
        JXLConverter.show_info(self, "Conversión completada", mensaje)
        
        # Cargar la primera imagen convertida si existe
        if rutas_convertidas and os.path.exists(rutas_convertidas[0]):
            ### self.cargar_imagen_normal(rutas_convertidas[0])
            self.limpiar()
    
    def _desconversion_error(self, mensaje):
        """Maneja errores durante la desconversión"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
        JXLConverter.show_error(self, "❌ Error de desconversión", mensaje)
        
    def _desconversion_cancelada(self):
        """Maneja cancelación por el usuario"""
        if hasattr(self, 'progress_dialog') and self.progress_dialog:
            self.progress_dialog.close()
        JXLConverter.show_info(self, "Cancelado", "La desconversión fue cancelada.")

    def _crear_progress_dialog(self, titulo, texto_inicial, total):
        """Crea un QProgressDialog estilizado sin porcentaje visible"""
        dialog = QProgressDialog(
            texto_inicial,
            "Cancelar",
            0,
            total,
            self
        )
        dialog.setWindowTitle(titulo)
        
        # Ocultar el % de la barra
        for child in dialog.children():
            if isinstance(child, QtWidgets.QProgressBar):
                child.setTextVisible(False)
                break
        
        # StyleSheet limpio (sin color de texto de barra)
        dialog.setStyleSheet("""
            QProgressDialog {
                background-color: #1a1a2e;
                border: 2px solid #00c3ff;
                border-radius: 10px;
            }
            
            QProgressDialog QLabel {
                color: #00eaff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            
            QProgressBar {
                border: 2px solid #00c3ff;
                border-radius: 5px;
                background-color: #0a0a0f;
                min-height: 22px;
            }
            
            QProgressBar::chunk {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007c99, stop:1 #00eaff
                );
                border-radius: 3px;
            }
            
            QPushButton {
                background-color: #101820;
                color: #00eaff;
                border: 2px solid #00c3ff;
                border-radius: 7px;
                padding: 8px 20px;
                font-weight: bold;
                min-width: 80px;
            }
            
            QPushButton:hover {
                background-color: #00c3ff;
                color: #071018;
            }
        """)
        
        dialog.setWindowModality(Qt.WindowModal)
        dialog.setMinimumDuration(0)
        dialog.setMinimumWidth(400)
        dialog.setValue(0)
        
        return dialog

    # ========================================================
    # MOSTRAR IMAGEN
    #
    # IMPORTANTE:
    #
    # QPixmap NO necesita saber qué es JXL.
    #
    # Pillow decodifica JXL.
    #
    # Pillow → PNG en memoria → QImage → QPixmap
    #
    # No se crea ningún archivo temporal.
	# ========================================================
    def mostrar_imagen(self, imagen):

	    try:
	        # ------------------------------------------------
	        # Asegurar RGB/RGBA
	        # ------------------------------------------------
	        if imagen.mode not in ("RGB", "RGBA"):
	            imagen = imagen.convert("RGBA")

	        # ------------------------------------------------
	        # PIL → PNG EN MEMORIA
	        # ------------------------------------------------
	        buffer = BytesIO()
	        imagen.save(buffer, format="PNG")
	        datos_png = buffer.getvalue()

	        # ------------------------------------------------
	        # PNG → QImage
	        # ------------------------------------------------
	        qimage = QImage()
	        if not qimage.loadFromData(datos_png, "PNG"):
	            raise RuntimeError("Qt no pudo cargar la imagen.")

	        # ------------------------------------------------
	        # QImage → QPixmap
	        # ------------------------------------------------
	        pixmap = QPixmap.fromImage(qimage)
	        if pixmap.isNull():
	            raise RuntimeError("QPixmap produjo una imagen nula.")

	        # ------------------------------------------------
	        # GUARDAR ORIGINAL (sin escalar)
	        # ------------------------------------------------
	        self.pixmap_original = pixmap
	        
	        # ------------------------------------------------
	        # Escalar y mostrar
	        # ------------------------------------------------
	        self._escalar_imagen()

	    except Exception as e:
	        self.lbl_imagen.setText(f"❌ Error mostrando imagen:\n{e}")
	        self.pixmap_original = None

    def _escalar_imagen(self):
	    """
	    Escala la imagen al tamaño actual del label.
	    """
	    if hasattr(self, 'pixmap_original') and self.pixmap_original:
	        pixmap = self.pixmap_original.scaled(
	            self.lbl_imagen.size(),
	            Qt.KeepAspectRatio,
	            Qt.SmoothTransformation
	        )
	        self.lbl_imagen.setPixmap(pixmap)

    def resizeEvent(self, event):
        """
        Se ejecuta automáticamente cuando la ventana cambia de tamaño.
        """
        super().resizeEvent(event)
        self._escalar_imagen()

        self.left_button.move(25, self.height() // 2 - 25)
        self.right_button.move(self.width() - 75, self.height() // 2 - 25)

    # ============================================================
    # NAVEGACIÓN (next/previous)
    # ============================================================
    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            ruta = self.images[self.current_index]
            self.comprovate(ruta)

    def previous_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            ruta = self.images[self.current_index]
            self.comprovate(ruta)

    def comprovate(self, ruta):

        try:

            extension = os.path.splitext(ruta)[1].lower()

            # ------------------------------------------------
            # JXL
            # ------------------------------------------------
            if extension == ".jxl":

                self.cargar_jxl(ruta)

            # ------------------------------------------------
            # IMÁGENES NORMALES
            # ------------------------------------------------
            else:

                self.cargar_imagen_normal(ruta)
                print(ruta)

        except Exception as e:
            self.lbl_imagen.setText(f"❌ Error mostrando imagen:\n{e}")
            self.pixmap_original = None

	# ========================================================
	# MUESTRA REFERENCIAS, DE CUALQUIER IMAGEN...
	# ========================================================
    def mostrar_referencias(self, ruta, es_jxl=False, datos_jxl=None, info_jxl=None, pixels=None):
	    """
	    Muestra referencias detalladas de cualquier imagen en el diálogo TXT_Lec.
	    """
	    import os
	    
	    archivo = ruta
	    tamano_bytes = os.path.getsize(ruta) if os.path.exists(ruta) else 0
	    ancho, alto = self.imagen_pil.size if self.imagen_pil else (0, 0)
	    modo = self.imagen_pil.mode if self.imagen_pil else "Desconocido"
	    formato = self.formato_imagen or "Desconocido"
	    
	    if es_jxl and info_jxl:
	        # Para JXL - usar los datos del decoder
	        pixel_bytes = len(pixels) if pixels else info_jxl.width * info_jxl.height * info_jxl.num_channels
	        
	        text = f'''  • Archivo: {archivo}
	  • Bytes JXL: {len(datos_jxl)}
	  • JXL decodificado correctamente
	  • Width: {info_jxl.width}
	  • Height: {info_jxl.height}
	  • Mode: {info_jxl.mode}
	  • Channels: {info_jxl.num_channels}
	  • Alpha: {info_jxl.has_alpha_channel}
	  • Pixel bytes: {pixel_bytes}'''
	    else:
	        # Para formatos normales
	        canales = {"L": 1, "LA": 2, "RGB": 3, "RGBA": 4}.get(modo, "Desconocido")
	        tiene_alpha = "True" if "A" in modo else "False"
	        pixel_bytes = ancho * alto * (4 if "A" in modo else 3)
	        
	        text = f'''  • Archivo: {archivo}
	  • Formato: {formato}
	  • Tamaño: {tamano_bytes:,} bytes ({tamano_bytes/1024:.2f} KB)
	  • Width: {ancho}
	  • Height: {alto}
	  • Mode: {modo}
	  • Channels: {canales}
	  • Alpha: {tiene_alpha}
	  • Pixel bytes: {pixel_bytes}'''

	    TXT_Lec.Frame_TXT_Lec(self, text)

	# ========================================================
	# INFORMACIÓN
	# ========================================================
    def actualizar_info(self):

	    if self.imagen_pil is None:
	        return

	    ancho, alto = (self.imagen_pil.size)
	    modo = (self.imagen_pil.mode)
	    formato = (self.formato_imagen or "Desconocido")

	    self.lbl_info.setText(f"📐 {ancho} × {alto} px    |    " f"🎨 Modo: {modo}    |    "
	        f"📦 Formato: {formato}")

	# ========================================================
	# LIMPIAR
	# ========================================================
    def limpiar(self):
        self.imagen_pil = None
        self.ruta_imagen = None
        self.formato_imagen = None
        self.pixmap_original = None
        self.current_index = 0
        self.images.clear()
        self.lbl_imagen.clear()
        self.lbl_imagen.setText("")
        self.lbl_info.setText("Sin imagen cargada")

        self.cargar_Banner()

    def cargar_Banner(self):

    	self.expand = True
    	self.expand_lbl()

    	image_path = Path.resource_path("Ico\\Banner.png")
    	pixmap = QPixmap(image_path)
    	pixmap = pixmap.scaled(850, 570, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    	self.lbl_imagen.setPixmap(pixmap)
    	self.lbl_imagen.setAlignment(Qt.AlignCenter)

    def expand_lbl(self):

    	if self.expand == True:
    		self.lbl_imagen.setScaledContents(self.expand)

    	elif self.expand == False:
    		self.lbl_imagen.setScaledContents(self.expand)

    # ========================================================
    # ESTILO
    # ========================================================
    def aplicar_estilo(self):

        self.setStyleSheet("""

        QMainWindow {
            background-color: #0a0a0f;
        }

        QLabel {
            color: #d0d0d0;
        }

        QPushButton {
            background-color: #101820;
            color: #00eaff;
            border: 2px solid #00c3ff;
            border-radius: 7px;
            padding: 10px 18px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #00c3ff;
            color: #071018;
        }

        QPushButton:pressed {
            background-color: #007c99;
        }

        """)

    # =========================
    # MENSAJES
    # =========================
    def show_info(self, titulo, texto):
        msg = QMessageBox(self)

        msg.setWindowTitle(titulo)
        msg.setText(texto)

        msg.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
            }

            QLabel {
                color: white;
            }

            QPushButton {
                background-color: #444;
                color: white;
                padding: 6px;
            }
        """)

        msg.exec_()

    # =========================
    # MENSAJE ERROR
    # =========================
    def show_error(self, titulo, texto):

        msg = QMessageBox(self)

        msg.setWindowTitle(titulo)
        msg.setText(texto)

        msg.setIcon(QMessageBox.Critical)

        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        msg.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
            }

            QLabel {
                color: white;
            }

            QPushButton {
                background-color: #444;
                color: white;
                padding: 6px;
            }
        """)

        msg.exec_()

##====================================================================================
##====================================================================================

class TXT_Lec(JXLConverter):

    def __init__(self, parent=None):
        super().__init__(parent)

    def Frame_TXT_Lec(self, text):
        dialog = QDialog(self)
        dialog.setWindowTitle("Contenido del Archivo")
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        dialog.setLayout(layout)

        label = QLabel('Imagen cargada correctamente: ...')
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('''
            QLabel{
                background-color: #0a0a0a;
                color: #00ff41;
                font-size: 18px;
            }
            ''')
        layout.addWidget(label)

        self.font_txt = QtGui.QFont("Courier New")
        self.font_txt.setPointSize(6)
        self.font_txt.setBold(True)
        self.font_txt.setWeight(200)

        self.editor = QPlainTextEdit()
        self.editor.setFixedSize(600, 300)
        self.editor.setStyleSheet('''
            QPlainTextEdit{
                background-color: #0a0a0a;
                color: #00ff41;
                font-size: 20px;
            }
            ''')

        self.editor.setReadOnly(True)
        self.editor.setFont(self.font_txt)
        ##self.editor.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)

        layout.addWidget(self.editor)

        # >>> SOLUCIÓN: Ajustar al contenido y bloquear <<<
        dialog.adjustSize()
        dialog.setFixedSize(dialog.size())

        try:
            print(text)
            self.editor.setPlainText(text)
        except Exception as e:
            print(e)

        dialog.exec_()

##====================================================================================
# Diálogo de información
##====================================================================================
class app_info(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("✨ JXL Image Converter ✨")
        self.setFixedSize(600, 500)
        self.setModal(True)
        
        icon_path = ":/imagenes/Resources/1.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        title = QLabel("✨ JXL Image Converter ✨")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #00c3ff;
            }
        """)
        layout.addWidget(title)
        
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setText('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              🖼️ JXL Image Converter 🖼️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Desarrollado por: 👉 Cristian M. Veliz Cano ✔
Versión del Soft: 👉 V-03
Nombre del Soft: ✨ JXL Image Converter ✨
Lenguaje: 👉 Python 3.8.3
Interfaz Gráfica: 👉 PyQt5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          ✨ CONVERSOR DE IMÁGENES JPEG-XL ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Este Software ha sido desarrollado como una
herramienta sencilla, minimalista y práctica para
trabajar con imágenes en formato JPEG-XL (.JXL).

El programa permite visualizar imágenes y realizar
conversiones entre JPEG-XL y diferentes formatos
de imagen convencionales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 FORMATOS COMPATIBLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software permite ingresar imágenes en los
siguientes formatos:

    • PNG
    • JPG
    • JPEG
    • BMP
    • TIFF
    • WEBP
    • GIF
    • JXL / JPEG-XL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ➡️ CONVERSIÓN HACIA JXL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software permite convertir una imagen cargada
a formato JPEG-XL (.JXL).

Formatos de entrada:

    • PNG
    • JPG
    • JPEG
    • BMP
    • TIFF
    • WEBP
    • GIF

La conversión hacia JPEG-XL se realiza utilizando
compresión LOSSLESS (sin pérdida).

Esto permite conservar los datos de imagen sin
aplicar una pérdida de calidad intencional durante
la conversión.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ⬅️ CONVERSIÓN DESDE JXL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Las imágenes JPEG-XL (.JXL) pueden ser abiertas
y posteriormente convertidas a:

    • PNG
    • JPEG / JPG
    • BMP
    • TIFF

El usuario puede seleccionar el formato de salida
desde el cuadro de diálogo de guardado.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 🖼️ VISUALIZADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software incorpora un visor integrado que permite
mostrar la imagen cargada directamente dentro de la
ventana principal.

En el caso de JPEG-XL, el archivo es decodificado
mediante el módulo especializado:

    pillow_jxl

Los datos de imagen JPEG-XL son convertidos en una
imagen compatible con Pillow y posteriormente son
enviados al sistema gráfico de Qt para su
visualización.

El proceso de visualización se realiza en memoria,
sin necesidad de crear un archivo PNG temporal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              🔧 MOTOR DE PROCESAMIENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El procesamiento de imágenes se realiza mediante:

    • Python
    • Pillow
    • pillow-jxl
    • PyQt5

Pillow se utiliza para trabajar con los formatos
de imagen convencionales.

JPEG-XL utiliza el Decoder proporcionado por
pillow_jxl para realizar la decodificación del
formato JXL.

La imagen resultante es posteriormente transformada
para ser mostrada mediante QImage y QPixmap.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              📐 INFORMACIÓN DE IMAGEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Al cargar una imagen, el Software muestra
información básica sobre ella:

    • Ancho de la imagen
    • Alto de la imagen
    • Modo de color
    • Formato de imagen

Ejemplo:

    📐 1280 × 1024 px
    🎨 Modo: RGB
    📦 Formato: JXL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 🧹 LIMPIAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

La opción:

    🗑️ Limpiar

permite eliminar de la interfaz la imagen
actualmente cargada y restablecer el visor a su
estado inicial.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ⚙️ FUNCIONAMIENTO GENERAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El funcionamiento básico del Software es:

    1️⃣ Seleccionar una imagen.

    2️⃣ El Software identifica el formato.

    3️⃣ La imagen es cargada y procesada.

    4️⃣ La imagen es mostrada en el visor.

    5️⃣ Se presenta información básica de la imagen.

    6️⃣ El usuario puede convertirla a JPEG-XL.

    7️⃣ También puede abrir un JPEG-XL existente.

    8️⃣ Un archivo JXL puede ser convertido nuevamente
       a PNG, JPEG, BMP o TIFF.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             💾 PROCESAMIENTO EN MEMORIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Para la visualización de JPEG-XL, el Software
utiliza un proceso interno de decodificación.

El archivo .JXL es leído y convertido a datos de
píxeles mediante el Decoder de pillow_jxl.

Posteriormente, estos datos son reconstruidos como
una imagen de Pillow.

Finalmente:

    JXL
     ↓
    Decoder
     ↓
    Datos de píxeles
     ↓
    PIL.Image
     ↓
    PNG en memoria
     ↓
    QImage
     ↓
    QPixmap
     ↓
    Visor

No es necesario generar un archivo intermedio en
el disco solamente para visualizar la imagen.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                🖥️ INTERFAZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Software posee una interfaz gráfica minimalista
desarrollada con PyQt5.

Cuenta con:

    • Visor de imágenes
    • Información de la imagen
    • Selector de archivos
    • Conversión hacia JXL
    • Conversión desde JXL
    • Botón para limpiar el visor

Su diseño está orientado a mantener un entorno
simple y fácil de utilizar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   📌 OBJETIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El objetivo principal de este Software es ofrecer
una herramienta sencilla para experimentar,
visualizar y convertir imágenes utilizando el
formato moderno JPEG-XL.

JPEG-XL está diseñado como un formato de imagen
moderno que puede utilizarse tanto para imágenes
con compresión sin pérdida como para otros escenarios
de compresión.

Este Software se enfoca principalmente en:

    🖼️ Visualización
    🔄 Conversión
    📦 Manejo de archivos JXL
    🧪 Experimentación con JPEG-XL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               🛠️ CARACTERÍSTICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Interfaz gráfica.

✅ Visor integrado.

✅ Soporte para JPEG-XL.

✅ Conversión hacia JXL.

✅ Conversión desde JXL.

✅ Conversión LOSSLESS hacia JPEG-XL.

✅ Soporte para PNG.

✅ Soporte para JPG/JPEG.

✅ Soporte para BMP.

✅ Soporte para TIFF.

✅ Soporte para WEBP.

✅ Soporte para GIF.

✅ Información básica de imagen.

✅ Visualización de JXL mediante decodificación
   directa en memoria.

✅ Sin necesidad de archivos temporales para
   visualizar JXL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 📚 CARÁCTER DEL SOFTWARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Software de carácter:

    • Gratuito
    • Didáctico
    • Experimental
    • Minimalista
    • Free-Code
    • Open-Source

Desarrollado con fines educativos y prácticos,
permitiendo experimentar con el procesamiento,
visualización y conversión de imágenes JPEG-XL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos del Teclado:

📎 F1
• Para mostrar información del software.

📎 ESC
• Cierra inmediatamente el Soft-Ware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    📌 LICENCIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita, a cualquier
persona que obtenga una copia de este software y de
los archivos de documentación asociados, para utilizar
el Software sin restricción, incluyendo sin limitación
los derechos de uso, copia, modificación, fusión,
publicación, distribución, sublicencia y/o venta de
copias del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              🖼️ JXL Image Converter 🖼️

      Una herramienta sencilla para trabajar
             con imágenes JPEG-XL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ''')
        
        info_text.setStyleSheet("""
            QTextEdit {
                background-color: #111118;
                color: #F1F1F1;
                border: 1px solid #00c3ff;
                border-radius: 5px;
                padding: 8px;
                font-size: 10pt;
            }
        """)
        layout.addWidget(info_text)
        
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)
        close_button.setFixedHeight(32)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #1a1a2e;
                color: white;
                border: 1px solid #00c3ff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #00c3ff;
                color: black;
            }
        """)
        layout.addWidget(close_button)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

	app = QApplication(sys.argv)

	ventana = JXLConverter()
	ventana.show()

	sys.exit(app.exec_())