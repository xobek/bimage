import sys
from bimage.downloader import download_images
from bimage.validator import validate_images

class Handler():
    def parse(self, args):
        if args.command == "validate":
            self.validate(args)
        else:
            self.download(args)

    def download(self, args):
        download_images(args.query, args.amount, args.folderpath, args.resolution, sys.stderr)

    def validate(self, args):
        validate_images(args.folderpath, sys.stderr)