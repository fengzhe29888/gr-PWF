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
    docstring for block sigmagen
    """
    def __init__(self, nlinks,nt,Pt,gen_once):
        gr.sync_block.__init__(self,
            name="sigmagen",
            in_sig=None,
            out_sig=[(np.complex64, nt*nt) for i in range(nlinks)])
	self.nlinks = nlinks
	self.nt = nt #nt will be a common number for all nodes
	self.Pt = Pt
	P = 0
	V = np.zeros((nlinks,nt,nt), dtype = np.float32)
	self.Sinit = np.zeros((nlinks,nt,nt), dtype = np.float32) #nlinks nt x nt matrices
	self.sent = False
	self.gen_once = gen_once
	for l in range(self.nlinks):
		V[l] = np.random.standard_normal(size=(self.nt,self.nt))
		self.Sinit[l] = np.dot(V[l],V[l].transpose())
		P = P + self.Sinit[l].trace()
	alpha = np.true_divide(self.Pt,P)
	self.Sinit = np.dot(self.Sinit,alpha)



    def work(self, input_items, output_items):
        if self.gen_once:
		if self.sent:
			#print "sigmagen exit"
			return -1
	for l in range(self.nlinks):
		output_items[l][0] = self.Sinit[l].reshape(self.nt*self.nt)	
		self.sent = True
	#print "Initial Sigmas =" #debugging 
	#print self.Sinit	
       	return 1

