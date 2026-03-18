---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/mcux_lpcmp/README.html
original_path: samples/sensor/mcux_lpcmp/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NXP MCUX Low-power Analog Comparator (LPCMP)

## Overview

This sample show how to use the NXP MCUX Analog Comparator (LPCMP) driver.

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

Build the application for the [NXP FRDM-MCXN947](../../../boards/nxp/frdm_mcxn947/doc/index.md#frdm-mcxn947) board, and adjust the
LPCMP positive input port voltage by changing the voltage input to J2-17.

```shell
west build -b frdm_mcxn947//cpu0 samples/sensor/mcux_lpcmp
west flash
```
