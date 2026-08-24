---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/gd/gd32f470i_eval/doc/index.html
original_path: boards/gd/gd32f470i_eval/doc/index.html
---

# GD32F470I-EVAL

Board Overview

[![../../../../_images/gd32f470i_eval.jpg](https://docs.zephyrproject.org/4.2.0/_images/gd32f470i_eval.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/gd32f470i_eval.jpg)

GD32F470I-EVAL

Name:
:   `gd32f470i_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f470

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f470i_eval/doc/index.rst/../..)

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

The `gd32f470i_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32f470i_eval/gd32f470` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | GigaDevice GD32 ADC[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L225) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd,gd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L44) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd,gd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L408)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L390) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd,gd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L143) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd,gd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller with FIFO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L620) | [`gd,gd32-dma-v1`](../../../../build/dts/api/bindings/dma/gd,gd32-dma-v1.md#std-dtcompatible-gd-gd32-dma-v1) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L57) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd,gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L299)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L329) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd,gd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigaDevice GD32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L153)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L166) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd,gd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f470i_eval/gd32f470i_eval.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L264) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd,gd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f470i_eval/gd32f470i_eval.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f470i_eval/gd32f470i_eval.dts?plain=1#L59) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L39) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd,gd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| Miscellaneous | on-chip | GigaDevice GD32 System Configuration Registers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L258) | [`gd,gd32-syscfg`](../../../../build/dts/api/bindings/misc/gd,gd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L26) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L64) | [`gd,gd32-nv-flash-v3`](../../../../build/dts/api/bindings/mtd/gd,gd32-nv-flash-v3.md#std-dtcompatible-gd-gd32-nv-flash-v3) |
| on-board | I2C EEPROMs compatible with Atmel’s AT24 family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f470i_eval/gd32f470i_eval.dts?plain=1#L134) | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel,at24.md#std-dtcompatible-atmel-at24) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f470i_eval/gd32f470i_eval.dts?plain=1#L151) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | GD32 Pin Controller (AF Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L292) | [`gd,gd32-pinctrl-af`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L419)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L401) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd,gd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L50) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd,gd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L71)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L80) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd,gd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f450.dtsi?plain=1#L34)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L192) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd,gd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L34) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L277) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L283) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32F470I-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

The `gd32f470i_eval` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

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
