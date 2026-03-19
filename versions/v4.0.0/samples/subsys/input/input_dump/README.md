---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/input/input_dump/README.html
original_path: samples/subsys/input/input_dump/README.html
---

# Input dump

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/input/input_dump/README.rst/..)

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

## See also

[Input Event Definitions](../../../../doxygen/html/group__input__events.md)
