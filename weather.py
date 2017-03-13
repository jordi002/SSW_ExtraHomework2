#!/usr/bin/env python
# -*- coding: utf-8 -*-
#vim: set fileencoding=utf8 :
'''
Web client to consult weather data

@author: jgm17@alumnes.udl.cat
'''

import sys
import requests
import json
import time

api_key = None
hour = int(time.strftime("%H"))+1

class WeatherClient(object):
    '''Client for weather underground'''

    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac": "/almanac/q/CA/",
                    "hourly": "/hourly/q/CA/"}

    def __init__(self, api_key):
        self.api_key = api_key

    def almanac(self, location):
        # Obtenir url:

        url = WeatherClient.url_base + self.api_key + \
                WeatherClient.url_service["almanac"] + location + "." + "json"
        web = requests.get(url)

        #Dades i Retorn
        data = json.loads(web.text)
        return data["almanac"]

    def print_almanac(almanac_data):
        print "High Temperatures:"
        #Màxima diària record
        print "Record on this date %s (%s) " %(almanac_data["high"]["record"]["C"],almanac_data["high"]["year"])
        #Mitja de màximes
        print "Average on this date", almanac_data["high"]["normal"]["C"]

        print "Low Temperatures:"
        #Mínima diària record
        print "Record on this date %s (%s) " %(almanac_data["low"]["record"]["C"],almanac_data["low"]["year"])
        #Mitja de mínimes
        print "Average on this date", almanac_data["low"]["normal"]["C"]

    def hourly(self, location):
            # Obtenir url:

            url = WeatherClient.url_base + self.api_key + \
                    WeatherClient.url_service["hourly"] + location + "." + "json"
            web = requests.get(url)

            #Dades i Retorn
            data = json.loads(web.text)
            return data["hourly_forecast"]

    def print_hourly(hourly_data):
        '''
        Parse it to provide relevant information to the user, for example,
        a short hourly forecast.
        '''
        #source: https://www.wunderground.com/weather/api/d/docs?d=data/hourly&MR=1#fcttime
        print "HOURLY REPORT"
        current = hourly_data[0]
        print "Current weather:"
        #Temperatura:
        print "Temperature: %s C" % (current["temp"]["metric"])
        #Sensació tèrmica:
        print "Thermal sensation: %s C" % (current["feelslike"]["metric"])
        #Condició climàtica:
        print "Condition: %s" % (current["condition"])
        #Humitat:
        print "Humidity: %s %" % (current["humidity"])
        #Gebre:
        print "Dewpoint: %s %" % (current["dewpoint"])
        #Vent:
        print "Wind speed: %s Km/h" % (current["wspd"]["metric"])

        #Clothes advertisement:
        #First Time in the morning--->Calm
        if hour < 10 :
            print "Right now it's all calm, enjoy outside!"
        #Later wind and advise to take a sweater
        if hour > 10 :
            print "It's kinda gonna evolve on a windy weather"
            print "Don't forget a sweater to go outside or you will regret! "

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Introduir api_key per línia de comandes"

    wc = WeatherClient(api_key)
    print_almanac(wc.almanac("Lleida")
    
