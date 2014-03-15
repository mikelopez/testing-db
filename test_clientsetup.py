from local_settings import DB_APP_KEY, DB_APP_SECRET
from termprint import *
import urllib
import unittest
import dropbox


class TestDropboxClientSetup(unittest.TestCase):
    """Tests authenticating to dropbox"""

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_create_flow_start(self):
        """
        Start the authentication process 
        using DropboxOAuth2FlowNoRedirect.
        """
        key, secret = DB_APP_KEY, DB_APP_SECRET
        if not key or not secret:
            # promot input
            pass
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(key, secret)
        auth_url = flow.start()
        response_key = None
        data = urllib.urlopen(auth_url).read()
        termprint("INFO", "GO to the following URL in your browser")
        termprint('INFO', '\n\t%s' % auth_url) 
        self.assertTrue("http" in auth_url)


if __name__ == "__main__":
    unittest.main()
