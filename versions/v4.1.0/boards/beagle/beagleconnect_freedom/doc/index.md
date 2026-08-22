---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/beagle/beagleconnect_freedom/doc/index.html
original_path: boards/beagle/beagleconnect_freedom/doc/index.html
---

# BeagleConnect Freedom

Board Overview

[![../../../../_images/beagleconnect_freedom.webp](../../../../_images/beagleconnect_freedom.webp)
](../../../../_images/beagleconnect_freedom.webp)

BeagleConnect Freedom

Name:
:   `beagleconnect_freedom`

Vendor:
:   BeagleBoard.org Foundation

Architecture:
:   arm

SoC:
:   cc1352p7

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beagleconnect_freedom/doc/index.rst/../..)

## Overview

BeagleBoard.org BeagleConnect Freedom is a wireless
Internet of Things board based on the SimpleLink multi-Standard CC1352P7 wireless MCU.

## Hardware

BeagleBoard.org BeagleConnect Freedom board features the TI CC1352P7 wireless microcontroller.
The BeagleConnect Freedom is the first available BeagleConnect solution consisting
of a board and a case which ships programmed and ready to be used.

BeagleConnect Freedom board runs the Zephyr RTOS and has mikroBUS ports along
with BLE and Sub-GHz radios on it.

The CC1352P7 wireless MCU has a 48 MHz Arm Cortex-M4F SoC and a Bluetooth Low Energy and IEEE 802.15.4.

The board also features a TI MSP430F5503 microcontroller used as a USB-to-serial bridge and
GPIO expander.

### Supported Features

