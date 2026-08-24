---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/bytesatwork/bytesensi_l/doc/index.html
original_path: boards/bytesatwork/bytesensi_l/doc/index.html
---

# byteSENSI-L

Board Overview

[![../../../../_images/byteSENSI-L.jpg](https://docs.zephyrproject.org/4.1.0/_images/byteSENSI-L.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/byteSENSI-L.jpg)

byteSENSI-L

Name:
:   `bytesensi_l`

Vendor:
:   bytesatwork AG

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bytesatwork/bytesensi_l/doc/index.rst/../..)

## Overview

The byteSENSI-L is a fun LoRa device based on nRF52 MCU that integrates many
sensors.

## Hardware

### Supported Features

The `bytesensi_l` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `bytesensi_l/nrf52832` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L209) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L42) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family BPROT (Block Protection)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L91) | [`nordic,nrf-bprot`](../../../../build/dts/api/bindings/arm/nordic,nrf-bprot.md#std-dtcompatible-nordic-nrf-bprot) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L322) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic,nrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MWU (Memory Watch Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L420) | [`nordic,nrf-mwu`](../../../../build/dts/api/bindings/arm/nordic,nrf-mwu.md#std-dtcompatible-nordic-nrf-mwu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L392) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic,nrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L52) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L311) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L218) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L272) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L279) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L26) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L399) | [`nordic,nrf52-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller) |
| GNSS | on-board | Generic GNSS NMEA receiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L166) | [`gnss-nmea-generic`](../../../../build/dts/api/bindings/gnss/gnss-nmea-generic.md#std-dtcompatible-gnss-nmea-generic) |
| GPIO & Headers | on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L201) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L479) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWI (TWI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L122) | [`nordic,nrf-twi`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L158) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L470) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LoRa | on-board | Semtech SX1276 LoRa Modem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L134) | [`semtech,sx1276`](../../../../build/dts/api/bindings/lora/semtech,sx1276.md#std-dtcompatible-semtech-sx1276) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L35) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L414) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic,nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-board | TI TMP116 EEPROM controller binding[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L103) | [`ti,tmp116-eeprom`](../../../../build/dts/api/bindings/mtd/ti,tmp116-eeprom.md#std-dtcompatible-ti-tmp116-eeprom) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L148) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L407) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L34) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L97) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L194) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L59) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L384) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L83) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L67) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L265) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L248) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | APDS9960 digital proximity, ambient light, RGB, and gesture sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L89) | [`avago,apds9960`](../../../../build/dts/api/bindings/sensor/avago,apds9960.md#std-dtcompatible-avago-apds9960) |
| on-board | Texas Instruments TMP116 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L96) | [`ti,tmp116`](../../../../build/dts/api/bindings/sensor/ti,tmp116.md#std-dtcompatible-ti-tmp116) |
| on-board | CCS811 digital air quality sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L110) | [`ams,ccs811`](../../../../build/dts/api/bindings/sensor/ams,ccs811.md#std-dtcompatible-ams-ccs811) |
| on-board | STMicroelectronics LPS22HB pressure sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bytesatwork/bytesensi_l/bytesensi_l.dts?plain=1#L118) | [`st,lps22hb-press`](../../../../build/dts/api/bindings/sensor/st,lps22hb-press.md#std-dtcompatible-st-lps22hb-press) |
| on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L258) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L304) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L113) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPI (SPI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L176)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L140) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic,nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L48) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L287) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

#### External Connectors

External Supply @ X1

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VBAT | Power input instead of CR2477 battery |
| 2 | GND | Ground |

Programming Connector @ SL1

| PIN # | Signal Name |
| --- | --- |
| 1 | VBAT |
| 2 | SWDIO |
| 3 | GND |
| 4 | SWDCLK |
| 5 | GND |
| 6 | NC (SWO) |
| 7 | NC (Key) |
| 8 | NC |
| 9 | GND |
| 10 | nReset |

I2C Sensor @ X3

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VBAT | Power out |
| 2 | SCL | I2C clock at P0.15 |
| 3 | SDA | I2C data at P0.16 |
| 4 | INT | Interrupt at P0.13 |
| 5 | I2C\_ADDR | tied to VBAT |
| 6 | GND | Ground |

One Wire Sensor @ X2

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VDD | 4V8 |
| 2 | IO | One Wire |
| 3 | GND | Ground |

External BLE Antenna @ J1

External LoRa Antenna @ J2

External GPS Antenna @ J3

## Programming and Debugging

### Flashing

The byteSENSI-L board can be flashed with the SEGGER JLink programmer.

You can build and flash applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> ```shell
> west build -b bytesensi_l samples/hello_world
> west flash
> ```

### Debugging

Debugging your application can be done with `west debug`.

### Serial console

The byteSENSI-L board only uses Segger’s RTT console for providing serial
console. There is no physical serial port available.

## References

- [bytesatwork website](https://www.bytesatwork.io/)
- [bytesatwork wiki](https://wiki.bytesatwork.io/)
