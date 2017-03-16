#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep 23 20:15:22 2016
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import psk31
import sys

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate = samp_rate = 48000
        self.tx_freq = tx_freq = 2000
        self.interp = interp = int(samp_rate/31.25/sps)
        #mod
        self.message = str(sys.argv[1]) + "\n" #user message from command line parameter
        
        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=32,
                decimation=1,
                taps=([1]*32),
                fractional_bw=None,
        )
        self.psk31_varicode_enc_bb_0 = psk31.varicode_enc_bb()
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(1, ([math.sin(math.pi * t / 32) / 23.2 for t in xrange(32)]))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2)

        #mod
        self.blocks_vector_source_x_0 = blocks.vector_source_b(map(ord, self.message), True, 1, [])

        self.blocks_not_xx_0 = blocks.not_bb()
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1.0/2)
        self.blocks_and_const_xx_0 = blocks.and_const_bb(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.audio_sink_0_0 = audio.sink(samp_rate, "", True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, tx_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_and_const_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.audio_sink_0_0, 0))    
        self.connect((self.blocks_not_xx_0, 0), (self.blocks_and_const_xx_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.psk31_varicode_enc_bb_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.psk31_varicode_enc_bb_0, 0), (self.blocks_not_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_multiply_xx_0_0, 0))    

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_interp(int(self.samp_rate/31.25/self.sps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_interp(int(self.samp_rate/31.25/self.sps))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.analog_sig_source_x_0_0.set_frequency(self.tx_freq)

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
