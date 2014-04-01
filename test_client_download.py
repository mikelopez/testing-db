from base import *

class TestDropboxDownload(unittest.TestCase):
    """Tests the download file process"""
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_client_download(self):
        """Tests a download"""
        try:
            dlpath, savepath = sys.argv[1], sys.arv[2]
            termprint('INFO', 'Download Path %s %s' % (dlpath, savepath))
        except IndexError:
            dlpath, savepath = "/Test Uploads from API/samplevideo.mp4", \
                               "samplevideo-download.mp4"

            termprint('ERROR', 'No Params sent, downloading test samplevideo.mp4')
        key, secret, access_token = doauth()
        client = dropbox.client.DropboxClient(access_token)
        f, metadata = client.get_file_and_metadata(dlpath)
        out = open(savepath, 'wb')
        out.write(f.read())
        out.close()
        termprint("INFO", metadata)



if __name__ == "__main__":
    unittest.main()
