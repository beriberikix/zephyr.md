---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/dsa/README.html
original_path: samples/net/dsa/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DSA (Distributed Switch Architecture)

## Overview

Example on testing/debugging Distributed Switch Architecture

The source code for this sample application can be found at:
[samples/net/dsa](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/dsa).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

Host machine with [SEGGER IP Switch Board](../../../boards/arm/ip_k66f/doc/index.md#ip-k66f) board from Segger.

Follow these steps to build the DSA sample application:

```shell
west build -b <board to use> samples/net/dsa -- -DCONF_FILE=prj.conf
```
