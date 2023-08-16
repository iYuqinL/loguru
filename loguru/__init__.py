"""
The Loguru library provides a pre-instanced logger to facilitate dealing with logging in Python.

Just ``from loguru import logger``.
"""
import os
import atexit as _atexit
import sys as _sys

from . import _defaults
from ._logger import Core as _Core
from ._logger import Logger as _Logger

__version__ = "0.6.0"

__all__ = ["logger"]

urulogger_format = ("<green>{time:YY-MM-DD HH:mm:ss.SSS}</green> | "
                    "<level>{level}</level> | <cyan>{name}</cyan>:"
                    "<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                    "<level>\n{message}\n</level>")

logger = _Logger(
    core=_Core(),
    exception=None,
    depth=0,
    record=False,
    lazy=False,
    colors=False,
    raw=False,
    capture=True,
    patcher=[],
    extra={},
)


if _defaults.LOGURU_AUTOINIT and _sys.stderr:
    logger.add(_sys.stderr, format=urulogger_format)

_atexit.register(logger.remove)
