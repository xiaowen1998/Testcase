# logging四大组建：logger（日志器），handler（处理器），filter（过滤器），formatter（格式器）
# logger通过handler将日志进行目标输出
# 每个logger可以有多个handler，多个handler可以在不同位置进行日志输出
# 一个handler可以自己到filter/formatter，所以实现输出不同格式指定等级到日志信息

import logging
import time


def log(msg, level='debug'):
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)  # 指定日志到最低级别

    # 创建一个处理器handler
    sh = logging.StreamHandler()  # 控制台标准输出
    fh = logging.FileHandler(filename='../log/{}.log'.format(time.strftime("%Y-%m-%d-%H", time.localtime())),
                             encoding='utf-8')
    # 指定格式器formatter
    fo = logging.Formatter(fmt='%(asctime)s %(name)s %(filename)s %(levelname)s %(message)s ', datefmt="%Y-%m-%d %H:%M:%S")
    sh.setFormatter(fmt=fo)
    fh.setFormatter(fo)

    logger.addHandler(sh)
    logger.addHandler(fh)
    # 错误信息记录
    if level == 'debug':
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)
    # logger.warning(msg=msg)
    # 移除对应的处理器
    logger.removeHandler(sh)
    logger.removeHandler(fh)
    # logger.warning('warning信息')
    # logger.debug('debug信息')
    # logger.error('error信息')

# log("警告信息")
# log('警告')