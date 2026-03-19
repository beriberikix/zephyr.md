---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/stm32_min_dev/doc/index.html
original_path: boards/others/stm32_min_dev/doc/index.html
---

# STM32 Minimum Development Board

Board Overview

[![../../../../_images/stm32_min_dev.jpg](../../../../_images/stm32_min_dev.jpg)
](../../../../_images/stm32_min_dev.jpg)

STM32 Minimum Development Board

Name:
:   `stm32_min_dev`

Vendor:
:   Other/Unknown

Architecture:

SoC:
:   stm32f103xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/stm32_min_dev/doc/index.rst/../..)

## Overview

The STM32 Minimum Development Board, is a popular and inexpensive
breadboard-friendly breakout board for the [STM32F103x8](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf) CPU. There
are two variants of the board:

- Blue Pill Board
- Black Pill Board

Zephyr applications can use the [stm32\_min\_dev@blue](mailto:stm32_min_dev%40blue) or [stm32\_min\_dev@black](mailto:stm32_min_dev%40black) board
configuration to use these boards.

As the name suggests, these boards have the bare minimum components required to
power on the CPU. For practical use, you’ll need to add additional components
and circuits using a breadboard, for example.

### Pin Mapping

This port is a starting point for your own customizations and not a complete
port for a specific board. Most of the GPIOs on the STM32 SoC has been exposed
in the external header with silk screen labels that match the SoC’s pin names.

Each board vendor has their own variations in pin mapping on their boards’
external connectors and placement of components. Many vendors use port PC13/PB12
for connecting an LED, so only this device is supported by our Zephyr port.
Additional device support is left for the user to implement.

More information on hooking up peripherals and lengthy how to articles can be
found at [EmbedJournal](https://embedjournal.com/tag/stm32-min-dev/).

The pinout diagram of STM32 Minimum Development Blue Pill board can be seen
below. The Black Pill’s one is similar:

![Pinout for STM32 Minimum Development Blue Pill Board](../../../../_images/stm32_min_dev_pinout_blue.jpg)

Pinout for STM32 Minimum Development Blue Pill Board

### STLinkV2 connection:

The board can be flashed by using STLinkV2 with the following connections.

| Pin | STLINKv2 |
| --- | --- |
| G | GND |
| CLK | Clock |
| IO | SW IO |
| V3 | VCC |

### Boot Configuration

The boot configuration for this board is configured through jumpers on B0 (Boot 0)
and B1 (Boot 1). The pins B0 and B1 are present in between logic 0 and 1 lines. The
silk screen on the PCB reads BX- or BX+ to indicate 0 and 1 logic lines for B0 and B1
respectively.

| Boot 1 | Boot 0 | Boot Mode | Aliasing |
| --- | --- | --- | --- |
| X | 0 | Main Flash Memory | Main flash memory is selected as boot space |
| 0 | 1 | System Memory | System memory is selected as boot space |
| 1 | 1 | Embedded SRAM | Embedded SRAM is selected as boot space |

### Supported Features

The `stm32_min_dev` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX: PA9/PA10
- UART\_2 TX/RX: PA2/PA3
- UART\_3 TX/RX: PB10/PB11
- I2C\_1 SCL/SDA : PB6/PB7
- I2C\_2 SCL/SDA : PB10/PB11
- PWM\_1\_CH1: PA8
- SPI\_1 NSS\_OE/SCK/MISO/MOSI: PA4/PA5/PA6/PA7
- SPI\_2 NSS\_OE/SCK/MISO/MOSI: PB12/PB13/PB14/PB15
- USB\_DC DM/DP: PA11/PA12
- ADC\_1: PA0

#### System Clock

The on-board 8Mhz crystal is used to produce a 72Mhz system clock with PLL.

#### Serial Port

STM32 Minimum Development Board has 3 U(S)ARTs. The Zephyr console output is
assigned to UART\_1. Default settings are 115200 8N1.

#### On-Board LEDs

The board has one on-board LED that is connected to PB12/PC13 on the black/blue
variants respectively.

## Programming and Debugging

Applications for the `stm32_min_dev@(blue|black)` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32_min_dev samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32_min_dev samples/hello_world
west debug
```