The `beagleconnect_freedom` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `beagleconnect_freedom/cc1352p7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L23) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | TI CC13XX/CC26xx family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L235) | [`ti,cc13xx-cc26xx-adc`](../../../../build/dts/api/bindings/adc/ti%2Ccc13xx-cc26xx-adc.md#std-dtcompatible-ti-cc13xx-cc26xx-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L57) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Flash controller | on-chip | Texas Instruments CC13xx/CC26xx flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L85) | [`ti,cc13xx-cc26xx-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ti%2Ccc13xx-cc26xx-flash-controller.md#std-dtcompatible-ti-cc13xx-cc26xx-flash-controller) |
| GPIO & Headers | on-chip | TI SimpleLink CC13xx / CC26xx GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L69) | [`ti,cc13xx-cc26xx-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Ccc13xx-cc26xx-gpio.md#std-dtcompatible-ti-cc13xx-cc26xx-gpio) |
| I2C | on-chip | TI CC13xx / CC26xx I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L171) | [`ti,cc13xx-cc26xx-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Ccc13xx-cc26xx-i2c.md#std-dtcompatible-ti-cc13xx-cc26xx-i2c) |
| on-board | GPIO enabled analog switch to isolate devices from an I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L74) | [`gpio-i2c-switch`](../../../../build/dts/api/bindings/i2c/gpio-i2c-switch.md#std-dtcompatible-gpio-i2c-switch) |
| IEEE 802.15.4 | on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L217) | [`ti,cc13xx-cc26xx-ieee802154`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154) |
| on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node (sub-GHz)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L222) | [`ti,cc13xx-cc26xx-ieee802154-subghz`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154-subghz.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154-subghz) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L67) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | Skyworks SKY13317 pHEMT GaAs SP3T Antenna Switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L57) | [`skyworks,sky13317`](../../../../build/dts/api/bindings/misc/skyworks%2Csky13317.md#std-dtcompatible-skyworks-sky13317) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L92) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc1352r7.dtsi?plain=1#L19) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L167) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | TI SimpleLink CC13xx / CC26xx radio node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L207) | [`ti,cc13xx-cc26xx-radio`](../../../../build/dts/api/bindings/net/wireless/ti%2Ccc13xx-cc26xx-radio.md#std-dtcompatible-ti-cc13xx-cc26xx-radio) |
| Pin control | on-chip | TI SimpleLink CC13xx / CC26xx pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L64) | [`ti,cc13xx-cc26xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ccc13xx-cc26xx-pinctrl.md#std-dtcompatible-ti-cc13xx-cc26xx-pinctrl) |
| PWM | on-chip | TI SimpleLink CC13xx/CC26xx GPT timer PWM Controller Node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L106)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L134) | [`ti,cc13xx-cc26xx-timer-pwm`](../../../../build/dts/api/bindings/pwm/ti%2Ccc13xx-cc26xx-timer-pwm.md#std-dtcompatible-ti-cc13xx-cc26xx-timer-pwm) |
| RNG | on-chip | TI SimpleLink CC13xx / CC26xx TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L78) | [`ti,cc13xx-cc26xx-trng`](../../../../build/dts/api/bindings/rng/ti%2Ccc13xx-cc26xx-trng.md#std-dtcompatible-ti-cc13xx-cc26xx-trng) |
| RTC | on-chip | TI SimpleLink CC13xx/CC26xx RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L200) | [`ti,cc13xx-cc26xx-rtc-timer`](../../../../build/dts/api/bindings/rtc/ti%2Ccc13xx-cc26xx-rtc-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-rtc-timer) |
| Sensors | on-board | Texas Instruments OPT3001 ambient light sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L82) | [`ti,opt3001`](../../../../build/dts/api/bindings/sensor/ti%2Copt3001.md#std-dtcompatible-ti-opt3001) |
| on-board | Texas Instruments HDC2010 Temperature and Humidity Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_freedom/beagleconnect_freedom.dts?plain=1#L88) | [`ti,hdc2010`](../../../../build/dts/api/bindings/sensor/ti%2Chdc2010.md#std-dtcompatible-ti-hdc2010) |
| Serial controller | on-chip | TI SimpleLink CC13xx / CC26xx UART node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L155) | [`ti,cc13xx-cc26xx-uart`](../../../../build/dts/api/bindings/serial/ti%2Ccc13xx-cc26xx-uart.md#std-dtcompatible-ti-cc13xx-cc26xx-uart) |
| SPI | on-chip | TI SimpleLink CC13xx / CC26xx SPI node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L181)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L190) | [`ti,cc13xx-cc26xx-spi`](../../../../build/dts/api/bindings/spi/ti%2Ccc13xx-cc26xx-spi.md#std-dtcompatible-ti-cc13xx-cc26xx-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | TI SimpleLink CC13xx/CC26xx Timer Node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L99)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L127) | [`ti,cc13xx-cc26xx-timer`](../../../../build/dts/api/bindings/timer/ti%2Ccc13xx-cc26xx-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-timer) |
| Watchdog | on-chip | TI CC13xx/CC26xx watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L228) | [`ti,cc13xx-cc26xx-watchdog`](../../../../build/dts/api/bindings/watchdog/ti%2Ccc13xx-cc26xx-watchdog.md#std-dtcompatible-ti-cc13xx-cc26xx-watchdog) |

### Connections and IOs

[![Front connections](../../../../_images/beagleconnect_freedom_front_annotated.webp)
](../../../../_images/beagleconnect_freedom_front_annotated.webp)

BeagleConnect Freedom front connections

[![Back connections](../../../../_images/beagleconnect_freedom_back_annotated.webp)
](../../../../_images/beagleconnect_freedom_back_annotated.webp)

BeagleConnect Freedom back connections

| Pin | Function | Usage |
| --- | --- | --- |
| DIO5 | RST\_MB2 | Reset mikroBUS port 2 |
| DIO6 | RST\_MB1 | Reset mikroBUS port 1 |
| DIO7 | INT\_SENSOR | On-board sensor interrupts |
| DIO8 | FLASH\_CS | SPI flash chip-select |
| DIO9 | SDO / PICO | SPI serial data output |
| DIO10 | SCK | SPI serial clock |
| DIO11 | SDI / POCI | SPI serial data input |
| DIO12 | CC1352\_RX | UART RXD mikroBUS port 1 or MSP430 |
| DIO13 | CC1352\_TX | UART TXD mikroBUS port 1 or MSP430 |
| DIO14 | I2C\_CTRL | Enable on-board sensor I2C bus |
| DIO15 | USER\_BOOT | BOOT button status |
| DIO16 | INT\_MB1 | INTERRUPT PIN on mikroBUS port 1 |
| DIO17 | PWM\_MB1 | PWM PIN on mikroBUS port 1 |
| DIO18 | LED\_LINK | Radio link indicator LED |
| DIO19 | PWM\_MB2 | PWM PIN on mikroBUS port 2 |
| DIO20 | INT\_MB2 | INTERRUPT PIN on mikroBUS port 2 |
| DIO21 | MB2\_RX | UART RXD on mikroBUS port 2 |
| DIO22 | MB2\_TX | UART TXD on mikroBUS port 2 |
| DIO23 | AN\_MB1 | ANALOG PIN on mikroBUS port 1 |
| DIO24 | AN\_MB2 | ANALOG PIN on mikroBUS port 2 |
| DIO25 | SCL | I2C SCL |
| DIO26 | SDA | I2C SDA |
| DIO27 | CS\_MB2 | SPI CS on microBUS port 2 |
| DIO28 | CS\_MB1 | SPI CS on microBUS port 1 |
| DIO29 | REF\_SW\_CTRL1 | Antenna mux PA enable |
| DIO30 | REF\_SW\_CTRL2 | Antenna mux SubG enable |

### System requirements

#### Prerequisites

BeagleConnect Freedom requires [CC1352 Flasher](https://pypi.org/project/cc1352-flasher/) for
flashing Zephyr firmware using `west flash`.

```shell
pip3 install cc1352-flasher
```

## References

BeagleBoard.org BeagleConnect Freedom reference:
:   [https://beagleconnect.org](https://beagleconnect.org)
