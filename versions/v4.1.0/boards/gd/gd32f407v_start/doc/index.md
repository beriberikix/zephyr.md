---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32f407v_start/doc/index.html
original_path: boards/gd/gd32f407v_start/doc/index.html
---

# GD32F407V-START

Board Overview

[![../../../../_images/gd32f407v_start.webp](../../../../_images/gd32f407v_start.webp)
](../../../../_images/gd32f407v_start.webp)

GD32F407V-START

Name:
:   `gd32f407v_start`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f407

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f407v_start/doc/index.rst/../..)

## Overview

The GD32F407V-START board is a hardware platform that enables prototyping
on GD32F407VE Cortex-M4 High Performance MCU.

The GD32F407VE features a single-core ARM Cortex-M4 MCU which can run up
to 168 MHz with flash accesses zero wait states, 3072kiB of Flash, 192kiB of
SRAM and 82 GPIOs.

## Hardware

- GD32F407VET6 MCU
- 1 x User LEDs
- 1 x User Push buttons
- 1 x USART
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32F407 SoC and GD32F407V-START board:

- [GigaDevice Cortex-M4 High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/high-performance-line/)
- [GD32F407X Datasheet](https://gd32mcu.com/data/documents/datasheet/GD32F407xx_Datasheet_Rev2.5.pdf)
- [GD32F40X User Manual](https://gd32mcu.com/data/documents/userManual/GD32F4xx_User_Manual_Rev2.7.pdf)
- [GD32F407V-START User Manual](https://www.gd32mcu.com/data/documents/evaluationBoard/GD32F4xx_Demo_Suites_V2.6.1.rar)

### Supported Features

The `gd32f407v_start` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32f407v_start/gd32f407` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | GigaDevice GD32 ADC[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L225) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L44) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L426)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L390) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L143) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller with FIFO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L620) | [`gd,gd32-dma-v1`](../../../../build/dts/api/bindings/dma/gd%2Cgd32-dma-v1.md#std-dtcompatible-gd-gd32-dma-v1) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L57) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L299)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L309) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigiDevice GD32 I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L153) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f407v_start/gd32f407v_start.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L264) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f407v_start/gd32f407v_start.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f407v_start/gd32f407v_start.dts?plain=1#L39) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L39) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| Miscellaneous | on-chip | GigaDevice GD32 System Configuration Registers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L258) | [`gd,gd32-syscfg`](../../../../build/dts/api/bindings/misc/gd%2Cgd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L26) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L64) | [`gd,gd32-nv-flash-v3`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v3.md#std-dtcompatible-gd-gd32-nv-flash-v3) |
| Pin control | on-chip | The GD32 pin controller (AF model) is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L292) | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L436)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L401) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L50) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L71)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L80) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L192) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L34) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L277) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L283) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32F407V-START board has one serial communication port. The default port
is USART0 with TX connected at PB6 and RX at PB7.

## Programming and Debugging

Before programming your board make sure to configure boot jumpers as
follows:

- JP3/4: Select 2-3 for both (boot from user memory)

### Using GD-Link or J-Link

The board comes with an embedded GD-Link programmer.
You need to install CMSIS-Pack which is required by pyOCD
when programming or debugging by the GD-Link programmer.
Execute the following command to install CMSIS-Pack for GD32F407VK
if not installed yet.

> ```shell
> pyocd pack install gd32f407vk
> ```

Also, J-Link can be used to program the board via the SWD interface
(PA13/SWDIO and PA14/SWCLK in the JP6 header).

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   ```
2. Connect Serial-USB adapter to PB6, PB7, and GND.
3. Run your favorite terminal program to listen for output. On Linux the
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
4. To flash an image:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   west flash
   ```

   When using J-Link, append `--runner jlink` option after `west flash`.

   You should see “Hello World! gd32f407v\_start” in your terminal.
5. To debug an image:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   west debug
   ```

   When using J-Link, append `--runner jlink` option after `west debug`.
