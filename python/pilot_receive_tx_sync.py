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

class pilot_receive_tx_sync(gr.basic_block):
    """
    docstring for block pilot_receive
    """
    def __init__(self, rfrom_file, filename, pilot_seq,nt,pilot_length, NHAT, frame_length, weight):
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
	self.NHAT = NHAT
	self.nt = nt
	self.pilot_length = pilot_length
	self.frame_length = frame_length
	self.weight = weight
	self.state = 0
        #self.set_history(self.frame_length)
	#self.scounter = 0 #symbol count
	#self.fcounter = 1 #frame count


    def general_work(self, input_items, output_items):
        in0 = input_items[0]
	flags = input_items[1]
        out = output_items[0]
	if len(in0) !=len(flags):
	  print "TX:input length buffer DOESN'T EQUAL"
	len_in = min(len(in0), len(flags))
	if self.state == 0:
	  for i in range(len_in):
	    if flags[i] == 1:
	      print "TX: FLAG FOUND!!!", i
              self.state =1
	      self.consume(0,i+1)
	      self.consume(1,i+1)
              return 0
        if self.state == 1:
	  Y = in0[-self.pilot_length:0]
	  corr = np.true_divide(np.dot(Y.transpose(),self.pilot_seq.conj()),self.pilot_length)
	  A = np.dot(corr,corr.transpose().conj())
	  B = np.true_divide(np.dot(Y.transpose(),Y.conj()),self.pilot_length)
	  Omega_hat = B-A
	  Omega = Omega_hat - self.NHAT + np.identity(self.nt)
	  Sigma = np.dot(np.linalg.pinv(Omega)-np.linalg.pinv(B),self.weight) #nt x nt
	  #=====================debugging msg========================
	  print "Pilot detected! TX sync Sigma ="
	  print Sigma
          out[:]=Sigma.reshape(self.nt*self.nt)
	  self.consume(0,len_in)
	  self.consume(1,len_in)
          return 1
