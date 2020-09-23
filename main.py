import sys

import requests
from PySide2.QtCore import Slot, QDate
from PySide2.QtWidgets import QMainWindow, QApplication

from ui_principal import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.le_fecha_registro.setDate(QDate().currentDate())
        self.init_provincias()

    def init_provincias(self):
        url = "https://apis.datos.gob.ar/georef/api/provincias?orden=nombre&campos=nombre"
        provinces = requests.get(url).json()["provincias"]
        for i, province in enumerate(provinces):
            province_name = province["nombre"]
            self.ui.cb_provincia.addItem(province_name)
            self.ui.cb_provincia.setItemText(i, province_name)

    @Slot()
    def clear_all(self):
        self.ui.le_dni.setText("")
        self.ui.le_apellido.setText("")
        self.ui.le_edad.setText("")
        self.ui.le_nombre.setText("")
        self.ui.cb_provincia.setCurrentIndex(0)
        self.ui.cb_sexo.setCurrentIndex(0)
        self.ui.le_fecha_registro.setDate(QDate().currentDate())

    @Slot()
    def register(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    principal = MainWindow()
    principal.show()

    sys.exit(app.exec_())
