import hashlib
import sys
import argparse

class HASHES:
    def __init__(self, filename, block_bytesize):
        self.filename = filename
        self.BLOCK_BYTESIZE = block_bytesize

        pass

    def hashit(self, file_hash):
        with open(self.filename, 'rb') as f:
            fb = f.read(self.BLOCK_BYTESIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(self.BLOCK_BYTESIZE)
        return file_hash

    def sha256(self):
        file_hash = hashlib.sha256()
        hash = self.hashit(file_hash)
        print(hash.hexdigest())
        pass

    def sha512(self):
        file_hash = hashlib.sha512()
        hash = self.hashit(file_hash)
        print(hash.hexdigest())
        pass

    pass

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Print or check SHA1 (160-bit) checksums."
    )
    parser.add_argument("-2", "--sha256", action="store_true", help="encode using SHA256")
    parser.add_argument("-5", "--sha512", action="store_true", help="encode using SHA512")
    parser.add_argument('-f', type=str, help="file path")
    parser.add_argument('-s', type=int, help="block bytesize")
    return parser

def main():
    parser = init_argparse()
    args = parser.parse_args()
    hash = HASHES(args.f, args.s)
    if args.sha256:
        hash.sha256()
    if args.sha512:
        hash.sha512()

    pass

if __name__ == "__main__":
    main()
    pass

