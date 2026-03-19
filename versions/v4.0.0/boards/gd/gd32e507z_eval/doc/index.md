---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gd/gd32e507z_eval/doc/index.html
original_path: boards/gd/gd32e507z_eval/doc/index.html
---

# GD32E507Z-EVAL

Board Overview

[![../../../../_images/gd32e507z_eval.webp](../../../../_images/gd32e507z_eval.webp)
](../../../../_images/gd32e507z_eval.webp)

GD32E507Z-EVAL

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32e507

## Overview

The GD32E507Z-EVAL board is a hardware platform that enables prototyping
on GD32E507ZE Cortex-M33 High Performance MCU.

The GD32E507ZE features a single-core ARM Cortex-M33 MCU which can run up
to 180 MHz with flash accesses zero wait states, 512kiB of Flash, 128kiB of
SRAM and 112 GPIOs.

## Hardware

- GD32E507ZET6 MCU
- AT24C02C 2Kb EEPROM
- GD25Q16 16Mbit SPI and QSPI NOR Flash
- GD9FU1G8F2A 1Gbit NAND Flash
- Micron MT48LC16M16A2P-6AIT 256Mbit SDRAM
- 4 x User LEDs
- 1 x Joystick (L/R/U/D/C)
- 1 x USART (connected to USB VCOM at J1 connector)
- 1 x POT connected to an ADC input
- Headphone interface
- USB FS connector
- 1 x CAN (includes SN65HVD230 PHY)
- Ethernet Interface
- 3.2” RGB-LCD (320x240)
- GD-Link on board programmer
- J-Link/JTAG connector

For more information about the GD32E507 SoC and GD32E507Z-EVAL board:

- [GigaDevice Cortex-M33 High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m33/high-performance-line/)
- [GD32E507X Datasheet](https://gd32mcu.com/download/down/document_id/252/path_type/1)
- [GD32E50X User Manual](https://www.gd32mcu.com/download/down/document_id/249/path_type/1)
- [GD32E507Z-EVAL User Manual](https://www.gd32mcu.com/data/documents/evaluationBoard/GD32E50x_Demo_Suites_V1.2.1.rar)

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

### Serial Port

The GD32E507Z-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10. USART0 is exposed as a
virtual COM port via the J1 USB connector.

## Programming and Debugging

Before programming your board make sure to configure boot jumpers as
follows:

- JP3/4: Select 2-3 for both (boot from user memory)

### Using GD-Link or J-Link

The board comes with an embedded GD-Link programmer. It can be used with pyOCD
provided you install the necessary CMSIS-Pack:

```shell
pyocd pack install gd32e507ze
```

J-Link can also be used to program the board using the JTAG interface exposed in
the JP2 header.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32e507z_eval samples/hello_world
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
   west build -b gd32e507z_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32e507z\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32e507z_eval samples/hello_world
   west debug
   ```
