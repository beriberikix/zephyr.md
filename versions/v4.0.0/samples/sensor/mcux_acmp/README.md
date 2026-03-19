---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/mcux_acmp/README.html
original_path: samples/sensor/mcux_acmp/README.html
---

# NXP MCUX Analog Comparator (ACMP)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/mcux_acmp/README.rst/..)

## Overview

This sample show how to use the NXP MCUX Analog Comparator (ACMP) driver. The
sample supports the [TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f), [MIMXRT1170-EVK/EVKB](../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170_evk), [FRDM-KE17Z](../../../boards/nxp/frdm_ke17z/doc/index.md#frdm_ke17z)
, [FRDM-KE17Z512](../../../boards/nxp/frdm_ke17z512/doc/index.md#frdm_ke17z512) and [MIMXRT1180-EVK](../../../boards/nxp/mimxrt1180_evk/doc/index.md#mimxrt1180_evk).

The input voltage for the negative input of the analog comparator is
provided by the ACMP Digital-to-Analog Converter (DAC). The input voltage for
the positive input can be adjusted by turning the on-board potentiometer for
[TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f) board, for [MIMXRT1170-EVK/EVKB](../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170_evk) the voltage signal is
captured on J25-13, the [FRDM-KE17Z](../../../boards/nxp/frdm_ke17z/doc/index.md#frdm_ke17z) and [FRDM-KE17Z512](../../../boards/nxp/frdm_ke17z512/doc/index.md#frdm_ke17z512) boards are
captured in J2-3, the [MIMXRT1180-EVK](../../../boards/nxp/mimxrt1180_evk/doc/index.md#mimxrt1180_evk) board are captured in J45-13, need
change the external voltage signal to check the output.

The output value of the analog comparator is reported on the console.

## Building and Running

### Building and Running for TWR-KE18F

Build the application for the [TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f) board, and adjust the
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

### Building and Running for FRDM-KE17Z

Build the application for the FRDM-KE17Z board, and adjust the
ACMP input voltage by changing the voltage input to J2-3.

```shell
west build -b frdm_ke17z samples/sensor/mcux_acmp
west flash
```

### Building and Running for FRDM-KE17Z512

Build the application for the FRDM-KE17Z512 board, and adjust the
ACMP input voltage by changing the voltage input to J2-3.

```shell
west build -b frdm_ke17z512 samples/sensor/mcux_acmp
west flash
```

### Building and Running for MIMXRT1180-EVK

Build the application for the MIMXRT1180-EVK board, and adjust the
ACMP input voltage by changing the voltage input to J45-13.

```shell
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/sensor/mcux_acmp
west flash
```

```shell
west build -b mimxrt1180_evk/mimxrt1189/cm7 samples/sensor/mcux_acmp
west flash
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
