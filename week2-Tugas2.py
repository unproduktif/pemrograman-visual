# NAMA  : DODI WIJAYA
# NIM   : F1D02310047
# KELAS : PEMROGRAMAN VISUAL D


import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt


class KonversiSuhu(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Konversi Suhu")
        self.setGeometry(300, 300, 380, 350)

        self.setStyleSheet("""
        QWidget{
            background:#f1f2f4;
            font-family:Segoe UI;
            font-size:14px;
        }

        QLineEdit{
            padding:8px;
            border:1px solid #4CAF50;
            border-radius:6px;
            background:#dce8d9;
            color:black;
        }

        QPushButton{
            background:#3b8ec2;
            color:white;
            border:none;
            padding:10px;
            border-radius:6px;
        }

        QPushButton:hover{
            background:#2f7cb0;
        }

        QPushButton:pressed{
            background:#1f6391;
        }
        """)

        self.judul = QLabel("KONVERSI SUHU")
        self.judul.setAlignment(Qt.AlignCenter)
        self.judul.setFixedHeight(48)
        self.judul.setStyleSheet("""
        background:#3b8ec2;
        color:white;
        font-size:16px;
        font-weight:bold;
        padding:12px;
        border-radius:8px;
        """)

        self.label_input = QLabel("Masukkan Suhu (Celsius):")
        self.label_input.setFixedHeight(30)
        self.label_input.setAlignment(Qt.AlignBottom)
        self.label_input.setStyleSheet("""
        color:black;
        """)

        self.input_celsius = QLineEdit()

        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")

        self.label_hasil = QLabel(
            "<b>Hasil Konversi:</b>\n\n"
        )
        self.label_hasil.setAlignment(Qt.AlignTop)
        self.label_hasil.setStyleSheet("""
        background:#c9d9ea;
        border-left:5px solid #1f4f82;
        padding:12px;
        border-radius:8px;
        color:#123a63;
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20,15,20,15)

        layout.addWidget(self.judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_celsius)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        btn_layout.addWidget(self.btn_fahrenheit)
        btn_layout.addWidget(self.btn_kelvin)
        btn_layout.addWidget(self.btn_reamur)

        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

        self.btn_fahrenheit.clicked.connect(self.ke_fahrenheit)
        self.btn_kelvin.clicked.connect(self.ke_kelvin)
        self.btn_reamur.clicked.connect(self.ke_reamur)

    def ambil_celsius(self):
        try:
            return float(self.input_celsius.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus berupa angka")
            return None

    def tampilkan_hasil(self, text):
        self.label_hasil.setText(
            f"<b>Hasil Konversi:</b><br><br>{text}"
        )

    def ke_fahrenheit(self):
        c = self.ambil_celsius()
        if c is None:
            return
        f = (c * 9/5) + 32

        if c.is_integer():
            c = int(c)

        self.tampilkan_hasil(f"{c} Celsius = {f:.2f} Fahrenheit")

    def ke_kelvin(self):
        c = self.ambil_celsius()
        if c is None:
            return
        k = c + 273.15

        if c.is_integer():
            c = int(c)

        self.tampilkan_hasil(f"{c} Celsius = {k:.2f} Kelvin")

    def ke_reamur(self):
        c = self.ambil_celsius()
        if c is None:
            return
        r = c * 4/5

        if c.is_integer():
            c = int(c)
            
        self.tampilkan_hasil(f"{c} Celsius = {r:.2f} Reamur")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())