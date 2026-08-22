---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sipeed/longan_nano/doc/index.html
original_path: boards/sipeed/longan_nano/doc/index.html
---

# Longan Nano

Board Overview

[![../../../../_images/longan_nano.jpg](../../../../_images/longan_nano.jpg)
](../../../../_images/longan_nano.jpg)

Longan Nano

Name:
:   `longan_nano`

Vendor:
:   Shenzhen Sipeed Technology Co., Ltd.

Architecture:
:   riscv

SoC:
:   gd32vf103

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sipeed/longan_nano/doc/index.rst/../..)

## Overview

The Sipeed Longan Nano and Longan Nano Lite is an simple and tiny development board with
an GigaDevice GD32VF103 SoC that based on N200 RISC-V IP core by Nuclei system technology.
More information can be found on:

- [Sipeed Longan website](https://longan.sipeed.com/en/)
- [GD32VF103 datasheet](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103 user manual](https://www.gd32mcu.com/data/documents/userManual/GD32VF103_User_Manual_Rev1.4.pdf)
- [Nuclei website](https://www.nucleisys.com/download.php)
- [Nuclei Bumblebee core documents](https://github.com/nucleisys/Bumblebee_Core_Doc)
- [Nuclei ISA Spec](https://doc.nucleisys.com/nuclei_spec/)

## Hardware

- 4 x universal 16-bit timer
- 2 x basic 16-bit timer
- 1 x advanced 16-bit timer
- Watchdog timer
- RTC
- Systick
- 3 x USART
- 2 x I2C
- 3 x SPI
- 2 x I2S
- 2 x CAN
- 1 x USBFS(OTG)
- 2 x ADC(10 channel)
- 2 x DAC

### Supported Features

The `longan_nano` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `longan_nano/gd32vf103` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Nuclei Bumblebee RISC-V Core[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L24) | [`nuclei,bumblebee`](../../../../build/dts/api/bindings/cpu/nuclei%2Cbumblebee.md#std-dtcompatible-nuclei-bumblebee) |
| ADC | on-chip | GigaDevice GD32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L136)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L147) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L64) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L315)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L297) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L158) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L82) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix%2Cst7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L405) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L77) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L246)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L276) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigaDevice GD32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L168) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | Nuclei ECLIC interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L51) | [`nuclei,eclic`](../../../../build/dts/api/bindings/interrupt-controller/nuclei%2Ceclic.md#std-dtcompatible-nuclei-eclic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L210) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L59) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L83) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | GD32 AFIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L203) | [`gd,gd32-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-afio.md#std-dtcompatible-gd-gd32-afio) |
| on-chip | GD32 Pin Controller (AFIO Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L239) | [`gd,gd32-pinctrl-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L325)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L308) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L70) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L91)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L100) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L181) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L32) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Nuclei System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L43) | [`nuclei,systimer`](../../../../build/dts/api/bindings/timer/nuclei%2Csystimer.md#std-dtcompatible-nuclei-systimer) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L224) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L230) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

#### `longan_nano/gd32vf103/lite` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Nuclei Bumblebee RISC-V Core[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L24) | [`nuclei,bumblebee`](../../../../build/dts/api/bindings/cpu/nuclei%2Cbumblebee.md#std-dtcompatible-nuclei-bumblebee) |
| ADC | on-chip | GigaDevice GD32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L136)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L147) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd%2Cgd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L64) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd%2Cgd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L315)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L297) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd%2Cgd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L158) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd%2Cgd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L82) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix%2Cst7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L405) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd%2Cgd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L77) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd%2Cgd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L246)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L276) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd%2Cgd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigaDevice GD32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L168) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd%2Cgd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | Nuclei ECLIC interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L51) | [`nuclei,eclic`](../../../../build/dts/api/bindings/interrupt-controller/nuclei%2Ceclic.md#std-dtcompatible-nuclei-eclic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L210) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd%2Cgd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sipeed/longan_nano/longan_nano-common.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L59) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd%2Cgd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L83) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd%2Cgd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | GD32 AFIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L203) | [`gd,gd32-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-afio.md#std-dtcompatible-gd-gd32-afio) |
| on-chip | GD32 Pin Controller (AFIO Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L239) | [`gd,gd32-pinctrl-afio`](../../../../build/dts/api/bindings/pinctrl/gd%2Cgd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L325)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L308) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd%2Cgd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L70) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd%2Cgd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L91)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L100) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L181) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd%2Cgd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L32) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Nuclei System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L43) | [`nuclei,systimer`](../../../../build/dts/api/bindings/timer/nuclei%2Csystimer.md#std-dtcompatible-nuclei-systimer) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L224) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L230) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd%2Cgd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

The microSD card reader in Longan Nano board is connected to SPI1.

### Serial Port

USART0 is on the opposite end of the USB.
Connect to TX0 (PA9) and RX0 (PA10).

## Programming and debugging

The `longan_nano` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **dfu-util** | ✅ |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Building & Flashing

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west flash
```

When using a custom toolchain it should be enough to have the downloaded
version of the binary in your `PATH`.

The default runner tries to flash the board via an external programmer using openocd.
To flash via the USB port, select the DFU runner when flashing:

```shell
west flash --runner dfu-util
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west debug
```
