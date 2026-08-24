---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.html
original_path: boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.html
---

# Labs Papyr

Board Overview

[![../../../../_images/nrf52840_papyr.jpg](https://docs.zephyrproject.org/4.2.0/_images/nrf52840_papyr.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/nrf52840_papyr.jpg)

Labs Papyr

Name:
:   `nrf52840_papyr`

Vendor:
:   Electronut Labs

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.rst/../..)

## Overview

Zephyr applications use the nrf52840\_papyr board configuration
to run on Electronut Labs Papyr hardware. It provides
support for the Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU and
the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- SPI
- UART
- USB
- WDT
- COUNTER

More information about the board is available at [https://gitlab.com/electronutlabs-public/papyr](https://gitlab.com/electronutlabs-public/papyr).

## Hardware

Papyr has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf52840_papyr` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nrf52840_papyr/nrf52840` target

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
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/electronut/nrf52840_papyr/nrf52840_papyr.dts?plain=1#L58) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/electronut/nrf52840_papyr/nrf52840_papyr.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/electronut/nrf52840_papyr/nrf52840_papyr.dts?plain=1#L42) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L44) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L432) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic,nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L425) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf52840_partition.dtsi?plain=1#L16) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L100) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L205) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L68) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L395)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L444) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L92) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF52X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840_qiaa.dtsi?plain=1#L19) | [`nordic,nrf52x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf52x-regulator-hv.md#std-dtcompatible-nordic-nrf52x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L76) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L276) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L259) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L269) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L315) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L124) | [`nordic,nrf-uart`](../../../../build/dts/api/bindings/serial/nordic,nrf-uart.md#std-dtcompatible-nordic-nrf-uart) |
| on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L509) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L151) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| on-chip | Nordic nRF family SPI (SPI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L187) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic,nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L497) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52840.dtsi?plain=1#L298) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

#### LED

- LED1 (green) = P0.13
- LED2 (blue) = P0.15
- LED3 (red) = P0.14

#### Push buttons

- Reset = SW0 = P0.18 (can be used as GPIO also)

#### UART

- TX = P0.8
- RX = P0.7

#### I2C

I2C pins connected to onboard sensors (I2C\_0):

- SDA = P0.5
- SCL = P0.6

#### SPI

The e-paper display is connected to the chip via SPI on the following pins (SPI\_1):

- SCK = P0.31
- MOSI = P0.29
- MISO = P1.1 (not used by the display)

NOTE: P1.1 is pin 33 in absolute enumeration.

Other pins used by the e-paper display are:

- E-ink enable = P0.11 (cuts off power to the display with MOSFET)
- CS = P0.30
- BUSY = P0.3
- D/C = P0.28
- RES = P0.2

## Programming and Debugging

The `nrf52840_papyr` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** |
| --- | --- | --- | --- |
| **[blackmagicprobe](../../../../develop/flash_debug/host-tools.md#runner-blackmagicprobe)** | ✅ (default) | ✅ (default) | ✅ |
| **nrfjprog** | ✅ |  |  |
| **nrfutil** | ✅ |  |  |

Applications for the `nrf52840_papyr` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); Black Magic
Probe debugger presents itself as two USB-serial ports. On Linux,
they may come up as `/dev/ttyACM0` and `/dev/ttyACM1`. The first
one of these (`/dev/ttyACM0` here) is the debugger port.
GDB can directly connect to this port without requiring a GDB server by specifying
`target external /dev/ttyACM0`. The second port acts as a
serial port, connected to the SoC.

### Flashing

By default, papyr is configured to be used with a blackmagicprobe compatible
debugger (see \_Bumpy).

Applications are flashed and run as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the serial port of Black Magic Probe.
For example, under Linux, `/dev/ttyACM1`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf52840_papyr samples/hello_world
west flash
```

### Debugging

Debug and attach configurations are available using Black Magic Probe, and
`ninja debug`, or `ninja attach` (or with `make`) are available.

NOTE: You may need to press the reset button once after using `ninja flash`
to start executing the code. (not required with `debug` or `attach`)

## References
