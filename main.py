import sys

import requests
from PySide2.QtCore import Slot, QDate
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_lista import Ui_ListWindow

from Persona import Persona
from ui_principal import Ui_MainWindow
from ventana_lista import ListWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.le_fecha_registro.setDate(QDate().currentDate())
        self.init_provincias()
        self.personas = []
        self.list_window = ListWindow()

        if len(self.personas):
            self.list_window.show()
            for persona in self.personas:
                self.list_window.agregar_row(persona)



        def closeEvent(self, event):
        self.settings = QSettings('Demolandico', 'CovidHelper')
        geometry = self.settings.value('geometryMain', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        super(MainWindow, self).closeEvent(event)

        def closeEvent(self, event):
        geometry = self.setValue('geometryList', geometry)
        self.list_window.close()
        super(MainWindow, self).closeEvent(event)

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
        persona = Persona(
            self.ui.le.dni.text(),
            self.ui.le_nombre.text(),
            self.ui.le_edad.text(),
            self.ui.le_apellido.text(),
            self.ui.le_fecha_registro.text(),
            self.ui.cb_sexo,
            self.ui.cb_provincia,
        )
        print(persona)
        self.personas.append(persona)
        self.clear_all()
        self.list_window.agregar_row(persona)
    else:
        message = QMessageBox().warning(self, "datos faltantes", "faltan datos para continuar")

        def save_file(self):
            with open("personas.vector","w") as pickle_file:
                pickle.dump(self.personas, pickle_file)

        def reaf_file
            personas = []
            with open("personas.vector", "rb") as pickle_file:
                personas = pickle.load(pickle_file)
            return personas

        def closeEvent(self, event):
            geometry = self.saveGeometry()
            self.settings.setValue('geometryMain', geometry)
            self.list_window.close()
            super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    principal = MainWindow()
    principal.show()

    sys.exit(app.exec_())
