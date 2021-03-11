class Weather:
    _cratereffect={"SUNNY":-10,"RAINY":20,"WINDY":0}
    Sunny_weather={"Car": True,"Bike":True,"TukTuk":True}
    Rainy_weather={"Car": True,"Bike":False,"TukTuk":True}
    Windy_weather={"Car": True,"Bike":True,"TukTuk":False}

    def __init__(self, name):
        self._name=name

    def crater_change(self):
        return self._cratereffect[self._name]

    def vehicles_allowed(self,vehicle):
        if self._name=="SUNNY":
            return self.Sunny_weather[vehicle._name]
        elif self._name=="RAINY":
            return self.Rainy_weather[vehicle._name]
        if self._name=="WINDY":
            return self.Windy_weather[vehicle._name]


