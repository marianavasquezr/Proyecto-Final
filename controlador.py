from modelo import *
from vista import *

class PacienteControlador:
    def __init__(self):
        self.modelo = PacienteModelo()
        self.terapia_modelo = TerapiaModelo()
        self.historial_modelo = HistorialModelo()  # Añadido

    def agregar_paciente(self, nombre, edad, enfermedad, id_paciente):
        try:
            self.modelo.agregar_paciente(nombre, edad, enfermedad, id_paciente)
            return True, "Paciente agregado correctamente"
        except ValueError as e:
            return False, str(e)

    def obtener_pacientes(self):
        return self.modelo.obtener_pacientes()

    def buscar_paciente_por_id(self, id_paciente):
        paciente = self.modelo.buscar_paciente_por_id(id_paciente)
        terapias = self.terapia_modelo.obtener_terapias_por_paciente(id_paciente)
        historial = self.historial_modelo.obtener_historial_por_paciente(id_paciente)  # Añadido
        return paciente, terapias, historial  # Modificado

    def eliminar_paciente(self, id_paciente):
        self.modelo.eliminar_paciente(id_paciente)
        return True, "Paciente eliminado exitosamente"

    def asignar_terapia(self, id_paciente, terapia, fecha, sesiones):
        self.terapia_modelo.asignar_terapia(id_paciente, terapia, fecha, sesiones)  # Modificado
        return "Terapia asignada correctamente"

    def agregar_historial(self, id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias):
        self.historial_modelo.agregar_historial(id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias)
        return "Historial médico agregado correctamente"

class Controlador:
    def __init__(self, vista):
        self.modelo = UsuarioModelo()
        self.vista = vista

    def set_username_entry(self, entry):
        self.username_entry = entry

    def set_password_entry(self, entry):
        self.password_entry = entry

    def verificar_credenciales(self, username, password):
        return self.modelo.verificar_credenciales(username, password)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "medico" and password == "1234":
            self.vista.pantalla()
        elif username == "observador" and password == "5678":
            self.vista.panttalla2()
        else:
            self.vista.show_message("Error", "Credenciales incorrectas")

    def logout(self):
        self.vista.entrar()
