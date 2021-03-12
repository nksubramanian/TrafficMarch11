from weather import Weather
class Vehicle:
    def __init__(self,name,speed,time_for_crater):
        self._name=name
        self._speed=speed
        self._time_for_crater=time_for_crater

    def get_time_taken(self,OrbitWithTraffic,weather):
        road_time = (OrbitWithTraffic._distance / min(self._speed, OrbitWithTraffic._speed))
        crater_change = weather.crater_change()
        crater_with_weather=OrbitWithTraffic._no_of_craters+(crater_change*OrbitWithTraffic._no_of_craters/100)
        crater_time=(crater_with_weather* self._time_for_crater / 60)
        return road_time+crater_time



