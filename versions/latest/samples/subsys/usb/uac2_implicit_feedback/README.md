---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/usb/uac2_implicit_feedback/README.html
original_path: samples/subsys/usb/uac2_implicit_feedback/README.html
---

# USB Audio asynchronous implicit feedback sample

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/uac2_implicit_feedback/README.rst/..)

## Overview

This sample demonstrates how to implement USB asynchronous bidirectional audio
with implicit feedback. The host adjusts number of stereo samples sent for
headphones playback based on the number of mono microphone samples received.

Warning

Microsoft Windows USB Audio 2.0 driver available since Windows 10,
release 1703 does not support implicit feedback.

## Requirements

Target must be able to measure I2S block start (i.e. first sample from output
buffer gets out) relative to USB SOF. The relative offset must be reported with
single sample accuracy.

This sample has been tested on [nRF5340 DK](../../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340). While for actual audio
experience it is necessary to connect external I2S ADC and I2S DAC, simple echo
can be accomplished by shorting I2S data output with I2S data input.

Theoretically it should be possible to obtain the timing information based on
I2S and USB interrupts, but currently neither subsystem currently provides
necessary timestamp information.

## Building and Running

The code can be found in [samples/subsys/usb/uac2\_implicit\_feedback](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/uac2_implicit_feedback).

To build and flash the application:

```shell
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/usb/uac2_implicit_feedback
west flash
```

## See also

[USB device core API](../../../../doxygen/html/group__usbd__api.md)

[USB Audio Class 2 device API](../../../../doxygen/html/group__uac2__device.md)

[I2S Interface](../../../../doxygen/html/group__i2s__interface.md)
