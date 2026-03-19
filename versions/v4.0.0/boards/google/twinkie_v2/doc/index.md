---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/google/twinkie_v2/doc/index.html
original_path: boards/google/twinkie_v2/doc/index.html
---

# Twinkie V2

Board Overview

Vendor:
:   Google, Inc.

Architecture:
:   arm

SoC:
:   stm32g0b1xx

## Overview

Google Twinkie V2 is a reference board for the google power delivery analyzer
(PDA) Twinkie V2.

## Hardware

- STM32G0B1REI6

### Supported Features

The following features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |

The default configuration can be found in the defconfig file:
[boards/google/twinkie\_v2/google\_twinkie\_v2\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/google/twinkie_v2/google_twinkie_v2_defconfig)

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
