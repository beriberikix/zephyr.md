---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/gd/gd32l233r_eval/doc/index.html
original_path: boards/gd/gd32l233r_eval/doc/index.html
---

# GD32L233R-EVA

Board Overview

[![../../../../_images/gd32l233r_eval.jpg](../../../../_images/gd32l233r_eval.jpg)
](../../../../_images/gd32l233r_eval.jpg)

GD32L233R-EVA

Name:
:   `gd32l233r_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32l233

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32l233r_eval/doc/index.rst/../..)

## Overview

The GD32L233R-EVAL board is a hardware platform that enables design and debug
of the GigaDevice GD32L233 Cortex-M23 Low Power MCU.

The GD32RCT6 features a single-core ARM Cortex-M4F MCU which can run up
to 64-MHz with flash accesses zero wait states, 256kB of Flash, 32kB of
SRAM and 59 GPIOs.

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

The `gd32l233r_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32l233r_eval/gd32l233` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M23 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L19) | [`arm,cortex-m23`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m23.md#std-dtcompatible-arm-cortex-m23) |
| ADC | on-chip | GigaDevice GD32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L96) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L37) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L56) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L127) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32l233r_eval/gd32l233r_eval.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L107) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32l233r_eval/gd32l233r_eval.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L32) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| Miscellaneous | on-chip | GigaDevice GD32 System Configuration Registers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L50) | [`gd,gd32-syscfg`](../../../../build/dts/api/bindings/misc/gd%2Cgd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L63) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | GD32 Pin Controller (AF Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L120) | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L43) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L78)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L69) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32l23x/gd32l23x.dtsi?plain=1#L27) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

### Serial Port

The GD32L233R-EVAL board has one serial communication port. The default port
is USART1 with TX connected at PA2 and RX at PA3. USART1 have connect to a
CH04E serial connector with Mini-USB.

## Programming and Debugging

The `gd32l233r_eval` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Using J-Link

The GD32L233R-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
which can be used with tools like Segger J-Link(latest version required).

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

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
