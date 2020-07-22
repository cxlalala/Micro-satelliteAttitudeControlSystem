'''
File Name: log.py
Author: ChuXuan
Date:07-04-2019

It is using for creating the log files.
'''
import numpy as np
import logging


def hex2str_coding(i):
    '''
    It is using for transfer the hex numbers to the srtings.
    Args:
        i = the hex number
    Return:
        coding[i] = the string corresponding to the hex number
    '''
    return '%d' %i


def logger(log_name):
    '''
    It is using for creating a log file.
    Args:
        log_name = the name of log file
    Return:
        mylogger = an instance of the logger
    '''
    mylogger = logging.getLogger()
    mylogger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
    mylogger.addHandler(file_handler)
    return mylogger
