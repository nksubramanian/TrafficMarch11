import enum
from vehicletype import VehicleType
from orbit import Orbit
from orbitwithtraffic import OrbitWithTraffic


class WeatherType(enum.Enum):
   SUNNY = "SUNNY"
   RAINY = "RAINY"
   WINDY = "WINDY"


class Weather:

    def __init__(self, crater_effect, allowed_vehicles):
        self._crater_effect = crater_effect
        self._allowed_vehicles = allowed_vehicles

    def crater_change(self):
        return self._crater_effect
    T='''
    def vehicles_allowed(self, vehicle):
        if VehicleType.name in self._allowed_vehicles:
            return True
        else:
            return False
    '''

    def filter_allowedvehicles(self, vehicles_list):
        permitted_vehicles = []
        for iter in vehicles_list:
            if iter._type in self._allowed_vehicles:
                permitted_vehicles.append(iter)
        return permitted_vehicles

    def alter_orbits(self,orbit_list):
        modified_orbit=[]
        for iter in orbit_list:
            name=iter._name
            distance=iter._distance
            no_of_craters = iter._no_of_craters+(self._crater_effect*iter._no_of_craters/100)
            orbit_speed = iter._speed
            orb_temp = Orbit(name, distance, no_of_craters)
            modified_orbit.append(OrbitWithTraffic(orb_temp ,orbit_speed))
        return modified_orbit


class WeatherFactory:
    @staticmethod
    def get_weather(weathertype):
        if WeatherType.SUNNY == weathertype:
            return Weather(-10, [VehicleType.Bike, VehicleType.TukTuk, VehicleType.Car])
        if WeatherType.RAINY == weathertype:
            return Weather(20, [VehicleType.TukTuk, VehicleType.Car])
        if WeatherType.WINDY == weathertype:
            return Weather(0, [VehicleType.Bike, VehicleType.Car])