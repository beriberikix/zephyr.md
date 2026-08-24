---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/dev_kits/sltb009a/doc/index.html
original_path: boards/silabs/dev_kits/sltb009a/doc/index.html
---

# EFM32GG12 Thunderboard (SLTB009A)

Board Overview

[![../../../../../_images/sltb009a.jpg](https://docs.zephyrproject.org/4.2.0/_images/sltb009a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sltb009a.jpg)

EFM32GG12 Thunderboard (SLTB009A)

Name:
:   `sltb009a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32gg12b810f1024gm64

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sltb009a/doc/index.rst/../..)

## Overview

The EFM32GG12 Thunderboard Kit (SLTB009A) is an evaluation platform for the
EFM32GG12 Giant Gecko Microcontroller, featuring an ARM Cortex-M4 with FPU,
1024kB flash, and 192kB RAM.

## Hardware

- PDM stereo microphones
- USB connectivity
- On-board Segger J-Link USB debugger
- 2 user buttons and 2 LEDs
- USB C connector

For more information about the WGM160P and SLTB009A board:

- [SLTB009A Website](https://www.silabs.com/development-tools/thunderboard/thunderboard-gg12-kit)
- [SLTB009A User Guide](https://www.silabs.com/documents/public/user-guides/ug371-sltb009a-user-guide.pdf)
- [EFM32GG12 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32gg12-datasheet.pdf)
- [EFM32GG12 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32gg12-rm.pdf)

### Supported Features

The `sltb009a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sltb009a/efm32gg12b810f1024gm64` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L22) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L33) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L156) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L166) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L136) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb009a/sltb009a.dts?plain=1#L47) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb009a/sltb009a.dts?plain=1#L33) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L41) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb009a/sltb009a.dts?plain=1#L139) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L244) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L221) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs,gecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L48) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs,gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L57) | [`silabs,gecko-uart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-uart.md#std-dtcompatible-silabs-gecko-uart) |
| on-chip | Gecko USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L75)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L84) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L120)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L128) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L28) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L228)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg12b.dtsi?plain=1#L236) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The EFM32GG12 MCU has six GPIO controllers (PORTA to PORTF), all of which are
currently enabled for the SLTB009A board.

In the following table, the column **Name** contains pin names. For example, PE1
means pin number 1 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PE12 | GPIO | LED0 |
| PA13 | GPIO | LED1 |
| PD5 | GPIO | Push Button PB0 |
| PD8 | GPIO | Push Button PB1 |
| PE7 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #1 |
| PE6 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #1 |
| PC0 | I2C\_SDA | SENSOR\_I2C\_SDA I2C0\_SDA #1 |
| PC1 | I2C\_SCL | SENSOR\_I2C\_SCL I2C0\_SCL #1 |
| PC4 | I2C\_SDA | SENSOR\_I2C\_SDA I2C1\_SDA #1 |
| PC5 | I2C\_SCL | SENSOR\_I2C\_SCL I2C1\_SCL #1 |

### System Clock

The EFM32GG12 MCU is configured to work at 72 MHz.

### Serial Port

The EFM32GG12 SoC has five USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `sltb009a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLTB009A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLTB009A

Connect the SLTB009A to your host computer using the USB port.

Here is an example to build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sltb009a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! sltb009a
```
