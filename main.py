from dataclasses import dataclass
from collections import namedtuple
import math
import time
import socket

from craigslist import CraigslistHousing
import geopy.distance

#import matplotlib.path as mplPath
import numpy as np

from re import sub
from decimal import Decimal
from contextlib import contextmanager

        conn.sendall(sendable_data(a + b))

import socket
from contextlib import contextmanager

@contextmanager
def socketcontext(*args, **kw):
    s = socket.socket(*args, **kw)
    try:
        yield s
    finally:
        s.close()

#with socketcontext(socket.AF_INET, socket.SOCK_DGRAM) as s:
def main():

    HOST = 'questdb'
    PORT = 9009
    # For UDP, change socket.SOCK_STREAM to socket.SOCK_DGRAM
    #time.sleep(30)
    filename = 'results.csv'
    file_ = open(filename,'w')
#    with socketcontext(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #    s.connect((HOST, PORT))
    for result in search_craigslist_housing("newjersey"):
        print(result)
        #file_.write(result)
   #file_.write('hey')
            #value = price_convert(result['price'])
            #d_ = calculate_subway(result['geotag'])
            #newport = d_['newport']
            #id_ = result['id']
            #url = result['url']
            #record = b'test2,id={id_},rent={value},url={url},distance={newport},timestamp={time.time_ns())).encode()}'

        #    s.sendall((record))
            #  except socket.error as e:
   #     print("Got error: %s" % (e))

#        sock.close()

#    try:
#      sock.connect((HOST, PORT))
#      # Single record insert
#      # Omitting the timestamp allows the server to assign one
#      sock.sendall(('trades,name=server_timestamp value=12.4\n').encode())
#      # Streams of readings must be newline-delimited
#      sock.sendall(('trades,name=ilp_stream_1 value=12.4\ntrades,name=ilp_stream_2 value=11.4\n').encode())



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


#        str_ = "%s, %s" % (dist, value)
#        print(result)
#        print(str_)

        #print(result)


if __name__ == "__main__":
    main()



