from local_settings import DB_APP_KEY, DB_APP_SECRET
from termprint import *
import urllib
import unittest
import dropbox


class TestDropboxClientSetup(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_create_flow_finish(self):
        key, secret = DB_APP_KEY, DB_APP_SECRET
        if not key or not secret:
            # promot input
            pass
        termprint('ERROR', '\n\nNow enter the authorization code below ')
        authcode = raw_input('Authorization code: ').strip()

        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(key, secret)
        access_token, user_id = flow.finish(authcode)

        termprint('INFO', 'OK Access token is: %s' % (access_token))

        client = dropbox.client.DropboxClient(access_token)
        self.assertTrue(client)

        termprint('WARNING', 'Checking account info')
        txt = 'Linked account: %s' % client.account_info()
        termprint('INFO', 'Linked account: %s' % txt)



if __name__ == "__main__":
    unittest.main()
