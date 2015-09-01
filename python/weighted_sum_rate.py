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

class weighted_sum_rate(gr.sync_block):
    """
    docstring for block weighted_sum_rate
    """
    def __init__(self, nlinks,nt,Pt,H,ichn_gain_dB,weights,prewhiten,rfrom_file,filename):
        gr.sync_block.__init__(self,
            name="weighted_sum_rate",
            in_sig=[(np.complex64, nt*nt) for i in range(nlinks)], #input Sigma
            out_sig=[(np.float32),(np.float32)]) #output rate
	self.nlinks = nlinks
	self.nt = nt
	self.Sigma = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.Omega = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.A = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	self.prewhiten = prewhiten
	self.counter = 1
	self.weights = weights
	ichn_gain = np.sqrt(np.power(10,np.true_divide(ichn_gain_dB,10))) #convert dB to linear
	#======================read channel from file/variable============================
	self.H = np.zeros((nlinks,nlinks,nt,nt), dtype = np.complex64)
	if rfrom_file:	#read channel from 'filename'
		f1=open(filename,'rb')
		content = np.fromfile(f1,dtype=np.complex64).reshape(4,4,order='F')
		for l in range(nlinks):
			for k in range(nlinks):
				for m in range(nt):
					self.H[l][k][m] = content[l*nt+m][k*nt:(k+1)*nt]
	else:	#read random channel H generated in a variable block
		for k in range(nlinks):
			for l in range(nlinks):
				if k!=l:
					self.H[k][l] = np.dot(H[k][l],ichn_gain) #interference channel gain
				else:
					self.H[k][l] = H[k][l]
	#=================================================================================
	#====================evaluate rate using identity Sigma===========================
	Sigma_I = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	Omega_I = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	A_I = np.zeros((nlinks,nt,nt), dtype=np.complex64)
	alpha_I = np.true_divide(Pt,nlinks*nt) #trace sum = nlinks*nt 
	for l in range(nlinks):
		Sigma_I[l] = np.dot(np.identity(nt,dtype=np.complex64),alpha_I) #adjust power
	for l in range(nlinks):
		Omega_I[l] = np.identity(nt,dtype=np.complex64)
		for k in range(nlinks):
			if k!=l:
				tmp_I = np.dot(self.H[l][k],Sigma_I[k])
				Omega_I[l] = Omega_I[l] + np.dot(tmp_I,self.H[l][k].transpose().conj())
	R_I = 0
	for l in range(nlinks):
		A_I[l] = np.dot(np.dot(self.H[l][l],Sigma_I[l]),self.H[l][l].transpose().conj())
		R_I = R_I + np.dot(weights[l],np.log2(np.linalg.det(Omega_I[l]+A_I[l]))-np.log2(np.linalg.det(Omega_I[l])))
	self.R_I = np.real(R_I)
	print "Rate with Identity Sigma = %8.4f" %self.R_I
	#==================================================================================


    def work(self, input_items, output_items):
	for l in range(self.nlinks):
		self.Sigma[l] = input_items[l][0].reshape((self.nt,self.nt))
		#=====================debugging msg=========================
		#print "Sigma[%d] in iteration %d =" %(l,self.counter)
		#print self.Sigma[l]
		#===========================================================

	for l in range(self.nlinks):
		self.Omega[l] = np.identity(self.nt,dtype=np.complex64)
		for k in range(self.nlinks):
			if k!=l:
				tmp1 = np.dot(self.prewhiten[l], self.H[l][k])
				tmp2 = np.dot(tmp1,self.Sigma[k])
				tmp3 = np.dot(tmp2, self.H[l][k].transpose().conj())
				self.Omega[l] = self.Omega[l] + np.dot(tmp3,self.prewhiten[l])

	R = 0
	for l in range(self.nlinks):
		tmp4 = np.dot(self.prewhiten[l], self.H[l][l])
		tmp5 = np.dot(np.dot(tmp4, self.Sigma[l]),self.H[l][l].transpose().conj())
		self.A[l] = np.dot(tmp5, self.prewhiten[l])
		R = R + np.dot(self.weights[l],np.log2(np.linalg.det(self.Omega[l]+self.A[l]))-np.log2(np.linalg.det(self.Omega[l])))

	output_items[0][0] = np.real(R)
	output_items[1][0] = self.R_I
	print "rate = %8.4f in iteration %d" %(output_items[0][0],self.counter)
	self.counter += 1

	return 1

