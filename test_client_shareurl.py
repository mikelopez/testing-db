from base import *


class TestDropboxShareURL(unittest.TestCase):
    """Tests the download file process"""
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_download(self):
        key, secret, access_token = doauth()
        client = dropbox.client.DropboxClient(access_token)
        #f, metadata = client.get_file_and_metadata('/Test Uploads from API/samplevideo.mp4')
        f = client.share('/Test Uploads from API/samplevideo.mp4')
        termprint("INFO", f)



if __name__ == "__main__":
    unittest.main()
