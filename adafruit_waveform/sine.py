# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_waveform.sine`
====================================================

This library generates sine waveforms that can be used to generate
sine audio signals.

* Author(s): Scott Shawcroft
"""

import array
import math

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Waveform.git"


def sine_wave(sample_frequency: float, pitch: float):
    """Generate a single sine wav cycle at the given sampling frequency and pitch."""
    length = int(sample_frequency / pitch)
    b = array.array("H", [0] * length)
    for i in range(length):
        b[i] = int(math.sin(math.pi * 2 * i / length) * ((2 ** 15) - 1) + 2 ** 15)
    return b
