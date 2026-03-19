---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/gd/gd32e507v_start/doc/index.html
original_path: boards/gd/gd32e507v_start/doc/index.html
---

# GD32E507V-START

Board Overview

[![../../../../_images/gd32e507v_start.jpg](../../../../_images/gd32e507v_start.jpg)
](../../../../_images/gd32e507v_start.jpg)

GD32E507V-START

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32e507

## Overview

The GD32E507V-START board is a hardware platform that enables prototyping
on GD32E507VE Cortex-M33 High Performance MCU.

The GD32E507VE features a single-core ARM Cortex-M33 MCU which can run up
to 180 MHz with flash accesses zero wait states, 512kiB of Flash, 128kiB of
SRAM and 80 GPIOs.

## Hardware

- GD32E507VET6 MCU
- 1 x User LEDs
- 1 x User Push buttons
- 1 x USART (RS-232 at J1 connector)
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32E507 SoC and GD32E507V-START board:

- [GigaDevice Cortex-M33 High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m33/high-performance-line/)
- [GD32E507X Datasheet](https://gd32mcu.com/download/down/document_id/252/path_type/1)
- [GD32E50X User Manual](https://www.gd32mcu.com/download/down/document_id/249/path_type/1)
- [GD32E507V-START User Manual](https://www.gd32mcu.com/data/documents/evaluationBoard/GD32E50x_Demo_Suites_V1.2.1.rar)

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

The GD32E507V-START board has one serial communication port. The default port
is USART0 with TX connected at PB6 and RX at PB7. USART0 is exposed as a
virtual COM port via the CN3 USB connector.

## Programming and Debugging

Before programming your board make sure to configure boot jumpers as
follows:

- JP3/4: Select 2-3 for both (boot from user memory)

### Using GD-Link or J-Link

The board comes with an embedded GD-Link programmer. It can be used with pyOCD
provided you install the necessary CMSIS-Pack:

```shell
pyocd pack install gd32e507ve
```

J-Link can also be used to program the board using the SWD interface exposed in
the JP1 header.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32e507v_start samples/hello_world
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
   west build -b gd32e507v_start samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32e507v\_start” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32e507v_start samples/hello_world
   west debug
   ```
