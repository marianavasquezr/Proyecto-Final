from controlador import PacienteControlador, Controlador
from vista import View

if __name__ == "__main__":
    paciente_controlador = PacienteControlador()
    vista = View(paciente_controlador, None)  # Inicializar View con None por ahora
    usuario_controlador = Controlador(vista)  # Pasar la instancia de View al Controlador
    vista.usercontroller = usuario_controlador  # Asignar el controlador a la vista
    vista.run()
