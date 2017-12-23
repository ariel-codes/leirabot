import json
import hashlib
from os import walk


def readChats(folder="./data/"):

    _, _, filenames = next(walk(mypath), (None, None, []))

    def getHash(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def genDigest():

    def checkIfNew():
