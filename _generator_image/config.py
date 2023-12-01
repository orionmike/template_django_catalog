import sys
from datetime import datetime
from pathlib import Path

from colorama import Fore, init
from loguru import logger

init(autoreset=True)


# ABS_PATH = Path('./src').resolve()  # windows
ABS_PATH = Path('_generator_image')  # windows
# ABS_PATH = sys.path[0]  # linux
APP_NAME = 'generate random image'

print(ABS_PATH)


# =====================================
# load config

try:

    if sys.version_info.major == 3 and sys.version_info.minor >= 11:

        import tomllib

        with open(f"{ABS_PATH}/config.toml", "rb") as f:
            config = tomllib.load(f)
    else:

        import toml

        with open(f"{ABS_PATH}/config.toml", "r") as f:
            config = toml.load(f)

    IND = config['utils']['console_indent']

    SEGMENT_SIZE = config['image_size']['segment_size']
    WIDTH = config['image_size']['ratio_width']
    HEIGHT = config['image_size']['ratio_height']

    BG_START, BG_FINISH = config['image_color']['bg']
    FG_START, FG_FINISH = config['image_color']['fg']
    BRD_START, BRD_FINISH = config['image_color']['border']

    PATH_DIR_RESULT = Path(f"{ABS_PATH}/{config['path']['result']}")
    FILE_NAME_TEMPLATE = config['path']['file_name_template']

    # logging
    log_file_name = f'{datetime.now().strftime("%Y-%m-%d")}'
    logger.remove()
    logger.add(f'{ABS_PATH}/logs/{log_file_name}_error.log', format='{time} {level} {message}', level='ERROR', rotation='1 day')

    # print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} start app: {APP_NAME}')
    # print(f'{IND} python {sys.version_info.major}.{sys.version_info.minor}')
    # print(f'{IND} config loaded: OK')
    # print()

except Exception as e:
    raise Exception(f'config load -> error: {e}')
