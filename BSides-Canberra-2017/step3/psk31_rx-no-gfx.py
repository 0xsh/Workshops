#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep 23 20:16:46 2016
##################################################

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


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4000
        self.lpf = lpf = firdes.low_pass_2(1, 4000, 30, 10, 40)
        self.baud_rate = baud_rate = 31.25
        self.tune_freq = tune_freq = 2000
        self.sps = sps = int(samp_rate / 4 / baud_rate)
        self.lpf_len = lpf_len = len(lpf)
        self.audio_samp_rate = audio_samp_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=4000,
                decimation=44100,
                taps=None,
                fractional_bw=None,
        )
        self.psk31_varicode_dec_b_0 = psk31.varicode_dec_b()
        self.hilbert_fc_1 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(4, (lpf), tune_freq-2000, samp_rate)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(sps/4, ([math.sin(math.pi*t/sps) / 50 / math.pi for t in xrange(sps)]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_costas_loop_cc_1 = digital.costas_loop_cc(2*math.pi/2/100, 2, False)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(4*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, audio_samp_rate*10,True)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(2*math.pi*-2000/audio_samp_rate)
        self.blocks_not_xx_0 = blocks.not_bb()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_and_const_xx_0 = blocks.and_const_bb(1)
        self.audio_source_0 = audio.source(audio_samp_rate, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_and_const_xx_0, 0), (self.psk31_varicode_dec_b_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_not_xx_0, 0), (self.blocks_and_const_xx_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.hilbert_fc_1, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.digital_costas_loop_cc_1, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_not_xx_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_costas_loop_cc_1, 0))    
        self.connect((self.hilbert_fc_1, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(int(self.samp_rate / 4 / self.baud_rate))

    def get_lpf(self):
        return self.lpf

    def set_lpf(self, lpf):
        self.lpf = lpf
        self.set_lpf_len(len(self.lpf))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.lpf))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_sps(int(self.samp_rate / 4 / self.baud_rate))

    def get_tune_freq(self):
        return self.tune_freq

    def set_tune_freq(self, tune_freq):
        self.tune_freq = tune_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.tune_freq-2000)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.fir_filter_xxx_0.set_taps(([math.sin(math.pi*t/self.sps) / 50 / math.pi for t in xrange(self.sps)]))

    def get_lpf_len(self):
        return self.lpf_len

    def set_lpf_len(self, lpf_len):
        self.lpf_len = lpf_len

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate
        self.blocks_rotator_cc_0.set_phase_inc(2*math.pi*-2000/self.audio_samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.audio_samp_rate*10)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
