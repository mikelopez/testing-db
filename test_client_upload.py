from base import *

class TestDropboxUpload(unittest.TestCase):
    """Test the upload process"""
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_upload(self):
        """Uploads a sample video clip"""
        key, secret, access_token = doauth()
        client = dropbox.client.DropboxClient(access_token)
        #folder_metadata = client.metadata('/')
        f = open('samplevideo.mp4', 'rb')
        response = client.put_file('%s' % fn, f)
        f.close()
        print 'Uploaded: ', response




if __name__ == "__main__":
    unittest.main()
