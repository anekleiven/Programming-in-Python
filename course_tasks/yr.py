# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:39:43 2024

@author: anekl
"""
"""
Hey play nice!
https://developer.yr.no/doc/TermsOfService/

Most important rules:
You must identify yourself
You must not cause unnecessary traffic
You must not overload our servers

https://developer.yr.no/doc/GettingStarted/
https://api.met.no/weatherapi/locationforecast/2.0/

Schema for the JSON format is included in the OpenAPI spec:
https://api.met.no/weatherapi/locationforecast/2.0/swagger
https://en.wikipedia.org/wiki/Geographic_coordinate_system

Longitude lines are perpendicular to and latitude lines are parallel to the
Equator.
Posisjoner:
latitude: parallel to Equator
Longitude: perpendicular to Equator
Order: lat-long-(height)

Ås
59.66705º N, 10.78863º Ø
59° 40′ 1.4′′N, 10° 47′ 19.1′′Ø
N,E(59.67, 10.79)

Bergen
60.35426º N, 5.35372º Ø
60° 21′ 15.3′′N, 5° 21′ 13.4′′Ø
(60.35, 5.35)

Trondheim
63.45163º N, 10.44784º Ø
63° 27′ 5.9′′N, 10° 26′ 52.2′′Ø
(63.45, 10.45)

Svanvik
69.45956º N, 30.03736º Ø
69° 27′ 34.4′′N, 30° 02′ 14.5′′Ø
(69.46, 30.04)

curl -A "MyTestApp/0.1" -s
'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=0'
you should never use more than 4 decimals in lat/lon coordinates anywhere in the
API
"""
import json
import urllib.request
import urllib.parse
import pandas as pd


# Noen posisjoner
latlon = {
'Ås': (59.67, 10.79),
'Bergen': (60.35, 5.35),
'Trondheim': (63.45, 10.45),
'Svanvik': (69.46, 30.04)
}


addr1 = 'https://www.tgxnet.no/squad.json'


# London
params = urllib.parse.urlencode({'lat': 51.5, 'lon': 0.0})
addr2 = "https://api.met.no/weatherapi/locationforecast/2.0/compact?{0}".format(params)

#req = urllib.request.Request(addr1)
req = urllib.request.Request(addr2)

# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: Thomas Graff<graff.thomas@gmail.com>)')


# %%

# Ask yr server for weather forcast for given location (London)

with urllib.request.urlopen(req) as response:
    jdata = response.read().decode('utf-8')
    print(response.info())
    
# %%

# Save JSON weather data to a file
with open('yr_london.json', 'w') as fh:
    fh.write(jdata)

# %%
# Read file with weather data and parse JSON into python datatypes
with open('yr_london.json', 'r') as fh:
    jdata = fh.read()
    
data = json.loads(jdata)


# dict_keys(['type', 'geometry', 'properties'])

# %%
# Extract some data from the data structure
loc = data['geometry']['coordinates']
time = data['properties']['meta']['updated_at']
timeseries = data['properties']['timeseries']

# %%
# Extract forcast data and put it into Pandas DataFrame
header = ('temp', 'relhum', 'press')
values = []
times = []
for td in timeseries:
    ts = td['time'] #[8:13]
    pred = td['data']['instant']['details']
    t = pred['air_temperature']
    rh = pred['relative_humidity']
    p = pred['air_pressure_at_sea_level']
    tup = (t, rh, p)
    times.append(ts)
    values.append(tup)
    
    
tsl = pd.DatetimeIndex(times)
weather = pd.DataFrame(values, columns=header, index=tsl)
weather.plot() 


# %%
#FINE