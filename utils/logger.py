import logging

logger = logging.getLogger()
fh = logging.FileHandler("fgo.log",encoding='utf-8',mode='a')
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='fgoLog.log', filemode='a', format=FORMAT,encoding='utf-8')


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)

if __name__ == "__main__":
    error("loop:"+str(5+1) )