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
        return json_string
