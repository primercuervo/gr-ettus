/* -*- c++ -*- */

#define RFNOC_EXAMPLE_API
#define ETTUS_API

%include "gnuradio.i"/*			*/// the common stuff

//load generated python docstrings
%include "rfnoc_example_swig_doc.i"
//Header from gr-ettus
%include "ettus/device3.h"
%include "ettus/rfnoc_block.h"
%include "ettus/rfnoc_block_impl.h"

%{
#include "ettus/device3.h"
#include "rfnoc_example/rfnoc_copy.h"
#include "ettus/rfnoc_block_impl.h"
%}
//
%include "rfnoc_example/rfnoc_copy.h"
GR_SWIG_BLOCK_MAGIC2(rfnoc_example, rfnoc_copy);

