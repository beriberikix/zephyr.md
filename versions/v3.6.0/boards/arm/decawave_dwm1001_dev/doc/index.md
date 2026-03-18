---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/decawave_dwm1001_dev/doc/index.html
original_path: boards/arm/decawave_dwm1001_dev/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Decawave DWM1001

## Overview

The DWM1001 development board includes the DWM1001 module, battery
connector and charging circuit, LEDs, buttons, Raspberry-Pi and USB
connector. In addition, the board comes with J-Link OB adding
debugging and Virtual COM Port capabilities.

See [Decawave DWM1001-DEV website](https://www.decawave.com/product/dwm1001-development-board) [[3]](#id5) for more information about the development
board, [Decawave DWM1001 website](https://www.decawave.com/product/dwm1001-module) [[2]](#id3) about the board itself, and [nRF52832 website](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832) [[1]](#id1) for the official reference on the IC itself.

## Programming and Debugging

Applications for the `decawave_dwm1001_dev` board configuration can be built,
flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF52 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b decawave_dwm1001_dev samples/hello_world
west flash
```

## References

[[1](#id2)]

[https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832)

[[2](#id4)]

[https://www.decawave.com/product/dwm1001-module](https://www.decawave.com/product/dwm1001-module)

[[3](#id6)]

[https://www.decawave.com/product/dwm1001-development-board](https://www.decawave.com/product/dwm1001-development-board)
