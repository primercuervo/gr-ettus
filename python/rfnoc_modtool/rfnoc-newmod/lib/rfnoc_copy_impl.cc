/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "rfnoc_copy_impl.h"
#include "rfnoc_example/copy_block_ctrl.hpp"


namespace gr {
  namespace rfnoc_example {

    rfnoc_copy::sptr
    rfnoc_copy::make(
          const gr::ettus::device3::sptr &dev,
          const ::uhd::stream_args_t &tx_stream_args,
          const ::uhd::stream_args_t &rx_stream_args,
          const int block_select,
          const int device_select
    )
    {
      return gnuradio::get_initial_sptr
        (new rfnoc_copy_impl(dev, tx_stream_args, rx_stream_args, block_select, device_select));
    }

    /*
     * The private constructor
     */
    rfnoc_copy_impl::rfnoc_copy_impl(
        const gr::ettus::device3::sptr &dev,
        const ::uhd::stream_args_t &tx_stream_args,
        const ::uhd::stream_args_t &rx_stream_args,
        const int block_select,
        const int device_select    
    
    )
      : gr::ettus::rfnoc_block("rfnoc_copy"),
	    gr::ettus::rfnoc_block_impl(
	    	dev,
	    	gr::ettus::rfnoc_block_impl::make_block_id("Copy",block_select, device_select),
	    	tx_stream_args, rx_stream_args    
	    )
	    /* Generated by gr_modtool. Not needed for rfnoc
              gr::io_signature::make(<+MIN_IN+>, <+MAX_IN+>, sizeof(<+ITYPE+>)),
              gr::io_signature::make(<+MIN_OUT+>, <+MAX_OUT+>, sizeof(<+OTYPE+>)))
            */
    {
    	//nothing yet for example, but your function here
    }

    /*
     * Our virtual destructor.
     */
    rfnoc_copy_impl::~rfnoc_copy_impl()
    {
    	//nothing yet for example, but your function here
    }


/* Gr-modtool generated, no needed here in rfnoc
    int
    rfnoc_copy_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
      <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }
*/

  } /* namespace rfnoc_example */
} /* namespace gr */
