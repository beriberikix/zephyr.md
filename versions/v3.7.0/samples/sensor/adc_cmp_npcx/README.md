---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/adc_cmp_npcx/README.html
original_path: samples/sensor/adc_cmp_npcx/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NPCX ADC Comparator

## Overview

This sample show how to use the NPCX ADC Comparator driver. The
sample supports the [Nuvoton NPCX9M6F\_EVB](../../../boards/nuvoton/npcx9m6f_evb/doc/index.md#npcx9m6f-evb).

This application is a voltage comparator with hysteresis, upper limit is
set at 1 V while lower limit is 250 mV. Initially configured to detect
upper limit.

## Building and Running

Build the application for the [Nuvoton NPCX9M6F\_EVB](../../../boards/nuvoton/npcx9m6f_evb/doc/index.md#npcx9m6f-evb) board, and provide voltage
to ADC channel 8, when voltages cross upper/lower limits, detection messages
will be printed.

```shell
west build -b npcx9m6f_evb samples/sensor/adc_cmp_npcx
west flash
```
