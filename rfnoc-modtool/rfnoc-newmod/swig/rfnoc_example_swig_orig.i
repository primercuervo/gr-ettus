/* -*- c++ -*- */

#define RFNOC_EXAMPLE_API
#define ETTUS_API

%include "gnuradio.i"			// the common stuff
//%include "ettus_swig.i"
//load generated python docstrings
%include "rfnoc_example_swig_doc.i"
%include "ettus/rfnoc_block.h"

%{
//#include "rfnoc_example/copy.h"
#include "rfnoc_example/rfnoc_copy.h"
%}

//%include "rfnoc_example/copy.h"
//GR_SWIG_BLOCK_MAGIC2(rfnoc_example, copy);
%include "rfnoc_example/rfnoc_copy.h"
GR_SWIG_BLOCK_MAGIC2(rfnoc_example, rfnoc_copy);
