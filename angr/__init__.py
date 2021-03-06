""" Angr module """
# pylint: disable=wildcard-import

import logging
logging.getLogger("angr").addHandler(logging.NullHandler())

from .project import *
from .functionmanager import *
from .variableseekr import *
from .regmap import *
from .path import *
from .errors import *
from .surveyor import *
from .service import *
from .analyses import *
from .analysis import *
from .tablespecs import *
from . import surveyors
from .blade import Blade
from .simos import SimOS
from .path_group import PathGroup
from .surveyors.caller import Callable
from .log import Loggers

import sys
i = 0
while True:
    i += 1
    module = sys._getframe(i).f_globals.get('__name__')
    if module == '__main__':
        loggers = Loggers()
        break
    elif module is not None and module.startswith('nose.'):
        break

del sys, i, module
