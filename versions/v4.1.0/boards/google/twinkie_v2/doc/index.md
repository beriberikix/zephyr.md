---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/google/twinkie_v2/doc/index.html
original_path: boards/google/twinkie_v2/doc/index.html
---

# Twinkie V2

Board Overview

Name:
:   `google_twinkie_v2`

Vendor:
:   Google, Inc.

Architecture:
:   arm

SoC:
:   stm32g0b1xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/twinkie_v2/doc/index.rst/../..)

## Overview

Google Twinkie V2 is a reference board for the google power delivery analyzer
(PDA) Twinkie V2.

## Hardware

- STM32G0B1REI6

### Supported Features

The `google_twinkie_v2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- CC1\_BUF : PA1
- CC2\_BUF : PA3
- VBUS\_READ\_BUF : PB11
- CSA\_VBUS : PC4
- CSA\_CC2 : PC5

## Programming and Debugging

Build application as usual for the `google_twinkie_v2` board, and flash
using dfu-util or J-Link.

### Debugging

Use SWD with a J-Link or ST-Link.
