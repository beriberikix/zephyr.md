---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/audio/dmic/README.html
original_path: samples/drivers/audio/dmic/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Digital Microphone (DMIC)

## Overview

This is a very simple application intended to show how to use the [Audio DMIC
API](../../../../hardware/peripherals/audio/dmic.md#audio-dmic-api) and also to be an aid in developing drivers to implement this API.
It performs two PDM transfers with different configurations (using one channel
and two channels) but does not in any way process the received audio data.

## Requirements

The device to be used by the sample is specified by defining a devicetree node
label named `dmic_dev`.
The sample has been tested on [nRF52840 DK](../../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840) (nrf52840dk\_nrf52840)
and [nRF5340 DK](../../../../boards/arm/nrf5340dk_nrf5340/doc/index.md#nrf5340dk-nrf5340) (nrf5340dk\_nrf5340\_cpuapp), and provides overlay
files for both of these boards.

## Building and Running

The code can be found in [samples/drivers/audio/dmic](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/audio/dmic).

To build and flash the application:

```shell
west build -b nrf52840dk_nrf52840 samples/drivers/audio/dmic
west flash
```
