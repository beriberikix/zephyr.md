---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/linkw/doc/index.html
original_path: boards/wch/linkw/doc/index.html
---

# WCH LinkW

Board Overview

[![../../../../_images/linkw.webp](https://docs.zephyrproject.org/4.2.0/_images/linkw.webp)
](https://docs.zephyrproject.org/4.2.0/_images/linkw.webp)

WCH LinkW

Name:
:   `linkw`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v208

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/linkw/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) LinkW hardware provides support for QingKe V4C 32-bit RISC-V
processor and the following devices:

- CLOCK
- GPIO
- NVIC

The board is equipped with two LEDs and two Buttons.
The [WCH webpage on CH32V208](https://www.wch-ic.com/products/CH32V208.html) [[2]](#id4) contains the processor’s manuals.
The [WCH webpage on LinkW](https://www.wch-ic.com/products/WCH-Link.html) [[3]](#id6) contains the LinkW’s schematic.

## Hardware

The QingKe V4C 32-bit RISC-V processor of the WCH LinkW is clocked by an external
32 MHz crystal or the internal 8 MHz oscillator and runs up to 144 MHz.
The CH32V208 SoC Features 4 USART, 4 GPIO ports, 2 SPI, 2 I2C, ADC, RTC,
CAN, 2 USB Device, USB Host, OPA, ETH with PHY, several timers, and BLE 5.3.

### Supported Features

The `linkw` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `linkw/ch32v208` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | WCH QingKe V4C RISC-V MCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4c.dtsi?plain=1#L15) | [`wch,qingke-v4c`](../../../../build/dts/api/bindings/cpu/wch,qingke-v4c.md#std-dtcompatible-wch-qingke-v4c) |
| Clock control | on-chip | WCH CH32V00x Reset and Clock Control (RCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L191) | [`wch,rcc`](../../../../build/dts/api/bindings/clock/wch,rcc.md#std-dtcompatible-wch-rcc) |
| on-chip | WCH CH32V00x HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L16) | [`wch,ch32v00x-hse-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v00x-hse-clock.md#std-dtcompatible-wch-ch32v00x-hse-clock) |
| on-chip | WCH CH32V00x HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L23) | [`wch,ch32v00x-hsi-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v00x-hsi-clock.md#std-dtcompatible-wch-ch32v00x-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L30) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | WCH CH32V20x/30x PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L37) | [`wch,ch32v20x_30x-pll-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v20x_30x-pll-clock.md#std-dtcompatible-wch-ch32v20x_30x-pll-clock) |
| GPIO & Headers | on-chip | WCH CH32V00x General-Purpose Input/Output (GPIO)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L96) | [`wch,gpio`](../../../../build/dts/api/bindings/gpio/wch,gpio.md#std-dtcompatible-wch-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/linkw/linkw.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | WCH CH32V00x Programmable Fast Interrupt Controller (PFIC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4c.dtsi?plain=1#L29) | [`wch,pfic`](../../../../build/dts/api/bindings/interrupt-controller/wch,pfic.md#std-dtcompatible-wch-pfic) |
| on-chip | WCH CH32V003/20x/30x External Interrupt and Event Controller (EXTI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L74) | [`wch,exti`](../../../../build/dts/api/bindings/interrupt-controller/wch,exti.md#std-dtcompatible-wch-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/linkw/linkw.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L57) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | WCH CH32V20x/30x AFIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L89) | [`wch,20x_30x-afio`](../../../../build/dts/api/bindings/pinctrl/wch,20x_30x-afio.md#std-dtcompatible-wch-20x_30x-afio) |
| Serial controller | on-chip | WCH CH32V00x UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L142)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L133) | [`wch,usart`](../../../../build/dts/api/bindings/serial/wch,usart.md#std-dtcompatible-wch-usart) |
| SPI | on-chip | WCH SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L169) | [`wch,spi`](../../../../build/dts/api/bindings/spi/wch,spi.md#std-dtcompatible-wch-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | WCH CH32V00x Systick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4c.dtsi?plain=1#L38) | [`wch,systick`](../../../../build/dts/api/bindings/timer/wch,systick.md#std-dtcompatible-wch-systick) |
| Watchdog | on-chip | WCH Independent Watchdog (IWDG)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v208/ch32v208.dtsi?plain=1#L68) | [`wch,iwdg`](../../../../build/dts/api/bindings/watchdog/wch,iwdg.md#std-dtcompatible-wch-iwdg) |

### Connections and IOs

#### LED

- LED0 = Green Mode LED
- LED1 = Blue Activity LED

#### Button

- SW0 = Mode Select Button (Active Low)
- SW1 = Bootstrap Button (Active High)

## Programming and Debugging

The `linkw` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **minichlink** | ✅ |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `linkw` board target can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer is required since the board
does not have any built-in debug support.

The following pins of the external programmer must be connected to the
following pins on the PCB:

- VCC = VCC
- GND = GND
- SWIO = PA13
- SWCLK = PA14

### Flashing

You can use `minichlink` to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b linkw samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V208.html](https://www.wch-ic.com/products/CH32V208.html)

[[3](#id7)]

[https://www.wch-ic.com/products/WCH-Link.html](https://www.wch-ic.com/products/WCH-Link.html)
