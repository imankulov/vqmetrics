#!/usr/bin/env python
"""
Set of functions to convert between different speech quality estimation metrics
such as PESQ MOS, MOS LQO, R-factor.

Contains also one helper class with Speex codec options:
    - mapping between speex "quality" and "mode" option
    - size (in bits) for earch speex frame with given mode
    - required bandwidth estimation

"""
from __future__ import division
import sys
from math import sqrt, pi, atan2, log, pow, cos, log

__all__ = 's'.split()

class SpeexMetric(object):
    """
    SpeexMetric class

    >>> m = SpeexMetric(quality=7)
    >>> m.mode
    5
    >>> m.size
    300

    >>> m = SpeexMetric(mode=5)
    >>> m.quality
    8
    >>> m.size
    300
    >>> m.get_bandwidth(1)
    31000
    >>> m.get_bandwidth(2)
    23000
    >>> m.get_bandwidth(3)
    20333
    """

    def __init__(self, quality=None, mode=None):
        if quality is None and mode is None:
            raise ValueError('Speex quality or mode must be set up')
        if quality is not None and mode is not None:
            raise ValueError('You must set up just one option: quality or mode')
        if quality:
            self.quality = quality
                       # 0  1  2  3  4  5  6  7  8  9  10
            self.mode = (1, 8, 2, 3, 3, 4, 4, 5, 5, 6, 7)[self.quality]
        else:
            self.mode = mode
            self.quality =  {
                1: 0, 8: 1, 2: 2, 3: 4, 4: 6, 5: 8, 6: 9, 7: 10,}[self.mode]
        self.size = {
                1: 43, 8: 79, 2: 119, 3: 160, 4: 220,
                5: 300, 6: 364, 7: 492, }[self.mode]

    def get_bandwidth(self, fpp=1):
        """
        Return bandwidth value (bits per second) required to transmit the
        speech encoded with given speex settings and given frames per packet.

        Assume that speech is transmitted over RTP/UDP/IP stack with 12+8+20=40
        bytes in the header.
        """
        ip_udp_rtp_hdr = (20 + 8 + 12) * 8
        size = self.size  * fpp + ip_udp_rtp_hdr
        # (50 packets with fpp=1)
        packets_per_second = 50.0 / fpp
        return int(packets_per_second * size)


def moslqo2r(mos):
    """ With given MOS LQO return R-factor  (1 < MOS < 4.5) """
    D = -903522 + 1113960 * mos - 202500 * mos * mos
    if D < 0:
        D = 0
    h = 1/3 * atan2(15*sqrt(D), 18556-6750*mos)
    R = 20/3 * (8 - sqrt(226) * cos(h+pi/3))
    return R



def r2moslqo(r):
    """ With given R-factor return MOS """
    if r < 0:
        return 1
    if r > 100:
        return 4.5
    return 1 + 0.035 * r  + r * (r - 60) * (100 - r) * 7e-6


def delay2id(Ta):
    """ Delay Ta (ms) render to Id penalty according to ITU-T G.107 and G.108
    recommendations. """
    if Ta < 100:
        Id = 0
    else:
        X = log(Ta/100) / log(2)
        Id = 25.0 * (
               pow((1 + pow(X, 6)), 1.0/6) - \
           3 * pow(1+ pow(X/3, 6), 1.0/6 ) + 2
        )
    return Id


def speexlossdelay2r(mode, loss, Ta):
    return 93.4 - delay2id(Ta) - speexloss2ie(mode, loss)



if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
