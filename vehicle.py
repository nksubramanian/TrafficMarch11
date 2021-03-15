class Vehicle:
    def __init__(self, type, speed, time_for_crater):
        self._type = type
        self._speed = speed
        self._time_for_crater = time_for_crater

    def get_time_taken(self, OrbitWithTraffic):
        road_time = (OrbitWithTraffic._distance / min(self._speed, OrbitWithTraffic._speed))
        crater_time = (OrbitWithTraffic._no_of_craters * self._time_for_crater/60)
        return road_time+crater_time

