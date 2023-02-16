import time

import loaders.elastic_search
from loaders.config import config_loader
from loaders.logger import logger_loader
from loaders.mongo import mongo_db
from loaders.elastic_search import elastic_search_db
from services.elastic_services import get_user_answers

def loader() -> None:
    config_loader()
    logger_loader()
    mongo_db.loader()
    elastic_search_db.loader()
    pass


def main():
    loader()
    get_user_answers()
    pass


if __name__ == '__main__':
    main()
    pass
