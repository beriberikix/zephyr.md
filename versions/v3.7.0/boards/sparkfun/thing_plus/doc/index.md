---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/sparkfun/thing_plus/doc/index.html
original_path: boards/sparkfun/thing_plus/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nRF9160 Thing Plus

![Sparkfun nRF9160 Thing Plus](../../../../_images/sparkfun_thing_plus_nrf9160.jpg)

nRF9160 Thing Plus (Credit: Sparkfun)

## Overview

The nRF9160 Thing Plus designed by Circuit Dojo is a single-board development
for bringing your LTE-M and NB-IoT applications to life. The sparkfun\_thing\_plus\_nrf9160
board configuration leverages the pre-existing support for the Nordic Semiconductor
nRF9160. Supported nRF9160 peripherals include:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT
- IDAU

More information about the board can be found at the
[nRF9160 Thing Plus Documentation](https://docs.jaredwolff.com/nrf9160-introduction.html) [[1]](#id2).

## Hardware

### Connections and IOs

The nRF9160 Thing Plus has everything you know and love about
the Feather platform. Here are some of the highlights:

#### LED

- D7 (blue) = P0.03

#### Push buttons and Switches

- MODE = P0.12
- RESET

#### USB

Contains a USB/UART connection for both debugging and loading new
code using a UART Enabled MCUBoot.

#### Standard Battery Connection

The nRF9160 Thing Plus has a 2 pin battery connector on board. Lithium Polymer batteries >
300mA required.

#### Nano SIM Holder

The nRF9160 Thing Plus has a built-in nano SIM (4FF) holder located
on the bottom side.

## Programming and Debugging

sparkfun\_thing\_plus\_nrf9160 can be used with most programmers like:

- J-Link (the nRF53-DK is recommended)
- CMSIS-DAP based programmers

Check out [Getting Started](https://docs.jaredwolff.com/nrf9160-getting-started.html) [[2]](#id4) for more info.

### Building an application

In most cases you’ll want to use the `ns` target with any of the Zephyr
or Nordic based examples.

Some of the examples do not use secure mode, so they do not required the `ns` suffix.
A great example of this is the hello\_world below.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ screen /dev/<tty_device> 115200
```

Replace `<tty_device>` with the port where the nRF9160 Thing Plus
can be found. In most cases (On Linux/Mac) it will be: `/dev/tty.SLAB_USBtoUART`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b sparkfun_thing_plus_nrf9160 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons on the nRF9160 Thing Plus

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/sparkfun/thing\_plus/sparkfun\_thing\_plus\_nrf9160\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus/sparkfun_thing_plus_nrf9160_common.dtsi).

## References

[[1](#id3)]

[https://docs.jaredwolff.com/nrf9160-introduction.html](https://docs.jaredwolff.com/nrf9160-introduction.html)

[[2](#id5)]

[https://docs.jaredwolff.com/nrf9160-getting-started.html](https://docs.jaredwolff.com/nrf9160-getting-started.html)

**Side note** This page was based on the documentation for the nRF9160 DK. Thanks to Nordic for
developing a great platform!
