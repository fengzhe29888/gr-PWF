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

class channel(gr.sync_block):
    """
    docstring for block channel
    """
    def __init__(self, nlinks,nt,ichn_gain_dB,H,is_forward):
        gr.sync_block.__init__(self,
            name="channel",
            in_sig=[(np.complex64, nt) for i in range(nlinks)],
            out_sig=[(np.complex64, nt) for i in range(nlinks)])
	self.nlinks = nlinks
	self.nt = nt
	ichn_gain = np.sqrt(np.power(10,np.true_divide(ichn_gain_dB,10))) #convert dB to linear
	#generate random channel H in a variable block
	#H = np.true_divide(np.random.standard_normal(size=(L,L,Nt,Nt))+np.random.standard_normal(size=(L,L,Nt,Nt))*1j,np.sqrt(2))
	self.H = np.zeros((nlinks,nlinks,nt,nt), dtype = np.complex64)
	for k in range(nlinks):
		for l in range(nlinks):
			if k!=l:
				self.H[k][l] = np.dot(H[k][l],ichn_gain) #interference channel gain
			else:
				self.H[k][l] = H[k][l]
	#print "channel H ="
	#print self.H
	self.is_forward = is_forward


    def work(self, input_items, output_items):
	length = len(input_items[0]) #input length
	Y = np.zeros((self.nlinks,length,self.nt), dtype = np.complex64)
	for l in range(self.nlinks):
		Y[l] = np.random.standard_normal(size=(length,self.nt))+np.random.standard_normal(size=(length,self.nt))*1j
		Y[l] = np.true_divide(Y[l],np.sqrt(2)).astype(np.complex64)
		for k in range(self.nlinks):
			if self.is_forward:
				Y[l] = Y[l] + np.dot(input_items[k],self.H[l][k].transpose())
			else:
				Y[l] = Y[l] + np.dot(input_items[k],self.H[k][l].conj())
		output_items[l][:] = Y[l]

        return length

