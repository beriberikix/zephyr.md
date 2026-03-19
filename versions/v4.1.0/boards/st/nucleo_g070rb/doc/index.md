---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_g070rb/doc/index.html
original_path: boards/st/nucleo_g070rb/doc/index.html
---

# Nucleo G070RB

Board Overview

[![../../../../_images/nucleo_g070rb.jpg](../../../../_images/nucleo_g070rb.jpg)
](../../../../_images/nucleo_g070rb.jpg)

Nucleo G070RB

Name:
:   `nucleo_g070rb`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g070xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_g070rb/doc/index.rst/../..)

## Overview

The Nucleo G070RB board features an ARM Cortex-M0+ based STM32G070RB MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo G070RB board:

- STM32 microcontroller in QFP64 package
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  > - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  > - Power management access point
- Three LEDs: USB communication (LD1), user LED (LD4), power LED (LD3)
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo G070RB website](https://www.st.com/en/evaluation-tools/nucleo-g070rb.html) [[1]](#id2).

## Hardware

Nucleo G070RB provides the following hardware components:

- STM32 microcontroller in LQFP64 package
- Two types of extension resources:

  - Arduino\* Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:

  - Selection-mode switch to use the kit as a standalone ST-LINK/V2-1
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs:

  - USB communication (LD1), user LED (LD4), power LED (LD3)
- Two push-buttons: USER and RESET
- USB re-enumeration capability. Three different interfaces supported on USB:

  - Virtual COM port
  - Mass storage
  - Debug port

More information about STM32G070RB can be found here:

- [G070RB on www.st.com](https://www.st.com/en/microcontrollers/stm32g070rb.html) [[3]](#id6)

### Supported Features

The `nucleo_g070rb` board supports the hardware features listed below.

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

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PC4/PC5
- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C2 SCL/SDA : PA11/PA12
- SPI1 NSS/SCK/MISO/MOSI : PB0/PA5/PA6/PA7 (Arduino SPI)
- SPI2 NSS/SCK/MISO/MOSI : PB12/PB13/PB14/PB15
- USER\_PB : PC13
- LD4 : PA5
- PWM : PA6
- ADC1 IN0 : PA0
- ADC1 IN1 : PA1
- DAC1\_OUT1 : PA4

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00452640.pdf) [[2]](#id4).

## Programming and Debugging

Nucleo G070RB board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_g070rb` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

#### Flashing an application to Nucleo G070RB

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g070rb samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g070rb samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-g070rb.html](https://www.st.com/en/evaluation-tools/nucleo-g070rb.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/dm00452640.pdf](https://www.st.com/resource/en/user_manual/dm00452640.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers/stm32g070rb.html](https://www.st.com/en/microcontrollers/stm32g070rb.html)

[[4](#id9)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
