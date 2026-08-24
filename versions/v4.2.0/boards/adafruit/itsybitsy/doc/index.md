---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adafruit/itsybitsy/doc/index.html
original_path: boards/adafruit/itsybitsy/doc/index.html
---

# ItsyBitsy nRF52840

Board Overview

[![../../../../_images/adafruit_itsybitsy_nrf52840.jpeg](https://docs.zephyrproject.org/4.2.0/_images/adafruit_itsybitsy_nrf52840.jpeg)
](https://docs.zephyrproject.org/4.2.0/_images/adafruit_itsybitsy_nrf52840.jpeg)

ItsyBitsy nRF52840

Name:
:   `adafruit_itsybitsy`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/itsybitsy/doc/index.rst/../..)

## Overview

The Adafruit ItsyBitsy nRF52840 Express is a small (36 mm x 18 mm) ARM
development board with an onboard RGB LED, USB port, 2 MB of QSPI flash,
and range of I/O broken out onto 21 GPIO pins.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- I2S
- MPU
- NVIC
- PWM
- QSPI
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- SPI
- UARTE
- USB
- WDT

## Hardware

- nRF52840 ARM Cortex-M4F CPU at 64MHz
- 1 MB of flash memory and 256 KB of SRAM
- 2 MB of QSPI flash
- A user LED
- A user switch
- An RGB DotStar LED
- Native USB port
- One reset button

### Supported Features

The `adafruit_itsybitsy` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `adafruit_itsybitsy/nrf52840` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L220) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L51) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L333) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic,nrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family ACL (Access Control List)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L410) | [`nordic,nrf-acl`](../../../../build/dts/api/bindings/arm/nordic,nrf-acl.md#std-dtcompatible-nordic-nrf-acl) |
| on-chip | Nordic nRF family MWU (Memory Watch Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L438) | [`nordic,nrf-mwu`](../../../../build/dts/api/bindings/arm/nordic,nrf-mwu.md#std-dtcompatible-nordic-nrf-mwu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L403) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic,nrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L61) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF52 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L35) | [`nordic,nrf52-hfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L322) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L229) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L283) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L290) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| on-chip | ARM TrustZone CryptoCell 310[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L570) | [`arm,cryptocell-310`](../../../../build/dts/api/bindings/crypto/arm,cryptocell-310.md#std-dtcompatible-arm-cryptocell-310) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L26) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L416) | [`nordic,nrf52-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller) |
| on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L516) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| GPIO & Headers | on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L212) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L547) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWI (TWI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L133) | [`nordic,nrf-twi`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L169) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L488) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L110) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LED strip | on-board | APA102 SPI LED strip[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts?plain=1#L103) | [`apa,apa102`](../../../../build/dts/api/bindings/led_strip/apa,apa102.md#std-dtcompatible-apa-apa102) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L44) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L432) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic,nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L425) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf52840_partition_uf2_sdv6.dtsi?plain=1#L28) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts?plain=1#L119) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic,qspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L100) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L205) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L68) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L395) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L92) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF52X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840_qiaa.dtsi?plain=1#L19) | [`nordic,nrf52x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf52x-regulator-hv.md#std-dtcompatible-nordic-nrf52x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L76) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L276) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L259) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L269) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L315) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L124) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L151) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| on-chip | Nordic nRF family SPI (SPI master)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L187) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic,nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L497) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L298) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

The [Adafruit ItsyBitsy nRF52840 Express Learn site](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express) [[1]](#id2) has detailed
information about the board including [pinouts](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads) [[3]](#id6).

#### LED

- LED0 (red) = P0.06
- LED1 (Adafruit DotStar)

  > - DATA = P0.08
  > - CLK = P1.09

#### Push buttons

- SWITCH = P0.29
- RESET = P0.18

#### Logging

Logging is done using the USB-CDC port. See the [Logging](../../../../samples/subsys/logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.") sample
or the [Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") sample applications to see how this works.

## Testing LEDs and buttons on the Adafruit ItsyBitsy nRF52840 Express

The [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.") sample lets you test the buttons (switches) and the red LED.
The [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample lets you test the red LED.

The DotStar LED has been implemented as a SPI device and can be tested
with the [LED strip](../../../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.") sample application.

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/adafruit/itsybitsy/adafruit\_itsybitsy\_nrf52840.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts).

## Programming and Debugging

The `adafruit_itsybitsy` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[bossac](../../../../develop/flash_debug/host-tools.md#runner-bossac)** | ✅ (default) |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

The ItsyBitsy ships with the BOSSA compatible UF2 bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

### First time setup

Some versions of this board were shipped with a buggy bootloader.
Ensure that the bootloader is up to date by following the
[Adafruit UF2 Bootloader update](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader) [[4]](#id8) tutorial. Note that this tutorial
was made for the Adafruit Feather nRF52840, but the steps to update
the bootloader are the same for the ItsyBitsy. The files for the
ItsyBitsy bootloader can be found in the [Adafruit nRF52 Bootloader repo](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases) [[5]](#id10).

The building and flashing of Zephyr applications have been tested with
release 0.7.0 of the UF2 bootloader.

### Flashing

Flashing is done by dragging and dropping the built Zephyr UF2-file
into the `ITSY840BOOT` drive.

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
   sample application:

   ```shell
   west build -b adafruit_itsybitsy/nrf52840 samples/basic/blinky
   ```
2. Connect the ItsyBitsy to your host computer using USB
3. Tap the reset button twice quickly to enter bootloader mode
4. Flash the image:

   Drag and drop the file `samples/basic/blinky/build/zephyr/zephyr.uf2`
   into `ITSY840BOOT`

The device will disconnect and you should see the red LED blink.

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads)

[[4](#id9)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader)

[[5](#id11)]

[https://github.com/adafruit/Adafruit\_nRF52\_Bootloader/releases](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases)
