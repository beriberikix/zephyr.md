---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/led_lp3943/README.html
original_path: samples/drivers/led_lp3943/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LP3943 RGBW LED

## Overview

This sample controls 16 LEDs connected to an LP3943 driver, in
a continuous pattern of turning them on one at a time (at a one
second interval) until they’re all on, and then turning them off in
reverse order.

## Requirements

The [96Boards Neonkey](../../../boards/96boards/neonkey/doc/index.md#b-neonkey) board has an LP3943 driver and 16 LEDs on board,
so we’ll use this board for our example.

## Building and Running

Build the application for the [96Boards Neonkey](../../../boards/96boards/neonkey/doc/index.md#b-neonkey) board, which has an
LP3943 driver included.

```shell
west build -b 96b_neonkey samples/drivers/led_lp3943
```

For flashing the application, refer to the Flashing section of the
[96Boards Neonkey](../../../boards/96boards/neonkey/doc/index.md#b-neonkey) board documentation.

When you connect to the board’s serial console, you should see the
following output in addition to the LED pattern:

```text
***** BOOTING ZEPHYR OS v1.11.99 *****
[general] [INF] main: Found LED device LP3943
[general] [INF] main: Displaying the pattern
```

## References

- LP3943: [http://www.ti.com/lit/ds/snvs256d/snvs256d.pdf](http://www.ti.com/lit/ds/snvs256d/snvs256d.pdf)
