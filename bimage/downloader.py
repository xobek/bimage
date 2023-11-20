from duckduckgo_search import DDGS
from fastdownload import download_url
from typing import Protocol 
from PIL import Image
from pathlib import Path
import concurrent.futures
from bimage.validator import validate_images
import sys

class Downloader(Protocol):
    def download_images(self, query: str, amount: int, folderpath: str, resolution: int) -> None:
        pass 

def download_images(query: str, amount: int, folderpath: str, resolution: int, to: Downloader) -> None:
    try:
        amount = int(amount)
    except ValueError:
        raise ValueError("Amount must be a valid integer")
    
    try:
        resolution = int(resolution)
    except ValueError:
        raise ValueError("Resolution must be a valid integer")
    
    if amount <= 0:
        raise ValueError("Amount must be a positive integer")

    if not query:
        raise ValueError("Query must not be empty")

    if not folderpath:
        folderpath = "."

    path = Path(folderpath).joinpath(query)
    if not path.is_dir():
        path.mkdir(parents=True)

    failed_to_download = 0

    print("Processing... Please wait.", end="", flush=True)
    
    with DDGS() as ddgs:
        try:
            urls = [r["image"] for r in ddgs.images(query, max_results=amount, type_image="photo", safesearch="off")]
        except Exception as e:
            print(f"\nFailed to establish connection to DDG.")
            return
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(downloaded_images, url, path, resolution) for url in urls]

            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result(timeout=30)
                except Exception as e:
                    failed_to_download += 1
                finally:
                    executor.shutdown(wait=True)

    sys.stdout.write("\r" + " " * len("Processing... Please wait."))
    sys.stdout.flush()

    print(f"Downloaded {amount - failed_to_download} images ({failed_to_download} Failed)")
    validate_images(path, sys.stderr)

def downloaded_images(url: str, path: Path, resolution: int) -> None:
    download_url(url, path, show_progress=False)
    if resolution > 0:
        image_path = path.joinpath(Path(url).name)
        with Image.open(image_path) as img:
            img.thumbnail((resolution, resolution))
            img.save(image_path)
