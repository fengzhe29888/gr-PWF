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

class pilot_receive_usrp(gr.decim_block):
    """
    docstring for block pilot_receive_usrp
    """
    def __init__(self, pilot_seq, nt, pilot_length, frame_length, weight):
        gr.decim_block.__init__(self,
            name="pilot_receive_usrp",
            in_sig=[(np.complex64, nt)],
            out_sig=[(np.complex64, nt*nt),(np.complex64, nt*nt),(np.complex64, nt*nt)], decim=frame_length)
	self.nt = nt
	self.pilot_seq = pilot_seq
	self.pilot_length = pilot_length
	self.frame_length = frame_length
	self.weight = weight
	self.scounter = 0 #symbol count
	self.fcounter = 1 #frame count

    def work(self, input_items, output_items):
        in0 = input_items[0]
	if len(in0) != self.frame_length:
		print "pilot receive input buffer size != frame length"
	if self.scounter==0: #start of a frame
		Y = in0[:self.pilot_length]
		corr = np.true_divide(np.dot(Y.transpose(),self.pilot_seq.conj()),self.pilot_length) #nt x nt
		#=====================debugging msg========================
		#print "Pilot detected! Estimated channel = "
		#print corr
		#==========================================================
		A = np.dot(corr,corr.transpose().conj())
		B = np.true_divide(np.dot(Y.transpose(),Y.conj()),self.pilot_length)
		Omega = B-A
		Sigma = np.dot(np.linalg.pinv(Omega)-np.linalg.pinv(B),self.weight) #nt x nt
		#=====================debugging msg========================
		print "Pilot detected! Sigma ="
		print Sigma
		print "A = :"
		print A
		print "B = :"
		print B
		#==========================================================
		output_items[0][0] = Sigma.reshape(self.nt*self.nt)
		output_items[1][0] = A.reshape(self.nt*self.nt)
		output_items[2][0] = B.reshape(self.nt*self.nt)
	self.scounter = self.scounter + len(in0)
	if self.scounter==self.frame_length:
		self.fcounter += 1
		self.scounter = 0

        return 1
