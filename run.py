#!/usr/bin/env python

from PIL import Image
from resizeimage import resizeimage
import os
import shutil
import re


def prep():
    if os.path.exists('out'):
        print('Cleaning up \'out\' directory')
        shutil.rmtree('out')
    os.makedirs('out')
    
    in_dirs = os.listdir('in')
    for dir in in_dirs:
        os.makedirs('out/' + dir)


def resize_images():
    for path, subdirs, files in os.walk('in'):
        for file in files:
            in_path = os.path.join(path, file)
            out_path = re.sub('in','out',os.path.join(path, file))
            with open(in_path, 'r+b') as i:
                with Image.open(i) as image:
                    resize = resizeimage.resize_cover(image, [252,338])
                    resize.save(out_path, image.format)


def main():
    prep()
    resize_images()


if __name__ == '__main__':
    main()
