import sqlite3

class PacienteModelo:
    def __init__(self):
        self.conexion = sqlite3.connect('hospital.db')
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                edad INTEGER,
                                enfermedad TEXT
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS terapias (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paciente INTEGER,
                                terapia TEXT,
                                fecha TEXT,
                                sesiones INTEGER,
                                FOREIGN KEY(id_paciente) REFERENCES pacientes(id)
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS historial (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paciente INTEGER,
                                fecha_nacimiento TEXT,
                                tipo_sangre TEXT,
                                contacto_emergencia TEXT,
                                ultimo_examen TEXT,
                                enfermedades TEXT,
                                cirugias TEXT,
                                FOREIGN KEY(id_paciente) REFERENCES pacientes(id)
                              )''')
        self.conexion.commit()

    def agregar_paciente(self, nombre, edad, enfermedad, id_paciente):
        self.cursor.execute("SELECT id FROM pacientes WHERE id=?", (id_paciente,))
        if self.cursor.fetchone() is not None:
            raise ValueError("El ID de paciente ya existe")
        self.cursor.execute('''INSERT INTO pacientes (id, nombre, edad, enfermedad)
                               VALUES (?, ?, ?, ?)''', (id_paciente, nombre, edad, enfermedad))
        self.conexion.commit()

    def obtener_pacientes(self):
        self.cursor.execute('''SELECT * FROM pacientes''')
        return self.cursor.fetchall()

    def buscar_paciente_por_id(self, id_paciente):
        self.cursor.execute("SELECT * FROM pacientes WHERE id=?", (id_paciente,))
        return self.cursor.fetchone()

    def eliminar_paciente(self, id_paciente):
        self.cursor.execute('''DELETE FROM pacientes WHERE id = ?''', (id_paciente,))
        self.cursor.execute('''DELETE FROM terapias WHERE id_paciente = ?''', (id_paciente,))
        self.cursor.execute('''DELETE FROM historial WHERE id_paciente = ?''', (id_paciente,))
        self.conexion.commit()

class UsuarioModelo:
    def __init__(self):
        self.usuarios = {"medico": "1234", "observador": "5678"}

    def verificar_credenciales(self, username, password):
        if username in self.usuarios and self.usuarios[username] == password:
            return True
        else:
            return False

class TerapiaModelo:
    def __init__(self):
        self.conexion = sqlite3.connect('hospital.db')
        self.cursor = self.conexion.cursor()

    def asignar_terapia(self, id_paciente, terapia, fecha, sesiones):
        self.cursor.execute('''INSERT INTO terapias (id_paciente, terapia, fecha, sesiones)
                               VALUES (?, ?, ?, ?)''', (id_paciente, terapia, fecha, sesiones))
        self.conexion.commit()

    def obtener_terapias_por_paciente(self, id_paciente):
        self.cursor.execute('''SELECT terapia, fecha, sesiones FROM terapias WHERE id_paciente=?''', (id_paciente,))
        return self.cursor.fetchall()

class HistorialModelo:
    def __init__(self):
        self.conexion = sqlite3.connect('hospital.db')
        self.cursor = self.conexion.cursor()

    def agregar_historial(self, id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias):
        self.cursor.execute('''INSERT INTO historial (id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias)
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (id_paciente, fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias))
        self.conexion.commit()

    def obtener_historial_por_paciente(self, id_paciente):
        self.cursor.execute('''SELECT fecha_nacimiento, tipo_sangre, contacto_emergencia, ultimo_examen, enfermedades, cirugias FROM historial WHERE id_paciente=?''', (id_paciente,))
        return self.cursor.fetchone()
