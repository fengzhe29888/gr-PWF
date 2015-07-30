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

class sigmagen(gr.sync_block):
    """
	This block is used to generate initial Sigmas for PWF algorithm, and then it will exit.
	By choosing not to read initial Sigmas from File, it will generate random Sigmas and multiply by a constant in order to have sum of traces equal to Pt, otherwise it will read from a file generated in Matlab for comparison purpose.
	Since GRC will accept 1-d array but not 2-d array, we need to reshape the initial Sigmas, and the output will be a vector of length nt*nt, where nt is antenna number.	
    """
    def __init__(self, nlinks,nt,Pt,rfrom_file,filename):
        gr.sync_block.__init__(self,
            name="sigmagen",
            in_sig=None,
            out_sig=[(np.complex64, nt*nt) for i in range(nlinks)])
	self.nlinks = nlinks
	self.nt = nt #nt is a common number for all nodes
	self.Pt = Pt
	self.sent = False
	#=============read Sinit from file or generate a random one======================
	self.Sinit = np.zeros((nlinks,nt,nt), dtype = np.complex64) #nlinks nt x nt matrices
	if rfrom_file:	#read Sinit from 'filename'
		f1=open(filename,'rb')
		content = np.fromfile(f1,dtype=np.complex64).reshape(nt,nlinks*nt,order='F')
		for l in range(nlinks):
			for k in range(nt):
				self.Sinit[l][k]= content[k][l*nt:(l+1)*nt]
	else:	#generate a random Sinit and adjust its power
		P = 0
		V = np.zeros((nlinks,nt,nt), dtype = np.float32)
		for l in range(self.nlinks):
			V[l] = np.random.standard_normal(size=(self.nt,self.nt))
			self.Sinit[l] = np.dot(V[l],V[l].transpose())
			P = P + self.Sinit[l].trace()
		alpha = np.true_divide(self.Pt,P)
		self.Sinit = np.dot(self.Sinit,alpha)
	#=================================================================================



    def work(self, input_items, output_items):
	if self.sent:
		#generate one Sinit for each link, then exit
		return -1
	for l in range(self.nlinks):
		output_items[l][0] = self.Sinit[l].reshape(self.nt*self.nt)	
		self.sent = True
	#=====================debugging msg========================
	#print "Initial Sigmas ="
	#print self.Sinit
	#==========================================================
       	return 1

