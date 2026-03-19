---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/segger/trb_stm32f407/doc/index.html
original_path: boards/segger/trb_stm32f407/doc/index.html
---

# Cortex-M Trace Reference Board V1.2

Board Overview

[![../../../../_images/segger_trb_stm32f407.jpg](../../../../_images/segger_trb_stm32f407.jpg)
](../../../../_images/segger_trb_stm32f407.jpg)

Cortex-M Trace Reference Board V1.2

Name:
:   `segger_trb_stm32f407`

Vendor:
:   SEGGER Microcontroller GmbH

Architecture:
:   arm

SoC:
:   stm32f407xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/segger/trb_stm32f407/doc/index.rst/../..)

## Overview

The Cortex-M Trace Reference Board V1.2 (SEGGER-TRB-STM32F407 for short)
board is a reference board, based on the ST Microelectronics STM32F407VE
ARM Cortex-M4 CPU, to test hardware tracing with the SEGGER Trace-Pro
debuggers. It is not meant for general prototype development because
it is extremely limited when it comes to IO, and only has 3 LEDs.

## Hardware

Information about the board can be found at the [SEGGER website](https://www.segger.com/products/debug-probes/j-trace/accessories/trace-reference-boards/overview/) .
The [ST STM32F407VE website](https://www.st.com/en/microcontrollers-microprocessors/stm32f407ve.html) contains the processor’s information
and the datasheet.

### Supported Features

The `segger_trb_stm32f407` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

#### LED

- LED0 (green) = PA8
- LED1 (green) = PA9
- LED2 (green) = PA10

#### External Connectors

JTAG/SWD debug

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | VTref | 2 | SWDIO/TMS |
| 3 | GND | 4 | SWCLK/TCK |
| 5 | GND | 6 | SWO/TDO |
| 7 | — | 8 | TDI |
| 9 | NC | 10 | nRESET |
| 11 | 5V-Supply | 12 | TRACECLK |
| 13 | 5V-Supply | 14 | TRACEDATA[0] |
| 15 | GND | 16 | TRACEDATA[1] |
| 17 | GND | 18 | TRACEDATA[2] |
| 19 | GND | 20 | TRACEDATA[3] |

### System Clock

SEGGER-STM32F407-TRB has one external oscillator. The frequency of
the main clock is 12 MHz. The processor can setup HSE to drive the
master clock, which can be set as high as 168 MHz.

## Programming and Debugging

The SEGGER-TRB-STM32F407 board is specially designed to test the SEGGER
Trace-Pro debuggers, so this example assumes a J-Trace or J-Link is used.

### Flashing an application to the SEGGER-TRB-STM32F407

Connect the J-Trace/J-Link USB dongle to your host computer and to the JTAG
port of the SEGGER-TRB-STM32F407 board. Then build and flash an application.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b segger_trb_stm32f407 samples/basic/blinky
west flash
```

After resetting the board, you should see LED0 blink with a 1 second interval.

### Debugging

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b segger_trb_stm32f407 samples/basic/blinky
west debug
```
