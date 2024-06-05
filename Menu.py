from controlador import *
from vista import *

if __name__ == "__main__":
    paciente_controlador = PacienteControlador()
    vista = View(paciente_controlador, None)
    usuario_controlador = Controlador(vista)
    vista.usercontroller = usuario_controlador  
    vista.run()
