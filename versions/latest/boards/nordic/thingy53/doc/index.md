---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/thingy53/doc/index.html
original_path: boards/nordic/thingy53/doc/index.html
---

# Thingy:53

Board Overview

[![../../../../_images/thingy53.webp](https://docs.zephyrproject.org/4.2.0/_images/thingy53.webp)
](https://docs.zephyrproject.org/4.2.0/_images/thingy53.webp)

Thingy:53

Name:
:   `thingy53`

Vendor:
:   Nordic Semiconductor

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/thingy53/doc/index.rst/../..)

## Overview

Zephyr uses the `thingy53/nrf5340` board configuration for building
for the Thingy:53 board. The board has the nRF5340 MCU processor, a set of
environmental sensors, a pushbutton, and RGB LED.

The nRF5340 is a dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running at
  a fixed 64 MHz, referred to as the **network core**.

The `thingy53/nrf5340/cpuapp` build target provides support for the application
core on the nRF5340 SoC. The `thingy53/nrf5340/cpunet` build target provides
support for the network core on the nRF5340 SoC.

The [Nordic Thingy:53 Hardware guide](https://docs.nordicsemi.com/bundle/ug_thingy53/page/UG/thingy53/intro/frontpage.html) [[1]](#id2) contains the processor’s information and
the datasheet.

## Hardware

### Supported Features

The `thingy53` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `thingy53/nrf5340/cpuapp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L16) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L49) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic,nrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L97) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic,nrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L103) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic,nrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L375) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic,nrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L492) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic,nrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L547) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic,nrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| on-chip | Nordic SPU (System Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L73) | [`nordic,nrf-spu`](../../../../build/dts/api/bindings/arm/nordic,nrf-spu.md#std-dtcompatible-nordic-nrf-spu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L449) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic,nrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic,nrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L64) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L364) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L294) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | ARM TrustZone CryptoCell 312[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L102) | [`arm,cryptocell-312`](../../../../build/dts/api/bindings/crypto/arm,cryptocell-312.md#std-dtcompatible-arm-cryptocell-312) |
| Debug | on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L23) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm,armv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L475) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L531) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L560) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L85)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L94) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This binding provides a nexus mapping for 20 pins (HW rev 1.1.0) as depicted below[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L72) | [`nordic-thingy53-edge-connector`](../../../../build/dts/api/bindings/gpio/nordic-thingy53-edge-connector.md#std-dtcompatible-nordic-thingy53-edge-connector) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L124)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L137) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L94) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L18) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L53) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L42) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L29) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L287) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic,qspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-board | This is a SPI device interface to the nRF21540 Radio Front-End module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L263) | [`nordic,nrf21540-fem-spi`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf21540-fem-spi.md#std-dtcompatible-nordic-nrf21540-fem-spi) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic,nrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic,nrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L433) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| on-board | Fixed voltage regulators[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L110)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L86) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | Bosch BMM150 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L222) | [`bosch,bmm150`](../../../../build/dts/api/compatibles/bosch,bmm150.md#std-dtcompatible-bosch-bmm150) |
| on-board | Bosch BME680 Environmental Sensor (I2C)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L233) | [`bosch,bme680`](../../../../build/dts/api/compatibles/bosch,bme680.md#std-dtcompatible-bosch-bme680) |
| on-board | ADXL362 3-axis SPI accelerometer When setting the accelerometer DTS properties and want to use streaming functionality, make sure to include adxl362.h and use the macros defined there for fifo-mode and fifo-watermark properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L249) | [`adi,adxl362`](../../../../build/dts/api/bindings/sensor/adi,adxl362.md#std-dtcompatible-adi-adxl362) |
| on-board | The BMI270 is an inertial measurement unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L256) | [`bosch,bmi270`](../../../../build/dts/api/compatibles/bosch,bmi270.md#std-dtcompatible-bosch-bmi270) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `thingy53/nrf5340/cpuapp/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic,nrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L97) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic,nrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L103) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic,nrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L375) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic,nrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L492) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic,nrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L547) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic,nrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L449) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic,nrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic,nrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic,nrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L64) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L364) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L294) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L475) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L531) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L560) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L59) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This binding provides a nexus mapping for 20 pins (HW rev 1.1.0) as depicted below[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L72) | [`nordic-thingy53-edge-connector`](../../../../build/dts/api/bindings/gpio/nordic-thingy53-edge-connector.md#std-dtcompatible-nordic-thingy53-edge-connector) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L124)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L137) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L94) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L18) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L53) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L287) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic,qspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-board | This is a SPI device interface to the nRF21540 Radio Front-End module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L263) | [`nordic,nrf21540-fem-spi`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf21540-fem-spi.md#std-dtcompatible-nordic-nrf21540-fem-spi) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic,nrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic,nrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L433) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| on-board | Fixed voltage regulators[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L110)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L86) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | Bosch BMM150 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L222) | [`bosch,bmm150`](../../../../build/dts/api/compatibles/bosch,bmm150.md#std-dtcompatible-bosch-bmm150) |
| on-board | Bosch BME680 Environmental Sensor (I2C)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L233) | [`bosch,bme680`](../../../../build/dts/api/compatibles/bosch,bme680.md#std-dtcompatible-bosch-bme680) |
| on-board | ADXL362 3-axis SPI accelerometer When setting the accelerometer DTS properties and want to use streaming functionality, make sure to include adxl362.h and use the macros defined there for fifo-mode and fifo-watermark properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L249) | [`adi,adxl362`](../../../../build/dts/api/bindings/sensor/adi,adxl362.md#std-dtcompatible-adi-adxl362) |
| on-board | The BMI270 is an inertial measurement unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi?plain=1#L256) | [`bosch,bmi270`](../../../../build/dts/api/compatibles/bosch,bmi270.md#std-dtcompatible-bosch-bmi270) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `thingy53/nrf5340/cpunet` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L21) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L43) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L234) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic,nrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family SWI (Software Interrupt)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L270) | [`nordic,nrf-swi`](../../../../build/dts/api/bindings/arm/nordic,nrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| on-chip | Nordic nRF family ACL (Access Control List)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L298) | [`nordic,nrf-acl`](../../../../build/dts/api/bindings/arm/nordic,nrf-acl.md#std-dtcompatible-nordic-nrf-acl) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L58) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L136) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L146) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L153) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L304) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L121) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L326) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-board | This binding provides a nexus mapping for 20 pins (HW rev 1.1.0) as depicted below[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L75) | [`nordic-thingy53-edge-connector`](../../../../build/dts/api/bindings/gpio/nordic-thingy53-edge-connector.md#std-dtcompatible-nordic-thingy53-edge-connector) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L193) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L100) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L46) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L183) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L36) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L162) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L313) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L144) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L90) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-board | This is a SPI device interface to the nRF21540 Radio Front-End module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L130) | [`nordic,nrf21540-fem-spi`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf21540-fem-spi.md#std-dtcompatible-nordic-nrf21540-fem-spi) |
| on-board | nRF21540 Radio Front-End module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy53/thingy53_nrf5340_cpunet.dts?plain=1#L65) | [`nordic,nrf21540-fem`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf21540-fem.md#std-dtcompatible-nordic-nrf21540-fem) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L65) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L320) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic,nrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L73) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L114) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L175) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L168) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L227) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L210) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L49) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L129) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

## Programming and Debugging

The `thingy53` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ (default) |  |  |  |  |

### Flashing

Flashing Zephyr onto Thingy:53 requires an external J-Link programmer. The
programmer is attached to the P9 programming header.

### Debugging

Thingy:53 does not have an on-board J-Link debug IC as some other nRF5
development boards, however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page
also apply to this board, with the additional step of connecting an external
debugger. A development board with a Debug out connector such as the
[nRF5340 DK](../../nrf5340dk/doc/index.md#nrf5340dk) can be used as a debugger with Thingy:53.

## References

[[1](#id3)]

[https://docs.nordicsemi.com/bundle/ug\_thingy53/page/UG/thingy53/intro/frontpage.html](https://docs.nordicsemi.com/bundle/ug_thingy53/page/UG/thingy53/intro/frontpage.html)
