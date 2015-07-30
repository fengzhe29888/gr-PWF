#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue May 26 22:55:28 2015
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PWF
import numpy as np
import sip
import sys

from distutils.version import StrictVersion
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
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
        # Variables
        ##################################################
        self.Nt = Nt = 2
        self.dft_coef = dft_coef = np.exp(-2*np.pi*1j/Nt)
        self.A = A = np.arange(Nt)[np.newaxis]
        self.tlen = tlen = 4000
        self.samp_rate = samp_rate = 100000
        self.dft_matrix = dft_matrix = np.power(dft_coef, np.dot(A.transpose(),A))
        self.scramble_2 = scramble_2 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.scramble_1 = scramble_1 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.max_iteration = max_iteration = 20
        self.interpo = interpo = samp_rate/1000
        self.dft_pilot_seq = dft_pilot_seq = np.tile(dft_matrix,(tlen/Nt,1))
        self.L = L = 2
        self.sigmagenfile = sigmagenfile = '/home/haili/Documents/SDR Project/Simulation/sigmagens/sigmagen_3.bin'
        self.pilot_seq_2 = pilot_seq_2 = np.multiply(dft_pilot_seq,scramble_2)
        self.pilot_seq_1 = pilot_seq_1 = np.multiply(dft_pilot_seq,scramble_1)
        self.pilot2file = pilot2file = '/home/haili/Documents/SDR Project/Simulation/pilots/pilot2_4000.bin'
        self.pilot1file = pilot1file = '/home/haili/Documents/SDR Project/Simulation/pilots/pilot1_4000.bin'
        self.payload_size = payload_size = 0
        self.npoints = npoints = max_iteration*interpo
        self.ichn_gain_dB = ichn_gain_dB = 10
        self.channelfile = channelfile = '/home/haili/Documents/SDR Project/Simulation/channels/2x2channel_10dB_3.bin'
        self.channel = channel = np.true_divide(np.random.standard_normal(size=(L,L,Nt,Nt))+np.random.standard_normal(size=(L,L,Nt,Nt))*1j,np.sqrt(2))
        self.Pt = Pt = 100

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	npoints, #size
        	samp_rate, #samp_rate
        	"Strong Interference (ichn_gain = 10dB)", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.1)
        self.qtgui_time_sink_x_0.set_y_axis(0, 20)
        
        self.qtgui_time_sink_x_0.set_y_label("Weighted Sum-Rate (bits/s/Hz)", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        
        labels = ["Dual Link", "Identity Sigma", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*4, 2)
        self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1_0 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_streams_to_vector_0_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, interpo)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, interpo)
        self.PWF_weighted_sum_rate_0 = PWF.weighted_sum_rate(L, Nt, Pt, channel, ichn_gain_dB, [1,1], False, channelfile)
        self.PWF_sigmagen_0 = PWF.sigmagen(L, Nt, Pt, False, sigmagenfile)
        self.PWF_power_adjust_1_0 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_power_adjust_1 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_pilot_receive_1_0 = PWF.pilot_receive(True, pilot1file, pilot_seq_1, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_1 = PWF.pilot_receive(True, pilot2file, pilot_seq_2, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_0_0 = PWF.pilot_receive(True, pilot2file, pilot_seq_2, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_receive_0 = PWF.pilot_receive(True, pilot1file, pilot_seq_1, Nt, tlen, tlen+payload_size, 1)
        self.PWF_pilot_gen_3 = PWF.pilot_gen(Nt, tlen, pilot_seq_2, True, pilot2file)
        self.PWF_pilot_gen_2 = PWF.pilot_gen(Nt, tlen, pilot_seq_1, True, pilot1file)
        self.PWF_pilot_gen_1 = PWF.pilot_gen(Nt, tlen, pilot_seq_2, True, pilot2file)
        self.PWF_pilot_gen_0 = PWF.pilot_gen(Nt, tlen, pilot_seq_1, True, pilot1file)
        self.PWF_debug_printmsg_0 = PWF.debug_printmsg(L, Nt, False, max_iteration)
        self.PWF_channel_1 = PWF.channel(L, Nt, ichn_gain_dB, channel, False, False, channelfile)
        self.PWF_channel_0 = PWF.channel(L, Nt, ichn_gain_dB, channel, True, False, channelfile)

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
        self.connect((self.PWF_sigmagen_0, 1), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.PWF_sigmagen_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 1), (self.blocks_repeat_0_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_repeat_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_udp_sink_1, 0))    
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.blocks_udp_sink_1_0, 0))    
        self.connect((self.blocks_udp_source_1, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.PWF_debug_printmsg_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.PWF_debug_printmsg_0, 1))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.PWF_weighted_sum_rate_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.PWF_weighted_sum_rate_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Nt(self):
        return self.Nt

    def set_Nt(self, Nt):
        self.Nt = Nt
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_A(np.arange(self.Nt)[np.newaxis])
        self.set_dft_coef(np.exp(-2*np.pi*1j/self.Nt))
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
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
        self.set_dft_pilot_seq(np.tile(self.dft_matrix,(self.tlen/self.Nt,1)))
        self.set_scramble_1(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)
        self.set_scramble_2(2*np.random.random_integers(0,1,size=(self.tlen,self.Nt))-1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_interpo(self.samp_rate/1000)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

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

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_sigmagenfile(self):
        return self.sigmagenfile

    def set_sigmagenfile(self, sigmagenfile):
        self.sigmagenfile = sigmagenfile

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

    def get_pilot1file(self):
        return self.pilot1file

    def set_pilot1file(self, pilot1file):
        self.pilot1file = pilot1file

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_npoints(self):
        return self.npoints

    def set_npoints(self, npoints):
        self.npoints = npoints

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

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
