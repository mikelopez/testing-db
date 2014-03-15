from local_settings import DB_APP_KEY, DB_APP_SECRET, ACCESS_TOKEN

from termprint import *
import simplejson
import sys
import os
import urllib
import unittest
import dropbox


class TestDropboxClientSetup(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_access(self):
        key, secret = DB_APP_KEY, DB_APP_SECRET
        access_token = ACCESS_TOKEN
        if not ACCESS_TOKEN:
            # promot input
            termprint('ERROR', 'You need to generate an access token first.\n')
            termprint('ERROR', 'Run: ./test-get-access-token.sh')
            sys.exit()
        client = dropbox.client.DropboxClient(access_token)
        root = client.metadata('/')

        for v in root:
            for content in v.get('contents'):
                for item in v:
                    if item.get('is_dir'):
                        dirs[item.get('path')] = client.metadata(item.get('path'))
                    print '\n==============\n'




if __name__ == "__main__":
    unittest.main()
