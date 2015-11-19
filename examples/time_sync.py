#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: time_sync
# Author: Zhe Feng
# Generated: Tue Sep  8 09:54:23 2015
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys

from distutils.version import StrictVersion
class time_sync(gr.top_block, Qt.QWidget):

    def __init__(self, look_ahead=0, factor=0, training_sequence=0, Q=1):
        gr.top_block.__init__(self, "time_sync")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("time_sync")
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

        self.settings = Qt.QSettings("GNU Radio", "time_sync")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.look_ahead = look_ahead
        self.factor = factor
        self.training_sequence = training_sequence
        self.Q = Q

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(Q, (training_sequence, ))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_peak_detector2_fb_0 = blocks.peak_detector2_fb(factor, look_ahead, 0.001)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_peak_detector2_fb_0, 0))    
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self, 0))    
        self.connect((self.blocks_peak_detector2_fb_0, 1), (self, 1))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self, 0), (self.fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "time_sync")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_look_ahead(self):
        return self.look_ahead

    def set_look_ahead(self, look_ahead):
        self.look_ahead = look_ahead
        self.blocks_peak_detector2_fb_0.set_look_ahead(self.look_ahead)

    def get_factor(self):
        return self.factor

    def set_factor(self, factor):
        self.factor = factor
        self.blocks_peak_detector2_fb_0.set_threshold_factor_rise(self.factor)

    def get_training_sequence(self):
        return self.training_sequence

    def set_training_sequence(self, training_sequence):
        self.training_sequence = training_sequence
        self.fir_filter_xxx_0.set_taps((self.training_sequence, ))

    def get_Q(self):
        return self.Q

    def set_Q(self, Q):
        self.Q = Q

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = time_sync()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
