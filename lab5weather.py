from enum import Enum

class WeatherType(Enum):
    SUNNY = 1
    CLOUDY = 2
    RAINY = 3
    FOGGY = 4


class Weather:
    def __init__(self, day, city , country, temp, humidity, wind_speed, weather_type ):
        self.day = day
        self.city = city
        self.country = country
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.weather_type = weather_type

    def __str__(self):
        return f"date: {self.day}, city: {self.city}, country: {self.country}, temp: {self.temp}°С ,\
              humidity: {self.humidity}%, wind: {self.wind_speed}m/s , Weather type: {self.weather_type.name} "
    
    def __repr__(self):
        return f"Wheather('{self.day}, {self.city}, {self.country}, {self.temp}, {self.humidity}, {self.wind_speed}') "


class WeatherCalendar(Weather):
    def __init__(self):
        self.weather_info = []

    def add_weather_info(self, weather):
        self.weather_info.append(weather)

    def find_max_temperature(self, day):
        max_temp = None
        for info in self.weather_info:
            if info.day == day:
                if max_temp is None or info.temp > max_temp:
                        max_temp = info.temp

        if max_temp is not None:
            result = max_temp
        else:
            result = "Not enough data" 
        return result    

    def is_lviv_weather(self, humitidy, weather_type):
        if humitidy > 80 and weather_type == WeatherType.RAINY:
            result = "The typical day in Lviv"
        else:
            result = "u r the lucky man"
        return result   
         
    def get_day(self, record):
        return record.day

    def sort_weather_info(self):
        self.weather_info.sort(key = self.get_day)


if __name__ == "__main__": 
    weather1 = Weather("2023-11-01", "Lviv", "Ukraine", 14, 91, 10, WeatherType.CLOUDY)
    weather2 = Weather("2023-11-02", "Lviv", "Ukraine", 14, 89, 5, WeatherType.SUNNY)
    weather3 = Weather("2023-11-03", "Lviv", "Ukraine", 16, 81, 12, WeatherType.RAINY)
    weather4 = Weather("2023-11-04", "Lviv", "Ukraine", 9, 92, 9, WeatherType.RAINY)

    calendar = WeatherCalendar()
    calendar.add_weather_info(weather2)
    calendar.add_weather_info(weather1)
    calendar.add_weather_info(weather3)
    calendar.add_weather_info(weather4)

    print("Weather Records:")
    for record in calendar.weather_info:
        print(record)

    calendar.sort_weather_info()

    print("\nWeather Records Sorted by Day:")
    for record in calendar.weather_info:
        print(record)

    max_temp = calendar.find_max_temperature("2023-11-03")
    print(f"\nMax Temperature for 2023-10-25: {max_temp}°C")

    prediction = calendar.is_lviv_weather(92, WeatherType.RAINY)
    print("\nLviv Weather Prediction:", prediction)




            
       
                    