---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/i2s/output/README.html
original_path: samples/drivers/i2s/output/README.html
---

# I2S output

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/i2s/output/README.rst/..)

## Overview

This sample demonstrates how to use an I2S driver to send an output stream of
audio data. Currently, no codec is used with this sample. The I2S output can
be verified with a signal analyzer.

The sample will send a short burst of audio data, consisting of a sine wave.
The I2S TX queue will then be drained, and audio output will stop.

## Requirements

The I2S device to be used by the sample is specified by defining
a devicetree alias named `i2s_tx`

This sample has been tested on [MIMXRT1060-EVK](../../../../boards/nxp/mimxrt1060_evk/doc/index.md#mimxrt1060_evk) (mimxrt1060\_evkb)

## Building and Running

The code can be found in [samples/drivers/i2s/output](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2s/output).

To build and flash the application:

```shell
west build -b mimxrt1060_evk@B samples/drivers/i2s/output
west flash
```

## See also

[I2S Interface](../../../../doxygen/html/group__i2s__interface.md)
