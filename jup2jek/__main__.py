import os
import sys
from .jup2jek import Jup2Jek

if __name__ == '__main__':
    root = os.getcwd()

    if sys.argv:
        options = sys.argv[0]
    else:
        options = None

    j = Jup2Jek(root, options)
    j.convert_notebooks()
