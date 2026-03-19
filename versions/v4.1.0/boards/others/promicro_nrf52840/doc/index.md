---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/promicro_nrf52840/doc/index.html
original_path: boards/others/promicro_nrf52840/doc/index.html
---

# Pro Micro nRF52840

Board Overview

[![../../../../_images/others_promicro_nrf52840.webp](../../../../_images/others_promicro_nrf52840.webp)
](../../../../_images/others_promicro_nrf52840.webp)

Pro Micro nRF52840

Name:
:   `promicro_nrf52840`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/promicro_nrf52840/doc/index.rst/../..)

More of a board type than a unique board, It is based on Nice!Nano.
Also referred to as Pro Micro, Promicro, SuperMini nRF52840 boards.

## Overview

The hardware provides support for the Nordic
Semiconductor nRF52840 ARM Cortex-M4F CPU and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- SPI
- UART
- USB
- WDT

More information about the original board can be found at the
[Nice!Nano website](https://nicekeyboards.com/docs/nice-nano/) [[1]](#id2).

Information about clones can be found at [Clone Wiki](https://github.com/joric/nrfmicro/wiki/Alternatives) [[2]](#id4).

Pinout and Schematic are available in the [Nice!Nano Documentation](https://nicekeyboards.com/docs/nice-nano/pinout-schematic) [[3]](#id6)

### Supported Features

The `promicro_nrf52840` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

- LED0 = P0.15, can be any color.

## Programming and Debugging

Applications for the `promicro_nrf52840/nrf52840` board target can be
built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Flashing

The board is factory-programmed with Adafruit’s UF2 booloader

#. Reset the board into the bootloader by bridging ground and RST 2 times
quickly

> The status LED should start a fade pattern, signalling the bootloader is
> running.

1. Compile a Zephyr application; we’ll use [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.").

   ```shell
   west build -b promicro_nrf52840/nrf52840/uf2 zephyr/samples/basic/blinky
   ```
2. Flash it onto the board. You may need to mount the device.

   ```shell
   west flash
   ```

   When this command exits, observe the red LED on the board blinking,

### Debugging

You may debug this board using the broken out pads on the back.
PyOCD and openOCD can be used to flash and debug this board.

### Recovery

In case of a error resulting in a board’s bootloader becoming inaccessible,
it is possible to flash anything directly using openOCD:

1. Setup OpenOCD correctly, here for WCH linkE in ARM mode:

   ```shell
   openocd -f interface/cmsis-dap.cfg -f target/nrf52.cfg
   ```

Note interface and target folders are from openOCD’s tcl folder.

1. Connect to openOCD, for example with telnet or GDB:

   ```shell
   telnet localhost 4444
   ```

   ```shell
   target extended-remote localhost:3333
   ```
2. Erase flash:

   ```shell
   reset halt
   nrf5 mass_erase
   ```

or

> ```shell
> mon reset halt
> mon nrf5 mass_erase
> ```

1. Flash Bootloader

   ```shell
   flash write_image erase nice_nano_bootloader-0.9.2_s140_6.1.1.hex
   ```

or

> ```shell
> mon flash write_image erase nice_nano_bootloader-0.9.2_s140_6.1.1.hex
> ```

## References

[[1](#id3)]

[https://nicekeyboards.com/docs/nice-nano/](https://nicekeyboards.com/docs/nice-nano/)

[[2](#id5)]

[https://github.com/joric/nrfmicro/wiki/Alternatives](https://github.com/joric/nrfmicro/wiki/Alternatives)

[[3](#id7)]

[https://nicekeyboards.com/docs/nice-nano/pinout-schematic](https://nicekeyboards.com/docs/nice-nano/pinout-schematic)
