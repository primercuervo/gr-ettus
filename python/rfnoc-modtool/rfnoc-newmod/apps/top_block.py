#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri May 20 12:28:49 2016
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
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ettus
import rfnoc_example
import sip
import sys


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
        self.device3 = variable_uhd_device3_0 = ettus.device3(uhd.device_addr_t( ",".join(("type=x300", "")) ))
        self.samp_rate = samp_rate = 2000000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_rfnoc_streamer_fifo_0 = ettus.rfnoc_generic(
            self.device3,
            uhd.stream_args( # TX Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="gr_vlen={0},{1}".format(1, "" if 1 == 1 else "spp={0}".format(1)),
            ),
            uhd.stream_args( # RX Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="gr_vlen={0},{1}".format(1, "" if 1 == 1 else "spp={0}".format(1)),
            ),
            "FIFO", -1, -1,
        )
        self.rfnoc_example_copy_0 = rfnoc_example.rfnoc_copy(
            self.device3,
            uhd.stream_args( # TX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                args="",
            ),
            uhd.stream_args( # RX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                args="",
            ),
            -1, -1,
          )
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Original", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        
        self.qtgui_sink_x_1.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Copy", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_sink_x_1, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_rfnoc_streamer_fifo_0, 0))    
        self.connect((self.rfnoc_example_copy_0, 0), (self.qtgui_sink_x_0, 0))    
        self.device3.connect(self.uhd_rfnoc_streamer_fifo_0.get_block_id(), 0, self.rfnoc_example_copy_0.get_block_id(), 0)    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_uhd_device3_0(self):
        return self.variable_uhd_device3_0

    def set_variable_uhd_device3_0(self, variable_uhd_device3_0):
        self.variable_uhd_device3_0 = variable_uhd_device3_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

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
