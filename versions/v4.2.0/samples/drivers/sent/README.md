---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/drivers/sent/README.html
original_path: samples/drivers/sent/README.html
---

# SENT interface

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/sent/README.rst/..)

## Overview

The sample application shows how to use the [SENT API](../../../hardware/peripherals/sent.md#sent-api):

- Receive data

## Requirements

This sample requires a SENT sensor to be connected and exposed as `sent0` Devicetree alias.

## Building, Flashing and Running

```shell
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/drivers/sent
west flash
```

Sample Output:

```shell
Received a frame on channel 1
```

## See also

[SENT Interface](../../../doxygen/html/group__sent__interface.md)
