"""
================================================
Script Argument Parsers (:mod:`jup2jek.scripts`)
================================================

Summary
-------
Includes a class for parsing command line arguments for the `jup2jek` script.

Classes
-------

"""

import sys
from argparse import ArgumentParser

class Jup2JekArgParser(ArgumentParser):
    """
    Command line argument parser for lca_writer scripts.

    .. code-block:: none
    """
    def __init__(self):
        ArgumentParser.__init__(self)
        self.add_argument('-o', '--options',
                          nargs = '?',
                          help = 'Options file path if not default (options).',
                          default = None)

    @staticmethod
    def _doc_string():
        """Returns a doc string with the usage and help formats included."""
        s = Jup2JekArgParser()
        s = s.format_help()
        s = '\n\t'.join(s.split('\n'))
        return Jup2JekArgParser.__doc__ + '\n\t' + s + '\n\n'

if sys.version_info[0] >=3:
    Jup2JekArgParser.__doc__ = Jup2JekArgParser._doc_string()
