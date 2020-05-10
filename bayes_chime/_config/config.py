"""_config/config.py

config module
=============

Configuration and user settings. Any configuration
should be considered upstream of package load, and
once package is loaded only user adjustable settings
should be changeable.

Goals
-----

- [ ] Minimal intra-package dependencies
- [ ] Resource file for saving user settings, reports, and parameters
- [ ] User settings accessible via dot notation
"""

from collections import namedtuple
from os import getcwd, environ
from pathlib import Path
from typing import NamedTuple

__location__ = str(Path(getcwd()).absolute())
__source_root__ = __location__.split('bayes_chime')[0]


class ConfigError(ValueError, KeyError):
    """
    Custom exception for errors encountered during configuration
    """


class Config(NamedTuple):
    """Configuration settings"""
    _date_format = "%Y-%m-%d"
    _time_format = "%H-%M-%S"  # 24 hour 0 padded
    _penn_dir = environ['PENN']


class Settings:
    """
    Settings
    =======

    User adjustable settings
    """
    _date_format = "%Y-%m-%d"
    _time_format = "%H-%M-%S"  # 24 hour 0 padded
