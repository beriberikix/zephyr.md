---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/microchip/ev11l78a/doc/index.html
original_path: boards/microchip/ev11l78a/doc/index.html
---

# UPD301C Basic Sink Application Example

Board Overview

[![../../../../_images/ev11l78a.jpg](../../../../_images/ev11l78a.jpg)
](../../../../_images/ev11l78a.jpg)

UPD301C Basic Sink Application Example

Name:
:   `ev11l78a`

Vendor:
:   Microchip Technology Inc.

Architecture:
:   arm

SoC:
:   samd20e16

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/ev11l78a/doc/index.rst/../..)

## Overview

The UPD301C Basic Sink Application Example Evaluation Kit (EV11L78A)
is a low-cost evaluation platform for Microchip’s UPD301C Standalone
Programmable USB Power Delivery (PD) Controller. This RoHS-compliant
evaluation platform comes in a small form factor and adheres to the
USB Type-C™ Connector Specification and USB PD 3.0 specification.

## Hardware

- ATSAMD20E16 ARM Cortex-M0+ processor at 48 MHz
- UPD301C combines a SAMD20 core and a UPD350 USB-PD controller
- Sink PDO Selector Switch
- Onboard LED Voltmeter

### Supported Features

The `ev11l78a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Refer to the [EV11L78A Schematics](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF) [[1]](#id2) for a detailed hardware diagram.

### Serial Port

The SAMD20 MCU has 6 SERCOM based USARTs. One of the USARTs
(SERCOM1) is available on the Debug/Status header.

### SPI Port

The SAMD20 MCU has 6 SERCOM based SPIs. One of the SPIs (SERCOM0)
is internally connected between the SAMD20 core and the UPD350.

### I²C Port

The SAMD20 MCU has 6 SERCOM based I2Cs. One of the I2Cs (SERCOM3)
is available on the Debug/Status header.

## References

[[1](#id3)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF)
