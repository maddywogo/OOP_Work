from vehiclePackage.CarClass import Car;  

class Hybrid(Car):
    def __init__(self, type, make, model, batteryKVA):
        self.batteryKVA = batteryKVA;
        Car.__init__(self, type, make, model);
        
    def printBatteryKVA(self):
        print(self.batteryKVA);
