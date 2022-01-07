import time
import socket

import json
import pdb
import ast

from decimal import Decimal
from re import sub
import socket

from crawl import helpers

import time

def price_convert(price):
    value = Decimal(sub(r'[^\d.]', '', price))
    return value

def parse_location(where):
    if 'bay ridge' in where:
        return 'bay ridge'
    elif 'gowanus' in where:
        return 'gowanus'
    elif 'windsor' in where:
        return 'windsor terrace'
    elif 'flatbush' in where:
        return 'flatbush'
    elif 'boreum' in where:
        return 'boreum hill'
    elif 'lefferts' in where:
        return 'prospect lefferts gardens'
    elif 'prospect heights' in where:
        return 'prospect heights'
    elif 'prospect park' in where:
        return 'prospect park'
    elif 'park slope' in where:
        return 'park slope'
    elif 'south slope' in where:
        return 'south slope'
    elif 'bedford' in where:
        return 'bedford-stuyvesant'
    elif 'greenpoint' in where:
        return 'greenpoint'
    elif 'williamsburg' in where:
        return 'williamsburg'
    elif 'dumbo' in where:
        return 'dumbo'
    elif 'yonkers' in where:
        return 'yonkers'
    elif 'woodside' in where:
        return 'woodside'
    elif 'woodlawn' in where:
        return 'woodlawn'
    elif 'yellowstone' in where:
        return 'yellowstone'
    elif 'yorktown' in where:
        return 'yorktown'
    elif 'staten' in where:
        return 'staten island'
    elif 'borough park' in where:
        return 'borough park'
    elif 'corona' in where:
        return 'corona'
    elif 'queens' in where:
        return 'queens'
    else:
        return 'notparsed'

def main():
    path = 'data/brooklyn.txt'
    file_ = open(path,'r')


    #df = pd.DataFrame(rows_list)  
    rows_list = []

    for i in file_.readlines():
        posting = i.rstrip()
        posting = ast.literal_eval(posting)
        posting['price'] = price_convert(posting['price'])
        if posting['price'] > 1000:
            try:
                lat = posting['geotag'][0]
                lon = posting['geotag'][1]
            except:
                lat = 0.0
                lon = 0.0
            posting['datetime'] = posting['datetime'].split(" ")[0]
            posting['where'] = posting['where'].rstrip()
            posting['location'] = parse_location(posting['where'].lower())
            last_updated = posting['last_updated'].split(" ")[0]

            rows_list.append(posting)
            price = int(posting['price'])
            count += 1

            msg = helpers.create_message("postings4", symbols = {
                                                                        'id': str(posting['id']),
                                                                        'last_updated': str(last_updated),
                                                                        'date': str(posting['datetime']),
                                                                        'place': str(posting['location'])},
                                                                        fields= {'lon': lon, 'lat': lat,'price': price})
                                            
            helpers.send_tcp_messages(msg)

if __name__ == "__main__":
    time.sleep(5)
    main()


