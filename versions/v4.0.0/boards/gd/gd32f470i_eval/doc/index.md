---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gd/gd32f470i_eval/doc/index.html
original_path: boards/gd/gd32f470i_eval/doc/index.html
---

# GD32F470I-EVAL

Board Overview

[![../../../../_images/gd32f470i_eval.jpg](../../../../_images/gd32f470i_eval.jpg)
](../../../../_images/gd32f470i_eval.jpg)

GD32F470I-EVAL

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f470

## Overview

The GD32F470I-EVAL board is a hardware platform that enables prototyping
on GD32F470IK Cortex-M4F Stretch Performance MCU.

The GD32F470IK features a single-core ARM Cortex-M4F MCU which can run up
to 240 MHz with flash accesses zero wait states, 3072kiB of Flash, 256kiB of
SRAM and 140 GPIOs.

## Hardware

- GD32F470IKH6 MCU
- 2Kb EEPROM
- 16Mbit SPI and QSPI NOR Flash
- 256Mbit SDRAM
- 3 x User LEDs
- 3 x User Push buttons
- 1 x USART (RS-232 at J1 connector)
- 1 x POT connected to an ADC input
- Headphone interface
- Micro SD Card Interface
- USB FS connector
- USB HS connector
- 1 x CAN
- Ethernet Interface
- 4.3” LCD (480x272)
- OV2640 Digital Camera
- GD-Link on board programmer
- J-Link/JTAG connector

For more information about the GD32F470 SoC and GD32F470I-EVAL board:

- [GigaDevice Cortex-M4F Stretch Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/gd32f470-series/)
- [GD32F470IKH6 Specifications](https://www.gigadevice.com/microcontroller/gd32f470ikh6/)
- [GD32F470xx Datasheet](https://gd32mcu.com/data/documents/datasheet/GD32F470xx_Datasheet_Rev1.3.pdf)
- [GD32F4xx User Manual](https://gd32mcu.com/data/documents/userManual/GD32F4xx_User_Manual_Rev2.7.pdf)

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| EXTI | [`CONFIG_GD32_EXTI`](../../../../kconfig.md#CONFIG_GD32_EXTI "CONFIG_GD32_EXTI") | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| NVIC | N/A | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| PWM | [`CONFIG_PWM`](../../../../kconfig.md#CONFIG_PWM "CONFIG_PWM") | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| SYSTICK | N/A | N/A |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| DAC | [`CONFIG_DAC`](../../../../kconfig.md#CONFIG_DAC "CONFIG_DAC") | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| I2C | [`CONFIG_I2C`](../../../../kconfig.md#CONFIG_I2C "CONFIG_I2C") | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| EEPROM | [`CONFIG_EEPROM`](../../../../kconfig.md#CONFIG_EEPROM "CONFIG_EEPROM") | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel%2Cat24.md#std-dtcompatible-atmel-at24) |
| SPI | [`CONFIG_SPI`](../../../../kconfig.md#CONFIG_SPI "CONFIG_SPI") | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |

### Serial Port

The GD32F470I-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

Before programming your board make sure to configure boot and serial jumpers
as follows:

- J2/3: Select 2-3 for both (boot from user memory)
- J5: Select 1-2 position (labeled as `USART0`)

### Using GD-Link

The GD32F470I-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a JTAG header
(J1) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. On Linux the
   terminal should be something like `/dev/ttyUSB0`. For example:

   ```shell
   minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
3. To flash an image:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32f470i\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   west debug
   ```
