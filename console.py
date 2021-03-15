from weather import WeatherType


class Console:

    def getuserinput(self):
        val = input("Enter your inputs: ")
        temp = []
        temp.append(val)
        temp = temp[0].split()
        r = [temp[0], int(temp[1]), int(temp[2])]
        return r

    def displayoutput(self, output):
        print(output)
