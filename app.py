from books_recommender.exception.exception_handler import AppException
from books_recommender.logger.log import logging
import sys


try:
    a=30/0
except Exception as e:
    logging.info(e)
    raise AppException(e,sys) from e
