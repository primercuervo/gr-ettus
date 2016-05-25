###RFNoC Modtool

include(GrPython)

GR_PYTHOB_INSTALL(FILES
        __init__.py
        cmakefile.editor.py
        grc_xml_generator.py #not here
        modtool_base.py
        modtool_makexml.py
        modtool_newmod.py
        util_functions.py
        DESTINATION ${GR_PYTHON_DIR}/gr-ettus/rfnoc-modtool
        COMPONENT "utils"
)

