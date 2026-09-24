print("==========================================")
print(" SISTEMA CENTRO DE SALUD GANÍMEDES")
print("==========================================")

print("Sistema iniciado correctamente.")
print("Proyecto de gestión asistencial y administrativa.")


# Lista donde se almacenan los pacientes
pacientes = []

# Lista donde se almacenan las citas
citas = []

# Lista donde se almacenan los usuarios
usuarios = []

# Lista donde se almacenan las historias clínicas
historias_clinicas = []


def registrar_paciente():
    print("\n===== REGISTRO DE PACIENTE =====")

    nombre = input("Ingrese el nombre del paciente: ")

    while True:
        dni = input("Ingrese el DNI del paciente: ")

        if dni.isdigit() and len(dni) == 8:
            break

        print("Error: el DNI debe tener exactamente 8 dígitos.")

    edad = input("Ingrese la edad del paciente: ")

    paciente = {
        "nombre": nombre,
        "dni": dni,
        "edad": edad
    }

    pacientes.append(paciente)

    print("\nPaciente registrado correctamente.")


def buscar_paciente():
    print("\n===== BÚSQUEDA DE PACIENTE =====")

    dni_buscar = input("Ingrese el DNI del paciente que desea buscar: ")

    for paciente in pacientes:
        if paciente["dni"] == dni_buscar:
            print("\nPaciente encontrado:")
            print("Nombre:", paciente["nombre"])
            print("DNI:", paciente["dni"])
            print("Edad:", paciente["edad"])
            return

    print("\nNo se encontró un paciente con ese DNI.")


def registrar_cita():
    print("\n===== REGISTRO DE CITA MÉDICA =====")

    dni = input("Ingrese el DNI del paciente: ")
    fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    especialidad = input("Ingrese la especialidad médica: ")

    cita = {
        "dni": dni,
        "fecha": fecha,
        "hora": hora,
        "especialidad": especialidad
    }

    citas.append(cita)

    print("\nCita médica registrada correctamente.")


def consultar_citas():
    print("\n===== CITAS REGISTRADAS =====")

    if not citas:
        print("No existen citas registradas.")
        return

    for numero, cita in enumerate(citas, start=1):
        print("\nCita", numero)
        print("DNI del paciente:", cita["dni"])
        print("Fecha:", cita["fecha"])
        print("Hora:", cita["hora"])
        print("Especialidad:", cita["especialidad"])


def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")

    nombre = input("Ingrese el nombre del usuario: ")
    usuario = input("Ingrese el nombre de usuario: ")

    print("\nSeleccione el rol:")
    print("1. Administrador")
    print("2. Médico")
    print("3. Recepcionista")

    opcion = input("Seleccione una opción: ")

    roles = {
        "1": "Administrador",
        "2": "Médico",
        "3": "Recepcionista"
    }

    if opcion not in roles:
        print("\nError: opción de rol no válida.")
        return

    rol = roles[opcion]

    nuevo_usuario = {
        "nombre": nombre,
        "usuario": usuario,
        "rol": rol
    }

    usuarios.append(nuevo_usuario)

    print("\nUsuario registrado correctamente.")
    print("Nombre:", nombre)
    print("Usuario:", usuario)
    print("Rol:", rol)


def registrar_historia_clinica():
    print("\n===== HISTORIA CLÍNICA =====")

    dni = input("Ingrese el DNI del paciente: ")
    diagnostico = input("Ingrese el diagnóstico: ")
    tratamiento = input("Ingrese el tratamiento indicado: ")

    historia = {
        "dni": dni,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento
    }

    historias_clinicas.append(historia)

    print("\nHistoria clínica registrada correctamente.")


# Ejecución del sistema

print("\n--- Módulo de pacientes ---")
registrar_paciente()
buscar_paciente()

print("\n--- Módulo de citas ---")
registrar_cita()
consultar_citas()

print("\n--- Módulo de usuarios ---")
registrar_usuario()

print("\n--- Módulo de historia clínica ---")
registrar_historia_clinica()