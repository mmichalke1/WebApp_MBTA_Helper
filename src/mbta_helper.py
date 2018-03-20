import urllib.request   # urlencode function
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# url_testing = "https://maps.googleapis.com/maps/api/geocode/json?address=Babson%20College"
# print(get_json(url_testing))


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = GMAPS_BASE_URL + place_name.replace(' ', '%20')
    JSON = get_json(url)
    lat = JSON['results'][0]['geometry']['location']['lat']
    lng = JSON['results'][0]['geometry']['location']['lng']
    return lat, lng


# place_testing = 'Boston College'
# print(get_lat_long(place_testing))

latitude = 0
longitude = 0
def get_nearest_station(lat, lng):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    url = MBTA_BASE_URL + '?api_key={}&lat={}&lon={}&format=json'.format(MBTA_DEMO_API_KEY, lat,lng)
    JSON = get_json(url)
    nearest_station = JSON['stop'][0]['stop_name']
    distance = JSON['stop'][0]['distance']
    return nearest_station, distance

# print(get_nearest_station(42.33554, -71.16849))
# a, b = get_lat_long('Boston College')
# print(get_nearest_station(a, b))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    a, b = get_lat_long(place_name)
    return get_nearest_station(a, b)

