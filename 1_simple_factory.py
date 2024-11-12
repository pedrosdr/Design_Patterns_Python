from abc import ABC, abstractmethod
from enum import Enum, auto


class VehicleType(Enum):
    LUXURY_CAR = auto()
    COMPACT_CAR = auto()


class Vehicle:
    @abstractmethod
    def fetch_client(self) -> None: pass


class LuxuryCar(Vehicle):
    def fetch_client(self) -> None:
        print("The Luxury Car is fetching the client")


class CompactCar(Vehicle):
    def fetch_client(self) -> None:
        print("The Compact Car is fetching the client")


class VehicleFactory:
    @staticmethod
    def get_vehicle(type:VehicleType) -> Vehicle:
        if type == VehicleType.COMPACT_CAR:
            return CompactCar()
        elif type == VehicleType.LUXURY_CAR:
            return LuxuryCar()
        else:
            raise ValueError("An invalid vehicle type was selected")
        
        
if __name__ == "__main__":
    car = VehicleFactory.get_vehicle(VehicleType.LUXURY_CAR)
    car.fetch_client()
