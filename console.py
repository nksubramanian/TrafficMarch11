from weather import WeatherOption
class Console:
    def getuserinput(self):
        val = input("Enter your inputs: ")
        temp = []
        temp.append(val)
        temp = temp[0].split()
        if (temp[0] not in {WeatherOption(1).name,WeatherOption(2).name,WeatherOption(3).name}):
            raise Exception("Please enter valid weather as first input")
        r = [temp[0], int(temp[1]), int(temp[2])]
        return r

    def displayoutput(self,output):
        print(output)







