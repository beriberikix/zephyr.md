---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/uart/single_wire/README.html
original_path: samples/boards/st/uart/single_wire/README.html
---

# Single-wire UART

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/uart/single_wire/README.rst/..)

## Overview

A simple application demonstrating how to use the single-wire/half-duplex
UART functionality of STM32 devices. The example runs on various STM32
boards with minimal adaptations.
Add a `single_wire_uart_loopback` fixture to your board in the hardware map to allow
twister to verify this sample’s output automatically.

## Hardware Setup

You need to establish a physical connection between UART pins on the board.
Refer to the specific board overlay file for the exact pin connections.

## Building and Running

Build and flash as follows, replacing `stm32f3_disco` with your board:

> ```shell
> west build -b stm32f3_disco samples/boards/st/uart/single_wire
> west flash
> ```

After flashing the console output should not show any failure reports,
but the following message repeated every 2s:

```text
Received c
```

## See also

[UART Interface](../../../../../doxygen/html/group__uart__interface.md)
