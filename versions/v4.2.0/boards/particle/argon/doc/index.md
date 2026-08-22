---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/particle/argon/doc/index.html
original_path: boards/particle/argon/doc/index.html
---

# Argon

Board Overview

[![../../../../_images/particle_argon.jpg](../../../../_images/particle_argon.jpg)
](../../../../_images/particle_argon.jpg)

Argon

Name:
:   `particle_argon`

Vendor:
:   Particle.io

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/particle/argon/doc/index.rst/../..)

## Overview

The Particle Argon is a Wi-Fi enabled development board with a Nordic
Semiconductor nRF52840 for mesh support and an ESP32 for Wi-Fi. The
board was developed by Particle Industries and has a SWD connector on it
for programming.

It is equipped with a onboard LIPO circuit and conforms to the
Adafruit Feather formfactor.

The Particle Argon provides support for the Nordic Semiconductor nRF52840 ARM® Cortex®-M4F SoC with an integrated 2.4 GHz transceiver supporting
Bluetooth® Low Energy and IEEE® 802.15.4.

For more information about the Particle Argon board:

- [Argon Datasheet](https://docs.particle.io/datasheets/wi-fi/argon-datasheet/)
- [Argon Hardware Files](https://github.com/particle-iot/argon)

## Hardware

On the front of the board are RGB-LED, LED and LIPO circuitry.
The RGB-LED is controlled by the nRF52840 via GPIO pins.

### Power supply

The board is optimized for low power applications and supports two
power source configurations: battery and micro USB connector.

It contains circuitry for LIPO usage and can be charged via the USB port.

### Supported Features

The `particle_argon` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `particle_argon/nrf52840` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L220) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L51) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L333) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family ACL (Access Control List)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L410) | [`nordic,nrf-acl`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-acl.md#std-dtcompatible-nordic-nrf-acl) |
| on-chip | Nordic nRF family MWU (Memory Watch Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L438) | [`nordic,nrf-mwu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mwu.md#std-dtcompatible-nordic-nrf-mwu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L403) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L61) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF52 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L35) | [`nordic,nrf52-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L322) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L229) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L283) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L290) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| on-chip | ARM TrustZone CryptoCell 310[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L570) | [`arm,cryptocell-310`](../../../../build/dts/api/bindings/crypto/arm%2Ccryptocell-310.md#std-dtcompatible-arm-cryptocell-310) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L26) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L416) | [`nordic,nrf52-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller) |
| on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L516) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| GPIO & Headers | on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L212) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L547) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-board | GPIO pins exposed on Particle Gen3 (Feather) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/dts/mesh_feather.dtsi?plain=1#L69) | [`particle-gen3-header`](../../../../build/dts/api/bindings/gpio/particle-gen3-header.md#std-dtcompatible-particle-gen3-header) |
| on-board | GPIO pins exposed on Adafruit Feather headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/dts/mesh_feather.dtsi?plain=1#L98) | [`adafruit-feather-header`](../../../../build/dts/api/bindings/gpio/adafruit-feather-header.md#std-dtcompatible-adafruit-feather-header) |
| I2C | on-chip | Nordic nRF family TWI (TWI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L133) | [`nordic,nrf-twi`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L169) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L488) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L110) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/particle_argon.dts?plain=1#L23) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/dts/mesh_feather.dtsi?plain=1#L54) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/dts/mesh_feather.dtsi?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L44) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L432) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| on-board | Output selectors on the SKY13351 GaAs SPDT FET I/C switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/particle_argon.dts?plain=1#L17) | [`skyworks,sky13351`](../../../../build/dts/api/bindings/misc/skyworks%2Csky13351.md#std-dtcompatible-skyworks-sky13351) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L425) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf52840_partition.dtsi?plain=1#L16) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/argon/dts/mesh_feather.dtsi?plain=1#L167) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L100) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L205) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L68) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L395) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L92) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF52X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840_qiaa.dtsi?plain=1#L19) | [`nordic,nrf52x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf52x-regulator-hv.md#std-dtcompatible-nordic-nrf52x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L76) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L276) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic%2Cnrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L259) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L269) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L315) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L124) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L151) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| on-chip | Nordic nRF family SPI (SPI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L460) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L497) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic%2Cnrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L298) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

Please see the [Argon Datasheet](https://docs.particle.io/datasheets/wi-fi/argon-datasheet/) for header pin assignments, which are
common to all Feather-compatible Particle boards. Some peripherals are
available to applications through DTS overlay include directives:

- `mesh_feather_i2c1_twi1.dtsi` exposes TWI1 on labeled Feather
  SDA1/SCL1 pins
- `mesh_feather_spi_spi1.dtsi` exposes SPI1 on labeled Feather
  SPI pins
- `mesh_feather_spi_spi3.dtsi` exposes SPI3 on labeled Feather
  SPI pins
- `mesh_feather_spi1_spi3.dtsi` exposes SPI3 on labeled Feather
  SPI1 pins
- `mesh_feather_uart1_rtscts.dtsi` adds hardware flow control to
  labeled Feather UART pins

#### LED

- LED0 (blue)
- LED1 (red)
- LED2 (green)
- LED3 (blue)

#### Push buttons

- SW0 via MODE
- SW1 via RESET

#### I2C

- TWI0 enabled on labeled header (SDA/SCL)
- TWI1 selectable with overlay (SDA1/SCL1)

#### SPI

- SPI0 disabled due to TWI0 conflict
- SPI1 selectable with overlay (SPI)
- SPI2 internal to 32 Mb CFI flash chip
- SPI3 selectable with overlay (SPI or SPI1)

#### UART

- UARTE0 enabled RX/TX on labeled header (UART1); add RTS/CTS with overlay
- UARTE1 internal to ESP32

## Programming and Debugging

The `particle_argon` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ |  |  |  |  |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `particle_argon` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Build and flash an application in the usual way, for example:

```shell
# From the root of the zephyr repository
west build -b particle_argon samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b particle_argon samples/hello_world
west debug
```

## Testing the LEDs and buttons

There are 2 samples that allow you to test that the buttons (switches) and
LEDs on the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board.
