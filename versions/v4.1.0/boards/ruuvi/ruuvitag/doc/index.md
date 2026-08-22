---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ruuvi/ruuvitag/doc/index.html
original_path: boards/ruuvi/ruuvitag/doc/index.html
---

# RuuviTag

Board Overview

[![../../../../_images/ruuvitag.jpg](../../../../_images/ruuvitag.jpg)
](../../../../_images/ruuvitag.jpg)

RuuviTag

Name:
:   `ruuvi_ruuvitag`

Vendor:
:   Ruuvi Innovations Ltd (Oy)

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruuvi/ruuvitag/doc/index.rst/../..)

## Overview

RuuviTag is an advanced battery-operated open-source Bluetooth
enabled sensor beacon platform capable of sending temperature, humidity,
pressure, and motion information over Bluetooth Low Energy.

More information about the board can be found at the
[ruuvitag website](https://ruuvi.com) [[1]](#id2).

## Hardware

RuuviTag’s have the following physical features:

- Nordic Semiconductor nRF52832 System-on-Chip
- STMicroelectronics LIS2DH12 accelerometer
- Bosch BME 280 temperature + relative air humidity + air pressure sensor
- NFC™-A tag antenna
- 1000mAh CR2477 battery
- 2 buttons
- 1 Green LED
- 1 Red LED
- IP67 Enclosure
- Long range RF antenna

### Supported Features

The `ruuvi_ruuvitag` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ruuvi_ruuvitag/nrf52832` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L209) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L42) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family BPROT (Block Protection)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L91) | [`nordic,nrf-bprot`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-bprot.md#std-dtcompatible-nordic-nrf-bprot) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L322) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MWU (Memory Watch Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L420) | [`nordic,nrf-mwu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mwu.md#std-dtcompatible-nordic-nrf-mwu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L392) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L52) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L311) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L218) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L272) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L279) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L26) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L399) | [`nordic,nrf52-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L201) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L479) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L122) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L470) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruuvi/ruuvitag/ruuvi_ruuvitag.dts?plain=1#L48) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruuvi/ruuvitag/ruuvi_ruuvitag.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L35) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L414) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L407) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruuvi/ruuvitag/ruuvi_ruuvitag.dts?plain=1#L108) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L97) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L194) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L59) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L384) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L83) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L67) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L265) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic%2Cnrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L248) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | BME280 integrated environmental sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruuvi/ruuvitag/ruuvi_ruuvitag.dts?plain=1#L91) | [`bosch,bme280`](../../../../build/dts/api/compatibles/bosch%2Cbme280.md#std-dtcompatible-bosch-bme280) |
| on-board | STMicroelectronics LIS2DH 3-axis accelerometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruuvi/ruuvitag/ruuvi_ruuvitag.dts?plain=1#L97) | [`st,lis2dh`](../../../../build/dts/api/compatibles/st%2Clis2dh.md#std-dtcompatible-st-lis2dh) |
| on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L258) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L304) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L113) | [`nordic,nrf-uart`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uart.md#std-dtcompatible-nordic-nrf-uart) |
| SPI | on-chip | Nordic nRF family SPI (SPI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L140)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L176) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L48) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L287) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

#### LED

- LED0 (red) = P0.17
- LED1 (green) = P0.19

#### Push buttons

- BUTTON0 = SW1 = P0.13

#### Pin descriptions

![RUUVI Pinout](../../../../_images/pinout1.jpg)

- 2 = P0.29 = SPI\_SCK
- 3 = P0.28 = SPI\_MISO
- 10 = P0.04 = GPIO (can be used as a GPIO / ADC pin)
- 11 = P0.05 = GPIO (can be used as a GPIO / ADC pin)
- 12 = P0.25 = SPI\_MOSI
- 13 = P0.19 = LED2 (green) / GPIO (can be used as a GPIO pin but the LED will blink)
- 14 = P0.17 = LED1 (red) / GPIO (can be used as a GPIO pin but the LED will blink)
- 15 = P0.13 = Button / GPIO (can be used as a GPIO pin)
- 16 = GND (Battery’s negative contact)
- 17 = Battery’s positive contact
- 18 = Battery’s positive contact
- 19 = SWDIO
- 20 = SWDCLK
- 21 = P0.18 = SWO / GPIO (can be used as a GPIO pin)
- 22 = P0.21 = Reset / GPIO (can be used as a GPIO pin if no need to reset the device)
- 23 = GND (Battery’s negative contact)
- 24 = P0.31 = GPIO (can be used as a GPIO / ADC pin)
- 25 = P0.30 = GPIO (can be used as a GPIO / ADC pin)

GPIO = General Purpose Input Output pin

P1 = Standard 10-pin ARM Cortex debug connector (on RuuviTag Rev.B1-B5)

- 1 = VDD
- 2 = SWDIO
- 3 = GND (Battery’s negative contact)
- 4 = SWDCLK
- 5 = GND (Battery’s negative contact)
- 6 = SWO
- 7 = No Connect
- 8 = No Connect
- 9 = GND (Battery’s negative contact)
- 10 = Reset

P1 = TC2030 TagConnect (on RuuviTag Rev.B6)

- 1 = Battery’s positive contact
- 2 = SWDIO
- 3 = Reset
- 4 = SWDCLK
- 5 = GND (Battery’s negative contact)
- 6 = SWO

## Programming and Debugging

### Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

The easiest way to flash Zephyr onto a RuuviTag requires an external Ruuvi DEVKIT. More information about the board can be found at the
[ruuvitag devkit](https://lab.ruuvi.com/devshield/) [[2]](#id4).

Once your tag is connected to the DEVKIT and connected to your PC, build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ruuvi_ruuvitag samples/basic/blinky
west flash
```

Advanced users may want to program the RuuviTag without the DEVKIT, this can be achieved via the SWDIO and SWDCLK pins located on the back of the RuuviTag.

### Debugging

If using the Ruuvi DEVKIT refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons on the RuuviTag

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in `boards/ruuvi//ruuvi_ruuvitag/ruuvi_ruuvitag.dts`.

## References

[[1](#id3)]

[https://ruuvi.com](https://ruuvi.com)

[[2](#id5)]

[https://lab.ruuvi.com/devshield/](https://lab.ruuvi.com/devshield/)
