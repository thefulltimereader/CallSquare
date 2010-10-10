#! /usr/bin/env python
"""\
Handles gathers -- checks into location number n
"""

import sys
import os
import foursquare

USER = 'sobell@nyu.edu'
PASS = 'password1'

def usage():
    sys.stdout.write( __doc__ % os.path.basename(sys.argv[0]))

if __name__ == "__main__":

    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    num = sys.argv[1]
    ids = sys.argv[2]

    ids = ids.split('&')
    vid = ids[int(num)-1]

    f = foursquare.Api()
    x = f.checkin(USER,PASS,vid=vid)
