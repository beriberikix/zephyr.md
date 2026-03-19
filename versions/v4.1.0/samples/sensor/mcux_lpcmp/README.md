---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/mcux_lpcmp/README.html
original_path: samples/sensor/mcux_lpcmp/README.html
---

# NXP MCUX Low-power Analog Comparator (LPCMP)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/mcux_lpcmp/README.rst/..)

## Overview

This sample show how to use the NXP MCUX Low-power Analog Comparator (LPCMP) driver.

In this application, the negative input port of the LPCMP is set to 7 which
means the input voltage comes from the LPCMP internal DAC, the reference
voltage of the DAC is set to 0 (for the specific chip, the user needs to
check the reference manual to confirm where this reference voltage comes
from), the output voltage of the DAC is equal to (VREF/256)\*(data+1), where
data is set through the attribute `SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE`.
The positive input port is set to 0, the user needs to check the reference
manual and board schematic to confirm which specific port is used and can
connect an external voltage to that port and change the input voltage to
see the output change of the LPCMP.

The output value of the LPCMP is reported on the console.

## Building and Running

### Building and Running for NXP FRDM-MCXN947

Build the application for the [FRDM-MCXN947](../../../boards/nxp/frdm_mcxn947/doc/index.md#frdm_mcxn947) board, and adjust the
LPCMP positive input port voltage by changing the voltage input to J2-17.

```shell
west build -b frdm_mcxn947//cpu0 samples/sensor/mcux_lpcmp
west flash
```

### Building and Running for NXP FRDM-MCXN236

Build the application for the [FRDM-MCXN236](../../../boards/nxp/frdm_mcxn236/doc/index.md#frdm_mcxn236) board, and adjust the
LPCMP positive input port voltage by changing the voltage input to J2-8.

```shell
west build -b frdm_mcxn236 samples/sensor/mcux_lpcmp
west flash
```

### Building and Running for NXP FRDM-MCXA156

Build the application for the [FRDM-MCXA156](../../../boards/nxp/frdm_mcxa156/doc/index.md#frdm_mcxa156) board, and adjust the
LPCMP positive input port voltage by changing the voltage input to J2-9.

```shell
west build -b frdm_mcxa156 samples/sensor/mcux_lpcmp
west flash
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
