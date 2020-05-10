"""bayes_chime/_config

_config
=======

configuration and settings modules

contents
--------

- config.py
"""
__all__ = ["Config", "Settings"]

from .config import Config, Settings


def load_config():
    return Config, Settings
