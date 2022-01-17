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
    cl_h = CraigslistHousing(site=site, area = area,
                             category='apa',
                             filters={'min_price': 1000,
                                      'max_price': 4000,
                                      'min_bedrooms': 2,
                                      'max_bedrooms': 2})

    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        yield result

def main(site = "newyork",
         area = "brk",
         num_postings = 5):

    count = 0
    for result in search_craigslist_housing("newyork", "brk"):
        if count > 5:
            sys.exit()
        else:
            price = helpers.parse_price(result['price'])
            lat, lon = helpers.parse_location(result['geotag'])
            last_updated = result['last_updated'].split(" ")[0]
            datetime = result['datetime'].split(" ")[0]
            location = helpers.parse_where(result['where'].lower())
            url = result['url']
            id_ = int(result['id'])

            msg = helpers.create_message("postings", symbols = { 'url': url,
                                                                  'last_updated': last_updated,
                                                                  'date': datetime,
                                                                  'place': location},
                                                      fields= {'posting_id': id_, 'lon': lon, 'lat': lat,'price': int(price)})

            print(msg)
            helpers.send_tcp_messages(msg)
            count += 1


if __name__ == "__main__":
    main() 
