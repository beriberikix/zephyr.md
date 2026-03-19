---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/waveshare/open103z/doc/index.html
original_path: boards/waveshare/open103z/doc/index.html
---

# Open103Z

Board Overview

[![../../../../_images/waveshare_open103z.jpg](../../../../_images/waveshare_open103z.jpg)
](../../../../_images/waveshare_open103z.jpg)

Open103Z

Name:
:   `waveshare_open103z`

Vendor:
:   Waveshare Electronics

Architecture:
:   arm

SoC:
:   stm32f103xe

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/waveshare/open103z/doc/index.rst/../..)

## Overview

The Waveshare Open103Z-64 is a development board equipped with STM32F103ZE MCU.

## Hardware

The Waveshare Open103Z provides the following hardware components:

![../../../../_images/waveshare_connector.PNG](../../../../_images/waveshare_connector.PNG)
![../../../../_images/waveshare_connector_list.PNG](../../../../_images/waveshare_connector_list.PNG)

### Supported Features

The `waveshare_open103z` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `waveshare_open103z` board configuration can be built and
flashed in the usual way.

### Flashing

Build and flash applications as usual. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b waveshare_open103z samples/hello_world
west flash
```

### Debugging

Debug applications as usual. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b waveshare_open103z samples/hello_world
west debug
```

## References
