---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32f350r_eval/doc/index.html
original_path: boards/gd/gd32f350r_eval/doc/index.html
---

# GD32F350R-EVAL

Board Overview

[![../../../../_images/gd32f350r_eval.webp](https://docs.zephyrproject.org/4.1.0/_images/gd32f350r_eval.webp)
](https://docs.zephyrproject.org/4.1.0/_images/gd32f350r_eval.webp)

GD32F350R-EVAL

Name:
:   `gd32f350r_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f350

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f350r_eval/doc/index.rst/../..)

## Overview

The GD32F350R-EVAL board is a hardware platform that enables design and debug
of the GigaDevice F350 Cortex-M4F High Performance MCU.

The GD32F350RBT6 features a single-core ARM Cortex-M4F MCU which can run up
to 108-MHz with flash accesses zero wait states, 128kB of Flash, 16kB of
SRAM and 55 GPIOs.

## Hardware

- GD32F350RBT6 MCU
- AT24C02C 2Kb EEPROM
- 4 x User LEDs
- 4 x User Push buttons
- 1 x USART (RS-232 at J2 connector)
- 1 x POT connected to an ADC input
- Headphone interface
- Micro SD Card Interface
- 2.4’’ TFT-LCD (36x48)
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32F350 SoC and GD32F350R-EVAL board:

- [GigaDevice Cortex-M4F Stretch Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/)
- [GD32F350xx Datasheet](http://gd32mcu.com/download/down/document_id/133/path_type/1)
- [GD32F3x0 User Manual](http://gd32mcu.com/download/down/document_id/136/path_type/1)
- [GD32F350R-EVAL User Manual](https://www.tme.com/Document/ff0a3609934053c07d78ef8662781da9/GD32350R-EVAL%20User%20Manual-V1.0.pdf)

### Supported Features

The `gd32f350r_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32f350r_eval/gd32f350` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | GigaDevice GD32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L83) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd,gd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L37) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd,gd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f350.dtsi?plain=1#L12) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd,gd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L95) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd,gd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L50) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd,gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L127) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd,gd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| Multi-Function Device | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L32) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd,gd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L57) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd,gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | The GD32 pin controller (AF model) is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L120) | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| Reset controller | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L43) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd,gd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L65)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L74) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd,gd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L105) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L111) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32F350R-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

Before programming your board make sure to configure boot and serial jumpers as follows:

- J4: Select 2-3 for both (labeled as `L`)
- J13: Select 1-2 position (labeled as `USART`)

### Using GD-Link

The GD32F350R-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
(J3) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f350r_eval samples/hello_world
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
   west build -b gd32f350r_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32f350r\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32f350r_eval samples/hello_world
   west debug
   ```
