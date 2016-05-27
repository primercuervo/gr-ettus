###RFNoC Modtool

""" Utility functions for RFNoC Modtool """

import re
import sys

def get_modname():
    # OK, there's no gnuradio.project. So, we need to guess.
    modname_trans = {'howto-write-a-block': 'rfnoc_example'}
    cmfile = open('CMakeLists.txt', 'r').read()
    regexp = r'(project\s*\(\s*|GR_REGISTER_COMPONENT\(")gr-(?P<modname>[a-zA-Z0-9-_]+)(\s*(CXX)?|" ENABLE)'
    try:
        modname = re.search(regexp, cmfile, flags=re.MULTILINE).group('modname').strip()
        if modname in modname_trans.keys():
            modname = modname_trans[modname]
        return modname
    except AttributeError:
        return None

def ask_yes_no(question, default):
    """ Asks a binary question. Returns True for yes, False for no.
    default is given as a boolean. """
    question += {True: ' [Y/n] ', False: ' [y/N] '}[default]
    if raw_input(question).lower() != {True: 'n', False: 'y'}[default]:
        return default
    else:
        return not default

