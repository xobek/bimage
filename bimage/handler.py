import sys
from bimage.downloader import download_images
from bimage.validator import validate_images

from collections import namedtuple

class Handler():
    Params = namedtuple("Params", ["query", "amount", "folderpath", "resolution"])
    def parse(self, args):
        if args.command == "validate":
            self.validate(args)
        else:
            self.download(args)

    def download(self, args):
        download_images(args.query, args.amount, args.folderpath, sys.stderr)

    def validate(self, args):
        validate_images(args.folderpath, sys.stderr)

