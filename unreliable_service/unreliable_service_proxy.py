import logging
from random import randint


logger = logging.getLogger(__name__)


class UnreliableServiceProxy:

    @staticmethod
    def use():
        logger.debug('entering')

        if randint(0, 1) == 1:
            logger.warning('RANDOM FAILURE')
            raise Exception('something random happened')

        logger.debug('returning')
