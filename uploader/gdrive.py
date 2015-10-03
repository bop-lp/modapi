import datetime
import json
import os
import subprocess
import tempfile

import gdrive_config as config

class GDriveUploader:
    def upload(self, filepath, title=None, parent=None):
        command = '%s upload' % config.GDRIVE_BINARY_PATH
        command += ' --file %s' % filepath

        if title:
            command += ' --title %s' % title
        if parent:
            command += ' --parent %s' % parent

        subprocess.call(command, shell=True)

    def quick_upload(self, obj, file_prefix=None, folder=None):
        fd, temp_path = tempfile.mkstemp()

        temp_file = open(temp_path, 'w')
        json.dump(obj, temp_file)

        filename = '%s.json' % datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        if file_prefix:
            filename = '%s-%s' % (file_prefix, filename)

        temp_file.close()

        self.upload(temp_file.name, title=filename, parent=folder)

        os.close(fd)
        os.remove(temp_path)

if __name__ == '__main__':
    uploader = GDriveUploader()
    uploader.upload('test.json')