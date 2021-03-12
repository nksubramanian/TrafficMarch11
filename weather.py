import enum
from vehiclename import VehicleName
# Using enum class create enumerations
class WeatherOption(enum.Enum):
  SUNNY = 1
  RAINY = 2
  WINDY = 3

class Weather:
    _cratereffect={WeatherOption(1).name:-10,WeatherOption(2).name:20,WeatherOption(3).name:0}
    Sunny_weather={VehicleName(3).name: True,VehicleName(1).name:True,VehicleName(2).name:True}
    Rainy_weather={VehicleName(3).name: True,VehicleName(1).name:False,VehicleName(2).name:True}
    Windy_weather={VehicleName(3).name: True,VehicleName(1).name:True,VehicleName(2).name:False}

    def __init__(self, name):
        self._name=name

    def crater_change(self):
        return self._cratereffect[self._name]

    def vehicles_allowed(self,vehicle):
        if self._name==WeatherOption(1).name:
            return self.Sunny_weather[vehicle._name]
        elif self._name==WeatherOption(2).name:
            return self.Rainy_weather[vehicle._name]
        if self._name==WeatherOption(3).name:
            return self.Windy_weather[vehicle._name]


    def filter_allowedvehicles(self,vehicles_list):
        #return list(filter(lambda x:self.vehicles_allowed(x),vehicles_list))
        allowed_vehicles=[]
        for vehicle in vehicles_list:
            if self.vehicles_allowed(vehicle):
                allowed_vehicles.append(vehicle)
        return allowed_vehicles

