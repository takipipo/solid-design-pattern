import string
import random


class VehicleInfo:
    def __init__(self, brand: str, catalogue_price: int, is_electric: bool) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.is_electric = is_electric

    def compute_tax(self) -> float:
        if self.is_electric:
            tax_ratio = 0.02
        else:
            tax_ratio = 0.05

        return self.catalogue_price * tax_ratio

    def display_vehicle_info(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    def __init__(self, vehicle_id: str, license_plate: str, info: VehicleInfo) -> None:
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.info = info

    def display_vehicle(self):
        self.info.display_vehicle_info()
        print(f"Id: {self.vehicle_id}")
        print(f"License plate: {self.license_plate}")


class VehicleRegistry:
    vehicle_info = {}

    def __init__(self) -> None:
        self._add_vehicle_info(
            "Tesla Model 3",
            60000,
            True,
        )
        self._add_vehicle_info("Volkswagen ID3", 80000, False)

    def _add_vehicle_info(self, brand: str, electric: bool, catalogue_price: int):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def _generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def _generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str) -> Vehicle:
        vehicle_id = self._generate_vehicle_id(12)
        license_plate = self._generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:
    def register_vehicle(self, brand: str):
        # create a registry instance
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        vehicle.display_vehicle()


if __name__ == "__main__":
    app = Application()
    app.register_vehicle("Tesla Model 3")
