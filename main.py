import sys
import logging.config

logging.config.fileConfig('logging.conf')

from unreliable_service.unreliable_service_proxy import UnreliableServiceProxy as UnreliableService


logger = logging.getLogger(__name__)


def get_sum(a, b):

    logger.debug('entering(%s, %s)', a, b)
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            the_sum = a + b
            logger.info('%s + %s = %s', a, b, the_sum)
            return the_sum
        else:
            raise Exception('the second parameter must be numeric; received: {}'.format(b))
    else:
        raise Exception('the first parameter must be numeric; received: {}'.format(a))


def do_all_the_things():

    logger.debug('entering')

    the_sum = None

    try:
        the_sum = get_sum('foo', 'bar')
    except Exception as e:
        logger.warning('the first call to get_sum didn\'t work. It\'s not a big deal, though; Caused by: %s', e)

    the_sum = get_sum(1, 2)
    logger.info('the sum is: %s', the_sum)

    try:
        UnreliableService.use()
        logger.info('the unreliable service didn\'t fail')
    except Exception as e:
        logger.exception('Exception: %s', e)
        logger.critical('the unreliable service failed, so the whole program is borked')
        sys.exit(1)

    logger.debug('returning: %s', the_sum)
    return the_sum


if __name__ == '__main__':
    do_all_the_things()
