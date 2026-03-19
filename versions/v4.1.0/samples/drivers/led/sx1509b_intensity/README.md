---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/sx1509b_intensity/README.html
original_path: samples/drivers/led/sx1509b_intensity/README.html
---

# SX1509B RGB LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/sx1509b_intensity/README.rst/..)

## Overview

This sample controls the intensity of the color LEDs in a Thingy:52 lightwell.
The red, green and blue LED fade up one by one, and this repeats forever.

## Building and Running

```shell
west build -b thingy52/nrf52832 samples/drivers/led/sx1509b_intensity
west flash
```

The log is configured to output to RTT. Segger J-Link RTT Viewer can be used to view the log.

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
