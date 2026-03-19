---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/adc_cmp_npcx/README.html
original_path: samples/sensor/adc_cmp_npcx/README.html
---

# NPCX ADC Comparator

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/adc_cmp_npcx/README.rst/..)

## Overview

This sample show how to use the NPCX ADC Comparator driver. The
sample supports the [NPCX9M6F\_EVB](../../../boards/nuvoton/npcx9m6f_evb/doc/index.md#npcx9m6f_evb).

This application is a voltage comparator with hysteresis, upper limit is
set at 1 V while lower limit is 250 mV. Initially configured to detect
upper limit.

## Building and Running

Build the application for the [NPCX9M6F\_EVB](../../../boards/nuvoton/npcx9m6f_evb/doc/index.md#npcx9m6f_evb) board, and provide voltage
to ADC channel 8, when voltages cross upper/lower limits, detection messages
will be printed.

```shell
west build -b npcx9m6f_evb samples/sensor/adc_cmp_npcx
west flash
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
