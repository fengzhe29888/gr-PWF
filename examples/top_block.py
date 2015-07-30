#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Jul 29 10:43:54 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PWF
import numpy as np

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.Nt = Nt = 2
        self.dft_coef = dft_coef = np.exp(-2*np.pi*1j/Nt)
        self.A = A = np.arange(Nt)[np.newaxis]
        self.tlen = tlen = 4000
        self.dft_matrix = dft_matrix = np.power(dft_coef, np.dot(A.transpose(),A))
        self.scramble_2 = scramble_2 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.scramble_1 = scramble_1 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.dft_pilot_seq = dft_pilot_seq = np.tile(dft_matrix,(tlen/Nt,1))
        self.L = L = 2
        self.samp_rate = samp_rate = 32000
        self.pilot_seq_2 = pilot_seq_2 = np.multiply(dft_pilot_seq,scramble_2)
        self.pilot_seq_1 = pilot_seq_1 = np.multiply(dft_pilot_seq,scramble_1)
        self.payload_size = payload_size = 0
        self.ichn_gain_dB = ichn_gain_dB = 10
        self.channel = channel = np.true_divide(np.random.standard_normal(size=(L,L,Nt,Nt))+np.random.standard_normal(size=(L,L,Nt,Nt))*1j,np.sqrt(2))
        self.Pt = Pt = 100

        ##################################################
        # Blocks
        ##################################################
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*4, 2)
        self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1_0 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_streams_to_vector_0_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.PWF_weighted_sum_rate_0 = PWF.weighted_sum_rate(L, Nt, channel, ichn_gain_dB, [1,1])
        self.PWF_sigmagen_0 = PWF.sigmagen(L, Nt, Pt, True)
        self.PWF_power_adjust_1_0 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_power_adjust_1 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_pilot_receive_1_0 = PWF.pilot_receive(pilot_seq_1, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_1 = PWF.pilot_receive(pilot_seq_2, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_0_0 = PWF.pilot_receive(pilot_seq_2, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_0 = PWF.pilot_receive(pilot_seq_1, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_gen_3 = PWF.pilot_gen(Nt, tlen, pilot_seq_2)
        self.PWF_pilot_gen_2 = PWF.pilot_gen(Nt, tlen, pilot_seq_1)
        self.PWF_pilot_gen_1 = PWF.pilot_gen(Nt, tlen, pilot_seq_2)
        self.PWF_pilot_gen_0 = PWF.pilot_gen(Nt, tlen, pilot_seq_1)
        self.PWF_debug_printmsg_0 = PWF.debug_printmsg(L, Nt, False)
        self.PWF_channel_1 = PWF.channel(L, Nt, ichn_gain_dB, channel, False)
        self.PWF_channel_0 = PWF.channel(L, Nt, ichn_gain_dB, channel, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.PWF_channel_0, 0), (self.PWF_pilot_receive_0, 0))    
        self.connect((self.PWF_channel_0, 1), (self.PWF_pilot_receive_1, 0))    
        self.connect((self.PWF_channel_1, 1), (self.PWF_pilot_receive_0_0, 0))    
        self.connect((self.PWF_channel_1, 0), (self.PWF_pilot_receive_1_0, 0))    
        self.connect((self.PWF_debug_printmsg_0, 0), (self.PWF_pilot_gen_0, 0))    
        self.connect((self.PWF_debug_printmsg_0, 1), (self.PWF_pilot_gen_1, 0))    
        self.connect((self.PWF_pilot_gen_0, 0), (self.PWF_channel_0, 0))    
        self.connect((self.PWF_pilot_gen_1, 0), (self.PWF_channel_0, 1))    
        self.connect((self.PWF_pilot_gen_2, 0), (self.PWF_channel_1, 0))    
        self.connect((self.PWF_pilot_gen_3, 0), (self.PWF_channel_1, 1))    
        self.connect((self.PWF_pilot_receive_0, 0), (self.PWF_power_adjust_1, 0))    
        self.connect((self.PWF_pilot_receive_0_0, 0), (self.PWF_power_adjust_1_0, 1))    
        self.connect((self.PWF_pilot_receive_1, 0), (self.PWF_power_adjust_1, 1))    
        self.connect((self.PWF_pilot_receive_1_0, 0), (self.PWF_power_adjust_1_0, 0))    
        self.connect((self.PWF_power_adjust_1, 0), (self.PWF_pilot_gen_2, 0))    
        self.connect((self.PWF_power_adjust_1, 1), (self.PWF_pilot_gen_3, 0))    
        self.connect((self.PWF_power_adjust_1_0, 1), (self.blocks_streams_to_vector_0_0, 1))    
        self.connect((self.PWF_power_adjust_1_0, 0), (self.blocks_streams_to_vector_0_0, 0))    
        self.connect((self.PWF_sigmagen_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.PWF_sigmagen_0, 1), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.PWF_weighted_sum_rate_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_udp_sink_1, 0))    
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.blocks_udp_sink_1_0, 0))    
        self.connect((self.blocks_udp_source_1, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.PWF_debug_printmsg_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.PWF_debug_printmsg_0, 1))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.PWF_weighted_sum_rate_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.PWF_weighted_sum_rate_0, 1))    


    def get_Nt(self):
        return self.Nt

    def set_Nt(self, Nt):
        self.Nt = Nt
        self.set_A(np.arange(self.Nt)[np.newaxis])
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_dft_coef(np.exp(-2*np.pi*1j/self.Nt))
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_dft_coef(self):
        return self.dft_coef

    def set_dft_coef(self, dft_coef):
        self.dft_coef = dft_coef
        self.set_dft_matrix(np.power(self.dft_coef, np.dot(self.A.transpose(),self.A)))

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.set_dft_matrix(np.power(self.dft_coef, np.dot(self.A.transpose(),self.A)))

    def get_tlen(self):
        return self.tlen

    def set_tlen(self, tlen):
        self.tlen = tlen
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)

    def get_dft_matrix(self):
        return self.dft_matrix

    def set_dft_matrix(self, dft_matrix):
        self.dft_matrix = dft_matrix
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))

    def get_scramble_2(self):
        return self.scramble_2

    def set_scramble_2(self, scramble_2):
        self.scramble_2 = scramble_2
        self.set_pilot_seq_2(np.multiply(self.dft_pilot_seq,self.scramble_2))

    def get_scramble_1(self):
        return self.scramble_1

    def set_scramble_1(self, scramble_1):
        self.scramble_1 = scramble_1
        self.set_pilot_seq_1(np.multiply(self.dft_pilot_seq,self.scramble_1))

    def get_dft_pilot_seq(self):
        return self.dft_pilot_seq

    def set_dft_pilot_seq(self, dft_pilot_seq):
        self.dft_pilot_seq = dft_pilot_seq
        self.set_pilot_seq_1(np.multiply(self.dft_pilot_seq,self.scramble_1))
        self.set_pilot_seq_2(np.multiply(self.dft_pilot_seq,self.scramble_2))

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_pilot_seq_2(self):
        return self.pilot_seq_2

    def set_pilot_seq_2(self, pilot_seq_2):
        self.pilot_seq_2 = pilot_seq_2

    def get_pilot_seq_1(self):
        return self.pilot_seq_1

    def set_pilot_seq_1(self, pilot_seq_1):
        self.pilot_seq_1 = pilot_seq_1

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_ichn_gain_dB(self):
        return self.ichn_gain_dB

    def set_ichn_gain_dB(self, ichn_gain_dB):
        self.ichn_gain_dB = ichn_gain_dB

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_Pt(self):
        return self.Pt

    def set_Pt(self, Pt):
        self.Pt = Pt


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
