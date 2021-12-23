from dataclasses import dataclass
from collections import namedtuple
import math

from craigslist import CraigslistHousing
import geopy.distance

import matplotlib.path as mplPath
import numpy as np

from re import sub
from decimal import Decimal

Coordinate = namedtuple('Coordinate', ['x','y'])

class SearchArea:

    def __init__(self, x, y):
        self.ref = Coordinate(x=x, y=y)
        self.input_coordinates = []
        self.input_coordinates.append(self.ref)
        self.norm_coords = []

    def add(self, x, y):
        self.input_coordinates.append(Coordinate(x=x, y=y))
        
    def dist_between(self, x, y):
        return math.sqrt((self.ref.x - x)**2 + (self.ref.y - y)**2)
        
    def create_polyogon(self):
        norm_coords = []
        for coord in self.input_coordinates:
            norm_dist = math.sqrt((self.ref.x - coord.x)**2 + (self.ref.y - coord.y)**2)
            norm_coords.append(norm_dist)
        poly = []
        mod = len(norm_coords)
        for index, value in enumerate(norm_coords):
            poly.append([norm_coords[index%mod], norm_coords[(index+1)%mod]])

        self.bb_path = mplPath.Path(np.array(poly))

    def __contains__(self, coord):
        return self.bb_path.contains_point((self.ref.x - coord[0], self.ref.y - coord[1]))


# You can get an approximate amount of results with the following call:
#print(cl_h.get_results_approx_count())

def determine_geo_location(coords1, coords2) -> int:
    return geopy.distance.distance(coords1, coords2).miles


def search_craigslist_housing(site: str, category: str = 'housing') -> CraigslistHousing:
    cl_h = CraigslistHousing(site=site,
                             category='housing',
                             filters={'min_price': 1000,
                                      'max_price': 4000,
                                      'min_bedrooms': 2,
                                      'max_bedrooms': 2})

    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        yield result


def price_convert(price):
    value = Decimal(sub(r'[^\d.]', '', price))
    return value

def calculate_subway(apartment_coord):
    subways = {"grove_street": Coordinate(x=40.719606, y=-74.050522),
    "newport": Coordinate(x=40.726676, y=-74.034767),
    "journal_square": Coordinate(x=40.7346, y=-74.0632)}
    d_ = {}
    for key, value in subways.items():
        dist = geopy.distance.distance((value.x, value.y), (apartment_coord[0], apartment_coord[1])).miles
        d_[key] = dist
    return d_
        

def main():
    #coord1 = (40.732896, -74.079393)
    #coord2 = (40.762678, -74.020342)
    #coord3 = (40.716635, -74.028581)
    #coord4 = (40.689696, -74.068774)
    #coord5 = (40.701800, -74.097417)
    #search = SearchArea(40.739861,-74.148238)
    #search.add(40.769963, -73.981463)
    #search.add(40.651475, -74.05977)
    #search.create_polyogon()
    #grove_street = (40.719074, -74.050552)

    for result in search_craigslist_housing("newjersey"):
        value = price_convert(result['price'])
        d_ = calculate_subway(result['geotag'])

#        str_ = "%s, %s" % (dist, value)
#        print(result)
#        print(str_)

        #print(result)

if __name__ == "__main__":
    main()



