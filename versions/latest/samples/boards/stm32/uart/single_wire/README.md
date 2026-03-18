---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/uart/single_wire/README.html
original_path: samples/boards/stm32/uart/single_wire/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 single-wire UART

## Overview

A simple application demonstrating how to use the single wire / half-duplex UART
functionality of STM32. Without adaptions this example runs on STM32F3 discovery
board. You need to establish a physical connection between pins PA2 (USART2\_TX) and
PC10 (UART4\_TX).

Add a single\_wire\_uart\_loopback fixture to your board in the hardware map to allow
twister to verify this sample’s output automatically.

## Building and Running

Build and flash as follows, replacing `stm32f3_disco` with your board:

> ```shell
> west build -b stm32f3_disco samples/boards/stm32/uart/single_wire
> west flash
> ```

After flashing the console output should not show any failure reports,
but the following message repeated every 2s:

```text
Received c
```
