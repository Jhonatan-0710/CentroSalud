print("==========================================")
print(" SISTEMA CENTRO DE SALUD GANÍMEDES")
print("==========================================")

print("Sistema iniciado correctamente.")
print("Proyecto de gestión asistencial y administrativa.")


pacientes = []


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


print("\n--- Módulo de pacientes ---")

registrar_paciente()
buscar_paciente()