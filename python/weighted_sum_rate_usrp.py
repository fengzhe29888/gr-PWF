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

class weighted_sum_rate_usrp(gr.sync_block):
    """
    docstring for block weighted_sum_rate_usrp
    """
    def __init__(self, nlinks, nt, Pt, weights):
        gr.sync_block.__init__(self,
            name="weighted_sum_rate_usrp",
            in_sig=[(np.complex64, nt*nt),(np.complex64, nt*nt), (np.complex64, nt*nt), (np.complex64, nt*nt), (np.complex64, nt*nt), (np.complex64, nt*nt)],
            out_sig=[(np.float32)])
	self.nlinks = nlinks
	self.nt = nt
	self.Sigma = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.Omega = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.A = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.B = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.Pt = Pt
	self.counter = 1
	self.weights = weights

    def work(self, input_items, output_items):
	trace_sum = 0
	for l in range(self.nlinks):
		self.Sigma[l] = input_items[l][0].reshape((self.nt,self.nt))
		self.A[l] = input_items[self.nlinks+l][0].reshape((self.nt,self.nt))
		self.B[l] = input_items[2*self.nlinks+l][0].reshape((self.nt,self.nt))
		trace_sum = trace_sum + self.Sigma[l].trace()
		print "Sigma"
		print self.Sigma[l]
		print "A"
		print self.A[l]
		print "B"
		print self.B[l]
	alpha = np.true_divide(self.Pt,trace_sum)
	print "alpha = "
	print alpha
	self.Sigma = np.dot(self.Sigma,alpha)
	#self.A = np.dot(self.A,alpha)
	#self.B = np.dot(self.B,alpha)
	print "updated Sigma"
	print self.Sigma
	print " updated A"
	print self.A
	print "updated B"
	print self.B
		#=====================debugging msg=========================
		#print "Sigma[%d] in iteration %d =" %(l,self.counter)
		#print self.Sigma[l]
		#===========================================================

	for l in range(self.nlinks):
		self.Omega[l] = np.identity(self.nt,dtype=np.complex64)
		for k in range(self.nlinks):
			if k!=l:
				self.Omega[l] = self.B[l] - self.A[l]

	R = 0
	for l in range(self.nlinks):
		R = R + np.dot(self.weights[l],np.log2(np.linalg.det(np.identity(self.nt,dtype=np.complex64)+ np.dot(alpha,np.dot(self.A[l],np.linalg.pinv(self.Omega[l]))))))
		print R

	output_items[0][0] = np.real(R)
	print "rate = %8.4f in iteration %d" %(output_items[0][0],self.counter)
	self.counter += 1

	return 1

