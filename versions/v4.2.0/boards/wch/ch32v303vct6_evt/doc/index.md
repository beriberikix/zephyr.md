---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/ch32v303vct6_evt/doc/index.html
original_path: boards/wch/ch32v303vct6_evt/doc/index.html
---

# WCH CH32V303VCT6\_EVT

Board Overview

[![../../../../_images/ch32v303vct6_evt.webp](../../../../_images/ch32v303vct6_evt.webp)
](../../../../_images/ch32v303vct6_evt.webp)

WCH CH32V303VCT6\_EVT

Name:
:   `ch32v303vct6_evt`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v303

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/ch32v303vct6_evt/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) CH32V303VCT6-EVT hardware provides support for QingKe V4F 32-bit RISC-V
processor.

The [WCH webpage on CH32V303](https://www.wch-ic.com/products/CH32V303.html) [[2]](#id4) contains
the processor’s information and the datasheet.

## Hardware

The QingKe V4F 32-bit RISC-V processor of the WCH CH32V303VCT6-EVT is clocked by an external
32 MHz crystal or the internal 8 MHz oscillator and runs up to 144 MHz.
The CH32V303 SoC features 8 USART, 4 GPIO ports, 3 SPI, 2 I2C, 2 ADC, RTC,
CAN, USB Host/Device, and 4 OPA.

### Supported Features

The `ch32v303vct6_evt` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ch32v303vct6_evt/ch32v303` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | WCH QingKe V4F RISC-V MCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4f.dtsi?plain=1#L15) | [`wch,qingke-v4f`](../../../../build/dts/api/bindings/cpu/wch%2Cqingke-v4f.md#std-dtcompatible-wch-qingke-v4f) |
| Clock control | on-chip | WCH CH32V00x Reset and Clock Control (RCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L194) | [`wch,rcc`](../../../../build/dts/api/bindings/clock/wch%2Crcc.md#std-dtcompatible-wch-rcc) |
| on-chip | WCH CH32V00x HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L16) | [`wch,ch32v00x-hse-clock`](../../../../build/dts/api/bindings/clock/wch%2Cch32v00x-hse-clock.md#std-dtcompatible-wch-ch32v00x-hse-clock) |
| on-chip | WCH CH32V00x HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L23) | [`wch,ch32v00x-hsi-clock`](../../../../build/dts/api/bindings/clock/wch%2Cch32v00x-hsi-clock.md#std-dtcompatible-wch-ch32v00x-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L30) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | WCH CH32V20x/30x PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L37) | [`wch,ch32v20x_30x-pll-clock`](../../../../build/dts/api/bindings/clock/wch%2Cch32v20x_30x-pll-clock.md#std-dtcompatible-wch-ch32v20x_30x-pll-clock) |
| DMA | on-chip | WCH DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L201) | [`wch,wch-dma`](../../../../build/dts/api/bindings/dma/wch%2Cwch-dma.md#std-dtcompatible-wch-wch-dma) |
| GPIO & Headers | on-chip | WCH CH32V00x General-Purpose Input/Output (GPIO)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L76) | [`wch,gpio`](../../../../build/dts/api/bindings/gpio/wch%2Cgpio.md#std-dtcompatible-wch-gpio) |
| Interrupt controller | on-chip | WCH CH32V00x Programmable Fast Interrupt Controller (PFIC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4f.dtsi?plain=1#L29) | [`wch,pfic`](../../../../build/dts/api/bindings/interrupt-controller/wch%2Cpfic.md#std-dtcompatible-wch-pfic) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L58) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | WCH CH32V20x/30x AFIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L69) | [`wch,20x_30x-afio`](../../../../build/dts/api/bindings/pinctrl/wch%2C20x_30x-afio.md#std-dtcompatible-wch-20x_30x-afio) |
| Serial controller | on-chip | WCH CH32V00x UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L122)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L131) | [`wch,usart`](../../../../build/dts/api/bindings/serial/wch%2Cusart.md#std-dtcompatible-wch-usart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v303/ch32v303.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | WCH CH32V00x Systick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v4f.dtsi?plain=1#L38) | [`wch,systick`](../../../../build/dts/api/bindings/timer/wch%2Csystick.md#std-dtcompatible-wch-systick) |

## Programming and Debugging

Applications for the `ch32v303vct6_evt` board target can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer (like the [WCH LinkE](https://www.wch-ic.com/products/WCH-Link.html) [[3]](#id6)) is required since the board
does not have any built-in debug support.

### Flashing

You can use `minichlink` to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b ch32v303vct6_evt samples/hello_world
west flash
```

### Debugging

This board can be debugged via OpenOCD using the WCH openOCD liberated fork, available at [https://github.com/jnk0le/openocd-wch](https://github.com/jnk0le/openocd-wch).

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V303.html](https://www.wch-ic.com/products/CH32V303.html)

[[3](#id7)]

[https://www.wch-ic.com/products/WCH-Link.html](https://www.wch-ic.com/products/WCH-Link.html)
