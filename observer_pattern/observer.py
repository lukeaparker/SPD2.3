class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers(self):
        pass


# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# WeatherData now implements the subject interface.
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):
    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData  # save the ref in an attribute.
        weatherData.registerObserver(self)  # register the observer
        # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(
            "Current conditions:",
            self.temerature,
            "F degrees and",
            self.humidity,
            "[%] humidity",
            "and pressure",
            self.pressure,
        )


class StatisticsDisplay(Observer):
    # The StatisticsDisplay class should keep track of the min/average/max
    # measurements and display them.

    # All recording weather data
    temps = []
    humidities = []
    pressures = []

    # stats are recorded as (Min,Average,Max)
    temps_stats = (None, None, None)
    humidities_stats = (None, None, None)
    pressures_stats = (None, None, None)

    def __init__(self, weather_data):
        # register observer
        self.weather_data = weather_data
        weather_data.register_observer(self)

    @staticmethod
    def update_helper(measurements, stat):
        m_min = measurements[0]
        m_max = measurements[0]
        for measurment in measurements:
            if measurment < m_min:
                m_min = measurment
            elif measurment > m_max:
                m_max = measurment
        stat = (m_min, sum(measurements) / \
            len(measurements), m_max)

    def update(self, temp, humidity, pressure):
        self.temps.append(temp)
        self.update_helper(self.temps, self.temps_stats)

        self.humidities.append(humidity)
        self.update_helper(self.humidities, self.humidities_stats)

        self.pressures.append(pressure)
        self.update_helper(self.pressures, self.pressures_stats)

        print("Updated!")

    def display(self):
        print(
            f"""Pressure
            min:     {self.pressures_stats[0]}
            max:     {self.pressures_stats[2]}
            average: {self.pressures_stats[1]}
        temps:
            min:     {self.temps_stats[0]}
            max:     {self.temps_stats[2]}
            average: {self.temps_stats[1]}
        humidity:
            min:     {self.humidities_stats[0]}
            max:     {self.humidities_stats[2]}
            average: {self.humidities_stats[1]}\n"""
        )


class ForecastDisplay(Observer):
    """
    The ForecastDisplay class shows the weather forcast based on the current
    temperature, humidity and pressure. Use the following formuals :
    forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
    forcast_humadity = humidity - 0.9 * humidity
    forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
    """

    forecast_temp = 0
    forecast_humidity = 0
    forecast_pressure = 0

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humidity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print(
            f"""Forecast Display
        temp:     {self.forecast_temp}
        humidity: {self.forecast_humidity}
        pressure: {self.forecast_pressure}
        """
        )


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
