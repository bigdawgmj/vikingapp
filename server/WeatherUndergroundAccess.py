from configparser import ConfigParser
import os, urllib2, json

class WeatherUndergroundAccess:
    def __init__(self):
        config = ConfigParser() 
        ini_path = os.path.join(os.getcwd(), 'server\\vsts_config.ini')
        config.read(ini_path)
        self.base_url = 'http://api.wunderground.com/api/' + config.get('wu', 'accessKey')

    def get_weather(self, city):
        f = urllib2.urlopen(self.base_url + '/' + 'conditions/q/UT/' + city + '.json')
        json_string = f.read()
        # my_json = json.loads(json_string)
        # full_city = my_json['display_location']['full']
        # my_json['temp_f']
        # my_json['weather']
        # my_json['relative_humidity']
        # my_json['feelslike_f']
        # my_json['UV']
        # my_json['precip_today_in']
        # my_json['visibility_']
        return json_string
