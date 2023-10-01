import os
import math
from pathlib import Path
# 3 = GB


def generate_file(path, fileprefix, filesize):
    _filesize = (1024**fileprefix) *filesize
    with open(path, 'wb') as fout:
        fout.write(os.urandom(_filesize))


def generate_testfiles(fileprefix, filesize, numfiles):
    prefix = {1:"kb", 2:"mb", 3:"gb"}
    path = "D:\\TEST\\"
    filename = "file"
    for i in range(0, numfiles):
        currpath = f"{path}{filesize}{prefix[fileprefix]}{numfiles}"
        #if not os.path.isdir(os.path.dirname(currpath)):
        Path(currpath).mkdir(parents=True, exist_ok=True)
        generate_file(currpath+"\\"+filename+str(i), fileprefix, filesize)


def main():
    # 4 8 16 32 64 128
    generate_testfiles(2, 120, 56)


main()