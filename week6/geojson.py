# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:44:10 2016

@author: karenyang
"""

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    
    
'''
Enter location: Seattle
Retrieving http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Seattle
Retrieved 1729 characters
{
    "status": "OK", 
    "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE", 
                "bounds": {
                    "northeast": {
                        "lat": 47.734145, 
                        "lng": -122.2359031
                    }, 
                    "southwest": {
                        "lat": 47.4919119, 
                        "lng": -122.4596959
                    }
                }, 
                "viewport": {
                    "northeast": {
                        "lat": 47.734145, 
                        "lng": -122.2359031
                    }, 
                    "southwest": {
                        "lat": 47.4919119, 
                        "lng": -122.4596959
                    }
                }, 
                "location": {
                    "lat": 47.6062095, 
                    "lng": -122.3320708
                }
            }, 
            "address_components": [
                {
                    "long_name": "Seattle", 
                    "types": [
                        "locality", 
                        "political"
                    ], 
                    "short_name": "Seattle"
                }, 
                {
                    "long_name": "King County", 
                    "types": [
                        "administrative_area_level_2", 
                        "political"
                    ], 
                    "short_name": "King County"
                }, 
                {
                    "long_name": "Washington", 
                    "types": [
                        "administrative_area_level_1", 
                        "political"
                    ], 
                    "short_name": "WA"
                }, 
                {
                    "long_name": "United States", 
                    "types": [
                        "country", 
                        "political"
                    ], 
                    "short_name": "US"
                }
            ], 
            "place_id": "ChIJVTPokywQkFQRmtVEaUZlJRA", 
            "formatted_address": "Seattle, WA, USA", 
            "types": [
                "locality", 
                "political"
            ]
        }
    ]
}
lat 47.6062095 lng -122.3320708
Seattle, WA, USA
'''    