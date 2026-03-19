---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/nordic/nrf_led_matrix/README.html
original_path: samples/boards/nordic/nrf_led_matrix/README.html
---

# LED matrix

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrf_led_matrix/README.rst/..)

## Overview

This is a simple application intended to present the nRF LED matrix display
driver in action and to serve as a test ensuring that this driver is buildable
for both the [micro:bit V2](../../../../boards/bbc/microbit_v2/doc/index.md#bbc_microbit_v2) and [micro:bit](../../../../boards/bbc/microbit/doc/index.md#bbc_microbit) boards.

## Requirements

The sample has been tested on the bbc\_microbit\_v2 and bbc\_microbit boards,
but it could be ported to any board with an nRF SoC and the proper number
of GPIOs available for driving an LED matrix. To do it, one needs to add an
overlay file with the corresponding `"nordic,nrf-led-matrix"` compatible
node.

## Building and Running

The code can be found in [samples/boards/nordic/nrf\_led\_matrix](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/nrf_led_matrix).

To build and flash the application:

```shell
west build -b bbc_microbit_v2 samples/boards/nordic/nrf_led_matrix
west flash
```
