import sys
import os

# TODO: Fix this garbage (something wrong with package itself)
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "GPIO"))

import GPIO
__version__ = GPIO.__version__
