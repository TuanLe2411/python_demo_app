import sys
from dotenv import load_dotenv


def config_loader() -> None:
    _envFilePath = "environments/.env." + sys.argv[1]
    load_dotenv(_envFilePath)
    pass
