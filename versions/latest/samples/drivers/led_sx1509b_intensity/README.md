---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/led_sx1509b_intensity/README.html
original_path: samples/drivers/led_sx1509b_intensity/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SX1509B RGB LED

## Overview

This sample controls the intensity of the color LEDs in a Thingy:52 lightwell.
The red, green and blue LED fade up one by one, and this repeats forever.

## Building and Running

```shell
west build -b thingy52_nrf52832 samples/drivers/led_sx1509b_intensity
west flash
```

The log is configured to output to RTT. Segger J-Link RTT Viewer can be used to view the log.
