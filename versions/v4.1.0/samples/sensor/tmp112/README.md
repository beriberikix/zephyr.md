---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/tmp112/README.html
original_path: samples/sensor/tmp112/README.html
---

# TMP112 Temperature Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/tmp112/README.rst/..)

## Overview

A sample showing how to use the [`ti,tmp112`](../../../build/dts/api/bindings/sensor/ti%2Ctmp112.md#std-dtcompatible-ti-tmp112) sensor.

## Requirements

A board with this sensor built in to its [devicetree](../../../build/dts/index.md#dt-guide), or a
devicetree overlay with such a node added.

## Building and Running

To build and flash the sample for the [FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f):

```shell
west build -b frdm_k64f samples/sensor/tmp112
west flash
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
