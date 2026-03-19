---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/i2s/i2s_codec/README.html
original_path: samples/drivers/i2s/i2s_codec/README.html
---

# I2S codec

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/i2s/i2s_codec/README.rst/..)

## Overview

This sample demonstrates how to use an I2S driver in a simple processing of
an audio stream. It configures and starts from memory buffer or from DMIC to
record i2s data and send to codec with DMA.

## Requirements

This sample has been tested on mimxrt595\_evk/mimxrt595s/cm33

## Building and Running

The code can be found in [samples/drivers/i2s/i2s\_codec](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2s/i2s_codec).

To build and flash the application:

```shell
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/drivers/i2s/i2s_codec
west flash
```

To run you can connect earphones to the lineout connect and hear the sound
from DMIC or from memory buffer.

## See also

[I2S Interface](../../../../doxygen/html/group__i2s__interface.md)
