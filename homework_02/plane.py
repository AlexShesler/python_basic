from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, num) -> None:
        if self.cargo + num > self.max_cargo:
            raise CargoOverload()
        self.cargo += num

    def remove_all_cargo(self) -> int:
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
