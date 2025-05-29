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
                return json.load(f)
        return []

    def guardar_tareas(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, indent=4, ensure_ascii=False)

    def agregar_tarea(self, descripcion):
        self.tareas.append({"descripcion": descripcion, "completada": False})
        self.guardar_tareas()

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
            return
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. [{estado}] {tarea['descripcion']}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            self.guardar_tareas()
        else:
            print("Índice no válido.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            self.guardar_tareas()
        else:
            print("Índice no válido.")

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
            i = int(input("Ingrese el número de la tarea: ")) - 1
            gestor.completar_tarea(i)
        elif opcion == "4":
            gestor.mostrar_tareas()
            i = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(i)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
