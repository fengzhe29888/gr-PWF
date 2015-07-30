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

class debug_printmsg(gr.sync_block):
    """
    docstring for block debug_printmsg
    """
    def __init__(self, nlinks,nt,is_output):
        gr.sync_block.__init__(self,
            name="debug_printmsg",
            in_sig=[(np.complex64, nt*nt) for i in range(nlinks)],
            out_sig=[(np.complex64, nt*nt) for i in range(nlinks)])
	self.nlinks = nlinks
	self.nt = nt
	self.is_output = is_output
	self.counter = 1


    def work(self, input_items, output_items):
	if self.counter >= 20: #maximum iteration
		return -1
		
	Sigma = np.zeros((self.nlinks,self.nt,self.nt), dtype = np.complex64)
	for l in range(self.nlinks):
		Sigma[l] = input_items[l][0].reshape([self.nt,self.nt])
		output_items[l][0] = input_items[l][0]
	
	if self.is_output:
		#print "ouput Sigma in iteration %d =" %self.counter
		#print Sigma
		self.counter += 1
	else:
		#print "input Sigma in iteration %d =" %self.counter
		#print Sigma
		self.counter += 1

        return 1

