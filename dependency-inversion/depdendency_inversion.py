from abc import ABC, abstractmethod

# Switchable Interface
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class AirConditioner(Switchable):
    def turn_on(self):
        print("Air Conditioner: turned on...")
    def turn_off(self):
        print("Air Conditioner: turned off...")
class ElectricPowerSwitch:

    def __init__(self, device: Switchable):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press() 