from weather import Weather
from vehicle import Vehicle
from internalorbit import InternalOrbit
from orbit import Orbit
from decisionmaker import DecisionMaker
from console import Console
if __name__ == '__main__':
    orbit1 = InternalOrbit("ORBIT1",18, 20)
    orbit2 = InternalOrbit("ORBIT2",20, 10)
    bike = Vehicle("Bike", 10, 2)
    car = Vehicle("Car", 20, 3)
    tuktuk=Vehicle("TukTuk", 12, 1)
    vehicle_list=[bike,tuktuk,car]

    #---------------------------
    console=Console()
    inputs=console.getuserinput()

    #------------------------------
    weather = Weather(inputs[0])
    orb1 = Orbit(orbit1, inputs[1])
    orb2 = Orbit(orbit2, inputs[2])

    orbit_list=[orb1,orb2]
    #------------------------------

    decisionmaker=DecisionMaker()
    outputs=decisionmaker.makedecision(vehicle_list,orbit_list,weather)
    console.displayoutput(outputs[0]._name+" "+outputs[1]._name)








