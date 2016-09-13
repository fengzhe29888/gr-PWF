#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: E310 Rx
# Generated: Tue Feb 23 21:00:24 2016
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

#from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import blocks
from gnuradio import analog
from gnuradio import gr
#from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time

class e310_tx_A(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "E310 Tx A")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 50
        self.tx_freq = tx_freq = 2450000000
        self.samp_rate = samp_rate = 32000
        self.freq = freq = 2450

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(('addr=192.168.10.1', '')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0_0.set_center_freq(tx_freq, 1)
        self.uhd_usrp_sink_0_0.set_gain(tx_gain, 1)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp2', False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp1', False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.uhd_usrp_sink_0_0, 1))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_sink_0_0.set_gain(self.tx_gain, 1)
        	

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_sink_0_0.set_center_freq(self.tx_freq, 0)
        self.uhd_usrp_sink_0_0.set_center_freq(self.tx_freq, 1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq


class e310_tx_B(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "E310 Tx B")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 50
        self.tx_freq = tx_freq = 2450000000
        self.samp_rate = samp_rate = 32000
        self.freq = freq = 2450

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(('addr=192.168.10.2', '')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0_0.set_center_freq(tx_freq, 1)
        self.uhd_usrp_sink_0_0.set_gain(tx_gain, 1)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp2', False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp1', False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.uhd_usrp_sink_0_0, 1))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_sink_0_0.set_gain(self.tx_gain, 1)
        	

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_sink_0_0.set_center_freq(self.tx_freq, 0)
        self.uhd_usrp_sink_0_0.set_center_freq(self.tx_freq, 1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

class e310_rx_A(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "E310 Rx A")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 50
        self.tx_freq = tx_freq = 2450000000
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('addr=192.168.10.1', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_source_0.set_gain(tx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_center_freq(tx_freq, 1)
        self.uhd_usrp_source_0.set_gain(tx_gain, 1)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/re2', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/re', False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_file_sink_0_0, 0))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_source_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.tx_gain, 1)
        	

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_source_0.set_center_freq(self.tx_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.tx_freq, 1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)



class e310_rx_B(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "E310 Rx B")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 50
        self.tx_freq = tx_freq = 2450000000
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('addr=192.168.10.2', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_source_0.set_gain(tx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_center_freq(tx_freq, 1)
        self.uhd_usrp_source_0.set_gain(tx_gain, 1)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/re2', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/zhe/Dropbox/gnuradio_trunk/gnufiles/re', False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_file_sink_0_0, 0))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_source_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.tx_gain, 1)
        	

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_source_0.set_center_freq(self.tx_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.tx_freq, 1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)




def main(tb_tx_A=e310_tx_A, tb_tx_B=e310_tx_B, tb_rx_A=e310_rx_A, tb_rx_B=e310_rx_B, options=None):

#    from distutils.version import StrictVersion
#    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
#        style = gr.prefs().get_string('qtgui', 'style', 'raster')
#        Qt.QApplication.setGraphicsSystem(style)
#    qapp = Qt.QApplication(sys.argv)

    tb_at = tb_tx_A() #tx
    tb_ar = tb_rx_A()
    tb_bt = tb_tx_B()
    tb_br = tb_rx_B()

 #   def quitting_tb_at():
 #       sleep(5)
 #       tb_at.stop()
 #   def quitting_tb_ar():
 #	sleep(5)
 #	tb_ar.stop()
    for k in range(5):
	  time.sleep(1)
          tb_br.start()
	  tb_at.start()
	  time.sleep(5)
	  tb_at.stop()
          tb_br.stop()
	  time.sleep(1)
	  tb_at.blocks_file_source_0.open("/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp1", False)	  
	  tb_at.blocks_file_source_0_0.open("/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp2", False)	  
	  tb_ar.start()
          tb_bt.start()
	  time.sleep(5)
          tb_bt.stop()
	  tb_ar.stop()
	  tb_bt.blocks_file_source_0.open("/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp1", False)
	  tb_bt.blocks_file_source_0_0.open("/home/zhe/Dropbox/gnuradio_trunk/gnufiles/intp2", False)	  

	
if __name__ == '__main__':
    main()
