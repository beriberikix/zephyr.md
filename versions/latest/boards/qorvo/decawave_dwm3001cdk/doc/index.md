---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/qorvo/decawave_dwm3001cdk/doc/index.html
original_path: boards/qorvo/decawave_dwm3001cdk/doc/index.html
---

# Decawave DWM3001CDK

Board Overview

Name:
:   `decawave_dwm3001cdk`

Vendor:
:   Qorvo, Inc.

Architecture:
:   arm

SoC:
:   nrf52833

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/qorvo/decawave_dwm3001cdk/doc/index.rst/../..)

## Overview

The DWM3001CDK development board includes the DWM3001C module, battery connector
and charging circuit, LEDs, buttons, Raspberry Pi connector, and USB connector.
In addition, the board comes with J-Link OB adding debugging and Virtual COM
Port capabilities.

See [Qorvo (Decawave) DWM3001CDK website](https://www.qorvo.com/products/p/DWM3001CDK) [[3]](#id5) for more information about the
development board, [Qorvo (Decawave) DWM3001C website](https://www.qorvo.com/products/p/DWM3001C) [[2]](#id3) about the module
itself, and [nRF52833 website](https://www.nordicsemi.com/products/nrf52833) [[1]](#id1) for the official reference on the IC itself.

## Programming and Debugging

Applications for the `decawave_dwm3001cdk` board target can be built, flashed,
and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect to the bottom micro-USB port labeled as J-Link and run your favorite
terminal program to listen for console output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the DWM3001CDK board can be
found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b decawave_dwm3001cdk samples/hello_world
west flash
```

## References

[[1](#id2)]

[https://www.nordicsemi.com/products/nrf52833](https://www.nordicsemi.com/products/nrf52833)

[[2](#id4)]

[https://www.qorvo.com/products/p/DWM3001C](https://www.qorvo.com/products/p/DWM3001C)

[[3](#id6)]

[https://www.qorvo.com/products/p/DWM3001CDK](https://www.qorvo.com/products/p/DWM3001CDK)
