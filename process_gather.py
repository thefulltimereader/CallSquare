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

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    vid = sys.argv[1]

    sys.stdout.write("ID: %s\n" % (id))

    f = foursquare.Api()
    x = f.checkin(USER,PASS,vid=vid)
