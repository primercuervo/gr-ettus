include(GrPython)

GR_PYTHON_INSTALL(
	PROGRAMS
	rfnoc_modtool
	DESTINATION ${GR_RUNTIME_DIR}
	COMPONENT "utils"
)
