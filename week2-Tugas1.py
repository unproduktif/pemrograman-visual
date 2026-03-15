# NAMA  : DODI WIJAYA
# NIM   : F1D02310047
# KELAS : PEMROGRAMAN VISUAL D


import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox
)


class FormBiodata(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setGeometry(300, 300, 380, 420)
        

        self.setStyleSheet("""
        QWidget{
            background:#f1f2f4;
            font-family:Segoe UI;
            font-size:14px;
        }

        QLabel{
            color:#333;
        }

        QLineEdit{
            padding:8px;
            border:1px solid #4CAF50;
            border-radius:6px;
            background:#dce8d9;
            color:black;
        }

        QComboBox{
            padding:8px;
            border:1px solid #ccc;
            border-radius:6px;
            background:white;
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
        """)

        self.label_nama = QLabel("Nama Lengkap:")
        self.nama = QLineEdit()
        self.nama.setPlaceholderText("Masukkan Nama")

        self.label_nim = QLabel("NIM:")
        self.nim = QLineEdit()
        self.nim.setPlaceholderText("Masukkan NIM")

        self.label_kelas = QLabel("Kelas:")
        self.kelas = QLineEdit()
        self.kelas.setPlaceholderText("Contoh: TI-2A")

        self.label_gender = QLabel("Jenis Kelamin:")
        self.gender = QComboBox()
        self.gender.addItems(["Laki-laki", "Perempuan"])
        self.gender.setStyleSheet("""
            color:#7f8c8d;
        """)

        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        self.btn_reset.setStyleSheet("""
        QPushButton{
            background:#7f8c8d;
            color:white;
            border:none;
            padding:10px;
            border-radius:6px;
        }
        QPushButton:hover{
            background:#6c7a7a;
        }
        """)

        self.hasil_container = QWidget()
        hasil_layout = QVBoxLayout(self.hasil_container)
        hasil_layout.setContentsMargins(0,0,0,0)
        self.hasil = QLabel("")
        self.hasil.setWordWrap(True)
        self.hasil.setMinimumHeight(120)
        hasil_layout.addWidget(self.hasil)

        self.hasil_container.hide()
        self.hasil.setStyleSheet("""
        background:#cfe3d4;
        border-left:5px solid #2ecc71;
        padding:12px;
        border-radius:8px;
        color:#1f4f30;
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20,15,20,15)

        layout.addWidget(self.label_nama)
        layout.addWidget(self.nama)

        layout.addWidget(self.label_nim)
        layout.addWidget(self.nim)

        layout.addWidget(self.label_kelas)
        layout.addWidget(self.kelas)

        layout.addWidget(self.label_gender)
        layout.addWidget(self.gender)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        btn_layout.addWidget(self.btn_tampil)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)
        layout.addWidget(self.hasil_container)

        self.setLayout(layout)

        self.btn_tampil.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_form)

    def tampilkan_data(self):

        nama = self.nama.text()
        nim = self.nim.text()
        kelas = self.kelas.text()
        gender = self.gender.currentText()

        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Error", "Semua field harus diisi")
            return

        self.hasil.setText(f"""
        <b>DATA BIODATA</b><br><br>
        Nama: {nama}<br>
        NIM: {nim}<br>
        Kelas: {kelas}<br>
        Jenis Kelamin: {gender}
        """)

        self.hasil_container.show()

    def reset_form(self):

        self.nama.clear()
        self.nim.clear()
        self.kelas.clear()
        self.gender.setCurrentIndex(0)
        self.hasil.setText("")
        self.hasil_container.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())