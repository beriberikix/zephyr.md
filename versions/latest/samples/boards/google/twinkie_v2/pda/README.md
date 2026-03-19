---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/google/twinkie_v2/pda/README.html
original_path: samples/boards/google/twinkie_v2/pda/README.html
---

# Power Delivery Analyzer

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/google/twinkie_v2/pda/README.rst/..)

## Overview

This provides access to [Twinkie V2](../../../../../boards/google/twinkie_v2/doc/index.md#google_twinkie_v2) so you can try out
the supported features.

## Building and Running

Build and flash Twinkie as follows:

```shell
west build -b google_twinkie_v2 samples/boards/google/twinkie_v2/pda
west flash
```

After flashing, the LED will start red. Putting the Twinkie in between any
usbc connection will cause the LED to turn blue. The LED will turn green instead
if the device is currently charging.

## See also

[ADC driver APIs](../../../../../doxygen/html/group__adc__interface.md)
