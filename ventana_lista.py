from ui_lista import Ui_ListWindow
from PySide2.QtWidgets import QMainWindow

class ListWindow(QMainWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.ui = Ui_ListWindow()
        self.ui.setupUi(self)

        self.settings = QSettings("demolandico", "covidHelper")
        geometry = self.settings.value("geometryList", bytes ("","utf-8"))
        self.restoreGeometry(geometry)

def agregar_row(self, persona):
    row_position = self.list_window.ui.tb_covid.rowCount()
    self.list_window.ui.tb_covid.insertRow(row_position)
    self.list_window.ui.tb_covid.SetItem(row_position, 0, QtWidgets.QTableWidgetItem(persona.dni))
    self.list_window.ui.tb_covid.SetItem(row_position, 1, QtWidgets.QTableWidgetItem(persona.nombre))
    self.list_window.ui.tb_covid.SetItem(row_position, 2, QtWidgets.QTableWidgetItem(persona.apellido))
    self.list_window.ui.tb_covid.SetItem(row_position, 3, QtWidgets.QTableWidgetItem(persona.fecha.toString()))

def closeEvent(self, event):
    geometry = self.saveGeometry()
    self.settings.setValue("geometryList", geometry)
    super(ListWindow, self).closeEvent(event)