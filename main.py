from weather import Weather
from vehicle import Vehicle
from orbit import Orbit
from orbitwithtraffic import OrbitWithTraffic
from decisionmaker import DecisionMaker
from console import Console
from vehicletype import VehicleType
from orbitname import OrbitName
from weather import WeatherFactory
from weather import WeatherType
if __name__ == '__main__':
    orb1 = Orbit("Orbit1", 18, 20)
    orb2 = Orbit("Orbit2", 20, 10)
    #orb1 = Orbit(OrbitName.Orbit1, 18, 20)
    #orb2 = Orbit(OrbitName.Orbit2, 20, 10)
    bike = Vehicle(VehicleType.Bike, 10, 1)
    tuktuk = Vehicle(VehicleType.TukTuk, 12, 1)
    car = Vehicle(VehicleType.Car, 20, 1)
    vehicle_list=[tuktuk,bike,car]

    #---------------------------
    console=Console()
    inputs=console.getuserinput()

    #------------------------------
    option = WeatherType(inputs[0])
    weather = WeatherFactory.get_weather(option)
    orbit1 = OrbitWithTraffic(orb1, inputs[1])
    orbit2 = OrbitWithTraffic(orb2, inputs[2])

    orbit_list=[orbit1,orbit2]


    #------------------------------


    decisionmaker=DecisionMaker()
    output=decisionmaker.makedecision(vehicle_list,orbit_list,weather)

    print(output.OrbitWithTraffic._name)
    print(output.estimated_time)
    print(output.vehicle._type)

     
    #output_string=output.OrbitWithTraffic._name+" "+output.vehicle._name
    #console.displayoutput(output_string)
    
    












