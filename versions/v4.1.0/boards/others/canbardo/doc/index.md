---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/canbardo/doc/index.html
original_path: boards/others/canbardo/doc/index.html
---

# CANbardo

Board Overview

[![../../../../_images/canbardo.webp](https://docs.zephyrproject.org/4.1.0/_images/canbardo.webp)
](https://docs.zephyrproject.org/4.1.0/_images/canbardo.webp)

CANbardo

Name:
:   `canbardo`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   same70n20b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/canbardo/doc/index.rst/../..)

## Overview

CANbardo is an open hardware Universal Serial Bus (USB) to Controller Area Network (CAN) adapter
board. It is designed to be compatible with the open source [CANnectivity USB to CAN adapter firmware](../../../../develop/manifest/external/cannectivity.md#external-module-cannectivity).

## Hardware

The CANbardo board is equipped with an Atmel SAME70N20B microcontroller and features an USB-C
connector (high-speed USB 2.0), two DB-9M connectors for CAN FD (up to 8 Mbit/s), a number of status
LEDs, and a push button. Schematics and component placement drawings are available in the [CANbardo
GitHub repository](https://github.com/CANbardo/canbardo).

### Supported Features

The `canbardo` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `canbardo/same70n20b` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L30) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | Atmel SAM family AFEC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L210) | [`atmel,sam-afec`](../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| ARM architecture | on-chip | Atmel SAM SSC (Synchronous Serial Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L49) | [`atmel,sam-ssc`](../../../../build/dts/api/bindings/arm/atmel%2Csam-ssc.md#std-dtcompatible-atmel-sam-ssc) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L175) | [`atmel,sam-can`](../../../../build/dts/api/bindings/can/atmel%2Csam-can.md#std-dtcompatible-atmel-sam-can) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L323) | [`atmel,sam-pmc`](../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L67) | [`atmel,sam-tc`](../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DAC | on-chip | Atmel SAM family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L219) | [`atmel,sam-dac`](../../../../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac) |
| DMA | on-chip | Atmel SAM XDMAC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L314) | [`atmel,sam-xdmac`](../../../../build/dts/api/bindings/dma/atmel%2Csam-xdmac.md#std-dtcompatible-atmel-sam-xdmac) |
| Ethernet | on-chip | Atmel SAM-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L228) | [`atmel,sam-gmac`](../../../../build/dts/api/bindings/ethernet/atmel%2Csam-gmac.md#std-dtcompatible-atmel-sam-gmac) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L347) | [`atmel,sam-flash-controller`](../../../../build/dts/api/bindings/flash_controller/atmel%2Csam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO PORT node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L370) | [`atmel,sam-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L421) | [`atmel,sam-rstc`](../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWIHS)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L118) | [`atmel,sam-i2c-twihs`](../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/canbardo/canbardo.dts?plain=1#L75) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/canbardo/canbardo.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L239) | [`atmel,sam-mdio`](../../../../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L37) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L357) | [`atmel,sam-flash`](../../../../build/dts/api/bindings/mtd/atmel%2Csam-flash.md#std-dtcompatible-atmel-sam-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/canbardo/canbardo.dts?plain=1#L134) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/canbardo/canbardo.dts?plain=1#L85) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L364) | [`atmel,sam-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L428) | [`atmel,sam-supc`](../../../../build/dts/api/bindings/power/atmel%2Csam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L140) | [`atmel,sam-pwm`](../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L306) | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L443) | [`atmel,sam-rtc`](../../../../build/dts/api/bindings/rtc/atmel%2Csam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| Sensors | on-chip | Atmel SAM Timer Counter (TC) QDEC mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L78) | [`atmel,sam-tc-qdec`](../../../../build/dts/api/bindings/sensor/atmel%2Csam-tc-qdec.md#std-dtcompatible-atmel-sam-tc-qdec) |
| Serial controller | on-chip | Atmel SAM family USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L151) | [`atmel,sam-usart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| on-chip | SAM family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L339)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L331) | [`atmel,sam-uart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| SPI | on-chip | Atmel SAM SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L57) | [`atmel,sam-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L44) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBHS) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L199) | [`atmel,sam-usbhs`](../../../../build/dts/api/bindings/usb/atmel%2Csam-usbhs.md#std-dtcompatible-atmel-sam-usbhs) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L435) | [`atmel,sam-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

### System Clock

The SAME70N20B is driven by a 12 MHz crystal and configured to provide a system clock of 300
MHz. The two CAN FD controllers have a core clock frequency of 80 MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b canbardo samples/basic/blinky
west flash
```
