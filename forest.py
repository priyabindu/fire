import random

class TemperatureSensor:
    def read_value(self):
        # Simulating temperature readings between 60°F to 100°F
        return random.uniform(60, 100)

class HumiditySensor:
    def read_value(self):
        # Simulating humidity readings between 10% to 90%
        return random.uniform(10, 90)

class FireAlarmSystem:
    def _init_(self, temperature_sensor, humidity_sensor):
        self.temperature_sensor = temperature_sensor
        self.humidity_sensor = humidity_sensor

    def check_conditions(self):
        temperature = self.temperature_sensor.read_value()
        humidity = self.humidity_sensor.read_value()

        if temperature > 90 and humidity < 20:
            print("High temperature and low humidity detected! Possible fire in the forest!")
        else:
            print("No fire detected.")

# Create temperature and humidity sensors
temperature_sensor = TemperatureSensor()
humidity_sensor = HumiditySensor()

# Create a fire alarm system with the sensors
fire_alarm = FireAlarmSystem(temperature_sensor, humidity_sensor)

# Check conditions
fire_alarm.check_conditions()
