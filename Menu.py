from controlador import PacienteControlador, Controlador
from vista import View

if __name__ == "__main__":
    paciente_controlador = PacienteControlador()
    vista = View(paciente_controlador, None)
    usuario_controlador = Controlador(vista)
    vista.usercontroller = usuario_controlador  # Configurar el controlador de usuario en la vista
    vista.run()

