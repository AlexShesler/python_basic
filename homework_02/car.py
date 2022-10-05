from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: Engine

    def set_engine(self, in_eng: Engine) -> None:
        self.engine = in_eng

