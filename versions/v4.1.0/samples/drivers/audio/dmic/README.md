---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/audio/dmic/README.html
original_path: samples/drivers/audio/dmic/README.html
---

# Digital Microphone (DMIC)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/audio/dmic/README.rst/..)

## Overview

This is a very simple application intended to show how to use the [Audio DMIC
API](../../../../hardware/peripherals/audio/dmic.md#audio-dmic-api) and also to be an aid in developing drivers to implement this API.
It performs two PDM transfers with different configurations (using one channel
and two channels) but does not in any way process the received audio data.

## Requirements

The device to be used by the sample is specified by defining a devicetree node
label named `dmic_dev`.
The sample has been tested on [nRF52840 DK](../../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) (nrf52840dk/nrf52840)
and [nRF5340 DK](../../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340) (nrf5340dk/nrf5340/cpuapp), and provides overlay
files for both of these boards.

## Building and Running

The code can be found in [samples/drivers/audio/dmic](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/audio/dmic).

To build and flash the application:

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/audio/dmic
west flash
```

## See also

[Digital Microphone Interface](../../../../doxygen/html/group__audio__dmic__interface.md)
