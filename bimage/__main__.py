import argparse
from bimage.handler import Handler

def main():
    args = parse_args()
    handler = Handler()
    handler.parse(args)


def parse_args():
    ap = argparse.ArgumentParser(description='Bulk Image Downloader', allow_abbrev=False)

    ap.add_argument("-q", "--query", help="Query to download images from", type=str, required=True)
    ap.add_argument("-a", "--amount", help="Amount of images to download", type=int, required=True, default=1)
    ap.add_argument("-f", "--folderpath", help="Folder to place all images into", type=str)
    ap.add_argument("-r", "--resolution", help="Specify a resolution to refit all images to (e.g.: -r 128)", type=str, default=0)
    
    subparsers = ap.add_subparsers(title="Commands", dest="command")
    validate_ap = subparsers.add_parser("validate", help="Validate images")
    validate_ap.add_argument("-f", "--folderpath", help="Path to folder to validate images in", type=str)

    return ap.parse_args()
