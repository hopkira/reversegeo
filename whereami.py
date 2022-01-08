import googlemaps
import json
from secrets import *

gmaps = googlemaps.Client(key=key)

address = gmaps.reverse_geocode((54.5041124, -1.3408161), result_type=["route"])

print("I am located in",address[0]["address_components"][1]["long_name"],"in",address[0]["address_components"][2]["long_name"])