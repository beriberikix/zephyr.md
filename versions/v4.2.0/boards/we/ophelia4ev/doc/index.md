---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/we/ophelia4ev/doc/index.html
original_path: boards/we/ophelia4ev/doc/index.html
---

# Ophelia-IV DK

Board Overview

[![../../../../_images/ophelia4ev.webp](../../../../_images/ophelia4ev.webp)
](../../../../_images/ophelia4ev.webp)

Ophelia-IV DK

Name:
:   `ophelia4ev`

Vendor:
:   Würth Elektronik GmbH.

Architecture:
:   riscv, arm

SoC:
:   nrf54l15

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/we/ophelia4ev/doc/index.rst/../..)

## Overview

Note

You can find more information about the nRF54L15 SoC on the [nRF54L15 website](https://www.nordicsemi.com/Products/nRF54L15) [[1]](#id2).
For the nRF54L15 technical documentation and other resources (such as
SoC Datasheet), see the [nRF54L15 documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html) [[2]](#id4) page.

The OPHELIA-IV EV board is an evaluation board of the Ophelia-IV radio module.

## Hardware

The Ophelia-IV uses the internal low frequency RC oscillator
and provides the so called smart antenna connection, that allows
to choose between the module’s integrated PCB antenna and an external
antenna that can be connected to the available SMA connector.

### Supported Features

The `ophelia4ev` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `ophelia4ev` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `ophelia4ev/nrf54l15/cpuapp` board target can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Applications for the `ophelia4ev/nrf54l15/cpuflpr` board target need
to be built using sysbuild to include the `vpr_launcher` image for the application core.

Enter the following command to compile `hello_world` for the FLPR core:

```shell
west build -p -b ophelia4ev/nrf54l15/cpuflpr --sysbuild
```

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

To build and program the sample to the OPHELIA-IV EV, complete the following steps:

First, connect the OPHELIA-IV EV to you computer using the USB port on the board.
Then connect a segger flasher to the SWD connector available on the board.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b ophelia4ev/nrf54l15/cpuapp samples/hello_world
west flash
```

Warning

When programming the device, you might get an error similar to the following message:

```text
ERROR: The operation attempted is unavailable due to readback protection in
ERROR: your device. Please use --recover to unlock the device.
```

This error occurs when readback protection is enabled.
To disable the readback protection, you must *recover* your device.

Enter the following command to recover the core:

```text
west flash --recover
```

The `--recover` command erases the flash memory and then writes a small binary into
the recovered flash memory.
This binary prevents the readback protection from enabling itself again after a pin
reset or power cycle.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

## References

[[1](#id3)]

[https://www.nordicsemi.com/Products/nRF54L15](https://www.nordicsemi.com/Products/nRF54L15)

[[2](#id5)]

[https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app\_dev/device\_guides/nrf54l/index.html](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html)
