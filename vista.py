import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from controlador import *


class View:
    def __init__(self, PacienteControlador, Controlador):
        self.controllerP = PacienteControlador
        self.usercontroller = Controlador
        self.root = tk.Tk()
        self.root.title("Gestión de Pacientes UDEA")

    def entrar(self):
        self.limpiar()
        self.root.configure(background="light green")
        self.root.geometry("800x400")
        
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.root, text="-(/◕ヮ◕)/-------------------------------------------------Bienvenidos al sistema de datos medicos--------------------------------------------------(/◕ヮ◕)/-\n",bg="light blue").pack() 
        tk.Label(self.root, text="Ingrese con su usuario y contraseña para poder ingresar al sistema \n_______________________________________________________________________________________________________________________________________________________________",bg="light green").pack()
        tk.Label(self.root, text="🧑🏼‍⚕️Usuario:",bg="light blue").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="🧑🏼‍⚕️Contraseña:",bg="light blue").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.usercontroller.login).pack()
        tk.Label(self.root, text="\n",bg="light green").pack()
        tk.Label(self.root, text="Contactenos para más información:\n\n Diana Rojas +57 3214569870\n Mateo hincapie +57 3698521475",bg="light blue").pack()
        
        # Configurar las entradas en el controlador después de definirlas
        self.usercontroller.set_username_entry(self.username_entry)
        self.usercontroller.set_password_entry(self.password_entry)



    def pantalla(self):
        self.limpiar()
        self.root.geometry("400x400")
        self.root.configure(background="light green")
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.root, text="\n\n\n\n",bg="light blue")
        tk.Label(self.root, text="Bienvenido, Doctor",bg="light blue").pack()
        tk.Button(self.root, text="Gestión de Pacientes", command=self.menu).pack()
        tk.Button(self.root, text="Cerrar Sesión", command=self.usercontroller.logout).pack()

    def panttalla2(self):
        self.limpiar()
        self.root.geometry("400x400")
        self.root.configure(background="light green")
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.root, text="\n\n\n",bg="light blue")
        tk.Label(self.root, text="Bienvenido, Observador",bg="light blue").pack()
        tk.Button(self.root, text="Ver lista de Pacientes", command=self.menu2).pack()
        tk.Button(self.root, text="Cerrar Sesión", command=self.usercontroller.logout).pack()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_pacientes(self):
        self.limpiar()
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        pacientes = self.controllerP.obtener_pacientes()
        text = ""
        for paciente in pacientes:
            text += f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Enfermedad: {paciente[3]}\n"
        self.mostrar_mensaje(text)
        tk.Button(self.root, text="Cerrar Sesión", command=self.usercontroller.logout).pack()

    def menu(self):
        self.limpiar()
        self.root.configure(background="light green")
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.root, text="\n\n\n",bg="light blue")
        tk.Label(self.root, text="Menú de Gestión de Pacientes",bg="light blue").pack()
        tk.Button(self.root, text="Agregar Paciente", command=self.agregar_paciente).pack()
        tk.Button(self.root, text="Eliminar Paciente", command=self.eliminar_paciente).pack()
        tk.Button(self.root, text="Ver Pacientes", command=self.mostrar_pacientes).pack()
        tk.Button(self.root, text="Buscar Paciente por ID", command=self.buscar_paciente_por_id).pack()
        tk.Button(self.root, text="Asignar Terapia", command=self.asignar_terapia).pack()
        tk.Button(self.root, text="Agregar Historial Médico", command=self.agregar_historial).pack()
        tk.Button(self.root, text="Cerrar Sesión", command=self.usercontroller.logout).pack()

    def menu2(self):
        self.limpiar()
        self.root.configure(background="light green")
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.root, text="\n\n\n",bg="light blue")
        tk.Label(self.root, text="Menú de Observador de Pacientes",bg="light blue").pack()
        tk.Button(self.root, text="Buscar Paciente por ID", command=self.buscar_paciente_por_id).pack()
        tk.Button(self.root, text="Cerrar Sesión", command=self.usercontroller.logout).pack()

    def agregar_paciente(self):
        nombre = simpledialog.askstring("Input", "Nombre del paciente:")
        edad = simpledialog.askinteger("Input", "Edad del paciente:")
        enfermedad = simpledialog.askstring("Input", "Enfermedad del paciente:")
        id_paciente = simpledialog.askinteger("Input", "ID del paciente:")
        if nombre and edad and enfermedad and id_paciente:
            exito, mensaje = self.controllerP.agregar_paciente(nombre, edad, enfermedad, id_paciente)
            self.mostrar_mensaje(mensaje)
        else:
            self.mostrar_mensaje("Todos los campos son obligatorios")

    def eliminar_paciente(self):
        id_paciente = simpledialog.askinteger("Input", "ID del paciente a eliminar:")
        if id_paciente:
            exito, mensaje = self.controllerP.eliminar_paciente(id_paciente)
            self.mostrar_mensaje(mensaje)
        else:
            self.mostrar_mensaje("El ID del paciente es obligatorio")

    def buscar_paciente_por_id(self):
        id_paciente = simpledialog.askinteger("Input", "ID del paciente:")
        if id_paciente:
            paciente, terapias, historial = self.controllerP.buscar_paciente_por_id(id_paciente)
            if paciente:
                text = f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Enfermedad: {paciente[3]}\n\nTerapias:\n"
                for terapia in terapias:
                    text += f"Terapia: {terapia[0]}, Fecha: {terapia[1]}, Sesiones: {terapia[2]}\n"
                text += "\nHistorial Médico:\n"
                if historial:
                    text += f"Fecha de Nacimiento: {historial[0]}, Tipo de Sangre: {historial[1]}, Contacto de Emergencia: {historial[2]}\n"
                    text += f"Último Examen: {historial[3]}, Enfermedades: {historial[4]}, Cirugías: {historial[5]}\n"
                else:
                    text += "No hay historial médico disponible."
                self.mostrar_mensaje(text)
            else:
                self.mostrar_mensaje("Paciente no encontrado")
        else:
            self.mostrar_mensaje("El ID del paciente es obligatorio")

    def asignar_terapia(self):
        id_paciente = simpledialog.askinteger("Input", "ID del paciente:")
        terapia = simpledialog.askstring("Input", "Nombre de la terapia:")
        fecha = simpledialog.askstring("Input", "Fecha de la terapia (DD-MM-YYYY):")
        sesiones = simpledialog.askinteger("Input", "Número de sesiones:")
        if id_paciente and terapia and fecha and sesiones:
            try:
                fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
                mensaje = self.controllerP.asignar_terapia(id_paciente, terapia, fecha, sesiones)
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Formato de fecha incorrecto. Debe ser DD-MM-YYYY")
        else:
            self.mostrar_mensaje("Todos los campos son obligatorios")

    def agregar_historial(self):
        id_paciente = simpledialog.askinteger("Input", "ID del paciente:")
        fecha_nacimiento = simpledialog.askstring("Input", "Fecha de nacimiento (DD-MM-YYYY):")
        tipo_sangre = simpledialog.askstring("Input", "Tipo de sangre:")
        contacto_emergencia = simpledialog.askstring("Input", "Contacto de emergencia:")
        ultimo_examen = simpledialog.askstring("Input", "Último examen (DD-MM-YYYY):")
        enfermedades = simpledialog.askstring("Input", "Enfermedades:")
        cirugias = simpledialog.askstring("Input", "Cirugías:")
        if id_paciente and fecha_nacimiento and tipo_sangre and contacto_emergencia and ultimo_examen and enfermedades and cirugias:
            try:
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y").date()
                ultimo_examen = datetime.strptime(ultimo_examen, "%d-%m-%Y").date()
                mensaje = self.controllerP.agregar_historial(id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias)
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Formato de fecha incorrecto. Debe ser DD-MM-YYYY")
        else:
            self.mostrar_mensaje("Todos los campos son obligatorios")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
