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

class pilot_receive_rx_sync(gr.basic_block):
    """
    docstring for block pilot_receive
    """
    def __init__(self, rfrom_file, filename, pilot_seq, prewhiten, nt,pilot_length,frame_length, weight):
        gr.basic_block.__init__(self,
            name="pilot_receive_rx_sync",
            in_sig=[(np.complex64, nt),(np.int8,1)],
            out_sig=[(np.complex64, nt*nt)])
	#=======================read pilot from file/variable===========================
	if rfrom_file:	#read pilot from 'filename'
		f1=open(filename,'rb') #read only in binary format
		self.pilot_seq = np.fromfile(f1,dtype=np.complex64).reshape(pilot_length,nt)
	else:	#read pilot generated in a variable block
		self.pilot_seq = pilot_seq
	#===============================================================================
	self.prewhiten = prewhiten
	self.nt = nt
	self.pilot_length = pilot_length
	self.frame_length = frame_length
	self.weight = weight
	#self.scounter = 0 #symbol count
	#self.fcounter = 1 #frame count


    def general_work(self, input_items, output_items):
	print "pilot"
        in0 = input_items[0]
	flags = input_items[1]
        out = output_items[0]
	if len(in0) != self.frame_length:
		print "pilot receive input buffer size != frame length"
	for i in range(len(in0)):
		#print "loop to",i
		if flags[i] != 0:
			print "forward input flag is =",i
			Y0 = in0[i-self.pilot_length+1:i+1]
			Y = np.dot(self.prewhiten, Y0.transpose())
			Y = Y.transpose()
			corr = np.true_divide(np.dot(Y.transpose(),self.pilot_seq.conj()),self.pilot_length) #nt x nt
				#=====================debugging msg========================
			#print "the received processed samples"
			#print Y0
			print "Pilot detected! Estimated channel = "
			print corr
				#==========================================================
			A = np.dot(corr,corr.transpose().conj())
			B = np.true_divide(np.dot(Y.transpose(),Y.conj()),self.pilot_length)
			Omega = B-A
			Sigma = np.dot(np.linalg.pinv(Omega)-np.linalg.pinv(B),self.weight) #nt x nt
				#=====================debugging msg========================
			print "Pilot detected! rx sync Sigma ="
			print Sigma
				#==========================================================
			out[0] = Sigma.reshape(self.nt*self.nt)
			break
	self.consume(0,len(in0))
	self.consume(1,len(in0))
        return 1


