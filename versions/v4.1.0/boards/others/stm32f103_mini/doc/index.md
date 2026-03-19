---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/stm32f103_mini/doc/index.html
original_path: boards/others/stm32f103_mini/doc/index.html
---

# STM32F103 Mini

Board Overview

[![../../../../_images/stm32f103_mini_pin.jpg](../../../../_images/stm32f103_mini_pin.jpg)
](../../../../_images/stm32f103_mini_pin.jpg)

STM32F103 Mini

Name:
:   `stm32f103_mini`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   stm32f103xe

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/stm32f103_mini/doc/index.rst/../..)

## Overview

The STM32F103\_MINI board features an ARM Cortex-M3 based STM32F103RC MCU
with a wide range of connectivity support and configurations. There are
multiple version of this board like `stm32f103_mini`.

![STM32F103 Mini Yellow](../../../../_images/stm32f103_mini_yellow.jpg)
![STM32F103 Mini Blue](../../../../_images/stm32f103_mini_blue.jpg)

## Hardware

STM32F103 Mini provides the following hardware components:

- STM32 microcontroller in QFP64 package
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Power management access point
- Two LEDs:

  - User LED (LD1), power LED (LD2)
- USB re-enumeration capability:

  - Mass storage

More information about STM32F103RC can be found here:

- [STM32F103 reference manual](https://www.st.com/resource/en/reference_manual/cd00171190.pdf) [[1]](#id2)
- [STM32F103 data sheet](https://www.st.com/resource/en/datasheet/stm32f103rc.pdf) [[2]](#id4)

### Supported Features

The `stm32f103_mini` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![Nucleo F103RB connectors](../../../../_images/stm32f103_mini_pin1.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX: PA9/PA10
- UART\_2 TX/RX: PA2/PA3 (ST-Link Virtual COM Port)
- SPI1 NSS/SCK/MISO/MOSI: PA4/PA5/PA6/PA7
- SPI2 NSS/SCK/MISO/MOSI: PB12/PB13/PB14/PB15
- I2C1 SDA/SCL: PB9/PB8
- PWM1\_CH1: PA8
- USER\_PB: PC13
- LD1: PA5
- USB\_DC DM/DP: PA11/PA12

#### System Clock

The on-board 8MHz crystal is used to produce a 72MHz system clock with PLL.

## Programming and Debugging

Applications for the `stm32f103_mini` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

There are 2 main entry points for flashing STM32F1X SoCs, one using the ROM
bootloader, and another by using the SWD debug port (which requires additional
hardware such as ST-Link). Flashing using the ROM bootloader requires a special activation
pattern, which can be triggered by using the BOOT0 pin.

#### Flashing an application to stm32f103 mini

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f103_mini samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f103_mini samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/resource/en/reference\_manual/cd00171190.pdf](https://www.st.com/resource/en/reference_manual/cd00171190.pdf)

[[2](#id5)]

[https://www.st.com/resource/en/datasheet/stm32f103rc.pdf](https://www.st.com/resource/en/datasheet/stm32f103rc.pdf)
