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


#ifndef INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_H
#define INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_H

#include <rfnoc_example/api.h>
#include <ettus/device3.h>
#include <ettus/rfnoc_block.h>
#include <uhd/stream.hpp>

namespace gr {
  namespace rfnoc_example {

    /*!
     * \brief <+description of block+>
     * \ingroup rfnoc_example
     *
     */

    class RFNOC_EXAMPLE_API rfnoc_copy : virtual public gr::ettus::rfnoc_block
    {
     public:
      typedef boost::shared_ptr<rfnoc_copy> sptr;


      /*!
       *! TAKEN FROM RFNOC_GENERIC
       * \param dev Device3 object
       * \param tx_stream_args Tx Stream Args
       * \param rx_stream_args Tx Stream Args
       * \param block_select In case there's multiple blocks with that name, specify which one to choose (-1 for auto)
       * \param device_select If this Device3 object contains multiple USRPs, specify which device to choose (-1 for auto)
       */
      static sptr make(
          const gr::ettus::device3::sptr &dev,
          const ::uhd::stream_args_t &tx_stream_args,
          const ::uhd::stream_args_t &rx_stream_args,
          const int block_select=-1,
          const int device_select=-1
      );

      /* your functions declaration HERE */
    };

  } // namespace rfnoc_example
} // namespace gr

#endif /* INCLUDED_RFNOC_EXAMPLE_RFNOC_COPY_H */


