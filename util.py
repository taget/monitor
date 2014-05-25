#
#
# @Eli Qiao @ 2014-05-25
#
#
#

import os
import tarfile
import gzip
import string 
import shutil
import traceback


class UtilException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    
# linux
#src : src dir
#dst : dst dir
#zipname : zipfile name
def zipDir(src, dst, zipname):
    files = os.listdir(src)
    zip_file_path = '%s/%s' % (dst, zipname)
    try:
        print zip_file_path
        tar = tarfile.open(zip_file_path,"w:gz")
        for file in files:
            tar.add(file)
        tar.close()
    except Exception:
        raise UtilException('tar error %s' % zipname)



def test():
    print "test"
    try:
        zipDir("/home/pi/images", "/home/pi/", "image.tgz")
    except UtilException as e:
        print e.msg
if __name__ == '__main__':
    test()
