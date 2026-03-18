---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_g070rb/doc/index.html
original_path: boards/st/nucleo_g070rb/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo G070RB

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

![Nucleo G070RB](../../../../_images/nucleo_g070rb.jpg)

More information about the board can be found at the [Nucleo G070RB website](https://www.st.com/en/evaluation-tools/nucleo-g070rb.html) [[1]](#id1).

## Hardware

Nucleo G070RB provides the following hardware components:

- STM32 microcontroller in LQFP64 package
- Two types of extension resources:

  - Arduino\* Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- ARM\* mbed\*
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
- Support of wide choice of Integrated Development Environments (IDEs) including:

  - IAR
  - ARM Keil
  - GCC-based IDEs

More information about STM32G070RB can be found here:

- [G070RB on www.st.com](https://www.st.com/en/microcontrollers/stm32g070rb.html) [[3]](#id5)

### Supported Features

The Zephyr nucleo\_g070rb board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | arm memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| COUNTER | on-chip | rtc |
| WATCHDOG | on-chip | independent watchdog |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| die-temp | on-chip | die temperature sensor |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_g070rb/nucleo\_g070rb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g070rb/nucleo_g070rb_defconfig)

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

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00452640.pdf) [[2]](#id3).

## Programming and Debugging

Applications for the `nucleo_g070rb` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo G070RB board includes an ST-LINK/V2-1 embedded debug tool interface.

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
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g070rb samples/hello_world
west debug
```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/nucleo-g070rb.html](https://www.st.com/en/evaluation-tools/nucleo-g070rb.html)

[[2](#id4)]

[https://www.st.com/resource/en/user\_manual/dm00452640.pdf](https://www.st.com/resource/en/user_manual/dm00452640.pdf)

[[3](#id6)]

[https://www.st.com/en/microcontrollers/stm32g070rb.html](https://www.st.com/en/microcontrollers/stm32g070rb.html)
