from weather import Weather
from vehicle import Vehicle
from orbit import Orbit
from orbitwithtraffic import OrbitWithTraffic
from decisionmaker import DecisionMaker
from console import Console
from vehiclename import VehicleName
from orbitname import OrbitName
if __name__ == '__main__':
    orb1 = Orbit(OrbitName(1).name, 18, 20)
    orb2 = Orbit(OrbitName(2).name, 20, 10)
    bike = Vehicle(VehicleName(1).name, 10, 1)
    tuktuk = Vehicle(VehicleName(2).name, 12, 1)
    car = Vehicle(VehicleName(3).name, 20, 1)
    vehicle_list=[tuktuk,bike,car]

    #---------------------------
    console=Console()
    inputs=console.getuserinput()

    #------------------------------
    weather = Weather(inputs[0])
    orbit1 = OrbitWithTraffic(orb1, inputs[1])
    orbit2 = OrbitWithTraffic(orb2, inputs[2])

    orbit_list=[orbit1,orbit2]
    #------------------------------



    decisionmaker=DecisionMaker()
    output=decisionmaker.makedecision(vehicle_list,orbit_list,weather)
    #print(output.OrbitWithTraffic._name)
    #print(output.estimated_time)
    #print(output.vehicle._name)
    output_string=output.OrbitWithTraffic._name+" "+output.vehicle._name
    console.displayoutput(output_string)
    












