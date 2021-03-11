class DecisionMaker:
    def calculatetime(self,orbit,vehicle,weather): #weather needs to be included
        if weather.vehicles_allowed(vehicle):
            temp=(orbit._distance/min(vehicle._speed,orbit._speed))+(orbit._no_of_craters*vehicle._time_for_crater/60)
            return temp
        else:
            return float('inf')


    def makedecision(self,vehicles_list,orbit_list,weather):
        time_taken_for_vehicle_in_each_orbit = []
        orbit_order_in_time_taken = []
        vehicle_order_in_time_taken=[]
        vehicles_position=0
        for vehicle in vehicles_list:
            orbit_position=0
            for orbit in orbit_list:
                vehicle_order_in_time_taken.append(vehicles_position)
                time_taken_for_vehicle_in_each_orbit.append(self.calculatetime(orbit,vehicle,weather))
                orbit_order_in_time_taken.append(orbit_position)
                orbit_position += 1
            vehicles_position += 1
        min_time_index = time_taken_for_vehicle_in_each_orbit.index(min(time_taken_for_vehicle_in_each_orbit))
        fastest_vehicle_index=vehicle_order_in_time_taken[min_time_index]
        fastest_orbit_index=orbit_order_in_time_taken[min_time_index]
        return [vehicles_list[fastest_vehicle_index],orbit_list[fastest_orbit_index]]





