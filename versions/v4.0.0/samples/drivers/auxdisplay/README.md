---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/auxdisplay/README.html
original_path: samples/drivers/auxdisplay/README.html
---

# Auxiliary display

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/auxdisplay/README.rst/..)

## Overview

This sample shows how to use the [auxiliary display driver](../../../hardware/peripherals/auxdisplay.md#auxdisplay-api)
by outputting a sample “Hello World” text to one.

## Building and Running

Note that this sample requires a board with an auxiliary display setup. A
sample overlay is provided for the `nucleo_f746zg` board fly-wired to a Hitachi
HD44780-compatible 20 character by 4 line display. See the overlay file
[samples/drivers/auxdisplay/boards/nucleo\_f746zg.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/auxdisplay/boards/nucleo_f746zg.overlay) for
wiring configuration.

```shell
west build -b nucleo_f746zg samples/drivers/auxdisplay
west flash
```

If successful, the display will show “Hello World from <board>”.

## See also

[Text Display Interface](../../../doxygen/html/group__auxdisplay__interface.md)
