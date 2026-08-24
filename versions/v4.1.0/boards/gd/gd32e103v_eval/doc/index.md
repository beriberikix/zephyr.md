---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32e103v_eval/doc/index.html
original_path: boards/gd/gd32e103v_eval/doc/index.html
---

# GD32E103V-EVAL

Board Overview

[![../../../../_images/gd32e103v_eval.jpg](https://docs.zephyrproject.org/4.1.0/_images/gd32e103v_eval.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/gd32e103v_eval.jpg)

GD32E103V-EVAL

Name:
:   `gd32e103v_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32e103

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32e103v_eval/doc/index.rst/../..)

## Overview

The GD32E103V-EVAL board is a hardware platform that enables design and debug
of the GigaDevice E103 Cortex-M4F High Performance MCU.

The GD32E103VB features a single-core ARM Cortex-M4F MCU which can run up
to 120-MHz with flash accesses zero wait states, 128kiB of Flash, 32kiB of
SRAM and 80 GPIOs.

## Hardware

- USB interface with mini-USB connector
- 4 user LEDs
- 4 user push buttons
- Reset Button
- ADC connected to a potentiometer
- 2 DAC channels
- GD25Q16 2Mib SPI Flash
- AT24C02C 2KiB EEPROM
- 3.2 TFT LCD (320x240)
- PCM1770 Stereo DAC with Headphone Amplifier
- GD-Link interface

  - CMSIS-DAP swd debug interface over USB HID.
- 2 CAN FD ports

  - This function is not available in this board due to hardware issues, please check `GD32C103` .

For more information about the GD32E103 SoC and GD32E103V-EVAL board:

- [GigaDevice Cortex-M4F High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/value-line/gd32e103-series/)
- [GD32E103 Datasheet](http://www.gd32mcu.com/download/down/document_id/235/path_type/1)
- [GD32E103 Reference Manual](http://www.gd32mcu.com/download/down/document_id/163/path_type/1)
- [GD32E103V Eval Schematics](http://www.gd32mcu.com/download/down/document_id/178/path_type/1)
- [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

### Supported Features

The `gd32e103v_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `gd32e103v_eval/gd32e103` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Clock control | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L39) | [`gd,gd32-cctl`](../../../../build/dts/api/bindings/clock/gd,gd32-cctl.md#std-dtcompatible-gd-gd32-cctl) |
| Counter | on-chip | GigaDevice GD32 timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L240)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L258) | [`gd,gd32-timer`](../../../../build/dts/api/bindings/counter/gd,gd32-timer.md#std-dtcompatible-gd-gd32-timer) |
| DAC | on-chip | GigaDevice GD32 series DAC module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L111) | [`gd,gd32-dac`](../../../../build/dts/api/bindings/dac/gd,gd32-dac.md#std-dtcompatible-gd-gd32-dac) |
| DMA | on-chip | GD32 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L468) | [`gd,gd32-dma`](../../../../build/dts/api/bindings/dma/gd,gd32-dma.md#std-dtcompatible-gd-gd32-dma) |
| Flash controller | on-chip | There are three types GD32 FMC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L52) | [`gd,gd32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/gd,gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller) |
| GPIO & Headers | on-chip | GD32 GPIO node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L189) | [`gd,gd32-gpio`](../../../../build/dts/api/bindings/gpio/gd,gd32-gpio.md#std-dtcompatible-gd-gd32-gpio) |
| I2C | on-chip | GigiDevice GD32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L121)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L134) | [`gd,gd32-i2c`](../../../../build/dts/api/bindings/i2c/gd,gd32-i2c.md#std-dtcompatible-gd-gd32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e103v_eval/gd32e103v_eval.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | GigaDevice External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L154) | [`gd,gd32-exti`](../../../../build/dts/api/bindings/interrupt-controller/gd,gd32-exti.md#std-dtcompatible-gd-gd32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e103v_eval/gd32e103v_eval.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e103v_eval/gd32e103v_eval.dts?plain=1#L63) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Multi-Function Device | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L34) | [`gd,gd32-rcu`](../../../../build/dts/api/bindings/mfd/gd,gd32-rcu.md#std-dtcompatible-gd-gd32-rcu) |
| MTD | on-chip | Flash memory binding of GD32 FMC v1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L58) | [`gd,gd32-nv-flash-v1`](../../../../build/dts/api/bindings/mtd/gd,gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1) |
| on-board | I2C EEPROMs compatible with Atmel’s AT24 family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32e103v_eval/gd32e103v_eval.dts?plain=1#L125) | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel,at24.md#std-dtcompatible-atmel-at24) |
| Pin control | on-chip | The AFIO peripheral is used to configure pin remapping, EXTI sources and, when available, enable the I/O compensation cell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L147) | [`gd,gd32-afio`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-afio.md#std-dtcompatible-gd-gd32-afio) |
| on-chip | The GD32 pin controller (AFIO model) is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L182) | [`gd,gd32-pinctrl-afio`](../../../../build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio) |
| PWM | on-chip | GigaDevice GD32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L251)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L268) | [`gd,gd32-pwm`](../../../../build/dts/api/bindings/pwm/gd,gd32-pwm.md#std-dtcompatible-gd-gd32-pwm) |
| Reset controller | on-chip | Gigadevice Reset and Clock Unit (RCU) if a multi-function peripheral in charge of reset control (RCTL) and clock control (CCTL) for all SoC peripherals[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L45) | [`gd,gd32-rctl`](../../../../build/dts/api/bindings/reset/gd,gd32-rctl.md#std-dtcompatible-gd-gd32-rctl) |
| Serial controller | on-chip | GigaDevice USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L66)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L75) | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd,gd32-usart.md#std-dtcompatible-gd-gd32-usart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L30) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | GD32 free watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L167) | [`gd,gd32-fwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt) |
| on-chip | GD32 window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32e10x/gd32e10x.dtsi?plain=1#L173) | [`gd,gd32-wwdgt`](../../../../build/dts/api/bindings/watchdog/gd,gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt) |

### Serial Port

The GD32E103V-EVAL board has 5 serial communication ports. The default port
is UART0 at PIN-9 and PIN-10.

## Programming and Debugging

Before program your board make sure to configure boot setting and serial port.
The default serial port is USART0. This port uses header JP-5/6 to route
signals between USB VBUS/ID and USART J2.

| Boot-0 | Boot-1 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | SRAM |
| 1-2 | 2-3 | Bootloader |
| 2-3 | Any | Flash |

| JP-5 | JP-6 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | USART0 / J2 |
| 2-3 | 2-3 | USB VBUS/ID |
| open | open | Free |

### Using GD-Link

The GD32E103V-EVAL includes an onboard programmer/debugger (GD-Link) which
allow flash programming and debug over USB. There are also program and debug
headers J1 and J100 that can be used with any ARM compatible tools.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
3. To flash an image:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32e103v\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   west debug
   ```

### Using ROM bootloader

The GD32E103 MCU have a ROM bootloader which allow flash programming. User
should install [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1) software at some Linux path. The recommended
is `$HOME/.local/bin`.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   ```
2. Enable board bootloader:

   - Remove boot-0 jumper
   - press reset button
3. To flash an image:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   west flash -r gd32isp [--port=/dev/ttyUSB0]
   ```
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1

   Press reset button

   You should see “Hello World! gd32e103v\_eval” in your terminal.
