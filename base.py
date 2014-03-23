from local_settings import DB_APP_KEY, DB_APP_SECRET, ACCESS_TOKEN

from termprint import *
import simplejson
import sys
import os
import urllib
import unittest
import dropbox

def doauth():
	key, secret = DB_APP_KEY, DB_APP_SECRET
	access_token = ACCESS_TOKEN

	if not ACCESS_TOKEN:
	    # promot input
	    termprint('ERROR', 'You need to generate an access token first.\n')
	    termprint('ERROR', 'Run: ./test-get-access-token.sh')
	    sys.exit()
	return key, secret, access_token

