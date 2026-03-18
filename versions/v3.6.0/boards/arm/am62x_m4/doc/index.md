---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/am62x_m4/doc/index.html
original_path: boards/arm/am62x_m4/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# AM62x M4F Core

## Overview

The Texas Instrument AM62x SoC contains a quad Cortex-A53 cluster and a single
Cortex-M4F core in the MCU domain. This chapter describes all boards with support
for the M4F subsystem.

Currently the following hardware platforms are supported:

### Supported Features

The AM62x M4F platform supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINCTRL | on-chip | pinctrl |
| UART | on-chip | serial |

Other hardware features are not currently supported by the port.
