from vista import View
from controlador import *

if __name__ == "__main__":
    paciente_controlador = PacienteControlador()
    usuario_controlador = Controlador(None)  # Inicializar el controlador sin la vista por ahora
    view = View(paciente_controlador, usuario_controlador)

    usuario_controlador.vista = view  # Asignar la vista después de crearla

    view.entrar()
    view.root.mainloop()
