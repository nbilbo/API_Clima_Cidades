from datetime import datetime
import typing
import requests


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def weather_info(api_key: str, city: str) -> typing.Optional[typing.Dict]:
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url)
    weather_info = response.json()
    if weather_info['cod'] == 200:
        kelvin = 273
        info = {}
        info['temp'] = int(weather_info['main']['temp'] - kelvin)
        info['feels_like'] = int(weather_info['main']['feels_like'] - kelvin)
        info['pressure'] = weather_info['main']['pressure']
        info['humidity'] = weather_info['main']['humidity']
        info['speed'] = weather_info['wind']['speed'] * 3.6
        info['sunrise'] = weather_info['sys']['sunrise']
        info['sunset'] = weather_info['sys']['sunset']
        info['timezone'] = weather_info['timezone']
        info['clouds'] = weather_info['clouds']['all']
        info['description'] = weather_info['weather'][0]['description']
        sunrise = info['sunrise']
        sunset = info['sunset']
        timezone = info['timezone']
        info['sunrise'] = time_format_for_location(sunrise + timezone)
        info['sunset'] = time_format_for_location(sunset + timezone)
        return info

    return None
