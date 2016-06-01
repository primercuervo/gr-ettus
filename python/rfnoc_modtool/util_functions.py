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

def is_number(s):
    """ Return True if the string s contains a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

def xml_indent(elem, level=0):
    """ Adds indents to XML for pretty printing """
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            xml_indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def ask_yes_no(question, default):
    """ Asks a binary question. Returns True for yes, False for no.
    default is given as a boolean. """
    question += {True: ' [Y/n] ', False: ' [y/N] '}[default]
    if raw_input(question).lower() != {True: 'n', False: 'y'}[default]:
        return default
    else:
        return not default

