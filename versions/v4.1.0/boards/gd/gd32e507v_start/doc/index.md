---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32e507v_start/doc/index.html
original_path: boards/gd/gd32e507v_start/doc/index.html
---

# GD32E507V-START

Board Overview

[![../../../../_images/gd32e507v_start.jpg](../../../../_images/gd32e507v_start.jpg)
](../../../../_images/gd32e507v_start.jpg)

GD32E507V-START

Name:
:   `gd32e507v_start`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32e507

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32e507v_start/doc/index.rst/../..)

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

The `gd32e507v_start` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32e507v_start/gd32e507` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L20) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| Clock control | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L39) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L332)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L296) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L134) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L406) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L52) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L225)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L235) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigiDevice GD32 I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L144) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e507v_start/gd32e507v_start.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L183) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e507v_start/gd32e507v_start.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e507v_start/gd32e507v_start.dts?plain=1#L40) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L34) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L74) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L59) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | The AFIO peripheral is used to configure pin remapping, EXTI sources and, when available, enable the I/O compensation cell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L196) | [`gd,gd32-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-afio.md#std-dtcompatible-gd-gd32-afio) |
| on-chip | The GD32 pin controller (AFIO model) is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L218) | [`gd,gd32-pinctrl-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L342)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L307) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L45) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L79)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L88) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L30) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L203) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e50x/gd32e50x.dtsi?plain=1#L209) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

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
