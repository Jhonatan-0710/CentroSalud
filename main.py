print("==========================================")
print(" SISTEMA CENTRO DE SALUD GANÍMEDES")
print("==========================================")

print("Sistema iniciado correctamente.")
print("Proyecto de gestión asistencial y administrativa.")


def registrar_paciente():
    print("\n===== REGISTRO DE PACIENTE =====")

    nombre = input("Ingrese el nombre del paciente: ")
    dni = input("Ingrese el DNI del paciente: ")
    edad = input("Ingrese la edad del paciente: ")

    print("\nPaciente registrado correctamente.")
    print("Nombre:", nombre)
    print("DNI:", dni)
    print("Edad:", edad)


print("\n--- Módulo de pacientes ---")
registrar_paciente()