---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nucleo_f446re/doc/index.html
original_path: boards/arm/nucleo_f446re/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST Nucleo F446RE

## Overview

The Nucleo F446RE board features an ARM Cortex-M4 based STM32F446RE MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F446RE board:

- STM32 microcontroller in QFP64 package
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs: USB communication (LD1), user LED (LD2), power LED (LD3)
- Two push-buttons: USER and RESET

![Nucleo F446RE](../../../../_images/nucleo_f446re.jpg)

More information about the board can be found at the [Nucleo F446RE website](https://www.st.com/en/evaluation-tools/nucleo-f446re.html).

## Hardware

Nucleo F446RE provides the following hardware components:

- STM32F446RET6 in LQFP64 package
- ARM® 32-bit Cortex®-M4 CPU with FPU
- Adaptive real-time accelerator (ART Accelerator)
- 180 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 512 KB Flash
- 128 KB SRAM
- 10 General purpose timers
- 2 Advanced control timers
- 2 basic timers
- SPI(4)
- I2C(3)
- USART(4)
- UART(2)
- USB OTG Full Speed and High Speed
- CAN(2)
- SAI(2)
- SPDIF\_Rx(1)
- HDMI\_CEC(1)
- Quad SPI(1)
- Camera Interface
- GPIO(50) with external interrupt capability
- 12-bit ADC(3) with 16 channels
- 12-bit DAC with 2 channels

More information about STM32F446RE can be found here:

- [STM32F446RE on www.st.com](https://www.st.com/en/microcontrollers/stm32f446re.html)
- [STM32F446 reference manual](https://www.st.com/resource/en/reference_manual/dm00135183.pdf)

### Supported Features

The Zephyr nucleo\_f446re board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| I2C | on-chip | i2c |
| Backup SRAM | on-chip | Backup SRAM |
| CAN 1/2 | on-chip | Controller Area Network |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/nucleo_f446re/nucleo_f446re_defconfig`

### Connections and IOs

Nucleo F446RE Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo F446RE Arduino connectors (top left)](../../../../_images/nucleo_f446re_arduino_top_left.jpg)
![Nucleo F446RE Arduino connectors (top right)](../../../../_images/nucleo_f446re_arduino_top_right.jpg)
![Nucleo F446RE Morpho connectors (top left)](../../../../_images/nucleo_f446re_morpho_top_left.jpg)
![Nucleo F446RE Morpho connectors (top right)](../../../../_images/nucleo_f446re_morpho_top_right.jpg)

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PB6
- UART\_1\_RX : PB7
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- USER\_PB : PC13
- LD2 : PA5
- I2C1\_SDA : PB9
- I2C1\_SCL : PB8
- I2C2\_SDA : PB3
- I2C2\_SCL : PB10
- I2C3\_SDA : PB4
- I2C3\_SCL : PA8

#### System Clock

Nucleo F446RE System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default, the System clock is driven by the PLL clock at 84MHz,
driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo F446RE board has 2 UARTs and 4 USARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB45` jumper on the back side of the board.

#### Controller Area Network

The TX/RX wires connected with D14/D15 of CN5 connector. Thus the board can be
used with [RS485 CAN Shield](https://www.waveshare.com/wiki/RS485_CAN_Shield).

## Programming and Debugging

Applications for the `nucleo_f446re` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo F446RE board includes an ST-LINK/V2-1 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to Nucleo F446RE

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_f446re samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f446re samples/hello_world
west debug
```
