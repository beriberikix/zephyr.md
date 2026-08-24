---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ezurio/rm1xx_dvk/doc/index.html
original_path: boards/ezurio/rm1xx_dvk/doc/index.html
---

# RM1xx DVK

Board Overview

[![../../../../_images/rm1xx_dvk.jpg](https://docs.zephyrproject.org/4.2.0/_images/rm1xx_dvk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/rm1xx_dvk.jpg)

RM1xx DVK

Name:
:   `rm1xx_dvk`

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf51822

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/rm1xx_dvk/doc/index.rst/../..)

## Overview

Ezurio’s RM1xx is a module which integrates both LoRa and
BLE communications, powered by a Nordic Semiconductor nRF51822 ARM
Cortex-M0 CPU and on-board Semtech SX1272 LoRa RF chip. This board
supports the RM1xx on the RM1xx development board - RM191 for the
915MHz version and RM186 for the 868MHz version.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

![RM1xx module](https://docs.zephyrproject.org/4.2.0/_images/RM186-SM.jpg)

RM1xx module (Credit: Ezurio)

More information about the module can be found on the
[RM1xx homepage](https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module) [[1]](#id3).

The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

The RM1xx has two internal oscillators. The frequency of
the slow clock is 32.768KHz. The frequency of the main clock
is 16MHz.

### Supported Features

The `rm1xx_dvk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rm1xx_dvk/nrf51822` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L18) | [`arm,cortex-m0`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | nRF ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L157) | [`nordic,nrf-adc`](../../../../build/dts/api/bindings/adc/nordic,nrf-adc.md#std-dtcompatible-nordic-nrf-adc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L42) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L76) | [`nordic,nrf-mpu`](../../../../build/dts/api/bindings/arm/nordic,nrf-mpu.md#std-dtcompatible-nordic-nrf-mpu) |
| on-chip | Nordic nRF family SWI (Software Interrupt)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L265) | [`nordic,nrf-swi`](../../../../build/dts/api/bindings/arm/nordic,nrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L69) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF51 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L26) | [`nordic,nrf51-hfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf51-hfxo.md#std-dtcompatible-nordic-nrf51-hfxo) |
| Comparator | on-chip | Nordic nRF LPCOMP (analog Low-Power COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L257) | [`nordic,nrf-lpcomp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-lpcomp.md#std-dtcompatible-nordic-nrf-lpcomp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L165) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L219) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L226) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L307) | [`nordic,nrf51-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf51-flash-controller.md#std-dtcompatible-nordic-nrf51-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L149) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L328) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWI (TWI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L112)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L139) | [`nordic,nrf-twi`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/rm1xx_dvk/rm1xx_dvk.dts?plain=1#L27) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LoRa | on-board | Semtech SX1272 LoRa Modem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/rm1xx_dvk/rm1xx_dvk.dts?plain=1#L91) | [`semtech,sx1272`](../../../../build/dts/api/bindings/lora/semtech,sx1272.md#std-dtcompatible-semtech-sx1272) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L35) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L322) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic,nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/rm1xx_dvk/rm1xx_dvk.dts?plain=1#L79) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/rm1xx_dvk/rm1xx_dvk.dts?plain=1#L145) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L315) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L82) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L52) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L60) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L212) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L195) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L205) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L250) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L94) | [`nordic,nrf-uart`](../../../../build/dts/api/bindings/serial/nordic,nrf-uart.md#std-dtcompatible-nordic-nrf-uart) |
| SPI | on-chip | Nordic nRF family SPI (SPI master)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L122)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L101) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic,nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L48) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L233) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

See [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
for a complete list of hardware features.

### Connections and IOs

The development board features a Microchip MCP23S08 SPI port expander -
note that this is not currently supported in Zephyr.

Refer to the [Microchip MCP23S08 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf) [[5]](#id12) for further details.

#### Push buttons

- BUTTON2 = SW0 = P0.05

### Internal Memory

#### EEPROM Memory

A 512KB (4Mb) Adesto AT25DF041B EEPROM is available via SPI for storage
of infrequently updated data and small datasets and can be used with
the spi-nor driver. Note that the EEPROM shares the same SPI bus as the
SX1272 LoRa transceiver so priority access should be given to the LoRa
radio.

Refer to the [Adesto AT25DF041B datasheet](https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b_040.pdf) [[3]](#id8) for further details.

### LoRa

A Semtech SX1272 transceiver chip is present in the module which can be
used in 915MHz LoRa frequency ranges if using an RM191 module or 868MHz
LoRa frequency ranges if uses an RM186 module

Refer to the [Semtech SX1272 datasheet](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v_VBhk1IolDgxwwnOpcS_vTFxPfSEPQbuneK3mWsXlU) [[4]](#id10) for further details.

## Programming and Debugging

The `rm1xx_dvk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ (default) |  |  |  |  |

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF51 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b rm1xx_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging boards
with a Segger IC.

## References

[[1](#id4)]

[https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module](https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id9)]

[https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b\_040.pdf](https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b_040.pdf)

[[4](#id11)]

[https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v\_VBhk1IolDgxwwnOpcS\_vTFxPfSEPQbuneK3mWsXlU](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v_VBhk1IolDgxwwnOpcS_vTFxPfSEPQbuneK3mWsXlU)

[[5](#id13)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf)
