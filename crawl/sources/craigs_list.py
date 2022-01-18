import sys
from dataclasses import dataclass
from collections import namedtuple
import math

from craigslist import CraigslistHousing

from re import sub
from decimal import Decimal

from crawl import helpers

Coordinate = namedtuple('Coordinate', ['x','y'])

def search_craigslist_housing(site: str, area, category: str = 'apa'):
        yield result

def main(site = "newyork",
         area = "brk",
         category = 'apa',
         num_postings = 500):

    count = 0
    cl_h = CraigslistHousing(site=site, area = area,
                             category=category,
                             filters={'min_price': 1000,
                                      'max_price': 4000,
                                      'min_bedrooms': 2,
                                      'max_bedrooms': 2})


    for result in cl_h.get_results(sort_by='newest', geotagged=True):

        if count >  num_postings:
            sys.exit()
        else:
            price = helpers.parse_price(result['price'])
            lat, lon = helpers.parse_location(result['geotag'])
            last_updated = result['last_updated'].split(" ")[0]
            datetime = result['datetime'].split(" ")[0]
            location = helpers.parse_where(result['where'].lower())
            url = result['url']
            id_ = "craigslist_" + result['id']

            msg = helpers.create_message("postings", symbols = {  'gid': id_,
                                                                  'site': site,
                                                                  'category': category,
                                                                  'area' : area,
                                                                  'last_updated': last_updated,
                                                                  'date': datetime,
                                                                  'place': location,
                                                                  'url' : url},
                                                      fields= {'lon': lon, 'lat': lat,'price': int(price)})

            print(msg)
            helpers.send_tcp_messages(msg)
            count += 1


if __name__ == "__main__":
    main() 
