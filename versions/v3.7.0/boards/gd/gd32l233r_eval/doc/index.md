---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/gd/gd32l233r_eval/doc/index.html
original_path: boards/gd/gd32l233r_eval/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# GigaDevice GD32L233R-EVA

## Overview

The GD32L233R-EVAL board is a hardware platform that enables design and debug
of the GigaDevice GD32L233 Cortex-M23 Low Power MCU.

The GD32RCT6 features a single-core ARM Cortex-M4F MCU which can run up
to 64-MHz with flash accesses zero wait states, 256kB of Flash, 32kB of
SRAM and 59 GPIOs.

![gd32l233r_eval](../../../../_images/gd32l233r_eval.jpg)

## Hardware

- GD32L233RCT6 MCU
- AT24C02C 2Kb EEPROM
- 4 x User LEDs
- 2 x User Push buttons
- 1 x USART (Mini-USB)
- 1 x POT connected to an ADC input
- Headphone interface
- SLCD segment code screen
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32L233 SoC and GD32L233R-EVAL board:

- [GigaDevice Cortex-M23 Low Power SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m23/low-power-line/)
- [GD32L233xx Datasheet](https://gd32mcu.com/download/down/document_id/289/path_type/1)
- [GD32L23x User Manual](https://gd32mcu.com/download/down/document_id/293/path_type/1)
- [GD32L23x Demo Suites](https://gd32mcu.com/download/down/document_id/292/path_type/1)

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| EXTI | [`CONFIG_GD32_EXTI`](../../../../kconfig.md#CONFIG_GD32_EXTI "CONFIG_GD32_EXTI") | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| NVIC | N/A | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| SYSTICK | N/A | N/A |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| PINMUX | [`CONFIG_PINCTRL`](../../../../kconfig.md#CONFIG_PINCTRL "CONFIG_PINCTRL") | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| ADC | [`CONFIG_ADC`](../../../../kconfig.md#CONFIG_ADC "CONFIG_ADC") | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |

### Serial Port

The GD32L233R-EVAL board has one serial communication port. The default port
is USART1 with TX connected at PA2 and RX at PA3. USART1 have connect to a
CH04E serial connector with Mini-USB.

## Programming and Debugging

### Using J-Link

The GD32L233R-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
which can be used with tools like Segger J-Link(latest version required).

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello-world) sample application:

   ```shell
   west build -b gd32l233r_eval samples/hello_world
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
   west build -b gd32l233r_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32l233r\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32l233r_eval samples/hello_world
   west debug
   ```
