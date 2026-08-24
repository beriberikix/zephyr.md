---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/others/serpente/doc/index.html
original_path: boards/others/serpente/doc/index.html
---

# Arturo182 Serpente

Board Overview

[![../../../../_images/serpente.jpg](https://docs.zephyrproject.org/4.2.0/_images/serpente.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/serpente.jpg)

Arturo182 Serpente

Name:
:   `serpente`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   samd21e18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/serpente/doc/index.rst/../..)

## Overview

The Serpente is a very small low-cost development and prototyping
board equipped with 4MiB flash storage, a PWM enabled RGB led and 6 I/O pins.
The board comes with 3 different USB connector options: USB Type-C plug,
USB Type-C socket and USB Type-A plug.

## Hardware

- ATSAMD21E18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Extra 4MiB SPI flash memory
- RGB User LED
- Reset button
- Native USB port

### Supported Features

The `serpente` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `serpente/samd21e18a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L44) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L202) | [`atmel,sam0-adc`](../../../../build/dts/api/bindings/adc/atmel,sam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L120)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L126) | [`atmel,sam0-sercom`](../../../../build/dts/api/bindings/arm/atmel,sam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L56) | [`atmel,sam0-id`](../../../../build/dts/api/bindings/arm/atmel,sam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L82) | [`atmel,sam0-mclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L90) | [`atmel,sam0-gclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L156) | [`atmel,sam0-tc32`](../../../../build/dts/api/bindings/counter/atmel,sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DAC | on-chip | Atmel SAM0 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L212) | [`atmel,sam0-dac`](../../../../build/dts/api/bindings/dac/atmel,sam0-dac.md#std-dtcompatible-atmel-sam0-dac) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L29) | [`atmel,sam0-dmac`](../../../../build/dts/api/bindings/dma/atmel,sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L65) | [`atmel,sam0-nvmctrl`](../../../../build/dts/api/bindings/flash_controller/atmel,sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L169) | [`atmel,sam0-gpio`](../../../../build/dts/api/bindings/gpio/atmel,sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L98) | [`atmel,sam0-eic`](../../../../build/dts/api/bindings/interrupt-controller/atmel,sam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/serpente/serpente.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/serpente/serpente.dts?plain=1#L56) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/serpente/serpente.dts?plain=1#L122) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L104) | [`atmel,sam0-pinmux`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L162) | [`atmel,sam0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L49) | [`atmel,sam0-tcc-pwm`](../../../../build/dts/api/bindings/pwm/atmel,sam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L190) | [`atmel,sam0-rtc`](../../../../build/dts/api/bindings/rtc/atmel,sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L132) | [`atmel,sam0-uart`](../../../../build/dts/api/bindings/serial/atmel,sam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L138) | [`atmel,sam0-spi`](../../../../build/dts/api/bindings/spi/atmel,sam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L20) | [`atmel,sam0-usb`](../../../../build/dts/api/bindings/usb/atmel,sam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L114) | [`atmel,sam0-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel,sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Connections and IOs

The [Serpente documentation](https://www.solder.party/docs/serpente/r2/) [[1]](#id2) has detailed information about the board
including [pinouts](https://www.solder.party/docs/serpente/r2/pinout/) [[2]](#id4) and the [schematic](https://www.solder.party/docs/serpente/r2/downloads/) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 8MHz internal oscillator
with the on-chip PLL generating the 48 MHz system clock.

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which prints “Hello World!”
to the host PC.

### Programming and Debugging

The `serpente` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **[bossac](../../../../develop/flash_debug/host-tools.md#runner-bossac)** | ✅ (default) |  |

The Serpente ships the BOSSA compatible UF2 bootloader. The bootloader
can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application:

   ```shell
   west build -b serpente samples/basic/blinky
   ```
2. Connect the Serpente to your host computer using USB
3. Tap the reset button twice quickly to enter bootloader mode
4. Flash the image:

   ```shell
   west build -b serpente samples/basic/blinky
   west flash
   ```

   You should see the User LED blink.

## References

[[1](#id3)]

[https://www.solder.party/docs/serpente/r2/](https://www.solder.party/docs/serpente/r2/)

[[2](#id5)]

[https://www.solder.party/docs/serpente/r2/pinout/](https://www.solder.party/docs/serpente/r2/pinout/)

[[3](#id7)]

[https://www.solder.party/docs/serpente/r2/downloads/](https://www.solder.party/docs/serpente/r2/downloads/)
