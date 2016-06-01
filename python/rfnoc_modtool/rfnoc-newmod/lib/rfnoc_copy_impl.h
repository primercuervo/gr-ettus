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

#ifndef INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_IMPL_H
#define INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_IMPL_H

#include <rfnoc_example/rfnoc_copy.h>
#include <ettus/rfnoc_block_impl.h>

namespace gr {
  namespace rfnoc_example {

    //class RFNOC_EXAMPLE_API rfnoc_copy_impl : public rfnoc_copy, public gr::ettus::rfnoc_block_impl
    class rfnoc_copy_impl : public rfnoc_copy, public gr::ettus::rfnoc_block_impl
    {
     private:
      // Nothing to declare in this block... yet

     public:
      rfnoc_copy_impl(
          const gr::ettus::device3::sptr &dev,
          const ::uhd::stream_args_t &tx_stream_args,
          const ::uhd::stream_args_t &rx_stream_args,
          const int block_select,
          const int device_select
      );
      ~rfnoc_copy_impl();

      
      /* Product of gr_modtool, not needed in rfnoc
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
         */
    };

  } // namespace rfnoc_example
} // namespace gr

#endif /* INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_IMPL_H */


