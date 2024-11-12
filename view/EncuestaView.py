import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class EncuestaVista:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Encuesta CRUD")
        self.root.geometry("1300x600")
        self.root.config(bg="#f4f4f4")  # Fondo gris suave
        self.create_widgets() # Crear los widgets de la interfaz
        self.mostrar_encuestas() # Mostrar todas las encuestas al iniciar la aplicación

    def create_widgets(self):
        # Marco para los filtros y ordenación
        self.filter_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.filter_frame.pack(pady=10, fill=tk.X)

        tk.Label(self.filter_frame, text="Ordenar por:", bg="#f4f4f4").pack(side=tk.LEFT, padx=5)
        self.order_var = tk.StringVar()
        self.order_menu = ttk.Combobox(self.filter_frame, textvariable=self.order_var)
        self.order_menu['values'] = ("Id", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                                     "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                                     "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza")
        self.order_menu.current(0)
        self.order_menu.pack(side=tk.LEFT, padx=5)

        tk.Label(self.filter_frame, text="Filtro:", bg="#f4f4f4").pack(side=tk.LEFT, padx=5)
        self.filter_var = tk.StringVar()
        self.filter_menu = ttk.Combobox(self.filter_frame, textvariable=self.filter_var)
        self.filter_menu['values'] = (
            "ninguno", "Tension alta (si)", "Problemas digestivos (si)", "Dependencia (si)", "Hombres (hombre)",
            "Mujeres (mujer)")
        self.filter_menu.current(0)  # Set "ninguno" as the default value
        self.filter_menu.pack(side=tk.LEFT, padx=5)

        self.filter_button = tk.Button(self.filter_frame, text="Aplicar", command=self.aplicar_filtro,
                                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.filter_button.pack(side=tk.LEFT, padx=5)

        # Marco para la tabla
        self.table_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.table_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Tabla para mostrar las encuestas
        self.tree = ttk.Treeview(self.table_frame, columns=("ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana",
                                                            "BebidasFinSemana", "BebidasDestiladasSemana",
                                                            "VinosSemana",
                                                            "PerdidasControl", "DiversionDependenciaAlcohol",
                                                            "ProblemasDigestivos", "TensionAlta", "DolorCabeza"),show='headings')
        # Personalizar encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("BebidasSemana", text="Bebidas por Semana")
        self.tree.heading("CervezasSemana", text="Cervezas por Semana")
        self.tree.heading("BebidasFinSemana", text="Bebidas Fin de Semana")
        self.tree.heading("BebidasDestiladasSemana", text="Bebidas Destiladas por Semana")
        self.tree.heading("VinosSemana", text="Vinos por Semana")
        self.tree.heading("PerdidasControl", text="Pérdidas de Control")
        self.tree.heading("DiversionDependenciaAlcohol", text="Diversión Dependencia Alcohol")
        self.tree.heading("ProblemasDigestivos", text="Problemas Digestivos")
        self.tree.heading("TensionAlta", text="Tensión Alta")
        self.tree.heading("DolorCabeza", text="Dolor de Cabeza")

        # Agregar barras de desplazamiento
        self.scrollbar_y = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = ttk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.scrollbar_x.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Marco para el menú de acciones
        self.menu_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.menu_frame.pack(pady=20, fill=tk.X)

        # Botones de menú
        self.create_button = tk.Button(self.menu_frame, text="Crear nueva encuesta",
                                       command=self.solicitar_datos_encuesta,
                                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.create_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.update_button = tk.Button(self.menu_frame, text="Actualizar encuesta",
                                       command=self.solicitar_actualizacion,
                                       bg="#FFC107", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.update_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.delete_button = tk.Button(self.menu_frame, text="Eliminar encuesta", command=self.solicitar_eliminacion,
                                       bg="#F44336", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.exit_button = tk.Button(self.menu_frame, text="Salir", command=self.root.quit,
                                     bg="#9E9E9E", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Botones para mostrar gráficos
        self.graph_button1 = tk.Button(self.menu_frame, text="Gráfico Alta Frecuencia",
                                       command=self.mostrar_grafico_alta_frecuencia,
                                       bg="#FF5722", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.graph_button1.pack(side=tk.LEFT, padx=10, pady=5)

        self.graph_button2 = tk.Button(self.menu_frame, text="Gráfico Perdidas Control",
                                       command=self.mostrar_grafico_perdidas_control,
                                       bg="#FF5722", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.graph_button2.pack(side=tk.LEFT, padx=10, pady=5)

        self.graph_button3 = tk.Button(self.menu_frame, text="Gráfico Problemas Salud",
                                       command=self.mostrar_grafico_problemas_salud,
                                       bg="#FF5722", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.graph_button3.pack(side=tk.LEFT, padx=10, pady=5)

    def mostrar_grafico_alta_frecuencia(self):
        encuestas = self.controller.consultar_encuestas(filtro="BebidasSemana > 10")
        edades = [encuesta[1] for encuesta in encuestas]
        bebidas_semana = [encuesta[3] for encuesta in encuestas]

        fig, ax = plt.subplots()
        ax.bar(edades, bebidas_semana)
        ax.set_xlabel('Edad')
        ax.set_ylabel('Bebidas por Semana')
        ax.set_title('Alta Frecuencia de Consumo de Alcohol')

        graph_window = tk.Toplevel(self.root)
        graph_window.title("Gráfico Alta Frecuencia de Consumo de Alcohol")
        graph_window.geometry("800x600")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def mostrar_grafico_perdidas_control(self):
        encuestas = self.controller.consultar_encuestas(filtro="PerdidasControl > 3")
        total_encuestas = self.controller.leer_encuestas()
        sizes = [len(encuestas), len(total_encuestas) - len(encuestas)]
        labels = ['Perdidas Control > 3', 'Otros']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Perdidas de Control por Consumo de Alcohol')

        graph_window = tk.Toplevel(self.root)
        graph_window.title("Gráfico Perdidas de Control")
        graph_window.geometry("800x600")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def mostrar_grafico_problemas_salud(self):
        encuestas = self.controller.consultar_encuestas(
            filtro="DolorCabeza = 'si' OR TensionAlta = 'si' OR ProblemasDigestivos = 'si'")
        total_encuestas = self.controller.leer_encuestas()
        problemas_salud = len(encuestas)
        sin_problemas_salud = len(total_encuestas) - problemas_salud
        labels = ['Sin Problemas de Salud', 'Con Problemas de Salud']
        sizes = [sin_problemas_salud, problemas_salud]
        colors = ['blue', 'red']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        ax.set_title('Distribución de Problemas de Salud')

        graph_window = tk.Toplevel(self.root)
        graph_window.title("Gráfico Problemas de Salud")
        graph_window.geometry("800x600")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def aplicar_filtro(self):
        orden = self.order_var.get()
        if orden == "Id":
            orden = None
        filtro = self.filter_var.get()
        if filtro == "ninguno":
            filtro = None
        elif filtro == "Tension alta (si)":
            filtro = "TensionAlta = 'si'"
        elif filtro == "Problemas digestivos (si)":
            filtro = "ProblemasDigestivos = 'si'"
        elif filtro == "Dependencia (si)":
            filtro = "DiversionDependenciaAlcohol = 'si'"
        elif filtro == "Hombres (hombre)":
            filtro = "Sexo = 'hombre'"
        elif filtro == "Mujeres (mujer)":
            filtro = "Sexo = 'mujer'"
        encuestas = self.controller.consultar_encuestas(orden, filtro)
        self.mostrar_encuestas(encuestas)

    def solicitar_datos_encuesta(self):
        self.data_window = tk.Toplevel(self.root)
        self.data_window.title("Datos de la Encuesta")
        self.data_window.geometry("400x500")
        self.data_window.config(bg="#ffffff")

        labels = ["ID de Encuesta", "Edad", "Sexo (Hombre/Mujer)", "Bebidas por Semana", "Cervezas por Semana",
                  "Bebidas Fin de Semana", "Bebidas Destiladas por Semana", "Vinos por Semana", "Pérdidas de Control",
                  "Diversión Dependencia Alcohol (si/no)", "Problemas Digestivos (si/no)",
                  "Tensión Alta (si/no/no lo sé)", "Dolor de Cabeza"]

        self.entries = []
        for i, label in enumerate(labels):
            tk.Label(self.data_window, text=label, font=("Arial", 10), bg="#ffffff").grid(row=i, column=0, padx=10,
                                                                                          pady=5, sticky="w")
            entry = tk.Entry(self.data_window, font=("Arial", 10))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        tk.Button(self.data_window, text="Guardar", command=self.guardar_datos_encuesta, bg="#4CAF50", fg="white",
                  font=("Arial", 12, "bold"), relief="flat").grid(row=len(labels), column=0, columnspan=2, pady=10)

    def guardar_datos_encuesta(self):
        datos = [entry.get() for entry in self.entries]
        try:
            self.controller.crear_encuesta(datos)
            messagebox.showinfo("Información", "Datos de la encuesta guardados")
        except Exception as e:
            messagebox.showerror("Error", f"No se ha agregado la encuesta: {e}")
        self.data_window.destroy()
        self.mostrar_encuestas()

    def mostrar_encuestas(self, encuestas=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if encuestas is None:
            encuestas = self.controller.leer_encuestas()
        for encuesta in encuestas:
            self.tree.insert("", "end", values=encuesta)

    def solicitar_actualizacion(self):
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Encuesta")
        self.update_window.geometry("400x300")
        self.update_window.config(bg="#ffffff")

        tk.Label(self.update_window, text="ID de Encuesta a actualizar", font=("Arial", 10), bg="#ffffff").grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=5,
                                                                                                                sticky="w")
        self.update_id_entry = tk.Entry(self.update_window, font=("Arial", 10))
        self.update_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.update_window, text="Campo a actualizar", font=("Arial", 10), bg="#ffffff").grid(row=1, column=0,
                                                                                                       padx=10, pady=5,
                                                                                                       sticky="w")
        self.update_field_entry = tk.Entry(self.update_window, font=("Arial", 10))
        self.update_field_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.update_window, text="Nuevo valor", font=("Arial", 10), bg="#ffffff").grid(row=2, column=0,
                                                                                                padx=10, pady=5,
                                                                                                sticky="w")
        self.update_value_entry = tk.Entry(self.update_window, font=("Arial", 10))
        self.update_value_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.update_window, text="Actualizar", command=self.guardar_actualizacion, bg="#FFC107", fg="white",
                  font=("Arial", 12, "bold"), relief="flat").grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_actualizacion(self):
        idEncuesta = self.update_id_entry.get()
        campo = self.update_field_entry.get()
        nuevo_valor = self.update_value_entry.get()
        self.controller.actualizar_encuesta(idEncuesta, campo, nuevo_valor)
        messagebox.showinfo("Información", "Encuesta actualizada")
        self.update_window.destroy()
        self.mostrar_encuestas()

    def solicitar_eliminacion(self):
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Eliminar Encuesta")
        self.delete_window.geometry("400x200")
        self.delete_window.config(bg="#ffffff")

        tk.Label(self.delete_window, text="ID de Encuesta a eliminar", font=("Arial", 10), bg="#ffffff").grid(row=0,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=5,
                                                                                                              sticky="w")
        self.delete_id_entry = tk.Entry(self.delete_window, font=("Arial", 10))
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.confirmar_eliminacion, bg="#F44336", fg="white",
                  font=("Arial", 12, "bold"), relief="flat").grid(row=1, column=0, columnspan=2, pady=10)

    def confirmar_eliminacion(self):
        idEncuesta = self.delete_id_entry.get()
        self.controller.eliminar_encuesta(idEncuesta)
        messagebox.showinfo("Información", "Encuesta eliminada")
        self.delete_window.destroy()
        self.mostrar_encuestas()