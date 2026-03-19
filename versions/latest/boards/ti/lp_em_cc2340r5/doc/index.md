---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ti/lp_em_cc2340r5/doc/index.html
original_path: boards/ti/lp_em_cc2340r5/doc/index.html
---

# CC2340R5 LaunchPad

Board Overview

[![../../../../_images/lp_em_cc2340r5.webp](../../../../_images/lp_em_cc2340r5.webp)
](../../../../_images/lp_em_cc2340r5.webp)

CC2340R5 LaunchPad

Name:
:   `lp_em_cc2340r5`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc2340r5

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/lp_em_cc2340r5/doc/index.rst/../..)

## Overview

The Texas Instruments CC2340R5 LaunchPad™ (LP\_EM\_CC2340R5) is a
development kit for the SimpleLink™ multi-Standard CC2340R5 wireless MCU.

See the [TI CC2340R5 LaunchPad Product Page](https://www.ti.com/tool/LP-EM-CC2340R5) for details.

## Hardware

The CC2340R5 LaunchPad™ development kit features the CC2340R5 wireless MCU.
The board is equipped with two LEDs, two push buttons and BoosterPack connectors
for expansion.

The CC2340R5 wireless MCU has a 48 MHz Arm® Cortex®-M0+ SoC and an
integrated 2.4 GHz transceiver supporting multiple protocols including Bluetooth® Low Energy and IEEE® 802.15.4.

See the [TI CC2340R5 Product Page](https://www.ti.com/product/CC2340R5) for additional details.

### Supported Features

The `lp_em_cc2340r5` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

All I/O signals are accessible from the BoosterPack connectors. Pin function
aligns with the LaunchPad standard.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO0 | GPIO |  |
| DIO1 | ANALOG\_IO | A4 |
| DIO2 | ANALOG\_IO | A3 |
| DIO5 | ANALOG\_IO | A5 |
| DIO6 | SPI\_CSN | SPI CS |
| DIO7 | ANALOG\_IO | A0 |
| DIO8 | GPIO |  |
| DIO9 | GPIO | Button 2 |
| DIO10 | GPIO | Button 1 |
| DIO11 | SPI\_CSN | SPI CS |
| DIO12 | SPI\_POCI | SPI POCI |
| DIO13 | SPI\_PICO | SPI\_PICO |
| DIO14 | GPIO | Red LED |
| DIO15 | GPIO | Green LED |
| DIO18 | SPI\_CLK | SPI CLK |
| DIO19 | GPIO |  |
| DIO20 | UART0\_TX | UART TX |
| DIO21 | GPIO |  |
| DIO22 | UART0\_RX | UART RX |
| DIO23 | ANALOG\_IO | A8 |
| DIO24 | ANALOG\_IO | A7 |

## Programming and Debugging

The LP\_EM\_CC2340R5 requires an external debug probe such as the LP-XDS110 or
LP-XDS110ET.

Currently there is no debug support in Zephyr for the LP\_EM\_CC2340R5, and the
built binaries for this target must be flashed/debugged using either Uniflash
or Code Composer Studio.

## References

CC2340R5 LaunchPad Quick Start Guide:
:   [https://www.ti.com/lit/pdf/swru588](https://www.ti.com/lit/pdf/swru588)
