---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/nrf54l15dk/doc/index.html
original_path: boards/nordic/nrf54l15dk/doc/index.html
---

# nRF54L15 DK

Board Overview

[![../../../../_images/nrf54l15dk_nrf54l15.webp](../../../../_images/nrf54l15dk_nrf54l15.webp)
](../../../../_images/nrf54l15dk_nrf54l15.webp)

nRF54L15 DK

Name:
:   `nrf54l15dk`

Vendor:
:   Nordic Semiconductor

Architecture:
:   riscv, arm

SoC:
:   nrf54l05, nrf54l15, nrf54l10

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/nrf54l15dk/doc/index.rst/../..)

## Overview

Note

You can find more information about the nRF54L15 SoC on the [nRF54L15 website](https://www.nordicsemi.com/Products/nRF54L15) [[1]](#id2).
For the nRF54L15 technical documentation and other resources (such as
SoC Datasheet), see the [nRF54L15 documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html) [[2]](#id4) page.

The nRF54L15 Development Kit hardware provides support for the Nordic Semiconductor
nRF54L15 Arm Cortex-M33 CPU and the following devices:

- SAADC
- CLOCK
- RRAM
- GPIO
- TWIM
- MEMCONF
- MPU
- NVIC
- PWM
- GRTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT

## Hardware

nRF54L15 DK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The `nrf54l15dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `nrf54l15dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `nrf54l15dk/nrf54l15/cpuapp` board target can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Applications for the `nrf54l15dk/nrf54l15/cpuflpr` board target need
to be built using sysbuild to include the `vpr_launcher` image for the application core.

Enter the following command to compile `hello_world` for the FLPR core:

```shell
west build -p -b nrf54l15dk/nrf54l15/cpuflpr --sysbuild
```

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

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

To build and program the sample to the nRF54L15 DK, complete the following steps:

First, connect the nRF54L15 DK to you computer using the IMCU USB port on the DK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54l15dk/nrf54l15/cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54L15 DK

Test the nRF54L15 DK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.

## nRF54L05 emulation on nRF54L15 DK

The `nrf54l15dk/nrf54l05` board is a modified version of the [nRF54L15 DK](#nrf54l15dk)
that enforces the limitations imposed by the nRF54L05 IC, which is a
cost-reduced variant of the original nRF54L15. Since Nordic does not offer a
development kit for the nRF54L05, you can use this board to develop for this
IC while using the nRF54L15 Development Kit (PCA10156).

See [nRF54L05 website](https://www.nordicsemi.com/Products/nRF54L05) [[3]](#id6) for the official reference on the IC itself.

## nRF54L10 emulation on nRF54L15 DK

The `nrf54l15dk/nrf54l10` board is a modified version of the [nRF54L15 DK](#nrf54l15dk)
that enforces the limitations imposed by the nRF54L10 IC, which is a
cost-reduced variant of the original nRF54L15. Since Nordic does not offer a
development kit for the nRF54L10 you can use this board to develop for this
IC while using the nRF54L15 Development Kit (PCA10156).

See [nRF54L10 website](https://www.nordicsemi.com/Products/nRF54L10) [[4]](#id8) for the official reference on the IC itself.

## References

[[1](#id3)]

[https://www.nordicsemi.com/Products/nRF54L15](https://www.nordicsemi.com/Products/nRF54L15)

[[2](#id5)]

[https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app\_dev/device\_guides/nrf54l/index.html](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html)

[[3](#id7)]

[https://www.nordicsemi.com/Products/nRF54L05](https://www.nordicsemi.com/Products/nRF54L05)

[[4](#id9)]

[https://www.nordicsemi.com/Products/nRF54L10](https://www.nordicsemi.com/Products/nRF54L10)
