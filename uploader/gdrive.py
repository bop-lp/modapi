from subprocess import call

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

if __name__ == '__main__':
    uploader = GDriveUploader()
    # uploader.upload('/tmp/example/file.path')
    # uploader.upload('/tmp/example/file.path', title='rename.txt', parent='asdjkfhadf')
    uploader.upload('~/drive')