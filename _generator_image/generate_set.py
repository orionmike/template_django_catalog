
from pathlib import Path
import time

from config.config import DIR_PHOTO
from . libs.image import generate_random_image
from . libs.utils import get_execute_time


def generate_image_category_product(file_path):

    start = time.time()

    path_dir_foto = Path(f'media/{file_path}').parent / DIR_PHOTO
    # print(path_dir_foto)
    # print(path_dir_foto.resolve())

    generate_random_image(f'media/{file_path}')

    '''
    for index in range(18):
        ind = str(index+1).zfill(2)
        file_path = path_dir_foto / f'category_product-{ind}.webp'
        # print(file_path)
        generate_random_image(file_path, num=index+1)
    '''

    get_execute_time(start)


def generate_image_product(file_path):

    start = time.time()

    generate_random_image(f'media/{file_path}')

    path_dir_foto = Path(f'media/{file_path}').parent / DIR_PHOTO
    print(path_dir_foto)

    for index in range(6):
        ind = str(index+1).zfill(2)
        file_path = path_dir_foto / f'product-{ind}.webp'
        # print(file_path)
        generate_random_image(file_path, num=index+1)

    get_execute_time(start)
