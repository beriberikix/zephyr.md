---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/starter_kits/slstk3400a/doc/index.html
original_path: boards/silabs/starter_kits/slstk3400a/doc/index.html
---

# EFM32 Happy Gecko (SLSTK3400A)

Board Overview

[![../../../../../_images/slstk3400a.jpg](https://docs.zephyrproject.org/4.2.0/_images/slstk3400a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/slstk3400a.jpg)

EFM32 Happy Gecko (SLSTK3400A)

Name:
:   `slstk3400a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32hg322f64

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/slstk3400a/doc/index.rst/../..)

## Overview

The EFM32 Happy Gecko Starter Kit SLSTK3400A contains a MCU from the
EFM32HG family built on ARM® Cortex®-M0+ processor with excellent low
power capabilities.

## Hardware

- Advanced Energy Monitoring system for precise current tracking
- Real-time energy and power profiling
- ARM Cortex M0+ with 64 kB Flash and 8 kB RAM
- 128 X 128 pixel Memory LCD
- 2 user buttons, 2 user LEDs and 2 touch buttons
- 20 pin expansion header
- Silicon Labs Si7021 Relative Humidity/Temperature sensor
- USB device interface
- Integrated SEGGER J-Link USB debugger/emulator with debug out functionality

See these documents for more information

- [EFM32HG Website](https://www.silabs.com/products/mcu/32-bit/efm32-happy-gecko)
- [EFM32HG Datasheet](https://www.silabs.com/documents/public/data-sheets/EFM32HG322.pdf)
- [EFM32HG Reference Manual](https://www.silabs.com/documents/public/reference-manuals/EFM32HG-RM.pdf)
- [SLSTK3400A Website](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-happy-gecko-starter-kit)
- [SLSTK3400A User Guide](https://www.silabs.com/documents/public/user-guides/ug255-stk3400-user-guide.pdf)
- [SLSTK3400A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD2012A-B01-schematic.pdf)

### Supported Features

The `slstk3400a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slstk3400a/efm32hg322f64` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L17) | [`arm,cortex-m0+`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L28) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L79) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L89)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L98) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L69) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3400a/slstk3400a.dts?plain=1#L44) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3400a/slstk3400a.dts?plain=1#L30) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L36) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3400a/slstk3400a.dts?plain=1#L93) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L144) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L52)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L43) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L61) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32hg.dtsi?plain=1#L23) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |

### Connections and IOs

The EFM32HG SoC has six GPIO controllers (PORTA to PORTF), but only three are
currently enabled (PORTB, PORTE and PORTF) for the SLSTK3400A board.

In the following table, the column Name contains Pin names. For example, PF4
means Pin number 4 on PORTF, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PC9 | GPIO | Push Button PB0 |
| PC10 | GPIO | Push Button PB1 |
| PF7 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PF2 | USART0\_TX | USART Console EFM\_BC\_TX U0\_TX #4 |
| PA9 | USART0\_RX | USART Console EFM\_BC\_RX U0\_RX #4 |

### System Clock

The EFM32HG SoC is configured to use the 24 MHz external oscillator on the
board.

### Serial Port

The EFM32HG SoC has two USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART1 is connected to the board controller and is used for the console.

## Programming and Debugging

The `slstk3400a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLSTK3400 includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a Mass Storage and a
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.

#### Flashing an application to EFM32-SLSTK3400A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b slstk3400a samples/hello_world
```

Connect the SLSTK3400A to your host computer using the USB port and
you should see a USB connection that exposes a mass storage device (STK3400)
and a USB Serial Port. Copy the generated `zephyr.bin` in the STK3400 drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you will see this message written to the serial port:

```shell
Hello World! slstk3400a
```
