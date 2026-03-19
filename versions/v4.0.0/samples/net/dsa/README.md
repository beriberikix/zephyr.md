---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/dsa/README.html
original_path: samples/net/dsa/README.html
---

# DSA (Distributed Switch Architecture)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/dsa/README.rst/..)

## Overview

Example on testing/debugging Distributed Switch Architecture

The source code for this sample application can be found at:
[samples/net/dsa](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/dsa).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

Host machine with [IP Switch Board](../../../boards/segger/ip_k66f/doc/index.md#ip_k66f) board from Segger.

Follow these steps to build the DSA sample application:

```shell
west build -b <board to use> samples/net/dsa -- -DCONF_FILE=prj.conf
```

## See also

[Distributed Switch Architecture definitions and helpers](../../../doxygen/html/group__DSA.md)
