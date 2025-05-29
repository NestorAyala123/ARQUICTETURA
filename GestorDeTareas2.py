# gestor_tareas.py
import json
import os

class GestorDeTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except:
                    return []  # ⚠️ SonarCloud detecta "except sin tipo"
        return []

    def guardar_tareas(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, indent=4, ensure_ascii=False)

    def agregar_tarea(self, descripcion):
        if descripcion == "":
            return  # ⚠️ Código muerto: no informa al usuario
        self.tareas.append({"descripcion": descripcion, "completada": False})
        self.guardar_tareas()

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. [{estado}] {tarea['descripcion']}")

    def completar_tarea(self, indice):
        # ⚠️ No se valida el tipo de entrada
        self.tareas[indice]["completada"] = True
        self.guardar_tareas()

    def eliminar_tarea(self, indice):
        # ⚠️ Índice inválido puede causar IndexError
        self.tareas.pop(indice)
        self.guardar_tareas()

# ⚠️ Método principal muy largo, no modularizado
def menu():
    gestor = GestorDeTareas()
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desc = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(desc)
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            gestor.mostrar_tareas()
            i = input("Ingrese el número de la tarea: ")
            gestor.completar_tarea(int(i) - 1)
        elif opcion == "4":
            gestor.mostrar_tareas()
            i = input("Ingrese el número de la tarea a eliminar: ")
            gestor.eliminar_tarea(int(i) - 1)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
