#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
import urllib
from datetime import datetime, timedelta
from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_url(city):
    str_url = 'http://sugg.us.search.yahoo.net/gossip-gl-location/?appid=weather&output=xml&command=' + city
    with request.urlopen(str_url) as f:
        data = f.read().decode('utf-8')
    data_lxml = BeautifulSoup(data, 'lxml').find('s')['d']
    data_woeid = data_lxml[data_lxml.index('woeid') + 6:data_lxml.index('woeid') + 13]
    str_sql = 'select+*+from+weather.forecast+where+woeid%3D' + data_woeid + '+and+u%3D%22c%22&diagnostics=true'
    new_url = 'https://query.yahooapis.com/v1/public/yql?q=' + str_sql
    return new_url

def get_weather(data) :
    weather = {}
    soup = BeautifulSoup(data, 'lxml')
    weather['city'] = soup.find('yweather:location')['city']
    weather['country'] = soup.find('yweather:location')['country']
    weather['province'] = soup.find('yweather:location')['region']
    weather_date = soup.find('yweather:condition')['date'].split(',')[0]
    weather_today = soup.find('yweather:forecast', day = weather_date)
    weather['today'] = {'text' : weather_today['text'], 'lowTemperature' : weather_today['low'], 'highTemperature' : weather_today['high']}

    current_day = datetime.today()
    current_day_next_1 = current_day + timedelta(days= 1)
    current_day_next_1_str = datetime.strftime(current_day_next_1, '%d %b %Y')
    current_day_next_1_data = soup.find('yweather:forecast', date = current_day_next_1_str)
    weather['nextDday'] = {'text' : current_day_next_1_data['text'], 'lowTemperature': current_day_next_1_data['low'], 'highTemperature' : current_day_next_1_data['high']}
    return weather

if __name__ == '__main__' :
    url = get_url(input('please input your city:'))
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'User-Agent:Mozilla/5.0'})) as f:
        data = f.read().decode('utf-8')
    print(get_weather(data))


