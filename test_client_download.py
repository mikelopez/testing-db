from base import *


class TestDropboxDownload(unittest.TestCase):
    """Tests the download file process"""
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_download(self):
        """Tests a download"""
        key, secret, access_token = doauth()
        client = dropbox.client.DropboxClient(access_token)
        f, metadata = client.get_file_and_metadata('/Test Uploads from API/samplevideo.mp4')
        out = open('samplevideo-download.mp4', 'wb')
        out.write(f.read())
        out.close()
        termprint("INFO", metadata)



if __name__ == "__main__":
    unittest.main()
