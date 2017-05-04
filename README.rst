
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-waveform/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/waveform/en/latest/
    :alt: Documentation Status

.. image :: https://badges.gitter.im/adafruit/circuitpython.svg
    :target: https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter

This library generates simple waveforms that can be used to generate different
type of audio signals.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

This example generates one wavelength of a 440hz sine wave when played at 16 kilosamples per second::

    from adafruit_waveform import sine
    wave = sine.sine_wave(16000, 440)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_waveform/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
