from base import *


class TestDropboxClientSetup(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_access(self):
        key, secret, access_token = doauth()
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
