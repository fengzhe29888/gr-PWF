/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_PWF_RX_FRAME_SYNC_IMPL_H
#define INCLUDED_PWF_RX_FRAME_SYNC_IMPL_H

#include <PWF/rx_frame_sync.h>
#include <stdio.h>
namespace gr {
  namespace PWF {

    class rx_frame_sync_impl : public rx_frame_sync
    {
     private:
      // Nothing to declare in this block.
	//std::vector<int> d_pilot_seq;
	//std::vector<int> d_prewhiten;
	//int d_nt;
	int d_pilot_length;
	int d_remaining;
	//int d_frame_length;
	//int d_weight;
	int d_state;
     public:
      rx_frame_sync_impl(int pilot_length);
      ~rx_frame_sync_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace PWF
} // namespace gr

#endif /* INCLUDED_PWF_RX_FRAME_SYNC_IMPL_H */

