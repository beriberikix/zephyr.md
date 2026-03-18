---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/usb/uac2_explicit_feedback/README.html
original_path: samples/subsys/usb/uac2_explicit_feedback/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# USB Audio asynchronous explicit feedback sample

## Overview

This sample demonstrates how to implement USB asynchronous audio playback with
explicit feedback. It can run on any board with USB and I2S support, but the
feedback calculation is currently only implemented for the Nordic nRF5340 IC.

The device running this sample presents itself to the host as a Full-Speed
Asynchronous USB Audio 2 class device supporting 48 kHz 16-bit 2-channel
(stereo) playback.

## Explicit Feedback

Asynchronous USB Audio is used when the actual sample clock is not controlled by
USB host. Because the sample clock is independent from USB SOF it is inevitable
that 1 ms according to audio sink (I2S) will be either slightly longer or
shorter than 1 ms according to audio source (USB host). In the long run, this
discrepancy leads to overruns or underruns. By providing explicit feedback to
host, the device can tell host how many samples on average it needs every frame.
The host achieves the average by sending either nominal or nominal ±1 sample
packets every frame.

The dummy feedback implementation, used when there is no target-specific
feedback code available, returns a feedback value that results in host sending
nominal number of samples every frame. Theoretically it should be possible to
obtain the timing information based on I2S and USB interrupts, but currently
neither subsystem provides the necessary timestamp information.

## Explcit Feedback on nRF5340

The nRF5340 is capable of counting both edges of I2S LRCLK relative to USB SOF
with the use of DPPI, TIMER and GPIOTE input. Alternatively, if the GPIOTE input
is not available, the DPPI and TIMER peripherals on nRF5340 can be configured to
provide relative timing information between I2S FRAMESTART and USB SOF.

This sample in both modes (direct sample counting and indirect I2S buffer output
to USB SOF offset) has been tested on [nRF5340 DK](../../../../boards/arm/nrf5340dk_nrf5340/doc/index.md#nrf5340dk-nrf5340).

The sample defaults to indirect feedback calculation because direct sample
counting requires external connection between I2S LRCLK output pin to GPIOTE
input pin (hardcoded to P1.09) on [nRF5340 DK](../../../../boards/arm/nrf5340dk_nrf5340/doc/index.md#nrf5340dk-nrf5340). In the indirect mode
no extra connections are necessary and the sample can even be used without any
I2S device connected where I2S signals can be checked e.g. on logic analyzer.

## Building and Running

The code can be found in [samples/subsys/usb/uac2\_explicit\_feedback](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/uac2_explicit_feedback).

To build and flash the application:

```shell
west build -b nrf5340dk_nrf5340_cpuapp samples/subsys/usb/uac2_explicit_feedback
west flash
```
