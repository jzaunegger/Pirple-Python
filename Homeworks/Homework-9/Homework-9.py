import random

class Vehicle:
    def __init__(self, make, model, year, weight):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight

        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    def __repr__(self):
        return "This is an instance of a Vehicle Object."

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.Make, self.Model, self.Year, self.Weight, self.NeedsMaintenance, self.TripsSinceMaintenance)

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # Getters
    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    # Setters
    def setMake(self, nMake):
        self.Make = nMake

    def setModel(self, nModel):
        self.Model = nModel

    def setYear(self, nYear):
        self.Year = nYear

    def setWeight(self, nWeight):
        self.Weight = nWeight

class Car(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):
        if self.TripsSinceMaintenance > 100:
            print("Your car needs repaired before it can drive again.")
        else:
            self.isDriving = True

    def Stop(self):
        if self.TripsSinceMaintenance > 100:
            self.isDriving = False
            self.NeedsMaintenance = True
            print("Your car needs maintenance before it can drive again.")

        else:
            self.isDriving = False
            self.TripsSinceMaintenance += 1

class Plane(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False

    def Flying(self):
        if self.TripsSinceMaintenance > 100:
            print("Your plane needs repaired before flying.")
            return False
        else:
            self.isFlying = True
            return True

    def Landing(self):
        if self.TripsSinceMaintenance > 100:
            self.isFlying = False
            self.NeedsMaintenance = True
            print("Your plane needs maintenance before flying again.")

        else:
            self.isFlying = False
            self.TripsSinceMaintenance += 1

v1 = Car("Porsche", "911 Carrera 4S", 2021, 3487)
v2 = Car("Audi", "TT RS", 2021, 3329)
v3 = Car("Lamborghini", "Huracan EVO", 2020, 3135)
p1 = Plane("Airplane", "x1", 2018, 1700)

v1_drive_range = random.randint(20, 120)
v2_drive_range = random.randint(20, 120)
v3_drive_range = random.randint(20, 120)
p1_fly_range = random.randint(20, 120)

for i in range(0, v1_drive_range):
    v1.Drive()
    v1.Stop()

for i in range(0, v2_drive_range):
    v2.Drive()
    v2.Stop()

for i in range(0, v3_drive_range):
    v3.Drive()
    v3.Stop()

for i in range(0, p1_fly_range):
    isFlying = p1.Flying()
    if isFlying == True:
        p1.Landing()

print(v1)
print(v2)
print(v3)
print(p1)
