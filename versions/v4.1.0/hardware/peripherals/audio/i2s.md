---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/audio/i2s.html
original_path: hardware/peripherals/audio/i2s.html
---

# Inter-IC Sound (I2S) Bus

## Overview

The I2S (Inter-IC Sound) API provides support for the standard I2S interface
as well as common non-standard extensions such as PCM Short/Long Frame Sync
and Left/Right Justified Data Formats.

## Configuration Options

Related configuration options:

- [`CONFIG_I2S`](../../../kconfig.md#CONFIG_I2S "CONFIG_I2S")

## API Reference

[I2S Interface](../../../doxygen/html/group__i2s__interface.md)

Related code samples

- [I2S codec](../../../samples/drivers/i2s/i2s_codec/README.md#i2s_codec "Process an audio stream to codec.")Process an audio stream to codec.
- [I2S echo](../../../samples/drivers/i2s/echo/README.md#i2s-echo "Process an audio stream to add an echo effect.")Process an audio stream to add an echo effect.
- [I2S output](../../../samples/drivers/i2s/output/README.md#i2s-output "Send I2S output stream")Send I2S output stream
- [USB Audio asynchronous explicit feedback sample](../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")USB Audio 2 explicit feedback sample playing audio on I2S.
- [USB Audio asynchronous implicit feedback sample](../../../samples/subsys/usb/uac2_implicit_feedback/README.md#uac2-implicit-feedback "USB Audio 2 implicit feedback sample playing stereo and recording mono audio on I2S interface.")USB Audio 2 implicit feedback sample playing stereo and recording mono audio
  on I2S interface.
