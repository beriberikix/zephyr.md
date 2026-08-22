---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/nrf54lm20dk/doc/index.html
original_path: boards/nordic/nrf54lm20dk/doc/index.html
---

# nRF54LM20 DK

Board Overview

Name:
:   `nrf54lm20dk`

Vendor:
:   Nordic Semiconductor

Architecture:
:   riscv, arm

SoC:
:   nrf54lm20a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/nrf54lm20dk/doc/index.rst/../..)

## Overview

The nRF54LM20 Development Kit hardware provides support for the Nordic Semiconductor
nRF54LM20A Arm Cortex-M33 CPU and the following devices:

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

nRF54LM20 DK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The `nrf54lm20dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `nrf54lm20dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `nrf54lm20dk/nrf54lm20a/cpuapp` board target can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Applications for the `nrf54lm20dk/nrf54lm20a/cpuflpr` board target need
to be built using sysbuild to include the `vpr_launcher` image for the application core.

Enter the following command to compile `hello_world` for the FLPR core:

```shell
west build -p -b nrf54lm20dk/nrf54lm20a/cpuflpr --sysbuild
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

To build and program the sample to the nRF54LM20 DK, complete the following steps:

First, connect the nRF54LM20 DK to you computer using the IMCU USB port on the DK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54lm20dk/nrf54lm20a/cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54LM20 DK

Test the nRF54LM20 DK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
