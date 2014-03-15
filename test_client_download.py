from local_settings import DB_APP_KEY, DB_APP_SECRET, ACCESS_TOKEN

from termprint import *
import simplejson
import sys
import os
import urllib
import unittest
import dropbox


class TestDropboxDownload(unittest.TestCase):
    """Tests the download file process"""
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_download(self):
        access_token = ACCESS_TOKEN
        if not ACCESS_TOKEN:
            # promot input
            termprint('ERROR', 'You need to generate an access token first.\n')
            termprint('ERROR', 'Run: ./test-get-access-token.sh')
            sys.exit()
        client = dropbox.client.DropboxClient(access_token)
        f, metadata = client.get_file_and_metadata('/Test Uploads from API/samplevideo.mp4')
        out = open('samplevideo-download.mp4', 'wb')
        out.write(f.read())
        out.close()
        termprint("INFO", metadata)



if __name__ == "__main__":
    unittest.main()
