from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web

def GoogleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)