---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/auxdisplay/README.html
original_path: samples/drivers/auxdisplay/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Auxiliary display

## Overview

This sample shows how to use the [auxiliary display driver](../../../hardware/peripherals/auxdisplay.md#auxdisplay-api)
by outputting a sample “Hello World” text to one.

## Building and Running

Note that this sample requires a board with an auxiliary display setup. A
sample overlay is provided for the nucleo\_f746zg board fly-wired to a Hitachi
HD44780-compatible 20 character by 4 line display. See the overlay file
[samples/drivers/auxdisplay/boards/nucleo\_f746zg.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/auxdisplay/boards/nucleo_f746zg.overlay) for
wiring configuration.

```shell
west build -b nucleo_f746zg samples/drivers/auxdisplay
west flash
```

If successful, the display will show Hello World from <board>.
