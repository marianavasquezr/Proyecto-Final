import tkinter as tk
from tkinter import messagebox, simpledialog

class View:
    def __init__(self, PacienteControlador, Controlador):
        self.controllerP = PacienteControlador
        self.usercontroller = Controlador
        self.root = tk.Tk()
        self.root.title("Gestión de Pacientes")

    def entrar(self):
        self.limpiar()
        self.root.geometry("350x200")
        tk.Label(self.root, text="Usuario:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.usercontroller.login).pack()

        # Configurar las entradas en el controlador después de definirlas
        self.usercontroller.set_username_entry(self.username_entry)
        self.usercontroller.set_password_entry(self.password_entry)

    def pantalla(self):
        self.limpiar()
        self.root.geometry("400x300")
        tk.Button(self.root, text="Agregar Paciente", command=self.agregar_paciente).pack()
        tk.Button(self.root, text="Buscar Paciente", command=self.obtener_paciente).pack()
        tk.Button(self.root, text="Agregar terapia", command=self.asignar_terapia).pack()
        tk.Button(self.root, text="Salir", command=self.usercontroller.logout).pack()

    def panttalla2(self):
        self.limpiar()
        self.root.geometry("450x350")
        tk.Button(self.root, text="Consultar Paciente", command=self.obtener_paciente).pack()
        tk.Button(self.root, text="Salir", command=self.usercontroller.logout).pack()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.entrar()
        self.root.mainloop()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def prompt(self, title, prompt):
        return simpledialog.askstring(title, prompt)

    def mostrar_resultados_busqueda(self, paciente, terapias):
        self.limpiar()
        self.root.geometry("400x300")
        if paciente:
            paciente_str = f"Nombre: {paciente[1]}, Edad: {paciente[2]}, Enfermedad: {paciente[3]}, ID: {paciente[0]}"
            tk.Label(self.root, text=paciente_str).pack()
            for terapia in terapias:
                tk.Label(self.root, text=f"Terapia: {terapia[0]}, Fecha: {terapia[1]}").pack()
        else:
            tk.Label(self.root, text="Paciente no encontrado").pack()
        tk.Button(self.root, text="Volver", command=self.pantalla).pack()

    def agregar_paciente(self):
        nombre = self.prompt("Agregar Paciente", "Nombre:")
        edad = self.prompt("Agregar Paciente", "Edad:")
        enfermedad = self.prompt("Agregar Paciente", "Enfermedad:")
        id_paciente = self.prompt("Agregar Paciente", "ID del Paciente:")
        success, message = self.controllerP.agregar_paciente(nombre, edad, enfermedad, id_paciente)
        self.show_message("Resultado", message)

    def asignar_terapia(self):
        id_paciente = self.prompt("Asignar Terapia", "ID del Paciente:")
        terapia = self.prompt("Asignar Terapia", "Terapia:")
        fecha = self.prompt("Asignar Terapia", "Fecha:")
        message = self.controllerP.asignar_terapia(id_paciente, terapia, fecha)
        self.show_message("Resultado", message)

    def obtener_paciente(self):
        id_paciente = self.prompt("Buscar Paciente", "ID del Paciente:")
        paciente, terapias = self.controllerP.buscar_paciente_por_id(id_paciente)
        self.mostrar_resultados_busqueda(paciente, terapias)

