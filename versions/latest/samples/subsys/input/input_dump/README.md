---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/input/input_dump/README.html
original_path: samples/subsys/input/input_dump/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Input dump

## Overview

The Input Dump sample prints any input event using the [Input](../../../../services/input/index.md#input) APIs.

## Requirements

The samples works on any board with an input driver defined in the board devicetree.

## Building and Running

Build and flash as follows, changing `nrf52dk_nrf52832` for your board:

```shell
west build -b nrf52dk_nrf52832 samples/subsys/input/input_dump
west flash
```

After starting, the sample will print any input event in the console.
