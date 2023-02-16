from loader.config import config_loader
from loader.logger import logger_loader


def loader() -> None:
    config_loader()
    logger_loader()
    pass


def main():
    loader()
    pass


if __name__ == '__main__':
    main()
    pass
