---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/drivers/psi5/README.html
original_path: samples/drivers/psi5/README.html
---

# PSI5 interface

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/psi5/README.rst/..)

## Overview

The sample application shows how to use the [PSI5 API](../../../hardware/peripherals/psi5.md#psi5-api):

- Receive data
- Transmit data

## Requirements

This sample requires a PSI5 sensor to be connected and exposed as `psi5-0` Devicetree alias.

## Building, Flashing and Running

```shell
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/drivers/psi5
west flash
```

Sample Output:

```shell
Transmitted data on channel 1

Received a frame on channel 1
```

## See also

[PSI5 Interface](../../../doxygen/html/group__psi5__interface.md)
