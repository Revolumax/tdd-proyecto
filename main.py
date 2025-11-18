from coffee_machine import CoffeeMachine

def mostrar_menu():
    print("\n=== ☕ MÁQUINA DE CAFÉ ===")
    print("1. Servir café")
    print("2. Ver estado de la máquina")
    print("3. Rellenar depósitos")
    print("4. Salir")

def main():
    machine = CoffeeMachine()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-4): ").strip()

        if opcion == "1":
            print("\nTamaños disponibles:")
            print(" - pequeño (3 oz)")
            print(" - mediano (5 oz)")
            print(" - grande (7 oz)")
            size = input("Selecciona tamaño de vaso: ").lower().strip()

            sugar = int(input("¿Cuántas cucharadas de azúcar?: "))

            try:
                mensaje = machine.make_coffee(size, sugar)
                print(f"\n✅ {mensaje}")
            except ValueError as e:
                print(f"\n❌ {e}")

        elif opcion == "2":
            estado = machine.status()
            print("\n=== ESTADO ACTUAL ===")
            print(f"Café disponible: {estado['café']} oz")
            print(f"Azúcar disponible: {estado['azúcar']} cucharadas")
            print(f"Vasos: {estado['vasos']}")

        elif opcion == "3":
            machine.refill()
            print("\n♻️ Máquina rellenada correctamente.")

        elif opcion == "4":
            print("\n👋 ¡Gracias por usar la máquina de café!")
            break

        else:
            print("\n⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
