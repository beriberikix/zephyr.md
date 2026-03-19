---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/i2s/echo/README.html
original_path: samples/drivers/i2s/echo/README.html
---

# I2S echo

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/i2s/echo/README.rst/..)

## Overview

This sample demonstrates how to use an I2S driver in a simple processing of
an audio stream. It configures and starts both the RX and TX streams and then
mixes the original signal with its delayed form that is buffered, providing
a simple echo effect.

## Requirements

The sample uses the WM8731 audio CODEC that can be found, for example,
on the Audio Codec Shield, but it can be easily adapted to use other
CODECs. The I2S device to be used by the sample is specified by defining
a devicetree node label named `i2s_rxtx` or separate node labels `i2s_rx`
and `i2s_tx` if separate I2S devices are to be used for the RX and TX
streams.

This sample has been tested on [nRF52840 DK](../../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) (nrf52840dk/nrf52840)
and [nRF5340 DK](../../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340) (nrf5340dk/nrf5340/cpuapp), using the Audio Codec
Shield, and provides overlay files for both of these boards.

More information about the used shield and the CODEC itself can be found here:

- [Audio Codec Shield](http://wiki.openmusiclabs.com/wiki/AudioCodecShield)
- [WM8731](https://www.cirrus.com/products/wm8731/)

## Building and Running

The code can be found in [samples/drivers/i2s/echo](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2s/echo).

To build and flash the application:

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/i2s/echo
west flash
```

Press Button 1 to toggle the echo effect and Button 2 to stop the streams.

## See also

[I2S Interface](../../../../doxygen/html/group__i2s__interface.md)
