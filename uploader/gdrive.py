import datetime
import json
from subprocess import call
import tempfile

import gdrive_config as config

class GDriveUploader:
    def upload(self, filepath, title=None, parent=None):
        command = '%s upload ' % config.GDRIVE_BINARY_PATH

        if title:
            command += '--title %s ' % title
        if parent:
            command += '--parent %s ' % parent

        command += '--file %s' % filepath

        call(command, shell=True)

    def quick_upload(self, obj, file_prefix=None, folder=None):
        temp_file = tempfile.NamedTemporaryFile()
        temp_file.write(json.dumps(obj))

        filename = '%s.json' % datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        if file_prefix:
            filename = '%s-%s' % (file_prefix, filename)

        self.upload(temp_file.name, title=filename, parent=folder)
        temp_file.close()

if __name__ == '__main__':
    uploader = GDriveUploader()
    # uploader.upload('/tmp/example/file.path')
    # uploader.upload('/tmp/example/file.path', title='rename.txt', parent='asdjkfhadf')
    uploader.upload('~/drive')