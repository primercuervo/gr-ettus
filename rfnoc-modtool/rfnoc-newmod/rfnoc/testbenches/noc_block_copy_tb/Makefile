#
# Copyright 2016 Ettus Research
#

#-------------------------------------------------
# Top-of-Makefile
#-------------------------------------------------

# Define BASE_DIR to point to the "top" dir
BASE_DIR = $(~/src/prefix/src/uhd/fpga-src/usrp3/top)
include ~/src/prefix/src/uhd/fpga-src/usrp3/tools/make/viv_sim_preamble.mak
#include $(BASE_DIR)/../tools/make/viv_sim_preamble.mak
#include $($PATH)/../src/uhd/fpga-src/usrp3/tools/make/viv_sim_preamble.mak

#-------------------------------------------------
# Testbench Specific
#-------------------------------------------------
# Define only one toplevel module
SIM_TOP = noc_block_copy_tb

# Add test bench, user design under test, and
# additional user created files
SIM_SRCS = \
$(abspath noc_block_copy_tb.sv) \
$(abspath ../../fpga-src/noc_block_copy.v)

MODELSIM_USER_DO = $(abspath wave.do)

#-------------------------------------------------
# Bottom-of-Makefile
#-------------------------------------------------
# Include all simulator specific makefiles here
# Each should define a unique target to simulate
# e.g. xsim, vsim, etc and a common "clean" target
include ~/src/prefix/src/uhd/fpga-src/usrp3/tools/make/viv_simulator.mak
