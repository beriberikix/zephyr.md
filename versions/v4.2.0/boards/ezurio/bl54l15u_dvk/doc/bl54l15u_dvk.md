---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ezurio/bl54l15u_dvk/doc/bl54l15u_dvk.html
original_path: boards/ezurio/bl54l15u_dvk/doc/bl54l15u_dvk.html
---

# BL54L15u DVK

Board Overview

[![../../../../_images/bl54l15u_dvk.webp](../../../../_images/bl54l15u_dvk.webp)
](../../../../_images/bl54l15u_dvk.webp)

BL54L15u DVK

Name:
:   `bl54l15u_dvk`

Vendor:
:   Ezurio

Architecture:
:   riscv, arm

SoC:
:   nrf54l15

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/bl54l15u_dvk/doc/bl54l15u_dvk.rst/../..)

## Overview

Note

You can find more information about the BL54L15u module on the [BL54L15u website](https://www.ezurio.com/wireless-modules/bluetooth-modules/bl54-series/bl54l15-micro-series-bluetooth-le-802-15-4-nfc).

You can find more information about the underlying nRF54L15 SoC on the
[nRF54L15 website](https://www.nordicsemi.com/Products/nRF54L15). For the nRF54L15 technical documentation and other
resources (such as SoC Datasheet), see the [nRF54L15 documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html) page.

The BL54L15u Development Kit provides support for the Ezurio BL54L15u module.

The module is based on the Nordic Semiconductor nRF54L15 Arm Cortex-M33 CPU.

The BL54L15u module incorporates the WLCSP package nRF54L15 (1524kB Flash, 256kB RAM).
The part features up to 32 configurable GPIOs and BLE Radio TX Power up to 8dBm.

The module includes the following devices:

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

The BL54L15u DVK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The `bl54l15u_dvk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `bl54l15u_dvk/nrf54l15/cpuapp` board target can be built,
flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

Applications for the `bl54l15u_dvk/nrf54l15/cpuflpr` board target need to be
built using sysbuild to include the `vpr_launcher` image for the application core.

Enter the following command to compile `hello_world` for the FLPR core:

```shell
west build -p -b bl54l15u_dvk/nrf54l15/cpuflpr --sysbuild
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

To build and program the sample to the BL54L15u DVK, complete the following steps:

First, connect the BL54L15u DVK to your computer using the IMCU USB port on the DVK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b bl54l15u_dvk/nrf54l15/cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons on the BL54L15u DVK

Test the BL54L15u DVK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
