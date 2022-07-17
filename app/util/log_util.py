import logging

logger = None


def get_logger():
    global logger
    if logger is None:
        logger = logging.getLogger("app")

        logging_formatter = logging.Formatter(f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('app.log', mode='w', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging_formatter)
        logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging_formatter)
        logger.addHandler(ch)

    return logger
