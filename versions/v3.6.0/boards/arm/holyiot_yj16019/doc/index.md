---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/holyiot_yj16019/doc/index.html
original_path: boards/arm/holyiot_yj16019/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Holyiot YJ-16019

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

![Holyiot YJ-16019](../../../../_images/holyiot_yj16019_front.jpg)

Holyiot YJ-16019 (Credit: Holyiot)

The board is equipped with one LED, one push button, and is powered by
a CR2032 coin cell. The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

The nRF52832 of the Holyiot YJ-16019 is clocked by an external crystal with a frequency of 32 MHz
(Y1). The 32.768 kHz crystal (Y2) shown on the board schematics is not mounted.

### Supported Features

The holyiot\_yj16019 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.

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
in [boards/arm/holyiot\_yj16019/holyiot\_yj16019.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/holyiot_yj16019/holyiot_yj16019.dts).

## References

[[1](#id4)]

[http://www.holyiot.com](http://www.holyiot.com)

[[2](#id6)]

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)
