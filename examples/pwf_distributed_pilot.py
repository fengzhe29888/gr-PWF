#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pwf Distributed Pilot
# Generated: Mon Nov 16 14:11:35 2015
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from pulse_recover import pulse_recover  # grc-generated hier_block
from pulse_shaping import pulse_shaping  # grc-generated hier_block
import PWF
import numpy as np
import sip


class pwf_distributed_pilot(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pwf Distributed Pilot")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pwf Distributed Pilot")
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

        self.settings = Qt.QSettings("GNU Radio", "pwf_distributed_pilot")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Nt = Nt = 2
        self.dft_coef = dft_coef = np.exp(-2*np.pi*1j/Nt)
        self.A = A = np.arange(Nt)[np.newaxis]
        self.tlen = tlen = 128
        self.samp_rate = samp_rate = 100000
        self.dft_matrix = dft_matrix = np.power(dft_coef, np.dot(A.transpose(),A))
        self.scramble_2 = scramble_2 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.scramble_1 = scramble_1 = 2*np.random.random_integers(0,1,size=(tlen,Nt))-1
        self.prefix = prefix = '/home/zhe/gr-PWF/examples'
        self.noise = noise = [np.identity(Nt), np.identity(Nt)]
        self.max_iteration = max_iteration = 30
        self.interpo = interpo = samp_rate/1000
        self.dft_pilot_seq = dft_pilot_seq = np.tile(dft_matrix,(tlen/Nt,1))
        self.Q = Q = 16
        self.L = L = 2
        self.sigmagenfile = sigmagenfile = prefix+'/sigmagens/sigmagen_10.bin'
        self.pulse = pulse = filter.firdes.root_raised_cosine(Q,Q,1,0.35,11*Q)
        self.prewhiten1 = prewhiten1 = np.linalg.pinv(noise[1])
        self.prewhiten0 = prewhiten0 = np.linalg.pinv(noise[0])
        self.pilot_seq_2 = pilot_seq_2 = np.multiply(dft_pilot_seq,scramble_2)
        self.pilot_seq_1 = pilot_seq_1 = np.multiply(dft_pilot_seq,scramble_1)
        self.pilot2file = pilot2file = prefix+'/pilots/pilot2_4000.bin'
        self.pilot2 = pilot2 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1])
        self.pilot1file = pilot1file = prefix+'/pilots/pilot1_4000.bin'
        self.pilot1 = pilot1 = np.array([1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1])
        self.payload_size = payload_size = 168
        self.npoints = npoints = max_iteration*interpo
        self.noise_hat = noise_hat = [np.identity(Nt), np.identity(Nt)]
        self.ichn_gain_dB = ichn_gain_dB = 10
        self.channelfile = channelfile = prefix+'/channels/2x2channel_10dB_3.bin'
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
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
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
        self.pulse_shaping_0_2 = pulse_shaping(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_shaping_0_0_1 = pulse_shaping(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_shaping_0_0 = pulse_shaping(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_shaping_0 = pulse_shaping(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_recover_0_1_0 = pulse_recover(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_recover_0_1 = pulse_recover(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_recover_0_0 = pulse_recover(
            Q=Q,
            pulse=pulse,
        )
        self.pulse_recover_0 = pulse_recover(
            Q=Q,
            pulse=pulse,
        )
        self.fir_filter_xxx_0_3_1_1_0 = filter.fir_filter_ccf(1, (pilot1[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_3_1_1 = filter.fir_filter_ccf(1, (pilot2[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_3_1_0 = filter.fir_filter_ccf(1, (pilot2[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_3_1 = filter.fir_filter_ccf(1, (pilot1[0::2][::-1]))
        self.fir_filter_xxx_0_3_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_3_0 = filter.fir_filter_ccc(1, (pilot2[0::2][::-1]))
        self.fir_filter_xxx_0_3_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_3 = filter.fir_filter_ccf(1, (pilot1[0::2][::-1]))
        self.fir_filter_xxx_0_3.declare_sample_delay(0)
        self.blocks_vector_to_streams_1_1_0_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_1_1_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_1_1 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_1_0_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_1_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_1 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*4, 2)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c(map(int, np.random.randint(0,3,payload_size)), True, 2, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c(map(int, np.random.randint(0,3,payload_size)), True, 2, [])
        self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_1_0 = blocks.udp_sink(gr.sizeof_gr_complex*8, "127.0.0.1", 1234, 1472, True)
        self.blocks_streams_to_vector_1_1 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_streams_to_vector_1_0_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_streams_to_vector_1_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_streams_to_vector_1 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_streams_to_vector_0_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*4, 2)
        self.blocks_stream_mux_0_1 = blocks.stream_mux(gr.sizeof_gr_complex*2, (tlen,payload_size))
        self.blocks_stream_mux_0_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*2, (tlen,payload_size))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*2, (tlen,payload_size))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*2, (tlen,payload_size))
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, interpo)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, interpo)
        self.blocks_peak_detector2_fb_0_1_1_0 = blocks.peak_detector2_fb(5, tlen+payload_size-22, 0.001)
        self.blocks_peak_detector2_fb_0_1_1 = blocks.peak_detector2_fb(25, tlen+payload_size-22, 0.001)
        self.blocks_peak_detector2_fb_0_1_0 = blocks.peak_detector2_fb(25, tlen+payload_size-22, 0.001)
        self.blocks_peak_detector2_fb_0_1 = blocks.peak_detector2_fb(25, tlen+payload_size-22, 0.001)
        self.blocks_peak_detector2_fb_0_0 = blocks.peak_detector2_fb(15, tlen+payload_size-22, 0.001)
        self.blocks_peak_detector2_fb_0 = blocks.peak_detector2_fb(25, tlen+payload_size-22, 0.001)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0_0_0_2 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_1_0 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_1 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_1 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((1/ float(Q), ))
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched5", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched4", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched3", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched2", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_2_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_2 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched1", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_2.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1_0 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags5", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags4", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags3", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags2", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags1", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_1 = blocks.file_sink(gr.sizeof_char*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/flags", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg5", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg4", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg3", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg2", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/a2", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/a1", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg1", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/avg", False)
        self.blocks_file_sink_0_0_0_1_1_1_1_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1_1_1_1 = blocks.file_sink(gr.sizeof_float*1, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/matched", False)
        self.blocks_file_sink_0_0_0_1_1_1_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_1 = blocks.file_sink(gr.sizeof_gr_complex*4, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/sigma01", False)
        self.blocks_file_sink_0_0_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*4, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/sigma02", False)
        self.blocks_file_sink_0_0_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*4, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/sigma14", False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*4, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/sigma13", False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*8, "/home/zhe/Dropbox/gnuradio_trunk/gnufiles/sigma_end", False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0_1_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.PWF_weighted_sum_rate_0 = PWF.weighted_sum_rate(L, Nt, Pt, channel, ichn_gain_dB, [1,1],[prewhiten0 ,prewhiten1], False, channelfile)
        self.PWF_sigmagen_0 = PWF.sigmagen(L, Nt, Pt, True, sigmagenfile)
        self.PWF_rx_frame_sync_0_2 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_1_0 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_1 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_0_1 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_0_0_0 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_0_0 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0_0 = PWF.rx_frame_sync(tlen)
        self.PWF_rx_frame_sync_0 = PWF.rx_frame_sync(tlen)
        self.PWF_power_adjust_1_0 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_power_adjust_1 = PWF.power_adjust(Nt, Pt, L)
        self.PWF_pilot_receive_tx_0_0 = PWF.pilot_receive_tx(False, pilot1file, pilot1.reshape(tlen,2), Nt, tlen,noise_hat[0], tlen, 1)
        self.PWF_pilot_receive_tx_0 = PWF.pilot_receive_tx(False, pilot2file, pilot2.reshape(tlen,2), Nt, tlen,noise_hat[1], tlen, 1)
        self.PWF_pilot_receive_rx_0_0 = PWF.pilot_receive_rx(False, pilot2file, pilot2.reshape(tlen,2), prewhiten1, Nt, tlen, tlen, 1)
        self.PWF_pilot_receive_rx_0 = PWF.pilot_receive_rx(False, pilot1file, pilot1.reshape(tlen,2), prewhiten0, Nt, tlen, tlen, 1)
        self.PWF_pilot_gen_tx_0_0 = PWF.pilot_gen_tx(Nt, tlen, pilot2.reshape(tlen,2), False, "")
        self.PWF_pilot_gen_tx_0 = PWF.pilot_gen_tx(Nt, tlen, pilot1.reshape(tlen,2), False, "")
        self.PWF_pilot_gen_rx_0_0 = PWF.pilot_gen_rx(Nt, tlen, prewhiten0, pilot1.reshape(tlen,2), False, pilot1file)
        self.PWF_pilot_gen_rx_0 = PWF.pilot_gen_rx(Nt, tlen, prewhiten1, pilot2.reshape(tlen,2), False, pilot2file)
        self.PWF_debug_printmsg_0 = PWF.debug_printmsg(L, Nt, False, max_iteration)
        self.PWF_channel_1 = PWF.channel(L, Nt, ichn_gain_dB, channel, False,noise_hat, True, channelfile)
        self.PWF_channel_0 = PWF.channel(L, Nt, ichn_gain_dB, channel, True,noise, True, channelfile)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.PWF_channel_0, 0), (self.pulse_recover_0, 0))    
        self.connect((self.PWF_channel_0, 1), (self.pulse_recover_0_0, 0))    
        self.connect((self.PWF_channel_1, 1), (self.pulse_recover_0_1, 0))    
        self.connect((self.PWF_channel_1, 0), (self.pulse_recover_0_1_0, 0))    
        self.connect((self.PWF_debug_printmsg_0, 0), (self.PWF_pilot_gen_tx_0, 0))    
        self.connect((self.PWF_debug_printmsg_0, 1), (self.PWF_pilot_gen_tx_0_0, 0))    
        self.connect((self.PWF_pilot_gen_rx_0, 0), (self.blocks_stream_mux_0_0_0, 0))    
        self.connect((self.PWF_pilot_gen_rx_0_0, 0), (self.blocks_stream_mux_0_1, 0))    
        self.connect((self.PWF_pilot_gen_tx_0, 0), (self.blocks_stream_mux_0, 0))    
        self.connect((self.PWF_pilot_gen_tx_0_0, 0), (self.blocks_stream_mux_0_0, 0))    
        self.connect((self.PWF_pilot_receive_rx_0, 0), (self.PWF_power_adjust_1, 0))    
        self.connect((self.PWF_pilot_receive_rx_0, 0), (self.blocks_file_sink_0_0_0_1, 0))    
        self.connect((self.PWF_pilot_receive_rx_0_0, 0), (self.PWF_power_adjust_1, 1))    
        self.connect((self.PWF_pilot_receive_rx_0_0, 0), (self.blocks_file_sink_0_0_0_0_0, 0))    
        self.connect((self.PWF_pilot_receive_tx_0, 0), (self.PWF_power_adjust_1_0, 1))    
        self.connect((self.PWF_pilot_receive_tx_0_0, 0), (self.PWF_power_adjust_1_0, 0))    
        self.connect((self.PWF_power_adjust_1, 1), (self.PWF_pilot_gen_rx_0, 0))    
        self.connect((self.PWF_power_adjust_1, 0), (self.PWF_pilot_gen_rx_0_0, 0))    
        self.connect((self.PWF_power_adjust_1, 0), (self.blocks_file_sink_0_0_0, 0))    
        self.connect((self.PWF_power_adjust_1, 1), (self.blocks_file_sink_0_0_0_0, 0))    
        self.connect((self.PWF_power_adjust_1_0, 0), (self.PWF_weighted_sum_rate_0, 0))    
        self.connect((self.PWF_power_adjust_1_0, 1), (self.PWF_weighted_sum_rate_0, 1))    
        self.connect((self.PWF_power_adjust_1_0, 0), (self.blocks_streams_to_vector_0_0, 0))    
        self.connect((self.PWF_power_adjust_1_0, 1), (self.blocks_streams_to_vector_0_0, 1))    
        self.connect((self.PWF_rx_frame_sync_0, 0), (self.blocks_multiply_const_vxx_0_0_0_1, 0))    
        self.connect((self.PWF_rx_frame_sync_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0, 0))    
        self.connect((self.PWF_rx_frame_sync_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))    
        self.connect((self.PWF_rx_frame_sync_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_1, 0))    
        self.connect((self.PWF_rx_frame_sync_0_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0))    
        self.connect((self.PWF_rx_frame_sync_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.PWF_rx_frame_sync_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0_0_2, 0))    
        self.connect((self.PWF_rx_frame_sync_0_2, 0), (self.blocks_multiply_const_vxx_0_0_0_1_0, 0))    
        self.connect((self.PWF_sigmagen_0, 1), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.PWF_sigmagen_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_0_0_1_0, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.PWF_weighted_sum_rate_0, 1), (self.blocks_repeat_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_peak_detector2_fb_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_2, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_peak_detector2_fb_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_2_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_peak_detector2_fb_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_2_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_0, 0), (self.blocks_peak_detector2_fb_0_1_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_1, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_1, 0), (self.blocks_peak_detector2_fb_0_1_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_1_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_2_0_1_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_1_0, 0), (self.blocks_peak_detector2_fb_0_1_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_streams_to_vector_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_streams_to_vector_1_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_streams_to_vector_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0), (self.blocks_streams_to_vector_1_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_1, 0), (self.blocks_streams_to_vector_1_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_1, 0), (self.blocks_streams_to_vector_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_1_0, 0), (self.blocks_streams_to_vector_1_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_2, 0), (self.blocks_streams_to_vector_1_0_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.PWF_rx_frame_sync_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.PWF_rx_frame_sync_0_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 0), (self.PWF_rx_frame_sync_0_0_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 0), (self.PWF_rx_frame_sync_0_1, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_1, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 0), (self.PWF_rx_frame_sync_0_0_0_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 0), (self.PWF_rx_frame_sync_0_0_1, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 0), (self.PWF_rx_frame_sync_0_1_0, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 0), (self.PWF_rx_frame_sync_0_2, 1))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_1_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_1, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_1, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_1_0, 1), (self.blocks_file_sink_0_0_0_1_1_1_1_0_1_1_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0_1_1_0, 0), (self.blocks_file_sink_0_0_0_1_1_1_1_1_0_0_1_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_repeat_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_stream_mux_0, 0), (self.pulse_shaping_0, 0))    
        self.connect((self.blocks_stream_mux_0_0, 0), (self.pulse_shaping_0_0, 0))    
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.blocks_vector_to_streams_1_1_0, 0))    
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.pulse_shaping_0_2, 0))    
        self.connect((self.blocks_stream_mux_0_1, 0), (self.blocks_vector_to_streams_1_1_0_0, 0))    
        self.connect((self.blocks_stream_mux_0_1, 0), (self.pulse_shaping_0_0_1, 0))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_udp_sink_1_0_0, 0))    
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.blocks_udp_sink_1_0, 0))    
        self.connect((self.blocks_streams_to_vector_1, 0), (self.PWF_pilot_receive_rx_0, 0))    
        self.connect((self.blocks_streams_to_vector_1_0, 0), (self.PWF_pilot_receive_rx_0_0, 0))    
        self.connect((self.blocks_streams_to_vector_1_0_0, 0), (self.PWF_pilot_receive_tx_0, 0))    
        self.connect((self.blocks_streams_to_vector_1_1, 0), (self.PWF_pilot_receive_tx_0_0, 0))    
        self.connect((self.blocks_udp_source_1, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 1))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0_0, 1))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_mux_0_0_0, 1))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_mux_0_1, 1))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.PWF_debug_printmsg_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.PWF_debug_printmsg_0, 1))    
        self.connect((self.blocks_vector_to_streams_1, 0), (self.PWF_rx_frame_sync_0, 0))    
        self.connect((self.blocks_vector_to_streams_1, 1), (self.PWF_rx_frame_sync_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_1, 0), (self.fir_filter_xxx_0_3, 0))    
        self.connect((self.blocks_vector_to_streams_1_0, 1), (self.PWF_rx_frame_sync_0_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_0, 0), (self.PWF_rx_frame_sync_0_1, 0))    
        self.connect((self.blocks_vector_to_streams_1_0, 0), (self.fir_filter_xxx_0_3_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_0_0, 1), (self.PWF_rx_frame_sync_0_0_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_0_0, 0), (self.PWF_rx_frame_sync_0_1_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_0_0, 0), (self.fir_filter_xxx_0_3_1_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_1, 1), (self.PWF_rx_frame_sync_0_0_1, 0))    
        self.connect((self.blocks_vector_to_streams_1_1, 0), (self.PWF_rx_frame_sync_0_2, 0))    
        self.connect((self.blocks_vector_to_streams_1_1, 0), (self.fir_filter_xxx_0_3_1, 0))    
        self.connect((self.blocks_vector_to_streams_1_1_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_1_0, 0), (self.fir_filter_xxx_0_3_1_1, 0))    
        self.connect((self.blocks_vector_to_streams_1_1_0_0, 0), (self.blocks_null_sink_0_0, 1))    
        self.connect((self.blocks_vector_to_streams_1_1_0_0, 1), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_1_1_0_0, 0), (self.fir_filter_xxx_0_3_1_1_0, 0))    
        self.connect((self.fir_filter_xxx_0_3, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.fir_filter_xxx_0_3_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.fir_filter_xxx_0_3_1, 0), (self.blocks_complex_to_mag_squared_0_1, 0))    
        self.connect((self.fir_filter_xxx_0_3_1_0, 0), (self.blocks_complex_to_mag_squared_0_1_0, 0))    
        self.connect((self.fir_filter_xxx_0_3_1_1, 0), (self.blocks_complex_to_mag_squared_0_1_1, 0))    
        self.connect((self.fir_filter_xxx_0_3_1_1_0, 0), (self.blocks_complex_to_mag_squared_0_1_1_0, 0))    
        self.connect((self.pulse_recover_0, 0), (self.blocks_vector_to_streams_1, 0))    
        self.connect((self.pulse_recover_0_0, 0), (self.blocks_vector_to_streams_1_0, 0))    
        self.connect((self.pulse_recover_0_1, 0), (self.blocks_vector_to_streams_1_0_0, 0))    
        self.connect((self.pulse_recover_0_1_0, 0), (self.blocks_vector_to_streams_1_1, 0))    
        self.connect((self.pulse_shaping_0, 0), (self.PWF_channel_0, 0))    
        self.connect((self.pulse_shaping_0_0, 0), (self.PWF_channel_0, 1))    
        self.connect((self.pulse_shaping_0_0_1, 0), (self.PWF_channel_1, 0))    
        self.connect((self.pulse_shaping_0_2, 0), (self.PWF_channel_1, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pwf_distributed_pilot")
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
        self.blocks_peak_detector2_fb_0_1.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_1.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_1_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_0.set_look_ahead(self.tlen+self.payload_size-22)

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
        self.blocks_multiply_const_vxx_0_0_0.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_0_1.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_1.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_1_0.set_k((1/ float(self.Q), ))
        self.blocks_multiply_const_vxx_0_0_0_2.set_k((1/ float(self.Q), ))
        self.pulse_recover_0.set_Q(self.Q)
        self.pulse_recover_0_0.set_Q(self.Q)
        self.pulse_recover_0_1.set_Q(self.Q)
        self.pulse_recover_0_1_0.set_Q(self.Q)
        self.pulse_shaping_0.set_Q(self.Q)
        self.pulse_shaping_0_0.set_Q(self.Q)
        self.pulse_shaping_0_0_1.set_Q(self.Q)
        self.pulse_shaping_0_2.set_Q(self.Q)

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L
        self.set_channel(np.true_divide(np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))+np.random.standard_normal(size=(self.L,self.L,self.Nt,self.Nt))*1j,np.sqrt(2)))

    def get_sigmagenfile(self):
        return self.sigmagenfile

    def set_sigmagenfile(self, sigmagenfile):
        self.sigmagenfile = sigmagenfile

    def get_pulse(self):
        return self.pulse

    def set_pulse(self, pulse):
        self.pulse = pulse
        self.pulse_recover_0.set_pulse(self.pulse)
        self.pulse_recover_0_0.set_pulse(self.pulse)
        self.pulse_recover_0_1.set_pulse(self.pulse)
        self.pulse_recover_0_1_0.set_pulse(self.pulse)
        self.pulse_shaping_0.set_pulse(self.pulse)
        self.pulse_shaping_0_0.set_pulse(self.pulse)
        self.pulse_shaping_0_0_1.set_pulse(self.pulse)
        self.pulse_shaping_0_2.set_pulse(self.pulse)

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
        self.fir_filter_xxx_0_3_0.set_taps((self.pilot2[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_0.set_taps((self.pilot2[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_1.set_taps((self.pilot2[0::2][::-1]))

    def get_pilot1file(self):
        return self.pilot1file

    def set_pilot1file(self, pilot1file):
        self.pilot1file = pilot1file

    def get_pilot1(self):
        return self.pilot1

    def set_pilot1(self, pilot1):
        self.pilot1 = pilot1
        self.fir_filter_xxx_0_3.set_taps((self.pilot1[0::2][::-1]))
        self.fir_filter_xxx_0_3_1.set_taps((self.pilot1[0::2][::-1]))
        self.fir_filter_xxx_0_3_1_1_0.set_taps((self.pilot1[0::2][::-1]))

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size
        self.blocks_peak_detector2_fb_0_1.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_1.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_1_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_vector_source_x_0.set_data(map(int, np.random.randint(0,3,self.payload_size)), [])
        self.blocks_vector_source_x_0_0.set_data(map(int, np.random.randint(0,3,self.payload_size)), [])
        self.blocks_peak_detector2_fb_0_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0.set_look_ahead(self.tlen+self.payload_size-22)
        self.blocks_peak_detector2_fb_0_1_0.set_look_ahead(self.tlen+self.payload_size-22)

    def get_npoints(self):
        return self.npoints

    def set_npoints(self, npoints):
        self.npoints = npoints

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

    def get_Pt(self):
        return self.Pt

    def set_Pt(self, Pt):
        self.Pt = Pt


def main(top_block_cls=pwf_distributed_pilot, options=None):

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
