#! /usr/bin/env python
"""
Usage: %s <lat> <lon>

From lat-lon location, returns a list of venues using the Foursquare API
"""

import sys
import os
import httplib2
import foursquare
import twilio

def usage():
    sys.stdout.write( __doc__ % os.path.basename(sys.argv[0]))

if __name__ == "__main__":

    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    lat = sys.argv[1]
    lon = sys.argv[2]
    lim = 20

    f = foursquare.Api()
    x = f.get_venues(lat,lon,l=lim)
    for i in x['groups'][0]['venues']:
        print i['name']

    
