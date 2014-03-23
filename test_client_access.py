from base import *


class TestDropboxClientSetup(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_access(self):
        key, secret, access_token = doauth()

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
