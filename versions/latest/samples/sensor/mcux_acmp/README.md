---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/mcux_acmp/README.html
original_path: samples/sensor/mcux_acmp/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP MCUX Analog Comparator (ACMP)

## Overview

This sample show how to use the NXP MCUX Analog Comparator (ACMP) driver. The
sample supports the [NXP TWR-KE18F](../../../boards/arm/twr_ke18f/doc/index.md#twr-ke18f), [NXP MIMXRT1170-EVK/EVKB](../../../boards/arm/mimxrt1170_evk/doc/index.md#mimxrt1170-evk).

The input voltage for the negative input of the analog comparator is
provided by the ACMP Digital-to-Analog Converter (DAC). The input voltage for
the positive input can be adjusted by turning the on-board potentiometer for
[NXP TWR-KE18F](../../../boards/arm/twr_ke18f/doc/index.md#twr-ke18f) board, for [NXP MIMXRT1170-EVK/EVKB](../../../boards/arm/mimxrt1170_evk/doc/index.md#mimxrt1170-evk) the voltage signal is
captured on J25-13, need change the external voltage signal to check the
output.

The output value of the analog comparator is reported on the console.

## Building and Running

### Building and Running for TWR-KE18F

Build the application for the [NXP TWR-KE18F](../../../boards/arm/twr_ke18f/doc/index.md#twr-ke18f) board, and adjust the
ACMP input voltage by turning the on-board potentiometer.

```shell
west build -b twr_ke18f samples/sensor/mcux_acmp
west flash
```

### Building and Running for MIMXRT1170-EVK

Build the application for the MIMXRT1170-EVK board, and adjust the
ACMP input voltage by changing the voltage input to J25-13.

```shell
west build -b mimxrt1170_evk_cm7 samples/sensor/mcux_acmp
west flash
```
