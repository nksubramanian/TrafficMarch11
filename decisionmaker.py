from vehicletype import VehicleType


class DecisionMaker:
    preference = {VehicleType.Bike: 1, VehicleType.TukTuk: 2, VehicleType.Car: 3}

    def makedecision(self, vehicles_list, orbit_list, weather):
        vehicles_list = weather.filter_allowedvehicles(vehicles_list)
        orbit_list = weather.alter_orbits(orbit_list)
        optionswithtime = self.get_optionswithtime(orbit_list, vehicles_list)
        fastest_options = self.get_fastest_options(optionswithtime)
        return self.get_best_vehicle_and_orbit(fastest_options)



    def get_fastest_options(self, optionswithtime):
        time = []
        for option in optionswithtime:
            time.append(option.estimated_time)
        min_time = min(time)
        indices = [i for i, x in enumerate(time) if x == min_time]
        fastest_options = []
        for index in indices:
            fastest_options.append(optionswithtime[index])
        return fastest_options

    def get_best_vehicle_and_orbit(self, fastest_options):
        temp = []
        for iter in fastest_options:
            temp.append(self.preference[iter.vehicle._type])
        return fastest_options[temp.index(min(temp))]

    def get_optionswithtime(self, orbit_list, vehicles_list):
        options = []
        for vehicle in vehicles_list:
            for orbit in orbit_list:
                options.append(Options(orbit, vehicle))
        return options


class Options:
    def __init__(self, OrbitWithTraffic, vehicle):
        self.OrbitWithTraffic = OrbitWithTraffic
        self.vehicle = vehicle
        self.estimated_time = self.vehicle.get_time_taken(self.OrbitWithTraffic)

    def get_time_taken(self):
        return self.estimated_time
