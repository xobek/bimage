from PIL import Image
from pathlib import Path
from typing import Protocol 

class Validator(Protocol):
    def is_valid_image(self, query: str, file_path: Path) -> bool:
        pass 

    def validate_images(self, folderpath: str) -> int:
        pass

def is_valid_image(file_path: Path, to: Validator) -> bool:
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False

def validate_images(folderpath: str, to: Validator) -> int:
    path = Path(folderpath)
    if not path.is_dir():
        raise ValueError(f"The specified folder does not exist: {folderpath}")

    image_files = path.glob("*.{jpg,jpeg,png,gif,bmp}")
    failed_images = [file for file in image_files if not to.is_valid_image(file)]

    for failed_image in failed_images:
        failed_image.unlink()

    num_removed = len(failed_images)
    print(f"Removed {num_removed} invalid images.")
    return num_removed
