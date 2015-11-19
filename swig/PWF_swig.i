/* -*- c++ -*- */

#define PWF_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "PWF_swig_doc.i"

%{
#include "PWF/rx_frame_sync.h"
%}

%include "PWF/rx_frame_sync.h"
GR_SWIG_BLOCK_MAGIC2(PWF, rx_frame_sync);
