---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/nrf/nrf_led_matrix/README.html
original_path: samples/boards/nrf/nrf_led_matrix/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nRF LED matrix sample

## Overview

This is a simple application intended to present the nRF LED matrix display
driver in action and to serve as a test ensuring that this driver is buildable
for both the [BBC MicroBit V2](../../../../boards/bbc/microbit_v2/doc/index.md#bbc-microbit-v2) and [BBC MicroBit](../../../../boards/bbc/microbit/doc/index.md#bbc-microbit) boards.

## Requirements

The sample has been tested on the bbc\_microbit\_v2 and bbc\_microbit boards,
but it could be ported to any board with an nRF SoC and the proper number
of GPIOs available for driving a LED matrix. To do it, one needs to add an
overlay file with the corresponding `"nordic,nrf-led-matrix"` compatible
node.

## Building and Running

The code can be found in [samples/boards/nrf/nrf\_led\_matrix](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nrf/nrf_led_matrix).

To build and flash the application:

```shell
west build -b bbc_microbit_v2 samples/boards/nrf/nrf_led_matrix
west flash
```
