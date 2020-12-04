import logging
import json
import requests
from pandas.io.json import json_normalize

def logger():
    return make_logger();


def make_logger(name=None):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] (%(levelname)s) %(filename)s : %(message)s")

    console = logging.StreamHandler()
    file_handler = logging.FileHandler(filename="myapp.log")

    console.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger