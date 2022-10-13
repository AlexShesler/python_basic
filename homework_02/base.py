from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int
    started: bool = False
    fuel: int
    fuel_consumption: int

    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError()
            self.started = True

    def move(self, distance: int) -> None:
        if distance:
            if self.fuel // self.fuel_consumption < distance:
                raise NotEnoughFuel
            self.fuel -= distance * self.fuel_consumption
