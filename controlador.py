from modelo import *

class PacienteControlador:
    def _init_(self):
        self.modelo = PacienteModelo()

    def agregar_paciente(self, nombre, edad, enfermedad, id_paciente):
        try:
            self.modelo.agregar_paciente(nombre, edad, enfermedad, id_paciente)
            return True, "Paciente agregado correctamente"
        except ValueError as e:
            return False, str(e)

    def obtener_pacientes(self):
        return self.modelo.obtener_pacientes()

    def buscar_paciente_por_id(self, id_paciente):
        return self.modelo.buscar_paciente_por_id(id_paciente)

    def buscar_pacientes_por_nombre(self, nombre):
        return self.modelo.buscar_pacientes_por_nombre(nombre)

    def eliminar_paciente(self, id_paciente):
        self.modelo.eliminar_paciente(id_paciente)
        return "Paciente eliminado correctamente"
class Controlador:
    def _init_(self):
        self.modelo = UsuarioModelo()

    def verificar_credenciales(self, username, password):
        return self.modelo.verificar_credenciales(username, password)