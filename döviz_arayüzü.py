import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import *

class Pencere(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = QLabel("Döviz Seç:")

        self.altin = QRadioButton("Altın")
        self.dolar = QRadioButton("Dolar")
        self.euro = QRadioButton("Euro")
        self.borsa = QRadioButton("Borsa")

        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Seç")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.altin)
        v_box.addWidget(self.dolar)
        v_box.addWidget(self.euro)
        v_box.addWidget(self.borsa)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.altin.isChecked(),self.dolar.isChecked(),self.euro.isChecked(),self.borsa.isChecked(),self.yazi_alani))

        self.setWindowTitle("Döviz Arayüzü")
        self.setGeometry(100,100,300,300)
        self.show()

    def click(self,altin,dolar,euro,borsa,yazi_alani):

        url = "https://www.doviz.com/"

        respone = requests.get(url)

        html_icerigi = respone.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        doviz = soup.find_all("span", {"class": "name"})
        deger = soup.find_all("span", {"class": "value"})

        if altin:
            for altin,degeri in zip(doviz,deger):
                altin = altin.text
                degeri = degeri.text

                if altin in "GRAM ALTIN" and "gram":
                    yazi_alani.setText(altin + ": " + degeri + " TL")

        if dolar:
            for dolar,degeri in zip(doviz,deger):
                dolar = dolar.text
                degeri = degeri.text

                if dolar in "DOLAR" and "USD":
                    yazi_alani.setText(dolar + ": " + degeri + " TL")

        if euro:
            for euro,degeri in zip(doviz,deger):
                euro = euro.text
                degeri = degeri.text

                if euro in "EURO" and "EUR":
                    yazi_alani.setText(euro + ": " + degeri + " TL")

        if borsa:
            for borsa,degeri in zip(doviz,deger):
                borsa = borsa.text
                degeri = degeri.text

                if borsa in "BIST 100" and "XU100":
                    yazi_alani.setText(borsa + ": " + degeri + " TL")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
