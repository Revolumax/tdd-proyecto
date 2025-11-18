class CoffeeMachine:
    def __init__(self):
        # cantidades en onzas y cucharadas
        self.coffee_amount = 50   # oz totales disponibles
        self.sugar_amount = 30    # cucharadas
        self.cups = {"pequeño": 5, "mediano": 5, "grande": 5}

        # definición de tamaños
        self.sizes = {"pequeño": 3, "mediano": 5, "grande": 7}

    def make_coffee(self, size, sugar):
        # Validar tamaño
        if size not in self.sizes:
            raise ValueError("Tamaño de vaso no válido")

        # Verificar si hay vasos
        if self.cups[size] <= 0:
            raise ValueError("No hay vasos disponibles")

        # Verificar si hay suficiente café
        required_coffee = self.sizes[size]
        if self.coffee_amount < required_coffee:
            raise ValueError("No hay café disponible")

        # Verificar azúcar
        if self.sugar_amount < sugar:
            raise ValueError("No hay azúcar disponible")

        # Descontar recursos
        self.coffee_amount -= required_coffee
        self.sugar_amount -= sugar
        self.cups[size] -= 1

        # Mensaje final
        return f"Recoge tu café {size} ☕ con {sugar} {'cucharada' if sugar == 1 else 'cucharadas'} de azúcar."

    def refill(self):
        """Rellena los depósitos."""
        self.coffee_amount = 50
        self.sugar_amount = 30
        self.cups = {"pequeño": 5, "mediano": 5, "grande": 5}

    def status(self):
        """Devuelve el estado de la máquina."""
        return {
            "café": self.coffee_amount,
            "azúcar": self.sugar_amount,
            "vasos": self.cups
        }
