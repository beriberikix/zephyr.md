---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/thingy52/doc/index.html
original_path: boards/nordic/thingy52/doc/index.html
---

# Thingy:52

Board Overview

[![../../../../_images/thingy52.jpg](https://docs.zephyrproject.org/4.2.0/_images/thingy52.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/thingy52.jpg)

Thingy:52

Name:
:   `thingy52`

Vendor:
:   Nordic Semiconductor

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/thingy52/doc/index.rst/../..)

Warning

Nordic Semiconductor no longer offers support for this board, so it is not
recommended for new prototypes.

## Overview

Zephyr uses the thingy52/nrf52832 (PCA20020) board configuration for building
for the Thingy:52 board. The board has the nRF52832 MCU with ARM Cortex-M4F
processor, a set of environmental sensors, a pushbutton, and two RGB LEDs.

- ADC
- CLOCK
- FLASH
- Gas sensor
- GPIO
- GPIO Expander
- Humidity and temperature sensor
- I2C
- MPU
- NVIC
- Pressure sensor
- PWM
- RADIO (Bluetooth Low Energy)
- RGB LEDs
- RTC
- SPI
- UART
- WDT

More information about the board can be found at the [nRF52 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52) [[1]](#id2). The
[Nordic Thingy:52 guide](https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html) [[2]](#id4) contains the processor’s information and the
datasheet.

## Hardware

Thingy:52 has the following features:

- Two RGB LEDs
- CO2 and TVOC sensor
- Humidity and temperature sensor
- Color sensor
- I2C GPIO expander
- Provisions for a pin header and I2C and serial connectors
- Bluetooth radio

### Supported Features

The `thingy52` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `thingy52/nrf52832` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L218) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L51) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family BPROT (Block Protection)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L100) | [`nordic,nrf-bprot`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-bprot.md#std-dtcompatible-nordic-nrf-bprot) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L331) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MWU (Memory Watch Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L429) | [`nordic,nrf-mwu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mwu.md#std-dtcompatible-nordic-nrf-mwu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L401) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L61) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF52 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L35) | [`nordic,nrf52-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L320) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L227) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L281) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L288) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L26) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L408) | [`nordic,nrf52-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller) |
| GPIO & Headers | on-board | SX1509B GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L146) | [`semtech,sx1509b`](../../../../build/dts/api/bindings/gpio/semtech%2Csx1509b.md#std-dtcompatible-semtech-sx1509b) |
| on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L210) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L488) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L131) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L479) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L69) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L58) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L38) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L44) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L423) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L416) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L197) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L106) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L203) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L68) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L393) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L92) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-board | Fixed voltage regulators[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L77)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L91) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L76) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L274) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic%2Cnrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L257) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | STMicroelectronics LPS22HB pressure sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L158) | [`st,lps22hb-press`](../../../../build/dts/api/bindings/sensor/st%2Clps22hb-press.md#std-dtcompatible-st-lps22hb-press) |
| on-board | STMicroelectronics HTS221 humidity and temperature sensor on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L164) | [`st,hts221`](../../../../build/dts/api/compatibles/st%2Chts221.md#std-dtcompatible-st-hts221) |
| on-board | CCS811 digital air quality sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L171) | [`ams,ccs811`](../../../../build/dts/api/bindings/sensor/ams%2Cccs811.md#std-dtcompatible-ams-ccs811) |
| on-board | STMicroelectronics LIS2DH12 3-axis accelerometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L189) | [`st,lis2dh12`](../../../../build/dts/api/bindings/sensor/st%2Clis2dh12-i2c.md#std-dtcompatible-st-lis2dh12) |
| on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L267) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L313) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L122) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPI (SPI master)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L149) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L296) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

#### Lightwell RGB LED

The LED is driven by the SX1509B GPIO expander chip (device name GPIO\_P0).

| GPIO Expander Pin | LED Channel |
| --- | --- |
| 5 | Green |
| 6 | Blue |
| 7 | Red |

#### Button

Thingy:52 has a pushbutton, connected to the P0.11 SOC GPIO pin.

#### Serial

By default the system UART has the following pin configuration:

| SOC Pin | Signal |
| --- | --- |
| P0.02 | TX |
| P0.03 | RX |

The pins can be found on the P4 and P6 connectors. The system UART console
uses these pins by default.

#### Internal I2C Bus

The internal I2C bus (I2C\_0) is not routed to any of the external connectors,
but most of the on-board devices are accessed through it. The following pins
have been assigned to the bus:

| SOC Pin | Signal |
| --- | --- |
| P0.07 | SDA |
| P0.08 | SCL |

The following devices are attached to the bus.

| Device | Address |
| --- | --- |
| SX1509B | 0x3e |
| LPS22HB | 0x5c |
| HTS221 | 0x5f |
| CCS811 | 0x5a |

#### External I2C Bus

The external I2C bus (I2C\_1) can be found on the P4 header and the P5 and P7
connectors.

