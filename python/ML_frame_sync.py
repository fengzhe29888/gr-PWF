#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr

class ML_frame_sync(gr.decim_block):
    """
    docstring for block ML_frame_sync
    """
    def __init__(self, pilot, pilot_length, nt, rho):
        gr.decim_block.__init__(self,
            name="ML_frame_sync",
            in_sig=[(np.complex64, nt)],
            out_sig=[(np.float32,1)], decim = 1)
	self.pilot = pilot
	self.pilot_length = pilot_length
	self.nt = nt
	self.rho = rho
	self.accum_length = 0
	self.G = np.kron(np.identity(nt,dtype=np.complex64),self.pilot)
	self.M = np.dot(self.G, np.linalg.pinv(self.G))*self.rho/(self.pilot_length+self.rho)
	self.set_history(self.pilot_length)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

	length = len(input_items[0]) #input length
	self.accum_length = self.accum_length +length
	Y = np.zeros((1,self.pilot_length), dtype = np.complex64)
	for l in range(length-self.pilot_length):
	    Y =  in0[l:l+self.pilot_length].transpose().reshape(1,2*self.pilot_length)
	    temp1 = np.dot(Y.conj(),self.M)
            out[l] = np.dot(temp1, Y.transpose())[0][0]

	#print "input length is"
	#print len(input_items[0]), length
        return length
