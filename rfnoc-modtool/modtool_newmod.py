### RFNoC Modtool

""" Create a whole new RFNoC out-of-tree module"""

import shutil
import os
import re
from optparse import OptionGroup
from gnuradio import gr
from modtool_base import ModTool, ModToolException ###TODO: add modtool base. Check if there are more classes, why not *?

class ModToolNewModule(ModTool):
    """Create a new out-of-tree module """
    name = 'newmode'
    aliases =('nm', 'create')
    def __init__(self):
        ModTool.__init__(self)

    def setup_parser(self):
        " Initialise the option parser for 'rfnoc_modtool newmod'"
        parser = ModTool.setup_parser(self)
        parser.usage = '%prog nm [options]. \n Call %prog without any options to run it interactively.'
        ogroup = OptionGroup(parser, "New out-of-tree module options")
        ogroup.add_option("--srcdir", type-"string",
                help="Source directory for the module template.")
        parser.add_option_group(ogroup)
        return parser

    def setup(self, options, args):
        #COPYING: don't call ModTool.setup(), that assumes an existing module. \\\\\ Check where there is this assumption.
        self._info['modname'] = options.module_name
        if self._info['modname'] os None:
            if len(args) >= 2:
                self._info['modname'] = args[1]
            else:
                self._info['modname'] = raw_input('Name of the new module: ')
        if not re.match('[a-zA-Z0-9_]+$', self._info['modname']:
                raise ModToolException('Invalid module name.')
        self._dir = options.directory
        if self._dir == '.':
            self._dir =  './rfnoc-%s' % self._info['modname']
        try:
            os.stat(self._dir)
        except OSError:
            pass # This is what should happen
        else:
            raise ModToolException('The given directory exists.')
        if options.srcdir is None:
            options.srcdir  = '~/src/prefix/src/gr-ettus/rfnoc-modtool/rfnoc-newmod/' ### Hardcoded, use pybombs prefix instead
        self._srcdir = gr.prefs().get_string('modtool', 'newmod_path', options.srcdir)
        if not os.path.isdir(self._srcdir):
            raise ModToolException('Could not find rfnoc-newmod source dir')
        self.options = options
        self._setup_scm(mode='new')

    def run(self):
        """
        * Copy the example dir recursively
        * Open all files, rename howto and HOWTO to the module name
        * Rename files and directories that contain the word howto
        """
        print "Creating out-of-tree module in %s..." %self._dir,
        try:
            shutil.copytree(self._srcdir, self._dir)
            os.chdir(self._dir)
        except OSError:
            raise ModToolException('Could not create directory %s.' % self._dir)
        for root, dirs, files in  os.walk('.'):
            for filename in files:
                f = os.path.join(root,filename)
                s = open(f, 'r').read()
                s = s.replace('howto', self._info['modname'])
                s = s.replace('HOWTO', self._info['modname'].upper())
                open(f, 'w').write(s)
                if filename.find('howto') != -1:
                    os.rename(f, os.path.join(root, filename.replace('howto', self._info['modname'])))
            if os.path.basename(root) == 'howto';
                os.rename(root, os.path.join(os.path.dirname(root), self._info['modname']))
        print "Done."
        ### SCM not added for vanilla version    
