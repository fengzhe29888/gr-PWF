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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "rx_frame_sync_impl.h"
#include <stdio.h>
namespace gr {
  namespace PWF {

    rx_frame_sync::sptr
    rx_frame_sync::make(int pilot_length)
    {
      return gnuradio::get_initial_sptr
        (new rx_frame_sync_impl(pilot_length));
    }

    /*
     * The private constructor
     */
    rx_frame_sync_impl::rx_frame_sync_impl(int pilot_length)
      : gr::block("rx_frame_sync",
              gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))), 
	d_pilot_length(pilot_length),
	d_remaining(d_pilot_length),
	d_state(0)
    {
	}	

    /*
     * Our virtual destructor.
     */
    rx_frame_sync_impl::~rx_frame_sync_impl()
    {
    }

    void
    rx_frame_sync_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
       ninput_items_required[0] = noutput_items + history()-1;
       ninput_items_required[1] = noutput_items + history()-1;

    }

    int
    rx_frame_sync_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      	const gr_complex *in_data = (const gr_complex *) input_items[0];
      	const char *in_flag = (const char *) input_items[1];
      	gr_complex *out = (gr_complex *) output_items[0];
	int ni=std::min(ninput_items[0],ninput_items[1]);
	//printf("item size of pilot receiver %d\n",itemsize);
      // Do <+signal processing+>
	if (d_state == 0){
	  printf("YYYYYYYY STATE 0 ninput_items is %d, input_data %d, input_flags %d\n",ni,ninput_items[0],ninput_items[1]);
	  for(int l = 0; l< ni; l++){
	  //printf("searching for flags %d\n",l);
	    if(in_flag[l] !=0){
	      printf("!!!!!!!!!   FLAG FOUND !!!!   at %d\n",l);
	      d_state =1;
              consume_each(l+1);
	      return 0;
	    }
	  }
	  consume_each(ni);
	  return 0;
	}
	else if(d_state ==1){
	  set_history(d_pilot_length);
	  printf("XXXXXX STATE 1 ninput_items is %d, input_data %d, input_flags %d\n",ni,ninput_items[0],ninput_items[1]);
	  //if(ni < d_pilot_length)
	    //return 0;
	  if (ni > d_remaining){
	    for (int i=0; i<d_remaining; i++){
	      out[i] = in_data[i-d_pilot_length];
	      //printf("GGGGGGGGGGGGGGGGGGGGGGGGG output value %f + i%f at %d\n",real(out[i]),imag(out[i]),i);
	    }
	    d_state = 0;
	    d_remaining = d_pilot_length;
	  //memcpy(out,in_data-d_pilot_length,d_pilot_length);
	  //printf("item size of pilot receiver %d\n",d_pilot_length);
      	    consume_each (d_remaining);
      	    return d_remaining;
	  }
	  else if (ni < d_pilot_length){
	    for (int i=0; i< ni; i++){
	     out[i] = in_data[i-d_pilot_length];
	     //printf("NI less than pilot_length output value %f + i%f at %d\n",real(out[i]),imag(out[i]),i);
	    }
	    d_state = 1;
	    d_remaining = d_pilot_length - ni;
	    consume_each (ni);
	    return ni;
	  }
	}
	
      // Tell runtime system how many input items we consumed on
      // each input stream.


      // Tell runtime system how many output items we produced.
    }

  } /* namespace PWF */
} /* namespace gr */

