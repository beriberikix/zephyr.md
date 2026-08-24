---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/gd/gd32vf103c_starter/doc/index.html
original_path: boards/gd/gd32vf103c_starter/doc/index.html
---

# GD32VF103C-STARTER

Board Overview

[![../../../../_images/gd32vf103c_starter.jpg](https://docs.zephyrproject.org/4.2.0/_images/gd32vf103c_starter.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/gd32vf103c_starter.jpg)

GD32VF103C-STARTER

Name:
:   `gd32vf103c_starter`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   riscv

SoC:
:   gd32vf103

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32vf103c_starter/doc/index.rst/../..)

## Overview

The GD32VF103C-STARTER board is a hardware platform that enables prototyping
on GD32VF103CB RISC-V MCU.

The GD32VF103CB features a single-core RISC-V 32-bit MCU which can run up
to 108 MHz with flash accesses zero wait states, 128 KiB of Flash, 32 KiB of
SRAM and 37 GPIOs.

## Hardware

- GD32VF103CBT6 MCU
- 1 x User LEDs
- 1 x USART (USB port with CH340E)
- USB FS connector
- GD-Link on board programmer
- J-Link/JTAG connector

For more information about the GD32VF103 SoC and GD32VF103C-STARTER board:

- [GigaDevice RISC-V Mainstream SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/risc-v/mainstream-line/)
- [GD32VF103 Datasheet](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103 User Manual](http://www.gd32mcu.com/download/down/document_id/222/path_type/1)
- [GD32VF103C-STARTER Documents](https://github.com/riscv-mcu/GD32VF103_Demo_Suites/tree/master/GD32VF103C_START_Demo_Suites/Docs)

### Supported Features

The `gd32vf103c_starter` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32vf103c_starter/gd32vf103` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Nuclei Bumblebee RISC-V Core[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L24) | [`nuclei,bumblebee`](../../../../build/dts/api/bindings/cpu/nuclei,bumblebee.md#std-dtcompatible-nuclei-bumblebee) |
| ADC | on-chip | GigaDevice GD32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L136) | [`gd,gd32-adc`](../../../../build/dts/api/bindings/adc/gd,gd32-adc.md#std-dtcompatible-gd-gd32-adc) |
| Clock control | on-chip | Gigadevice RCU - Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L64) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd,gd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L332)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L297) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd,gd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L158) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd,gd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L405) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd,gd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L77) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd,gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L246)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L276) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd,gd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigaDevice GD32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L168) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd,gd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | Nuclei ECLIC interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L51) | [`nuclei,eclic`](../../../../build/dts/api/bindings/interrupt-controller/nuclei,eclic.md#std-dtcompatible-nuclei-eclic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L210) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd,gd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L41) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice RCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L59) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd,gd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L83) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd,gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| Pin control | on-chip | GD32 AFIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L203) | [`gd,gd32-afio`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-afio.md#std-dtcompatible-gd-gd32-afio) |
| on-chip | GD32 Pin Controller (AFIO Model)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L239) | [`gd,gd32-pinctrl-afio`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L342)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L308) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd,gd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice RCU - Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L70) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd,gd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L91)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L100) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd,gd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SPI | on-chip | GigaDevice GD32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L181) | [`gd,gd32-spi`](../../../../build/dts/api/bindings/spi/gd,gd32-spi.md#std-dtcompatible-gd-gd32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L32) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Nuclei System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L43) | [`nuclei,systimer`](../../../../build/dts/api/bindings/timer/nuclei,systimer.md#std-dtcompatible-nuclei-systimer) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L224) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L230) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32VF103C-STARTER board has one serial communications port.
TX connected at PA9 and RX at PA10.

## Programming and Debugging

The `gd32vf103c_starter` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Before programming your board make sure to configure boot and serial jumpers
as follows:

- JP2/3: Select 2-3 for both (boot from user memory)
- JP5/6: Select 1-2 positions (labeled as `USART0`)

### Using GD-Link

The GD32VF103C-STARTER includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a JTAG header
(JP1) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32vf103c_starter samples/hello_world
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
   west build -b gd32vf103c_starter samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32vf103c\_starter” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32vf103c_starter samples/hello_world
   west debug
   ```
