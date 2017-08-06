#!/usr/bin/env python

"""
    1) Create a file outside of this proj dir called "plex_token.py":

    touch ../plex_token.py
    
    2) add this line to the newly created file:

    baseurl = 'the url to your server'
    token = 'your plex token'

    3) Edit the "basurl" variable below to point to your Plex server

    4) Edit the "plexClients" variable to include the name of your plex client(s) this app will control.

    5) Edit the "plexLibraries" variable to remap your specific library names to the app specific names. 
    ...for instance, if your Plex "Movies" are located in your Plex library as "Films", update that
    line so it looks like: 

    "Movies" : ["Films"],

    6) For Google Calendar integration add your "gkey" to the "plex_token.py" file 
    ...(https://docs.simplecalendar.io/find-google-calendar-id/):

    gkey = "the key"

    7) If using the Google Calendar integration exclusively, set this to true below:

    useGoogleCalendar
    
"""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../plex_token.py

try:
    import plex_token as plex_token
except ImportError as e:
    print "+++++ Cannot find plex_token file. Make sure you create a plex_token.py file with the appropriate data."
    raise e

baseurl = plex_token.baseurl
token = plex_token.token
gkey = plex_token.gkey

'''
*
* List of plex clients to use (add multiple clients to control multiple TV's)
*
'''
plexClients = ['RasPlex']

plexLibraries = {
    "TV Shows" : ["TV Shows"],
    "Movies"   : ["Movies"],
    "Music"    : ["Music"],
    "Commercials" : ["Commercials"],
}

useGoogleCalendar = False

useCommercialInjection = True

# How many seconds to pad commercials between each other / other media
commercialPadding = 5

"""
Specify the path to this controller on the network (i.e. 'http://192.168.1.28' - no trailing slash).
Also specify the desired port to run the simple http webserver. The daily generated
schedule will be served at "http://<your-ip>:<your-port>/" (i.e. "http://192.168.1.28:8000/"). 

You can also leave the below controllerServerPath empty if you'd like to run your own webserver.
"""
controllerServerPath = "http://192.168.1.28"
controllerServerPort = "8000"

dailyUpdateTime = "12:00 AM"

debug_mode = True