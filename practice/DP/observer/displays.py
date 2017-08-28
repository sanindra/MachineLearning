from models import Observer, DisplayElement


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weatherdata):
        #self.weatherData = weatherdata
        self.temp, self.humidity = 0.0, 0.0
        weatherdata.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp, self.humidity = temp, humidity
        self.display()

    def display(self):
        print "Current conditions: {0} F degrees and {1} % humidity".format(self.temp, self.humidity)
