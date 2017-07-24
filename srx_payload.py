#!/usr/bin/env python

import sys
import logging
import logging.handlers
#import requests


def create_payload(sourceip, srxuser, srxpass, srxmgtip, srxrestport):
    
    headers = {'content-type': 'application/xml'}
    payload = ("<lock-configuration/><load-configuration><configuration>"
               "<security><address-book><name>global</name><address>"
               "<name>" + srxuser + "_" + sourceip + "</name>"
               "<ip-prefix>" + sourceip + "</ip-prefix>"
               "</address><address-set><name>" + srxuser + "_addrs</name>"
               "<address><name>" + srxuser + "_" + sourceip + "</name>"
               "</address></address-set></address-book></security>"
               "</configuration></load-configuration><commit/>"
               "<unlock-configuration/>")

    url = "http://" + srxmgtip + ":" + srxrestport + "/rpc"
    print "Assembled URL: ", url, "/n request body is" + payload




def main():
    """Obtain the offending source IP and pass it to the update SRX function"""
    # Read in the source IP passed in from Custom Action Rule
    sourceip = str(sys.argv[1])
    print 'Offending Source IP: ', sourceip
    # Read in the srx user name passed in from Custom Action Rule
    srxuser = str(sys.argv[2])
    print 'SRX Username: ', srxuser
    # Read in the srx password passed in from Custom Action Rule
    srxpass = str(sys.argv[3])
    print 'SRX Password: ', srxpass
    # Read in the srx management IP passed in from Custom Action Rule
    srxmgtip = str(sys.argv[4])
    print 'SRX Management IP: ', srxmgtip
    # Read in the srx REST api listen port passed in from Custom Action Rule
    print 'Command line List length: ', len(sys.argv)
    # srxrestport = str(sys.argv[5]) if len(sys.argv) > 5 else '3000'
    try:
        srxrestport = str(sys.argv[5])
    except IndexError:
        srxrestport = '3000'
    print 'SRX REST API Port: ', srxrestport
    # Call the function to update the SRX configuration with the source IP
    create_payload(sourceip, srxuser, srxpass, srxmgtip, srxrestport)


if __name__ == "__main__":
    main()
