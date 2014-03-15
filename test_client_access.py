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
        print 'linked account: ', client.account_info()
        print '\n\n----------------\n\n'
        folder_metadata = client.metadata('/')
        print ''
        print 'metadata: ', folder_metadata
        print '\n\n---------\n\n'
        for k, v in folder_metadata.items():
            if not k == 'contents':
                print '%s = %s' % (k, v)
            else:
                for content in v:
                    for k2, v2 in content.items():
                        print '\t%s = %s' % (k2, v2)
                    print '\n==============\n'




if __name__ == "__main__":
    unittest.main()
