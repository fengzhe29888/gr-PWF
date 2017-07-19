#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jul 17 21:55:07 2017
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
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PWF
import numpy as np
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, EbNo_dB=15):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.EbNo_dB = EbNo_dB

        ##################################################
        # Variables
        ##################################################
        self.Nt = Nt = 2
        self.dft_coef = dft_coef = np.exp(-2*np.pi*1j/Nt)
        self.A = A = np.arange(Nt)[np.newaxis]
        self.tlen = tlen = 128
        self.dft_matrix = dft_matrix = np.power(dft_coef, np.dot(A.transpose(),A))
        self.symbol_rate = symbol_rate = 100000
        self.scramble_2 = scramble_2 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.scramble_1 = scramble_1 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.samp_rate = samp_rate = 400000
        self.prefix = prefix = '/home/zhe/gr-PWF/examples'
        self.noise = noise = [np.identity(Nt), np.identity(Nt)]
        self.dft_pilot_seq = dft_pilot_seq = np.tile(dft_matrix,(tlen/Nt,1))
        self.L = L = 1
        self.sigmagenfile = sigmagenfile = prefix+'/sigmagens/sigmagen_10.bin'
        self.prewhiten1 = prewhiten1 = np.linalg.pinv(noise[1])
        self.prewhiten0 = prewhiten0 = np.linalg.pinv(noise[0])
        self.pilot_seq_2 = pilot_seq_2 = np.multiply(dft_pilot_seq,scramble_2)
        self.pilot_seq_1 = pilot_seq_1 = np.multiply(dft_pilot_seq,scramble_1)
        self.pilot2file = pilot2file = prefix+'/pilots/pilot2_4000.bin'
        self.pilot2 = pilot2 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1])
        self.pilot1file = pilot1file = prefix+'/pilots/pilot1_4000.bin'
        self.pilot1 = pilot1 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1])
        self.payload_size = payload_size = 0
        self.payload = payload = 172
        self.noise_voltage = noise_voltage = (samp_rate/(2*symbol_rate)*10**(-EbNo_dB/10.0))**0.5
        self.noise_hat = noise_hat = [np.identity(Nt), np.identity(Nt)]
        self.ichn_gain_dB = ichn_gain_dB = 10
        self.channelfile = channelfile = prefix+'/channels/2x2channel_10dB_3.bin'
        self.channel = channel = np.true_divide(np.random.standard_normal(size=(L,L,Nt,Nt))+np.random.standard_normal(size=(L,L,Nt,Nt))*1j,np.sqrt(2))
        self.Q = Q = 16
        self.Pt = Pt = 100

        ##################################################
        # Blocks
        ##################################################
        self.single_pole_iir_filter_xx_0_0_1 = filter.single_pole_iir_filter_cc(0.001, 1)
        self.fir_filter_xxx_0_3_0_0 = filter.fir_filter_ccf(1, (pilot1[1::2][::-1]))
        self.fir_filter_xxx_0_3_0_0.declare_sample_delay(0)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_voltage,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(0.8, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_c(pilot1[1::2], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_peak_detector2_fb_0_0 = blocks.peak_detector2_fb(20, tlen/2, 0.001)
        self.blocks_file_sink_0_0_0_0_2_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/rx_frame', False)
        self.blocks_file_sink_0_0_0_0_2_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_2_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/rx', False)
        self.blocks_file_sink_0_0_0_0_2_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_2_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avged', False)
        self.blocks_file_sink_0_0_0_0_2_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flag2', False)
        self.blocks_file_sink_0_0_0_0_2.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_1_0 = blocks.file_sink(gr.sizeof_float*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched2', False)
        self.blocks_file_sink_0_0_0_0_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_1 = blocks.file_sink(gr.sizeof_float*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg2', False)
        self.blocks_file_sink_0_0_0_0_1.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.PWF_rx_frame_sync_0 = PWF.rx_frame_sync(tlen)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.PWF_rx_frame_sync_0, 0), (self.blocks_file_sink_0_0_0_0_2_0_1, 0))    
        self.connect((self.PWF_rx_frame_sync_0, 0), (self.single_pole_iir_filter_xx_0_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_file_sink_0_0_0_0_1_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_peak_detector2_fb_0_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 0), (self.PWF_rx_frame_sync_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 1), (self.blocks_file_sink_0_0_0_0_1, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 0), (self.blocks_file_sink_0_0_0_0_2, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.PWF_rx_frame_sync_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.fir_filter_xxx_0_3_0_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_file_sink_0_0_0_0_2_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.fir_filter_xxx_0_3_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0_0_1, 0), (self.blocks_file_sink_0_0_0_0_2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_EbNo_dB(self):
        return self.EbNo_dB

    def set_EbNo_dB(self, EbNo_dB):
        self.EbNo_dB = EbNo_dB
        self.set_noise_voltage((self.samp_rate/(2*self.symbol_rate)*10**(-self.EbNo_dB/10.0))**0.5)

    def get_Nt(self):
        return self.Nt

    def set_Nt(self, Nt):
        self.Nt = Nt
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_noise_hat([np.identity(self.Nt), np.identity(self.Nt)])
        self.set_noise([np.identity(self.Nt), np.identity(self.Nt)])
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_dft_coef(np.exp(-2*np.pi*1j/self.Nt))
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))
        self.set_A(np.arange(self.Nt)[np.newaxis])

    def get_dft_coef(self):
        return self.dft_coef

    def set_dft_coef(self, dft_coef):
        self.dft_coef = dft_coef
        self.set_dft_matrix(np.power(self.dft_coef, np.dot(A.transpose(),self.A)))

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.set_dft_matrix(np.power(self.dft_coef, np.dot(A.transpose(),self.A)))

    def get_tlen(self):
        return self.tlen

    def set_tlen(self, tlen):
        self.tlen = tlen
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.blocks_peak_detector2_fb_0_0.set_look_ahead(self.tlen/2)

    def get_dft_matrix(self):
        return self.dft_matrix

    def set_dft_matrix(self, dft_matrix):
        self.dft_matrix = dft_matrix
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_noise_voltage((self.samp_rate/(2*self.symbol_rate)*10**(-self.EbNo_dB/10.0))**0.5)

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_noise_voltage((self.samp_rate/(2*self.symbol_rate)*10**(-self.EbNo_dB/10.0))**0.5)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_sigmagenfile(self.prefix+'/sigmagens/sigmagen_10.bin')
        self.set_pilot2file(self.prefix+'/pilots/pilot2_4000.bin')
        self.set_pilot1file(self.prefix+'/pilots/pilot1_4000.bin')
        self.set_channelfile(self.prefix+'/channels/2x2channel_10dB_3.bin')

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.set_prewhiten1(np.linalg.pinv(self.noise[1]))
        self.set_prewhiten0(np.linalg.pinv(self.noise[0]))

    def get_dft_pilot_seq(self):
        return self.dft_pilot_seq

    def set_dft_pilot_seq(self, dft_pilot_seq):
        self.dft_pilot_seq = dft_pilot_seq
        self.set_pilot_seq_2(np.multiply(self.dft_pilot_seq,self.scramble_2))
        self.set_pilot_seq_1(np.multiply(self.dft_pilot_seq,self.scramble_1))

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_sigmagenfile(self):
        return self.sigmagenfile

    def set_sigmagenfile(self, sigmagenfile):
        self.sigmagenfile = sigmagenfile

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

    def get_pilot1(self):
        return self.pilot1

    def set_pilot1(self, pilot1):
        self.pilot1 = pilot1
        self.fir_filter_xxx_0_3_0_0.set_taps((self.pilot1[1::2][::-1]))
        self.blocks_vector_source_x_0.set_data(self.pilot1[1::2], [])

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload

    def get_noise_voltage(self):
        return self.noise_voltage

    def set_noise_voltage(self, noise_voltage):
        self.noise_voltage = noise_voltage
        self.channels_channel_model_0.set_noise_voltage(self.noise_voltage)

    def get_noise_hat(self):
        return self.noise_hat

    def set_noise_hat(self, noise_hat):
        self.noise_hat = noise_hat

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

    def get_Q(self):
        return self.Q

    def set_Q(self, Q):
        self.Q = Q

    def get_Pt(self):
        return self.Pt

    def set_Pt(self, Pt):
        self.Pt = Pt


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--EbNo-dB", dest="EbNo_dB", type="eng_float", default=eng_notation.num_to_str(15),
        help="Set EbNo_dB [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(EbNo_dB=options.EbNo_dB)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
