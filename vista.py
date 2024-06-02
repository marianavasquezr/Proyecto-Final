# creacion clase vistas
import tkinter as tk
from tkinter import messagebox, simpledialog

class View:
    def __init__(self, PacienteControlador):
        self.controller = PacienteControlador
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
        tk.Button(self.root, text="Login", command=self.controller.login).pack()

    def pantalla(self):
        self.limpiar()
        self.root.geometry("400x300")
        tk.Button(self.root, text="Agregar Paciente", command=self.controller.agregar_paciente).pack()
        tk.Button(self.root, text="Buscar Paciente", command=self.controller.obtener_paciente).pack()
        tk.Button(self.root, text="Salir", command=self.controller.logout).pack()

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

    def mostrar_resultados_busqueda(self, resultados):
        self.limpiar()
        self.root.geometry("400x300")
        for paciente in resultados:
            paciente_str = f"{paciente['nombre']} {paciente['apellido']}, Edad: {paciente['edad']}, ID: {paciente['identificacion']}"
            tk.Label(self.root, text=paciente_str).pack()
            tk.Button(self.root, text="Eliminar", command=lambda p=paciente: self.controller.eliminar_paciente(p['identificacion'])).pack()
        tk.Button(self.root, text="Volver", command=self.pantalla).pack()