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



def search_craigslist_housing(site: str, area, category: str = 'housing'):
    cl_h = CraigslistHousing(site=site, area = area,
                             category='housing',
                             filters={'min_price': 1000,
                                      'max_price': 4000,
                                      'min_bedrooms': 2,
                                      'max_bedrooms': 2})

    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        yield result



def main():
    postings = list()
    for result in search_craigslist_housing("newyork", "brk"):
        resilresult['name'] 
        import pdb;pdb.set_trace()

main() 
