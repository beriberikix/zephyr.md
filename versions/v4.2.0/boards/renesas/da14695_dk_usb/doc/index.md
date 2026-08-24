---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/da14695_dk_usb/doc/index.html
original_path: boards/renesas/da14695_dk_usb/doc/index.html
---

# DA14695 Development Kit USB

Board Overview

[![../../../../_images/da14695-00hqdevkt-u-usb-board.jpg](https://docs.zephyrproject.org/4.2.0/_images/da14695-00hqdevkt-u-usb-board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/da14695-00hqdevkt-u-usb-board.jpg)

DA14695 Development Kit USB

Name:
:   `da14695_dk_usb`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   da14695

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/da14695_dk_usb/doc/index.rst/../..)

## DA14695 Development Kit USB

### Overview

The DA14695 Development Kit USB is a low cost development board for DA14695.
The development kit comes with an integrated debugger and an USB hub
to have both the on-chip USB and the J-Link connected via a single port.

### Hardware

DA14695 Development Kit USB has two external oscillators. The frequency of
the sleep clock is 32768 Hz. The frequency of the system clock is 32 MHz.

#### Supported Features

The `da14695_dk_usb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

##### `da14695_dk_usb/da14695` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Renesas SmartBond(tm) ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L303) | [`renesas,smartbond-adc`](../../../../build/dts/api/bindings/adc/renesas%2Csmartbond-gpadc.md#std-dtcompatible-renesas-smartbond-adc) |
| on-chip | Renesas SmartBond(tm) ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L311) | [`renesas,smartbond-sdadc`](../../../../build/dts/api/bindings/adc/renesas%2Csmartbond-sdadc.md#std-dtcompatible-renesas-smartbond-sdadc) |
| Bluetooth | on-chip | Bluetooth HCI for Renesas DA1469x[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L412) | [`renesas,bt-hci-da1469x`](../../../../build/dts/api/bindings/bluetooth/renesas%2Cbt-hci-da1469x.md#std-dtcompatible-renesas-bt-hci-da1469x) |
| Clock control | on-chip | Smartbond low power oscillator[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L55) | [`renesas,smartbond-lp-osc`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-lp-osc.md#std-dtcompatible-renesas-smartbond-lp-osc) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L80)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L74) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Smartbond system clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L99) | [`renesas,smartbond-sys-clk`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-sys-clock.md#std-dtcompatible-renesas-smartbond-sys-clk) |
| on-chip | Smartbond low power clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L105) | [`renesas,smartbond-lp-clk`](../../../../build/dts/api/bindings/clock/renesas%2Csmartbond-lp-clock.md#std-dtcompatible-renesas-smartbond-lp-clk) |
| Counter | on-chip | Renesas SmartBond(tm) general purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L241) | [`renesas,smartbond-timer`](../../../../build/dts/api/bindings/counter/renesas%2Csmartbond-timer.md#std-dtcompatible-renesas-smartbond-timer) |
| Cryptographic accelerator | on-chip | Renesas SmartBond(tm) CRYPTO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L320) | [`renesas,smartbond-crypto`](../../../../build/dts/api/bindings/crypto/renesas%2Csmartbond-crypto.md#std-dtcompatible-renesas-smartbond-crypto) |
| Display | on-chip | Renesas Smartbond(tm) display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L354) | [`renesas,smartbond-display`](../../../../build/dts/api/bindings/display/renesas%2Csmartbond-display.md#std-dtcompatible-renesas-smartbond-display) |
| DMA | on-chip | Renesas Smartbond(tm) DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L395) | [`renesas,smartbond-dma`](../../../../build/dts/api/bindings/dma/renesas%2Csmartbond-dma.md#std-dtcompatible-renesas-smartbond-dma) |
| Flash controller | on-chip | Renesas SmartBond(tm) family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L177) | [`renesas,smartbond-flash-controller`](../../../../build/dts/api/bindings/flash_controller/renesas%2Csmartbond-flash-controller.md#std-dtcompatible-renesas-smartbond-flash-controller) |
| GPIO & Headers | on-chip | Renesas SmartBond(tm) GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L200) | [`renesas,smartbond-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Csmartbond-gpio.md#std-dtcompatible-renesas-smartbond-gpio) |
| on-board | GPIO pins exposed on Mikro BUS headers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L41) | [`mikro-bus`](../../../../build/dts/api/bindings/gpio/mikro-bus.md#std-dtcompatible-mikro-bus) |
| I2C | on-chip | Renesas SmartBond(tm) I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L334) | [`renesas,smartbond-i2c`](../../../../build/dts/api/bindings/i2c/renesas%2Csmartbond-i2c.md#std-dtcompatible-renesas-smartbond-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Renesas Smartbond(tm) NOR/PSRAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L405) | [`renesas,smartbond-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/renesas%2Csmartbond-nor-psram.md#std-dtcompatible-renesas-smartbond-nor-psram) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L187) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L102) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas SmartBond Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L194) | [`renesas,smartbond-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Csmartbond-pinctrl.md#std-dtcompatible-renesas-smartbond-pinctrl) |
| Regulator | on-chip | Renesas Smartbond(tm) LDO and DCDC regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L111) | [`renesas,smartbond-regulator`](../../../../build/dts/api/bindings/regulator/renesas%2Cda1469x-regulator.md#std-dtcompatible-renesas-smartbond-regulator) |
| RNG | on-chip | Renesas Smartbond TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L327) | [`renesas,smartbond-trng`](../../../../build/dts/api/bindings/rng/renesas%2Csmartbond-trng.md#std-dtcompatible-renesas-smartbond-trng) |
| RTC | on-chip | Renesas SmartBond(tm) RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L227) | [`renesas,smartbond-rtc`](../../../../build/dts/api/bindings/rtc/renesas%2Csmartbond-rtc.md#std-dtcompatible-renesas-smartbond-rtc) |
| Serial controller | on-chip | Renesas SmartBond(tm) UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L277) | [`renesas,smartbond-uart`](../../../../build/dts/api/bindings/serial/renesas%2Csmartbond-uart.md#std-dtcompatible-renesas-smartbond-uart) |
| SPI | on-chip | Renesas SmartBond(tm) SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L361) | [`renesas,smartbond-spi`](../../../../build/dts/api/bindings/spi/renesas%2Csmartbond-spi.md#std-dtcompatible-renesas-smartbond-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L159) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Renesas SmartBond USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L380) | [`renesas,smartbond-usbd`](../../../../build/dts/api/bindings/usb/renesas%2Csmartbond-usbd.md#std-dtcompatible-renesas-smartbond-usbd) |
| Watchdog | on-chip | Smartbond watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L235) | [`renesas,smartbond-watchdog`](../../../../build/dts/api/bindings/watchdog/renesas%2Csmartbond-watchdog.md#std-dtcompatible-renesas-smartbond-watchdog) |

For more information about the DA14695 Development Kit see:

- [DA14695 DK USB website](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit) [[1]](#id2)

#### System Clock

The DA14695 Development Kit USB is configured to use the 32 MHz external oscillator
on the board.

#### Connections and IOs

The DA14695 Development Kit USB has one LED and one push button which can be used
by applications. The UART is connected to on-board serial converter and accessible
via USB1 port on motherboard.

The pin connections are as follows:

- LED (red), = P1.01
- BUTTON, labeled k1 = P0.06
- UART RX, connected to J-Link serial = P0.08
- UART TX, connected to J-Link serial = P0.09

### Programming and Debugging

The `da14695_dk_usb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **ezflashcli** | ✅ (default) |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `da14695_dk_usb` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

#### Flashing

The DA14695 boots from an external flash connected to QSPI interface. The image
written to flash has to have proper header prepended. The process is simplified
by using dedicated [eZFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[3]](#id6) tool that takes care of writing header and can
handle different types of flash chips connected to DA1469x MCU. Follow instructions
on [ezFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[3]](#id6) to install the tool. Once installed, flashing can be done in the
usual way.

```shell
# From the root of the zephyr repository
west build -b da14695_dk_usb samples/basic/blinky
west flash
```

#### Debugging

The DA14695 Development Kit USB includes a [J-Link](https://www.segger.com/jlink-debug-probes.html) [[2]](#id4) adaptor built-in
which provides both debugging interface and serial port.
Application can be debugged in the usual way once DA14695 Development Kit USB
is connected to PC via USB.

### References

[[1](#id3)]

[https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit)

[[2](#id5)]

[https://www.segger.com/jlink-debug-probes.html](https://www.segger.com/jlink-debug-probes.html)

[3]
([1](#id7),[2](#id8))

[https://github.com/ezflash/ezFlashCLI/](https://github.com/ezflash/ezFlashCLI/)
