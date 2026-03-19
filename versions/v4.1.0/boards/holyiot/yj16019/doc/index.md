---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/holyiot/yj16019/doc/index.html
original_path: boards/holyiot/yj16019/doc/index.html
---

# YJ-16019

Board Overview

[![../../../../_images/holyiot_yj16019_front.jpg](../../../../_images/holyiot_yj16019_front.jpg)
](../../../../_images/holyiot_yj16019_front.jpg)

YJ-16019

Name:
:   `holyiot_yj16019`

Vendor:
:   Shenzhen Holyiot Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/holyiot/yj16019/doc/index.rst/../..)

## Overview

The [Holyiot](http://www.holyiot.com) [[1]](#id3) YJ-16019 hardware provides support for the Nordic
Semiconductor nRF52832 ARM Cortex-M4 CPU and the following devices:

- CLOCK
- FLASH
- GPIO
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- WDT

The board is equipped with one LED, one push button, and is powered by
a CR2032 coin cell. The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

The nRF52832 of the Holyiot YJ-16019 is clocked by an external crystal with a frequency of 32 MHz
(Y1). The 32.768 kHz crystal (Y2) shown on the board schematics is not mounted.

### Supported Features

The `holyiot_yj16019` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED and push button

- Push button = P0.28
- LED = P0.29

## Programming and Debugging

Applications for the `holyiot_yj16019` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); however, an external
Segger J-Link is required since the board does not have any on-board
debug IC.

The following pins of the Segger J-Link must be connected to the following test
pads on the PCB (see image):

- VTref = VCC
- GND = GND
- SWDIO = SDO
- SWCLK = SCK

![Holyiot YJ-16019 PCB](../../../../_images/holyiot_yj16019_pcb.jpg)

Holyiot YJ-16019 PCB (Credit: Holyiot)

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b holyiot_yj16019 samples/basic/blinky
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic
nRF52x-based boards with a Segger debugger.

## Testing the LED and button on the Holyiot YJ-16019

There are 2 samples that allow you to test that the button and LED on
the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The button and LED definitions can be found
in [boards/holyiot/yj16019/holyiot\_yj16019.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/holyiot/yj16019/holyiot_yj16019.dts).

## References

[[1](#id4)]

[http://www.holyiot.com](http://www.holyiot.com)

[[2](#id6)]

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)
