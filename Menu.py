
from controlador import PacienteControlador, Controlador
from vista import View

if __name__ == "__main__":
    paciente_controlador = PacienteControlador()
    usuario_controlador = Controlador()
    vista = View(paciente_controlador, usuario_controlador)
    vista.run()

