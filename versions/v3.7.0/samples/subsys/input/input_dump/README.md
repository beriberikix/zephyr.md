---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/input/input_dump/README.html
original_path: samples/subsys/input/input_dump/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Input dump

## Overview

The Input Dump sample prints any input event using the [Input](../../../../services/input/index.md#input) APIs.

## Requirements

The samples works on any board with an input driver defined in the board devicetree.

## Building and Running

Build and flash as follows, changing `nrf52dk/nrf52832` for your board:

```shell
west build -b nrf52dk/nrf52832 samples/subsys/input/input_dump
west flash
```

After starting, the sample will print any input event in the console.
