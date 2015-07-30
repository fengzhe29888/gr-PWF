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

class identity_sum_rate(gr.sync_block):
    """
    docstring for block identity_sum_rate
    """
    def __init__(self, nlinks,nt,H,ichn_gain_dB,weights,rfrom_file,filename):
        gr.sync_block.__init__(self,
            name="identity_sum_rate",
            in_sig=None,
            out_sig=[np.float32])
	self.nlinks = nlinks
	self.nt = nt
	self.Sigma = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.Omega = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.A = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	#self.counter = 1
	self.weights = weights
	ichn_gain = np.sqrt(np.power(10,np.true_divide(ichn_gain_dB,10))) #convert dB to linear
	self.H = np.zeros((nlinks,nlinks,nt,nt), dtype = np.complex64)
	if rfrom_file:
	#read channel from 'filename'
		f1=open(filename,'rb')
		content = np.fromfile(f1,dtype=np.complex64).reshape(4,4,order='F')
		for l in range(nlinks):
			for k in range(nlinks):
				for m in range(nt):
					self.H[l][k][m] = content[l*nt+m][k*nt:(k+1)*nt]
	else:
	#read random channel H generated in a variable block
		for k in range(nlinks):
			for l in range(nlinks):
				if k!=l:
					self.H[k][l] = np.dot(H[k][l],ichn_gain) #interference channel gain
				else:
					self.H[k][l] = H[k][l]
	
	for l in range(self.nlinks):
		self.Sigma[l] = np.identity(self.nt,dtype=np.complex64)

	for l in range(self.nlinks):
		self.Omega[l] = np.identity(self.nt,dtype=np.complex64)
		for k in range(self.nlinks):
			if k!=l:
				tmp = np.dot(self.H[l][k],self.Sigma[k])
				self.Omega[l] = self.Omega[l] + np.dot(tmp,self.H[l][k].transpose().conj())
	R = 0
	for l in range(self.nlinks):
		self.A[l] = np.dot(np.dot(self.H[l][l],self.Sigma[l]),self.H[l][l].transpose().conj())
		R = R + np.dot(self.weights[l],np.log2(np.linalg.det(self.Omega[l]+self.A[l]))-np.log2(np.linalg.det(self.Omega[l])))

	self.R = np.real(R)
	print "identity rate = %8.4f" %self.R
	self.sent = False



    def work(self, input_items, output_items):
        out = output_items[0]
        if self.sent:
		return -1
        out[:][0] = self.R
	self.sent = True
        return 1

