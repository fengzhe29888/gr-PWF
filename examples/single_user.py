#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Single User
# Generated: Mon Nov 16 16:15:28 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import PWF
import numpy as np
import sys
import time


class single_user(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Single User")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Single User")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "single_user")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Nt = Nt = 2
        self.pilot1 = pilot1 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1])
        self.dft_coef = dft_coef = np.exp(-2*np.pi*1j/Nt)
        self.A = A = np.arange(Nt)[np.newaxis]
        self.tlen = tlen = len(pilot1)/2
        self.samp_rate = samp_rate = 100000
        self.dft_matrix = dft_matrix = np.power(dft_coef, np.dot(A.transpose(),A))
        self.scramble_2 = scramble_2 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.scramble_1 = scramble_1 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.prefix = prefix = '/home/zhe/gr-PWF/examples'
        self.noise = noise = [np.identity(Nt), np.identity(Nt)]
        self.max_iteration = max_iteration = 20
        self.interpo = interpo = samp_rate/1000
        self.dft_pilot_seq = dft_pilot_seq = np.tile(dft_matrix,(tlen/Nt,1))
        self.Q = Q = 16
        self.L = L = 1
        self.tx_gain = tx_gain = 50
        self.tx_freq = tx_freq = 2400000000
        self.sigmagenfile = sigmagenfile = prefix+'/sigmagens/sigmagen_10.bin'
        self.pulse = pulse = filter.firdes.root_raised_cosine(Q,Q,1,0.35,11*Q)
        self.prewhiten1 = prewhiten1 = np.linalg.pinv(noise[1])
        self.prewhiten0 = prewhiten0 = np.linalg.pinv(noise[0])
        self.pilot_seq_2 = pilot_seq_2 = np.multiply(dft_pilot_seq,scramble_2)
        self.pilot_seq_1 = pilot_seq_1 = np.multiply(dft_pilot_seq,scramble_1)
        self.pilot2file = pilot2file = prefix+'/pilots/pilot2_4000.bin'
        self.pilot2 = pilot2 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1])
        self.pilot1file = pilot1file = prefix+'/pilots/pilot1_4000.bin'
        self.payload_size = payload_size = 178
        self.npoints = npoints = max_iteration*interpo
        self.noise_hat = noise_hat = [np.identity(Nt), np.identity(Nt)]
        self.initial_size = initial_size = 0
        self.ichn_gain_dB = ichn_gain_dB = 10
        self.channelfile = channelfile = prefix+'/channels/2x2channel_10dB_3.bin'
        self.channel = channel = np.true_divide(np.random.standard_normal(size=(L,L,Nt,Nt))+np.random.standard_normal(size=(L,L,Nt,Nt))*1j,np.sqrt(2))
        self.Pt = Pt = 100

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 100, 1, 50, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "tx_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_gain_win)
        self._tx_freq_range = Range(0, 5000000000, 1000, 2400000000, 200)
        self._tx_freq_win = RangeWidget(self._tx_freq_range, self.set_tx_freq, "tx_freq", "counter_slider", float)
        self.top_layout.addWidget(self._tx_freq_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_center_freq(tx_freq+10000000, 1)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 1)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 1)
        self.interp_fir_filter_xxx_0_1 = filter.interp_fir_filter_ccc(Q, (pulse))
        self.interp_fir_filter_xxx_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(Q, (pulse))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_vector_to_streams_1 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(map(int, np.random.randint(0,3,payload_size)), True, 2, [])
        self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_gr_complex*4*L, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_gr_complex*4*L, "127.0.0.1", 1234, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*2, (tlen,payload_size))
        self.PWF_sigmagen_0 = PWF.sigmagen(L, Nt, Pt, False, sigmagenfile)
        self.PWF_pilot_gen_tx_0 = PWF.pilot_gen_tx(Nt, tlen, pilot1.reshape(tlen,2), False, pilot1file)
        self.PWF_debug_printmsg_0 = PWF.debug_printmsg(L, Nt, False, max_iteration)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.PWF_debug_printmsg_0, 0), (self.PWF_pilot_gen_tx_0, 0))    
        self.connect((self.PWF_pilot_gen_tx_0, 0), (self.blocks_stream_mux_0, 0))    
        self.connect((self.PWF_sigmagen_0, 0), (self.blocks_udp_sink_1, 0))    
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_vector_to_streams_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.uhd_usrp_sink_0, 1))    
        self.connect((self.blocks_udp_source_1, 0), (self.PWF_debug_printmsg_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 1))    
        self.connect((self.blocks_vector_to_streams_1, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.blocks_vector_to_streams_1, 1), (self.interp_fir_filter_xxx_0_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.blocks_throttle_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "single_user")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_Nt(self):
        return self.Nt

    def set_Nt(self, Nt):
        self.Nt = Nt
        self.set_A(np.arange(self.Nt)[np.newaxis])
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))
        self.set_dft_coef(np.exp(-2*np.pi*1j/self.Nt))
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_noise([np.identity(self.Nt), np.identity(self.Nt)])
        self.set_noise_hat([np.identity(self.Nt), np.identity(self.Nt)])
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)

    def get_pilot1(self):
        return self.pilot1

    def set_pilot1(self, pilot1):
        self.pilot1 = pilot1
        self.set_tlen(len(self.pilot1)/2)

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
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_interpo(self.samp_rate/1000)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

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

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_channelfile(self.prefix+'/channels/2x2channel_10dB_3.bin')
        self.set_pilot1file(self.prefix+'/pilots/pilot1_4000.bin')
        self.set_pilot2file(self.prefix+'/pilots/pilot2_4000.bin')
        self.set_sigmagenfile(self.prefix+'/sigmagens/sigmagen_10.bin')

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.set_prewhiten0(np.linalg.pinv(self.noise[0]))
        self.set_prewhiten1(np.linalg.pinv(self.noise[1]))

    def get_max_iteration(self):
        return self.max_iteration

    def set_max_iteration(self, max_iteration):
        self.max_iteration = max_iteration
        self.set_npoints(self.max_iteration*self.interpo)

    def get_interpo(self):
        return self.interpo

    def set_interpo(self, interpo):
        self.interpo = interpo
        self.set_npoints(self.max_iteration*self.interpo)

    def get_dft_pilot_seq(self):
        return self.dft_pilot_seq

    def set_dft_pilot_seq(self, dft_pilot_seq):
        self.dft_pilot_seq = dft_pilot_seq
        self.set_pilot_seq_1(np.multiply(self.dft_pilot_seq,self.scramble_1))
        self.set_pilot_seq_2(np.multiply(self.dft_pilot_seq,self.scramble_2))

    def get_Q(self):
        return self.Q

    def set_Q(self, Q):
        self.Q = Q
        self.set_pulse(filter.firdes.root_raised_cosine(self.Q,self.Q,1,0.35,11*self.Q))

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 1)
        	

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_sink_0.set_center_freq(self.tx_freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.tx_freq+10000000, 1)

    def get_sigmagenfile(self):
        return self.sigmagenfile

    def set_sigmagenfile(self, sigmagenfile):
        self.sigmagenfile = sigmagenfile

    def get_pulse(self):
        return self.pulse

    def set_pulse(self, pulse):
        self.pulse = pulse
        self.interp_fir_filter_xxx_0.set_taps((self.pulse))
        self.interp_fir_filter_xxx_0_1.set_taps((self.pulse))

    def get_prewhiten1(self):
        return self.prewhiten1

    def set_prewhiten1(self, prewhiten1):
        self.prewhiten1 = prewhiten1

    def get_prewhiten0(self):
        return self.prewhiten0

    def set_prewhiten0(self, prewhiten0):
        self.prewhiten0 = prewhiten0

    def get_pilot_seq_2(self):
        return self.pilot_seq_2

    def set_pilot_seq_2(self, pilot_seq_2):
        self.pilot_seq_2 = pilot_seq_2

    def get_pilot_seq_1(self):
        return self.pilot_seq_1

    def set_pilot_seq_1(self, pilot_seq_1):
        self.pilot_seq_1 = pilot_seq_1

    def get_pilot2file(self):
        return self.pilot2file

    def set_pilot2file(self, pilot2file):
        self.pilot2file = pilot2file

    def get_pilot2(self):
        return self.pilot2

    def set_pilot2(self, pilot2):
        self.pilot2 = pilot2

    def get_pilot1file(self):
        return self.pilot1file

    def set_pilot1file(self, pilot1file):
        self.pilot1file = pilot1file

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size
        self.blocks_vector_source_x_0.set_data(map(int, np.random.randint(0,3,self.payload_size)), [])

    def get_npoints(self):
        return self.npoints

    def set_npoints(self, npoints):
        self.npoints = npoints

    def get_noise_hat(self):
        return self.noise_hat

    def set_noise_hat(self, noise_hat):
        self.noise_hat = noise_hat

    def get_initial_size(self):
        return self.initial_size

    def set_initial_size(self, initial_size):
        self.initial_size = initial_size

    def get_ichn_gain_dB(self):
        return self.ichn_gain_dB

    def set_ichn_gain_dB(self, ichn_gain_dB):
        self.ichn_gain_dB = ichn_gain_dB

    def get_channelfile(self):
        return self.channelfile

    def set_channelfile(self, channelfile):
        self.channelfile = channelfile

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_Pt(self):
        return self.Pt

    def set_Pt(self, Pt):
        self.Pt = Pt


def main(top_block_cls=single_user, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
