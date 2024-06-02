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
                                enfermedad TEXT,
                                historia_medica TEXT
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS terapias (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paciente INTEGER,
                                terapia TEXT,
                                fecha TEXT,
                                FOREIGN KEY(id_paciente) REFERENCES pacientes(id)
                              )''')
        self.conexion.commit()

    def agregar_paciente(self, nombre, edad, enfermedad, historia_medica, id_paciente):
        # Verificar que el ID no se repita
        self.cursor.execute("SELECT id FROM pacientes WHERE id=?", (id_paciente,))
        if self.cursor.fetchone() is not None:
            raise ValueError("El ID de paciente ya existe")

        self.cursor.execute('''INSERT INTO pacientes (id, nombre, edad, enfermedad, historia_medica)
                               VALUES (?, ?, ?, ?, ?)''', (id_paciente, nombre, edad, enfermedad, historia_medica))
        self.conexion.commit()

    def obtener_pacientes(self):
        self.cursor.execute('''SELECT * FROM pacientes''')
        return self.cursor.fetchall()

    def buscar_paciente_por_id(self, id_paciente):
        self.cursor.execute("SELECT * FROM pacientes WHERE id=?", (id_paciente,))
        return self.cursor.fetchone()

    def buscar_pacientes_por_nombre(self, nombre):
        # Convertir el nombre a minúsculas para hacer la búsqueda case-insensitive
        nombre = nombre.lower()
        self.cursor.execute("SELECT * FROM pacientes WHERE LOWER(nombre) LIKE ?", (f"{nombre}%",))
        return self.cursor.fetchall()

    def eliminar_paciente(self, id_paciente):
        self.cursor.execute('''DELETE FROM pacientes WHERE id = ?''', (id_paciente,))
        self.cursor.execute('''DELETE FROM terapias WHERE id_paciente = ?''', (id_paciente,))
        self.conexion.commit()

        
class UsuarioModelo:
    def __init__(self):
        self.usuarios = {"medico": "1234", "observador": "5678"}

    def verificar_credenciales(self, username, password):
        if username in self.usuarios and self.usuarios[username] == password:
            return True
        else:
            return False
