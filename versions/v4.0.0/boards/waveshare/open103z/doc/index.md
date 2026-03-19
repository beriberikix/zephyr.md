---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/waveshare/open103z/doc/index.html
original_path: boards/waveshare/open103z/doc/index.html
---

# Open103Z

Board Overview

[![../../../../_images/waveshare_open103z.jpg](../../../../_images/waveshare_open103z.jpg)
](../../../../_images/waveshare_open103z.jpg)

Open103Z

Vendor:
:   Waveshare Electronics

Architecture:
:   arm

SoC:
:   stm32f103xe

## Overview

The Waveshare Open103Z-64 is a development board equipped with STM32F103ZE MCU.

## Hardware

The Waveshare Open103Z provides the following hardware components:

![../../../../_images/waveshare_connector.PNG](../../../../_images/waveshare_connector.PNG)
![../../../../_images/waveshare_connector_list.PNG](../../../../_images/waveshare_connector_list.PNG)

### Supported Features

The Waveshare Open103Z configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| ADC | on-chip | adc |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| FLASH | on-chip | flash |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| CAN | on-chip | can (disabled by default) |
| USB | on-chip | usb |

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
