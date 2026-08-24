---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/ch32v006evt/doc/index.html
original_path: boards/wch/ch32v006evt/doc/index.html
---

# WCH CH32V006EVT

Board Overview

[![../../../../_images/ch32v006evt.webp](https://docs.zephyrproject.org/4.2.0/_images/ch32v006evt.webp)
](https://docs.zephyrproject.org/4.2.0/_images/ch32v006evt.webp)

WCH CH32V006EVT

Name:
:   `ch32v006evt`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v006

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/ch32v006evt/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) CH32V006EVT is an evaluation board for the RISC-V based CH32V006K8U6
SOC.

The board is equipped with a power LED, reset button, USB port for power, and
two user LEDs. The [WCH webpage on CH32V006](https://www.wch-ic.com/downloads/CH32V006DS0_PDF.html) [[2]](#id4) contains the processor’s
information and the datasheet.

## Hardware

The QingKe V2C 32-bit RISC-V processor of the WCH CH32V006EVT is clocked by an
external crystal and runs at 48 MHz.

### Supported Features

The `ch32v006evt` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ch32v006evt/ch32v006` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | WCH QingKe V2 RISC-V MCU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2c.dtsi?plain=1#L15) | [`wch,qingke-v2`](../../../../build/dts/api/bindings/cpu/wch,qingke-v2.md#std-dtcompatible-wch-qingke-v2) |
| Clock control | on-chip | WCH CH32V00x Reset and Clock Control (RCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L162) | [`wch,rcc`](../../../../build/dts/api/bindings/clock/wch,rcc.md#std-dtcompatible-wch-rcc) |
| on-chip | WCH CH32V00x HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L18) | [`wch,ch32v00x-hse-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v00x-hse-clock.md#std-dtcompatible-wch-ch32v00x-hse-clock) |
| on-chip | WCH CH32V00x HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L24) | [`wch,ch32v00x-hsi-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v00x-hsi-clock.md#std-dtcompatible-wch-ch32v00x-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L31) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | WCH CH32V00x PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L38) | [`wch,ch32v00x-pll-clock`](../../../../build/dts/api/bindings/clock/wch,ch32v00x-pll-clock.md#std-dtcompatible-wch-ch32v00x-pll-clock) |
| Counter | on-chip | WCH General-purpose Timer (GPTM) for PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L179) | [`wch,gptm`](../../../../build/dts/api/bindings/counter/wch,gptm.md#std-dtcompatible-wch-gptm) |
| DMA | on-chip | WCH DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L169) | [`wch,wch-dma`](../../../../build/dts/api/bindings/dma/wch,wch-dma.md#std-dtcompatible-wch-wch-dma) |
| GPIO & Headers | on-chip | WCH CH32V00x General-Purpose Input/Output (GPIO)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L96) | [`wch,gpio`](../../../../build/dts/api/bindings/gpio/wch,gpio.md#std-dtcompatible-wch-gpio) |
| I2C | on-chip | WCH I2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L133) | [`wch,i2c`](../../../../build/dts/api/bindings/i2c/wch,i2c.md#std-dtcompatible-wch-i2c) |
| Interrupt controller | on-chip | WCH CH32V00x Programmable Fast Interrupt Controller (PFIC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2c.dtsi?plain=1#L29) | [`wch,pfic`](../../../../build/dts/api/bindings/interrupt-controller/wch,pfic.md#std-dtcompatible-wch-pfic) |
| on-chip | WCH CH32V003/20x/30x External Interrupt and Event Controller (EXTI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L75) | [`wch,exti`](../../../../build/dts/api/bindings/interrupt-controller/wch,exti.md#std-dtcompatible-wch-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v006evt/ch32v006evt.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v006evt/ch32v006evt.dts?plain=1#L44) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L58) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | WCH CH32V00x Alternate Function (AFIO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L88) | [`wch,00x-afio`](../../../../build/dts/api/bindings/pinctrl/wch,00x-afio.md#std-dtcompatible-wch-00x-afio) |
| PWM | on-chip | WCH General-purpose Timer (GPTM) for PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L190) | [`wch,gptm-pwm`](../../../../build/dts/api/bindings/pwm/wch,gptm-pwm.md#std-dtcompatible-wch-gptm-pwm) |
| Serial controller | on-chip | WCH CH32V00x UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L144)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L153) | [`wch,usart`](../../../../build/dts/api/bindings/serial/wch,usart.md#std-dtcompatible-wch-usart) |
| SPI | on-chip | WCH SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L198) | [`wch,spi`](../../../../build/dts/api/bindings/spi/wch,spi.md#std-dtcompatible-wch-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | WCH CH32V00x Systick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2c.dtsi?plain=1#L38) | [`wch,systick`](../../../../build/dts/api/bindings/timer/wch,systick.md#std-dtcompatible-wch-systick) |
| Watchdog | on-chip | WCH Independent Watchdog (IWDG)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v006.dtsi?plain=1#L69) | [`wch,iwdg`](../../../../build/dts/api/bindings/watchdog/wch,iwdg.md#std-dtcompatible-wch-iwdg) |

### Connections and IOs

#### LED

- LED1 = Unconnected. Connect to an I/O pin (PD0).
- LED2 = Unconnected. Connect to an I/O pin (PC0).

## Programming and Debugging

The `ch32v006evt` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **minichlink** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `ch32v006evt` board can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer is required since the board
does not have any built-in debug support.

Connect the programmer to the following pins on the PCB:

- VCC = VCC (do not power the board from the USB port at the same time)
- GND = GND
- SWIO = PD1

### Flashing

You can use [minichlink](https://github.com/cnlohr/ch32fun/tree/master/minichlink) [[3]](#id6) to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ch32v006evt samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## Testing the LED on the WCH CH32V006EVT

The `blinky` sample can be used to test that the LEDs on the board are working
properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The LED definitions can be found in
[boards/wch/ch32v006evt/ch32v006evt.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v006evt/ch32v006evt.dts).

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/downloads/CH32V006DS0\_PDF.html](https://www.wch-ic.com/downloads/CH32V006DS0_PDF.html)

[[3](#id7)]

[https://github.com/cnlohr/ch32fun/tree/master/minichlink](https://github.com/cnlohr/ch32fun/tree/master/minichlink)
