from models import Subject

class WeatherData(Subject):

    def __init__(self):
        self.observers = []

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure )

    def measurements_changed(self):
        self.notify_observer()
