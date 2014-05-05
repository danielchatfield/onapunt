"""
    onapunt.tracking
    ~~~~~~~~~~~~~~~~

    Module used for tracking events, logging debug info and errors.
"""

import logging


def info(*args, **kwargs):
    return logging.info(*args, **kwargs)


def warning(*args, **kwargs):
    return logging.warning(*args, **kwargs)


def error(*args, **kwargs):
    return logging.error(*args, **kwargs)


def critical(*args, **kwargs):
    return logging.critical(*args, **kwargs)


def exception(*args, **kwargs):
    return logging.exception(*args, **kwargs)
