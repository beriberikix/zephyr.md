---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/lorawan/class_a/README.html
original_path: samples/subsys/lorawan/class_a/README.html
---

# LoRaWAN class A device

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/lorawan/class_a/README.rst/..)

## Overview

A simple application to demonstrate the [LoRaWAN subsystem](../../../../connectivity/lora_lorawan/index.md#lorawan-api) of Zephyr.

## Building and Running

This sample can be found under
[samples/subsys/lorawan/class\_a](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/lorawan/class_a) in the Zephyr tree.

Before building the sample, make sure to select the correct region in the
`prj.conf` file.

The following commands build and flash the sample.

```shell
west build -b nucleo_wl55jc samples/subsys/lorawan/class_a
west flash
```

## See also

[LoRaWAN APIs](../../../../doxygen/html/group__lorawan__api.md)
