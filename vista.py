import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from controlador import *

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Pacientes")


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
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()        
        tk.Label(self.root, text="Ƹ̵̡Ӝ̵̨̄Ʒ Hola Doctor! Bienvenido al sistema, seleccione la ocpion que desea ejecutar:\n\n",bg="light green").pack()
        tk.Button(self.root, text="Agregar Paciente", command=self.agregar_paciente).pack()
        tk.Button(self.root, text="Buscar Paciente", command=self.obtener_paciente).pack()
        tk.Button(self.root, text="Agregar terapia", command=self.asignar_terapia).pack()
        tk.Button(self.root, text="Salir", command=self.usercontroller.logout).pack()
        tk.Label(self.root, text="🧑🏼Para mas informacion comunicarte a nuestros correos:\n",font=("Helvetica", 10, "bold"),bg="light blue").pack()
        tk.Label(self.root,text="🏠 mariana.vasquez@udea.edu.co\n🏠 estefania.loaiza@udea.edu.co",bg="light blue").pack()

    def panttalla2(self):
        self.limpiar()
        self.root.geometry("450x350")
        tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()        
        tk.Label(self.root, text="(/◕ヮ◕)/Querido usuario, acontinuacion ingrese el ID para encontrar\n la informacion del paciente:",bg="light blue").pack()
        tk.Label(self.root, text="\n\n",bg="light green").pack()
        tk.Button(self.root, text="Consultar Paciente", command=self.obtener_paciente2).pack()
        tk.Button(self.root, text="Salir", command=self.usercontroller.logout).pack()
        tk.Label(self.root, text="\n\n",bg="light green").pack()
        tk.Label(self.root, text="🧑🏼Para mas informacion comunicarte a nuestros correos:\n",font=("Helvetica", 10, "bold"),bg="light blue").pack()
        tk.Label(self.root,text="🏠 mariana.vasquez@udea.edu.co\n🏠 estefania.loaiza@udea.edu.co",bg="light blue").pack()

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
            tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()        
            tk.Label(self.root, text="\n🥼A continuación los datos encontrados del paciente:\n",bg="light green").pack()
            tk.Label(self.root, text=paciente_str, bg="light blue").pack()
            for terapia in terapias:
                tk.Label(self.root, text=f"Terapia: {terapia[0]}, Fecha: {terapia[1]}",bg="light blue").pack()
            tk.Button(self.root, text="Eliminar", command=lambda p=paciente: self.controllerP.eliminar_paciente(p[0])).pack()
            tk.Button(self.root, text="Volver", command=self.pantalla).pack()
        
        else:
            tk.Label(self.root, text="Paciente no encontrado").pack()
            tk.Button(self.root, text="Volver", command=self.pantalla).pack()
        
    def mostrar_resultados_busqueda2(self, paciente, terapias):
        self.limpiar()
        self.root.geometry("400x300")
        if paciente:
            paciente_str = f"Nombre: {paciente[1]}, Edad: {paciente[2]}, Enfermedad: {paciente[3]}, ID: {paciente[0]}"
            tk.Label(self.root, text="                                                🫀 TECNOSALUD UDEA 🫀                                                 ", bg="green", font=("Helvetica", 18, "bold")).pack()        
            tk.Label(self.root, text="\n🥼A continuación los datos encontrados del paciente:\n",bg="light green").pack()
            tk.Label(self.root, text=paciente_str, bg="light blue").pack()
            for terapia in terapias:
                tk.Label(self.root, text=f"Terapia: {terapia[0]}, Fecha: {terapia[1]}",bg="light blue").pack()
            tk.Button(self.root, text="Volver", command=self.panttalla2).pack()
        else:
            tk.Label(self.root, text="Paciente no encontrado").pack()
            tk.Button(self.root, text="Volver", command=self.panttalla2).pack()

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
        while True:
            fecha = self.prompt("Asignar Terapia", "Fecha (formato: YYYY-MM-DD):")
            try:
                fecha_valida = datetime.strptime(fecha, '%Y-%m-%d')
                break
            except ValueError:
                print("-----------------------------------------------------------------------------------")
                print("Fecha inválida. Por favor, introduce una fecha en el formato correcto (YYYY-MM-DD).")
                print("-----------------------------------------------------------------------------------")
        message = self.controllerP.asignar_terapia(id_paciente, terapia, fecha)
        self.show_message("Resultado", message)

    def obtener_paciente(self):
        id_paciente = self.prompt("Buscar Paciente", "ID del Paciente:")
        paciente, terapias = self.controllerP.buscar_paciente_por_id(id_paciente)
        self.mostrar_resultados_busqueda(paciente, terapias)

    def obtener_paciente2(self):
        id_paciente = self.prompt("Buscar Paciente", "ID del Paciente:")
        paciente, terapias = self.controllerP.buscar_paciente_por_id(id_paciente)
        self.mostrar_resultados_busqueda2(paciente, terapias)
