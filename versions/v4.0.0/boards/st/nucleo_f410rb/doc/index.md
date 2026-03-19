---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_f410rb/doc/index.html
original_path: boards/st/nucleo_f410rb/doc/index.html
---

# Nucleo F410RB

Board Overview

[![../../../../_images/nucleo_f410rb.jpg](../../../../_images/nucleo_f410rb.jpg)
](../../../../_images/nucleo_f410rb.jpg)

Nucleo F410RB

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f410rx

## Overview

The Nucleo F410RB board features an ARM Cortex-M4 based STM32F410RB MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F410RB board:

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

More information about the board can be found at the [Nucleo F410RB website](https://www.st.com/en/evaluation-tools/nucleo-F410RB.html).

## Hardware

Nucleo F410RB provides the following hardware components:

- STM32F410RBT6 in LQFP64 package
- ARM® 32-bit Cortex®-M4 CPU with FPU
- Adaptive real-time accelerator (ART Accelerator)
- 100 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 128 KB Flash
- 32 KB SRAM
- General purpose timer (4)
- Low-power timer (1)
- Advanced-control timer (1)
- Random number generator (TRNG for HW entropy)
- SPI/I2S (3)
- I2C (3)
- USART (3)
- GPIO (50) with external interrupt capability
- 12-bit ADC with 16 channels
- 12-bit DAC with 1 channel
- RTC

More information about STM32F410RB can be found here:

- [STM32F410RB on www.st.com](https://www.st.com/en/microcontrollers/stm32f410rb.html)
- [STM32F410 reference manual](https://www.st.com/resource/en/reference_manual/dm00180366.pdf)

### Supported Features

The Zephyr nucleo\_f410rb board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| I2C | on-chip | i2c |
| I2S | on-chip | i2s |
| SPI | on-chip | spi |
| ADC | on-chip | ADC Controller |
| DAC | on-chip | DAC Controller |
| WATCHDOG | on-chip | window & independent |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in
[boards/st/nucleo\_f410rb/nucleo\_f410rb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f410rb/nucleo_f410rb_defconfig)

### Connections and IOs

Nucleo F410RB Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo F410RB Arduino connectors (top left)](../../../../_images/nucleo_f410rb_arduino_top_left.jpg)
![Nucleo F410RB Arduino connectors (top right)](../../../../_images/nucleo_f410rb_arduino_top_right.jpg)
![Nucleo F410RB Morpho connectors (top left)](../../../../_images/nucleo_f410rb_morpho_top_left.jpg)
![Nucleo F410RB Morpho connectors (top right)](../../../../_images/nucleo_f410rb_morpho_top_right.jpg)

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

#### System Clock

Nucleo F410RB System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default, the System clock is driven by the PLL clock at 84MHz,
driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo F410RB board has 3 USARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

Nucleo F410RB board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f410rb` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F410RB

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_f410rb samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f410rb samples/hello_world
west debug
```
