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

class power_adjust(gr.sync_block):
    """
    docstring for block power_adjust
    """
    def __init__(self, nt,Pt,nlinks):
        gr.sync_block.__init__(self,
            name="power_adjust",
            in_sig=[(np.complex64, nt*nt) for i in range(nlinks)],
            out_sig=[(np.complex64, nt*nt) for i in range(nlinks)]) #nlinks input output ports
	self.nlinks = nlinks
	self.nt = nt
	self.Pt = Pt
	


    def work(self, input_items, output_items):
	#print "length of power adjust input 0 size: %d" %len(input_items[0])
	P = 0
	Sigma = np.zeros((self.nlinks,self.nt,self.nt), dtype = np.complex64)
	for l in range(self.nlinks):
		Sigma[l] = input_items[l][0].reshape((self.nt,self.nt))
		P = P + Sigma[l].trace()
	alpha = np.true_divide(self.Pt,P)
	Sigma = np.dot(Sigma,alpha)
	#print "adjusted Sigma ="
	#print Sigma
	
	for l in range(self.nlinks):
		output_items[l][0] = Sigma[l].reshape(self.nt*self.nt)	

        return 1

