---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/da1469x_dk_pro/doc/index.html
original_path: boards/renesas/da1469x_dk_pro/doc/index.html
---

# DA1469x Development Kit Pro

Board Overview

[![../../../../_images/da14695-00hqdevkt-board.jpg](https://docs.zephyrproject.org/4.2.0/_images/da14695-00hqdevkt-board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/da14695-00hqdevkt-board.jpg)

DA1469x Development Kit Pro

Name:
:   `da1469x_dk_pro`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   da14699

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/da1469x_dk_pro/doc/index.rst/../..)

## DA1469x Development Kit Pro

### Overview

The DA1469x Development Kit Pro hardware provides support for the Renesas
DA1469x ARM Cortex-M33 MCU family. The development kit consist of a motherboard
with connectors and integrated debugger and an interchangeable daughterboard
with an actual MCU (e.g. DA14695 or DA14699).

### Hardware

DA1469x Development Kit Pro has two external oscillators. The frequency of
the sleep clock is 32768 Hz. The frequency of the system clock is 32 MHz.

#### Supported Features

The `da1469x_dk_pro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

##### `da1469x_dk_pro/da14699` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Renesas SmartBond(tm) ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L303) | [`renesas,smartbond-adc`](../../../../build/dts/api/bindings/adc/renesas%2Csmartbond-gpadc.md#std-dtcompatible-renesas-smartbond-adc) |
| on-chip | Renesas SmartBond(tm) ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L311) | [`renesas,smartbond-sdadc`](../../../../build/dts/api/bindings/adc/renesas%2Csmartbond-sdadc.md#std-dtcompatible-renesas-smartbond-sdadc) |
| Bluetooth | on-chip | Bluetooth HCI for Renesas DA1469x[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L412) | [`renesas,bt-hci-da1469x`](../../../../build/dts/api/bindings/bluetooth/renesas%2Cbt-hci-da1469x.md#std-dtcompatible-renesas-bt-hci-da1469x) |
| Clock control | on-chip | Smartbond low power oscillator[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L55)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L68) | [`renesas,smartbond-lp-osc`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-lp-osc.md#std-dtcompatible-renesas-smartbond-lp-osc) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L80)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L74) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Smartbond system clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L99) | [`renesas,smartbond-sys-clk`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-sys-clock.md#std-dtcompatible-renesas-smartbond-sys-clk) |
| on-chip | Smartbond low power clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L105) | [`renesas,smartbond-lp-clk`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-lp-clock.md#std-dtcompatible-renesas-smartbond-lp-clk) |
| Counter | on-chip | Renesas SmartBond(tm) general purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L241) | [`renesas,smartbond-timer`](../../../../build/dts/api/bindings/counter/renesas%2Csmartbond-timer.md#std-dtcompatible-renesas-smartbond-timer) |
| Cryptographic accelerator | on-chip | Renesas SmartBond(tm) CRYPTO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L320) | [`renesas,smartbond-crypto`](../../../../build/dts/api/bindings/crypto/renesas%2Csmartbond-crypto.md#std-dtcompatible-renesas-smartbond-crypto) |
| Display | on-chip | Renesas Smartbond(tm) display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L354) | [`renesas,smartbond-display`](../../../../build/dts/api/bindings/display/renesas%2Csmartbond-display.md#std-dtcompatible-renesas-smartbond-display) |
| DMA | on-chip | Renesas Smartbond(tm) DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L395) | [`renesas,smartbond-dma`](../../../../build/dts/api/bindings/dma/renesas%2Csmartbond-dma.md#std-dtcompatible-renesas-smartbond-dma) |
| Flash controller | on-chip | Renesas SmartBond(tm) family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L177) | [`renesas,smartbond-flash-controller`](../../../../build/dts/api/bindings/flash_controller/renesas%2Csmartbond-flash-controller.md#std-dtcompatible-renesas-smartbond-flash-controller) |
| GPIO & Headers | on-chip | Renesas SmartBond(tm) GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L200) | [`renesas,smartbond-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Csmartbond-gpio.md#std-dtcompatible-renesas-smartbond-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da1469x_dk_pro/da1469x_dk_pro.dts?plain=1#L46) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Renesas SmartBond(tm) I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L334) | [`renesas,smartbond-i2c`](../../../../build/dts/api/bindings/i2c/renesas%2Csmartbond-i2c.md#std-dtcompatible-renesas-smartbond-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da1469x_dk_pro/da1469x_dk_pro.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da1469x_dk_pro/da1469x_dk_pro.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Renesas Smartbond(tm) NOR/PSRAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L405) | [`renesas,smartbond-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/renesas%2Csmartbond-nor-psram.md#std-dtcompatible-renesas-smartbond-nor-psram) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L187) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da1469x_dk_pro/da1469x_dk_pro.dts?plain=1#L92) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas SmartBond Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L194) | [`renesas,smartbond-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Csmartbond-pinctrl.md#std-dtcompatible-renesas-smartbond-pinctrl) |
| Regulator | on-chip | Renesas Smartbond(tm) LDO and DCDC regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L111) | [`renesas,smartbond-regulator`](../../../../build/dts/api/bindings/regulator/renesas%2Cda1469x-regulator.md#std-dtcompatible-renesas-smartbond-regulator) |
| RNG | on-chip | Renesas Smartbond TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L327) | [`renesas,smartbond-trng`](../../../../build/dts/api/bindings/rng/renesas%2Csmartbond-trng.md#std-dtcompatible-renesas-smartbond-trng) |
| RTC | on-chip | Renesas SmartBond(tm) RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L227) | [`renesas,smartbond-rtc`](../../../../build/dts/api/bindings/rtc/renesas%2Csmartbond-rtc.md#std-dtcompatible-renesas-smartbond-rtc) |
| Serial controller | on-chip | Renesas SmartBond(tm) UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L277)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L285) | [`renesas,smartbond-uart`](../../../../build/dts/api/bindings/serial/renesas%2Csmartbond-uart.md#std-dtcompatible-renesas-smartbond-uart) |
| SPI | on-chip | Renesas SmartBond(tm) SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L361) | [`renesas,smartbond-spi`](../../../../build/dts/api/bindings/spi/renesas%2Csmartbond-spi.md#std-dtcompatible-renesas-smartbond-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L159) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Renesas SmartBond USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L380) | [`renesas,smartbond-usbd`](../../../../build/dts/api/bindings/usb/renesas%2Csmartbond-usbd.md#std-dtcompatible-renesas-smartbond-usbd) |
| Watchdog | on-chip | Smartbond watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L235) | [`renesas,smartbond-watchdog`](../../../../build/dts/api/bindings/watchdog/renesas%2Csmartbond-watchdog.md#std-dtcompatible-renesas-smartbond-watchdog) |

For more information about the DA14695 Development Kit see:

- [DA14695 DK website](https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro) [[1]](#id2)
- [DA14699 daughterboard website](https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard) [[2]](#id4)

#### System Clock

The DA1469x Development Kit Pro is configured to use the 32 MHz external oscillator
on the board.

#### Connections and IOs

The DA1469x Development Kit Pro has one LED and one push button which can be used
by applications. The UART is connected to on-board serial converter and accessible
via USB1 port on motherboard.

The pin connections are as follows:

- LED (red), located on daughterboard = P1.01
- BUTTON, located on motherboard = P0.06
- UART RX, via USB1 on motherboard = P0.08
- UART TX, via USB1 on motherboard = P0.09

### Programming and Debugging

The `da1469x_dk_pro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **ezflashcli** | ✅ (default) |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `da1469x_dk_pro` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

#### Flashing

The DA1469x boots from an external flash connected to QSPI interface. The image
written to flash has to have proper header prepended. The process is simplified
by using dedicated [eZFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[4]](#id8) tool that takes care of writing header and can
handle different types of flash chips connected to DA1469x MCU. Follow instructions
on [ezFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[4]](#id8) to install the tool. Once installed, flashing can be done in the
usual way.

```shell
# From the root of the zephyr repository
west build -b da1469x_dk_pro samples/basic/blinky
west flash
```

#### Debugging

The DA1469x Development Kit Pro includes a [J-Link](https://www.segger.com/jlink-debug-probes.html) [[3]](#id6) adaptor built-in on
motherboard which provides both debugging interface and serial port.
Application can be debugged in the usual way once DA1469x Development Kit Pro
is connected to PC via USB port on motherboard.

### References

[[1](#id3)]

[https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro](https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro)

[[2](#id5)]

[https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard](https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard)

[[3](#id7)]

[https://www.segger.com/jlink-debug-probes.html](https://www.segger.com/jlink-debug-probes.html)

[4]
([1](#id9),[2](#id10))

[https://github.com/ezflash/ezFlashCLI/](https://github.com/ezflash/ezFlashCLI/)
