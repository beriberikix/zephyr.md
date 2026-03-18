---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/tmp112/README.html
original_path: samples/sensor/tmp112/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# TMP112 sample

## Overview

A sample showing how to use the [`ti,tmp112`](../../../build/dts/api/bindings/sensor/ti%2Ctmp112.md#std-dtcompatible-ti-tmp112) sensor.

## Requirements

A board with this sensor built in to its [devicetree](../../../build/dts/index.md#dt-guide), or a
devicetree overlay with such a node added.

## Building and Running

To build and flash the sample for the [NXP FRDM-K64F](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f):

```shell
west build -b frdm_k64f samples/sensor/tmp112
west flash
```
