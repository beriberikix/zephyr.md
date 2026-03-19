---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/haptics/drv2605/README.html
original_path: samples/drivers/haptics/drv2605/README.html
---

# DRV2605 Haptic Driver

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/haptics/drv2605/README.rst/..)

## Overview

This sample demonstrates how to configure a ROM playback event on the DRV2605 and executes playback
of a tapping rhythmic pattern.

## Building and Running

Build the application for the [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board, and connect a DRV2605 haptic driver
on the bus I2C1 at the address 0x5A.

```shell
west build -b nucleo_f401re samples/drivers/haptics/drv2605
```

For flashing the application, refer to the Flashing section of the [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board
documentation.

```text
*** Booting Zephyr OS build v3.7.0-5-g3b4f8d80850e ***
[00:00:00.103,000] <inf> main: Found DRV2605 device drv2605@5a
```

## References

- DRV2605 Datasheet: [https://www.ti.com/lit/ds/symlink/drv2605.pdf](https://www.ti.com/lit/ds/symlink/drv2605.pdf)

## See also

[Haptics Interface](../../../../doxygen/html/group__haptics__interface.md)
