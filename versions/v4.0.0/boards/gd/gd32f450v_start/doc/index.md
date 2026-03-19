---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gd/gd32f450v_start/doc/index.html
original_path: boards/gd/gd32f450v_start/doc/index.html
---

# GD32F450V-START

Board Overview

[![../../../../_images/gd32f450v_start.webp](../../../../_images/gd32f450v_start.webp)
](../../../../_images/gd32f450v_start.webp)

GD32F450V-START

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f450

## Overview

The GD32F450V-START board is a hardware platform that enables prototyping
on GD32F450VK Cortex-M4F Stretch Performance MCU.

The GD32F450VK features a single-core ARM Cortex-M4F MCU which can run up
to 200 MHz with flash accesses zero wait states, 3072kiB of Flash, 256kiB of
SRAM and 82 GPIOs.

## Hardware

- GD32F450VKT6 MCU
- 1 x User LEDs
- 1 x User Push buttons
- USB FS/HS connectors
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32F450 SoC and GD32F450V-START board:

- [GigaDevice Cortex-M4F Stretch Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/)
- [GD32F450X Datasheet](https://gd32mcu.com/data/documents/datasheet/GD32F450xx_Datasheet_Rev2.3.pdf)
- [GD32F4XX User Manual](https://www.gigadevice.com/manual/gd32f450xxxx-user-manual/)
- [GD32F450V-START User Manual](https://gd32mcu.com/data/documents/evaluationBoard/GD32F4xx_Demo_Suites_V2.6.1.rar)

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| EXTI | [`CONFIG_GD32_EXTI`](../../../../kconfig.md#CONFIG_GD32_EXTI "CONFIG_GD32_EXTI") | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| NVIC | N/A | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| PWM | [`CONFIG_PWM`](../../../../kconfig.md#CONFIG_PWM "CONFIG_PWM") | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| SYSTICK | N/A | N/A |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |

Other peripherals may be used if shields are connected to the board.

### Serial Port

The GD32F450V-START board has no exposed serial communication port. The board
provides default configuration for USART0 with TX connected at PB6 and RX at
PB7. PB6/PB7 are exposed in JP6, so you can solder a connector and use a
UART-USB adapter.

## Programming and Debugging

Before programming your board make sure to configure boot jumpers as
follows:

- JP2/3: Select 2-3 for both (boot from user memory)

### Using GD-Link

The GD32F450V-START includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
(JP100) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f450v_start samples/hello_world
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
   west build -b gd32f450v_start samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32f450v\_start” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32f450v_start samples/hello_world
   west debug
   ```
