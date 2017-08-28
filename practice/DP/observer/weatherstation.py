from weatherdata import WeatherData
from displays import CurrentConditionDisplay

if __name__ == '__main__':
    weatherData = WeatherData()
    cdisplay = CurrentConditionDisplay(weatherData)
    weatherData.set_measurements(80, 65, 30.4)
    weatherData.set_measurements(82, 70, 29.2)
    weatherData.set_measurements(78, 90, 29.2)