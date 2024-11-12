import tkinter as tk
from model.EncuestaModel import EncuestaModelo
from view.EncuestaView import EncuestaVista

class EncuestaController:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = EncuestaModelo()
        self.vista = EncuestaVista(self.root, self)

    def ejecutar(self):
        try:
            self.root.mainloop()
        finally:
            self.modelo.cerrar_conexion()

    def crear_encuesta(self, datos):
        self.modelo.crear_encuesta(datos)

    def leer_encuestas(self):
        return self.modelo.leer_encuestas()

    def actualizar_encuesta(self, idEncuesta, campo, nuevo_valor):
        self.modelo.actualizar_encuesta(idEncuesta, campo, nuevo_valor)

    def eliminar_encuesta(self, idEncuesta):
        self.modelo.eliminar_encuesta(idEncuesta)

    def consultar_encuestas(self, orden=None, filtro=None):
        return self.modelo.consultar_encuestas(orden, filtro)