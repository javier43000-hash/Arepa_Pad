import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, 
                             QGraphicsDropShadowEffect, QPushButton)
from PyQt5.QtGui import QPixmap, QColor, QRegion, QFont
from PyQt5.QtCore import Qt

class ArepaPad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArepaPad: El Relleno")
        self.setFixedSize(600, 600)

        # --- Fondo de la Arepa ---
        self.fondo = QLabel(self)
        ruta_fondo = "C:/Arepa_Pad/arepa_pad.jpg"
        if os.path.exists(ruta_fondo):
            pixmap = QPixmap(ruta_fondo)
            self.fondo.setPixmap(pixmap)
        else:
            self.fondo.setStyleSheet("background-color: #F4D03F;")
        
        self.fondo.setScaledContents(True)
        self.fondo.resize(600, 600)

        # --- El "Relleno" (Editor de Texto) ---
        self.editor = QTextEdit(self)
        self.editor.resize(360, 360)
        self.editor.move(120, 120)

        # Máscara circular
        region = QRegion(0, 0, 360, 360, QRegion.Ellipse)
        self.editor.setMask(region)

        # ESTILO CORREGIDO (Línea 40 aproximada)
        # IMPORTANTE: Nota las tres comillas al principio y al final
        self.editor.setStyleSheet("""
            QTextEdit {
                background: rgba(60, 40, 20, 100); 
                color: #FFFFFF;
                font-size: 19px;
                font-weight: bold;
                border: none;
                padding-left: 50px;
                padding-right: 50px;
                padding-top: 90px;
            }
        """)
        
        self.editor.setPlaceholderText("\n\n\nEscribe el relleno aquí...")
        self.editor.setAlignment(Qt.AlignCenter)
        
        # Sombra
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(40)
        sombra.setColor(QColor(0, 0, 0, 200))
        self.editor.setGraphicsEffect(sombra)

        # --- Botón Guardar ---
        self.btn_guardar = QPushButton("💾 Guardar Receta", self)
        self.btn_guardar.setGeometry(225, 530, 150, 40)
        self.btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: #E67E22;
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #D35400; }
        """)
        self.btn_guardar.clicked.connect(self.guardar_texto)

    def guardar_texto(self):
        contenido = self.editor.toPlainText()
        try:
            with open("C:/Arepa_Pad/mi_relleno.txt", "w", encoding="utf-8") as f:
                f.write(contenido)
            print("¡Relleno guardado!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Comic Sans MS", 12))
    gui = ArepaPad()
    gui.show()
    sys.exit(app.exec_())