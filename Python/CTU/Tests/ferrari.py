class Car:
    def __init__(meow, fuelConsumption, tankCapacity):
        meow.fuelConsumption = fuelConsumption
        meow.tankCapacity = tankCapacity
    
    def distance_on_full_tank(self):
        return self.tankCapacity * 100 / self.fuelConsumption

# Instantiate the Ferrari and Bugatti cars
ferrari = Car(11, 45)
bugatti = Car(13, 58)

# Print the distance each car can travel on a full tank
print("Ferrari distance on full tank:", round(ferrari.distance_on_full_tank(),2), "km")
print("Bugatti distance on full tank:", round(bugatti.distance_on_full_tank(),2), "km")