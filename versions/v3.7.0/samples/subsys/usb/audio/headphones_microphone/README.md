---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/usb/audio/headphones_microphone/README.html
original_path: samples/subsys/usb/audio/headphones_microphone/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB Audio microphone & headphones

## Overview

This sample app demonstrates use of a USB Audio driver by the Zephyr
project. This very simple sample that performs loopback over IN/OUT
ISO endpoints. The device will show up as two audio devices. One
Input (Microphone) and one Output (Headphones) device.

## Building and Running

In order to build the sample an overlay file with required options
must be provided. By default app.overlay is added. An overlay contains
software and hardware specific information which allow to fully
describe the device.

After you have built and flashed the sample app image to your board, plug the
board into a host device.

## Testing

Steps to test the sample:

- Build and flash the sample as described above.
- Connect to the HOST.
- Chose default Audio IN/OUT.
- Start streaming audio (for example by playing an audio file on the HOST).
- Start recording audio stream (for example using Audacity).
- Verify the recorded audio stream.

This sample can be found under
[samples/subsys/usb/audio/headphones\_microphone](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/audio/headphones_microphone) in the Zephyr project tree.
