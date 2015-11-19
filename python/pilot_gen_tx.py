#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
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

class pilot_gen_tx(gr.interp_block):
    """
    For every input Sigma, this block will generate a pilot sequence. You could either read pilot from file generated in Matlab or read pilot sequence from a variable created in GRC.
    """
    def __init__(self, nt,pilot_length,pilot,rfrom_file,filename):
        gr.interp_block.__init__(self,
            name="pilot_gen_tx",
            in_sig=[(np.complex64, nt*nt)],
            out_sig=[(np.complex64, nt)], interp=pilot_length)
	self.nt = nt
	self.pilot_length = pilot_length
	#=======================read pilot from file/variable===========================
	if rfrom_file:	#read pilot from 'filename'
		f1=open(filename,'rb') #read only in binary format
		self.pilot_seq = np.fromfile(f1,dtype=np.complex64).reshape(pilot_length,nt) #read pilot from file
	else:	#read pilot generated in a variable block
		self.pilot_seq = pilot
	#===============================================================================



    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
	Sigma = in0[0].reshape((self.nt,self.nt))
	#=====================debugging msg========================
	print "The Sigmas ="
	print Sigma
	U, d, V = np.linalg.svd(Sigma) #SVD, d is a 1-d array, need to convert to a matrix D
	D = np.zeros((self.nt,self.nt))
	np.fill_diagonal(D,d)
	pilot_send = np.dot(np.dot(self.pilot_seq, np.sqrt(D)),U.transpose()) #pilot_seq * sqrt(D) * U_transpose
	for i in range(self.pilot_length):
		out[i] = pilot_send[i]

        return self.pilot_length
