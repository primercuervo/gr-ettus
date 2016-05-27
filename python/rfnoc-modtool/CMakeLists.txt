###RFNoC Modtool

include(GrPython)

GR_PYTHON_INSTALL(FILES
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

set(GR_PKG_RFNOC_MODTOOL_DATA_DIR ${GR_PKG_DATA_DIR}/rfnoc-modtool)
install(DIRECTORY rfnoc-newmod
    DESTINATION ${GR_PKG_RFNOC_MODTOOL_DATA_DIR}
    COMPONENT "utils"
    )

#################################################################
# Create and install the rfnoc-modtool conf file
#################################################################
file(TO_NATIVE_PATH ${CMAKE_INSTALL_PREFIX}/${GR_PKG_RFNOC_MODTOOL_DATA_DIR}/rfnoc-newmod newmoddir)

configure_file(
	${CMAKE_CURRENT_SOURCE_DIR}/rfnocmodtool.conf.in
	${CMAKE_CURRENT_BINARY_DIR}/rfnocmodtool.conf
@ONLY)

install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/rfnocmodtool.conf
    DESTINATION ${GR_PREFSDIR}
    COMPONENT "utils"
)