| SOC Pin | Signal |
| --- | --- |
| P0.14 | SDA\_EXT |
| P0.15 | SCL\_EXT |

#### Pin Header

This is the pinout of the P4 pin header. Some of the SOC GPIO pins and I2C GPIO
expander pins are accessible through it. It also allows attaching external
devices to the four on-board N-channel MOSFET transistors.

| Pin | Device | Signal / Device Pin |
| --- | --- | --- |
| 1 | SOC | SCL\_EXT / P0.15 |
| 2 | SOC | SDA\_EXT / P0.14 |
| 3 | SOC | ANA/DIG0 / P0.02 |
| 4 | SOC | ANA/DIG1 / P0.03 |
| 5 | SOC | ANA/DIG2 / P0.04 |
| 6 |  | GND |
| 7 | GPIO Expander | Pin 0 |
| 8 | GPIO Expander | Pin 1 |
| 9 | GPIO Expander | Pin 2 |
| 10 | GPIO Expander | Pin 3 |
| 11 | MOSFET 1 | Drain |
| 12 | MOSFET 1 | Source |
| 13 | MOSFET 2 | Drain |
| 14 | MOSFET 2 | Source |
| 15 | MOSFET 3 | Drain |
| 16 | MOSFET 3 | Source |
| 17 | MOSFET 4 | Drain |
| 18 | MOSFET 4 | Source |
| 19 |  | VDD |
| 20 |  | GND |

##### MOSFETs

The MOSFETs are attached to the following SOC GPIO pins:

| Device | Gate Pin |
| --- | --- |
| MOSFET 1 | P0.18 |
| MOSFET 2 | P0.19 |
| MOSFET 3 | P0.20 |
| MOSFET 4 | P0.21 |

#### Power Rails

Thing:52 has multiple power rails. The necessary rails for the currently
supported devices are listed here.

| Name | Derived from | Controlled by |
| --- | --- | --- |
| VREG | The battery | Always on |
| VDD\_nRF | VREG | Always on |
| VDD | VREG | SOC pin P0.30 |
| VDD\_CCS | VDD | GPIO expander pin 10 |

Due to the dependencies of the power rails, multiple rails may need to be
powered for a given device to turn on. The correct order of powering up the
rails is the order of the rails down the dependency chain. For example, in order
to power the CCS811 gas sensor, VDD has to be turned on first and VDD\_CCS after
it. Here’s a list of the devices and their power rails:

| Device | Rail |
| --- | --- |
| nRF52832 | VDD\_nRF |
| SX1509B | VDD |
| LPS22HB | VDD |
| HTS221 | VDD |
| CCS811 | VDD\_CCS |

#### Sensors

| Device | Function | Bus | I2C Address | Power Rail |
| --- | --- | --- | --- | --- |
| LPS22HB | Pressure and Temperature sensor | I2C\_0 | 0x5c | VDD |
| HTS221 | Humidity and Temperature sensor | I2C\_0 | 0x5f | VDD |
| CCS811 | Gas sensor | I2C\_0 | 0x5a | VDD\_CCS |

#### Misc. Device Pins

##### SX1509B

| Device Signal | SOC Pin |
| --- | --- |
| SX\_OSCIO | P0.05 |
| SX\_RESET | P0.16 |

##### LPS22HB

| Sensor Signal | SOC Pin |
| --- | --- |
| LPS\_INT | P0.23 |

##### HTS221

| Sensor Signal | SOC Pin |
| --- | --- |
| HTS\_INT | P0.24 |

##### CCS811

| Sensor Signal | GPIO Expander Pin |
| --- | --- |
| CCS\_RESET | 11 |
| CCS\_WAKE | 12 |

## Programming and Debugging

The `thingy52` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Flashing

Flashing Zephyr onto Thingy:52 requires an external J-Link programmer. The
programmer is attached to the P9 programming header.

### Debugging

Thingy:52 does not have an on-board J-Link debug IC as some other nRF5
development boards, however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page
also apply to this board, with the additional step of connecting an external
debugger. A development board with a Debug out connector such as the
[nRF52 DK](../../nrf52dk/doc/index.md#nrf52dk) can be used as a debugger with Thingy:52.

## Testing board features

The green lightwell LED can be tested with the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") example.

```shell
# From the root of the zephyr repository
west build -b thingy52/nrf52832 samples/basic/blinky
west flash
```

Also the temperature and humidity sensor can be tested with the [HTS221 Temperature and Humidity Monitor](../../../../samples/sensor/hts221/README.md#hts221 "Get temperature and humidity data from an HTS221 sensor (polling & trigger mode).")
sample.

```shell
# From the root of the zephyr repository
west build -b thingy52/nrf52832 samples/sensor/hts221
west flash
```

## References

[[1](#id3)]

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52)

[[2](#id5)]

[https://docs.nordicsemi.com/bundle/ug\_thingy52/page/UG/thingy52/intro/frontpage.html](https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html)
