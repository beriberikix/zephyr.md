---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/microchip/sam/sama7g54_ek/doc/index.html
original_path: boards/microchip/sam/sama7g54_ek/doc/index.html
---

# SAMA7G54 Evaluation Kit

Board Overview

[![../../../../../_images/sama7g54_ek.webp](../../../../../_images/sama7g54_ek.webp)
](../../../../../_images/sama7g54_ek.webp)

SAMA7G54 Evaluation Kit

Name:
:   `sama7g54_ek`

Vendor:
:   Microchip Technology Inc.

Architecture:
:   arm

SoC:
:   sama7g54

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/sam/sama7g54_ek/doc/index.rst/../..)

## Overview

The SAMA7G54-EK evaluation kit is intended for evaluating and prototyping with
the SAMA7G54 microprocessor (MPU). The SAMA7G54 is a Arm Cortex-A7 based MPU
running up to 1GHz supporting up to 2GBytes of 16-bit DDR2, DDR3, DDR3L, LPDDR2,
LPDDR3, with octal/quad SPI, NAND and e.MMC Flash support.

The SAMA7G54 integrates a complete imaging and audio subsystems with 12-bit
parallel and MIPI-CSI2 camera interfaces up to 8 Mp and 720p @ 60 fps, up to
four I2S, one SPDIF transmitter and receiver and a 4-stereo channel audio sample
rate converter. The device also features a large number of connectivity options
including Dual Ethernet (one Gigabit ethernet and one 10/100 Ethernet), six
CAN-FD and three high-speed USB and offers advanced security functions such as:
secure boot, secure key storage, high-performance crypto accelerators for AES,
SHA, RSA and ECC.

The SAMA7G54-EK board itself features connectors and expansion headers for easy
customization and quick access to leading edge embedded features such as MIKROE
Click boards™ and Raspberry Pi expansion header plus MIPI CSI camera.

## Hardware

- SAMA7G54-V/4HB Microprocessor
- Raspberry Pi CSI camera interface
- One 16-bit, 4Gb DDR3L
- One 32Gb e.MMC
- 1Gb Octal SPI Flash
- 2 EEPROMs w/ EUI-48TM MAC ID
- 1 SD card slot
- 3 HS USB ports
- 2 CAN interfaces
- 2 Ethernet ports (Gigabit and 10/100)
- Pad for ATWILC3000 Wi-Fi/BT module (unpopulated)
- S/PDIF RX and TX ports
- 4 digital microphone ports
- 40-pin Raspberry Pi expansion header
- 2 mikroBUS™ connectors
- USB powered

### Supported Features

The `sama7g54_ek` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [SAMA7G54-EK User Guide](https://ww1.microchip.com/downloads/aemDocuments/documents/MPU32/ProductDocuments/UserGuides/SAMA7G54-EK-User%27s-Guide-DS50003273.pdf) has detailed information about board connections.

## References

SAMA7G54 Product Page:
:   [https://www.microchip.com/en-us/product/sama7g54](https://www.microchip.com/en-us/product/sama7g54)

SAMA7G54 Evaluation Kit Page:
:   [https://www.microchip.com/en-us/development-tool/EV21H18A](https://www.microchip.com/en-us/development-tool/EV21H18A)
