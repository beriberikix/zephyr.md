---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/drivers/auxdisplay_digits/README.html
original_path: samples/drivers/auxdisplay_digits/README.html
---

# Auxiliary digits display

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/auxdisplay_digits/README.rst/..)

## Overview

This sample demonstrates the use of the
[auxiliary display driver](../../../hardware/peripherals/auxdisplay.md#auxdisplay-api) for digit-based displays, such
as 7-segment displays.

## Building and Running

Note that this sample requires a board with a 7-segment display setup. You can
build your own setup by fly-wiring a 7-segment display to any board you have.

A sample overlay is provided for the `native_sim` target. See the overlay file
[samples/drivers/auxdisplay\_digits/boards/native\_sim.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/auxdisplay_digits/boards/native_sim.overlay) for a
demonstration.

```shell
west build -b native_sim samples/drivers/auxdisplay_digits
```

If successful, the display first lights up all segments (e.g., 8.8.8. on a
3-digit display), blinks once, sequentially lights up each digit from left to
right, and then counts up from 0 to the maximum number that can be displayed.

## See also

[Text Display Interface](../../../doxygen/html/group__auxdisplay__interface.md)
