---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/i2s/output/README.html
original_path: samples/drivers/i2s/output/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# I2S output

## Overview

This sample demonstrates how to use an I2S driver to send an output stream of
audio data. Currently, no codec is used with this sample. The I2S output can
be verified with a signal analyzer.

The sample will send a short burst of audio data, consisting of a sine wave.
The I2S TX queue will then be drained, and audio output will stop.

## Requirements

The I2S device to be used by the sample is specified by defining
a devicetree alias named `i2s_tx`

This sample has been tested on [NXP MIMXRT1060-EVK](../../../../boards/nxp/mimxrt1060_evk/doc/index.md#mimxrt1060-evk) (mimxrt1060\_evkb)

## Building and Running

The code can be found in [samples/drivers/i2s/output](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2s/output).

To build and flash the application:

```shell
west build -b mimxrt1060_evkb samples/drivers/i2s/output
west flash
```
