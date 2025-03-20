# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:17:56 2024

@author: anekl
"""

def request_met(lat,lon): 
    ''' 
    input latitude and longitude
    return json data

    '''
    import urllib.parse
    import urllib.request
    params = urllib.parse.urlencode({'lat': lat, 'lon': lon})
    addr2 = "https://api.met.no/weatherapi/locationforecast/2.0/compact?{0}".format(params)
    req = urllib.request.Request(addr2)
    # Customize the default User-Agent header value:
    req.add_header('User-Agent', 'urllib-example/0.1 (Contact: Ane Kleiven<ane.kleiven@live.no>)')
    print(addr2)
    
    with urllib.request.urlopen(req) as response:
        jdata = response.read().decode('utf-8')
        #print(response.info())
        
    return jdata

data = request_met(51.5, 0.0)


#%% 

def download_json_met(loc_name): 
    ''' 
    Input location name 
    Save to json file 
    '''
    latlon = {
        'Ås': (59.67, 10.79),
        'Bergen': (60.35, 5.35),
        'Trondheim': (63.45, 10.45),
        'Svanvik': (69.46, 30.04)
        }
    lat,lon = latlon[loc_name]
    jdata = request_met(lat, lon)
    filename = f"yr_{loc_name}.json"
    with open(filename, 'w') as fh:
        fh.write(jdata)

download_json_met("Ås")

#%%
def tableize_json(loc_name):
    '''
    Read file with weather data and parse JSON into python datatypes
    Extract forecast data and put it into Pandas DataFrame
    '''
    import json
    import pandas as pd
    
    filename = f"yr_{loc_name}.json"
    with open(filename, 'r') as fh:
        jdata = fh.read()
        # convert json string to python datatype     
        data = json.loads(jdata)  
        print(data.keys())
        
        times = []
        values = [] 
        
        timeseries = data['properties']['timeseries']
        
        for td in timeseries:
            ts = td['time'] #[8:13]
            pred = td['data']['instant']['details']
            t = pred['air_temperature']
            rh = pred['relative_humidity']
            p = pred['air_pressure_at_sea_level']
            tup = (t, rh, p)
            times.append(ts)
            values.append(tup)
        print(times[-1], values[-1])
        tsl = pd.DatetimeIndex(times)
        header = ('temp', 'relhum', 'press')
        weather = pd.DataFrame(values, columns=header, index=tsl)
        return(weather) 

df = tableize_json("Ås")
         
#%%

def plot_weather(weatherdf, loc_name): 
    '''
    plot weather 
    '''
    weatherdf.plot()

plot_weather(df, "Ås")


'''
Next steps: 
    Error handling 
    Data in DB 
    Cache handling? 
''' 
