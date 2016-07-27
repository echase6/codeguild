"""Project that rotates a .jpg and stores as a .png"""

from PIL import Image
import sys


def get_filenames():
    """Grab filenames from command line arguments."""
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
    return in_filename, out_filename


def main():
    in_filename, out_filename = get_filenames()
    im = Image.open(in_filename)
    out = im.rotate(45)
    out.save(out_filename)


if __name__ == '__main__':
    main()
