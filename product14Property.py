# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        print("constructor")
        self.temperature = temperature #   @temperature.setter 
        print("constructor end")

    def to_fahrenheit(self):
         print("to_fahrenheit")
         return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...",value )
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())

#coldest_thing = Celsius(-300)
