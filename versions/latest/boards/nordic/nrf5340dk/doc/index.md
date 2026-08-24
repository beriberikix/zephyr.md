---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/nrf5340dk/doc/index.html
original_path: boards/nordic/nrf5340dk/doc/index.html
---

# nRF5340 DK

Board Overview

[![../../../../_images/nrf5340dk.jpg](https://docs.zephyrproject.org/4.2.0/_images/nrf5340dk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/nrf5340dk.jpg)

nRF5340 DK

Name:
:   `nrf5340dk`

Vendor:
:   Nordic Semiconductor

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/nrf5340dk/doc/index.rst/../..)

## Overview

The nRF5340 DK (PCA10095) is a single-board development kit for evaluation
and development on the Nordic nRF5340 System-on-Chip (SoC).

The nRF5340 is a dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running at
  a fixed 64 MHz, referred to as the **network core**.

The `nrf5340dk/nrf5340/cpuapp` build target provides support for the application
core on the nRF5340 SoC. The `nrf5340dk/nrf5340/cpunet` build target provides
support for the network core on the nRF5340 SoC.

nRF5340 SoC provides support for the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- IDAU
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- USB
- WDT

More information about the board can be found at the
[nRF5340 DK website](https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF5340-DK) [[2]](#id4).
The [nRF5340 DK Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf5340/page/keyfeatures_html5.html) [[3]](#id6)
contains the processor’s information and the datasheet.

## Hardware

nRF5340 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf5340dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nrf5340dk/nrf5340/cpuapp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L16) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| on-board | ADC channels exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L31) | [`arduino,uno-adc`](../../../../build/dts/api/bindings/adc/arduino,uno-adc.md#std-dtcompatible-arduino-uno-adc) |
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
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L60) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L42) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L8) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L23) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L42) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L29) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L124) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic,qspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic,nrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic,nrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L425) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L183) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `nrf5340dk/nrf5340/cpuapp/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic,nrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| on-board | ADC channels exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L31) | [`arduino,uno-adc`](../../../../build/dts/api/bindings/adc/arduino,uno-adc.md#std-dtcompatible-arduino-uno-adc) |
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
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L60) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L42) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic,nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L8) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L23) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi?plain=1#L124) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic,qspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic,nrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic,nrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L425) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic,nrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic,nrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L183) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic,nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic,nrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic,nrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `nrf5340dk/nrf5340/cpunet` target

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
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L60) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L193) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L100) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic,nrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_common.dtsi?plain=1#L8) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L183) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic,mbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L36) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L162) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic,nrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L313) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340dk_nrf5340_cpunet.dts?plain=1#L79) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L90) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
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

See [nRF5340 DK Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf5340/page/keyfeatures_html5.html) [[3]](#id6)
for a complete list of nRF5340 DK board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.28
- LED2 (green) = P0.29
- LED3 (green) = P0.30
- LED4 (green) = P0.31

#### Push buttons

- BUTTON1 = SW1 = P0.23
- BUTTON2 = SW2 = P0.24
- BUTTON3 = SW3 = P0.8
- BUTTON4 = SW4 = P0.9
- BOOT = SW5 = boot/reset

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id2)) on the application core.
  The IDAU is implemented with the System Protection Unit and is used to
  define secure and non-secure memory maps. By default, all of the memory
  space (Flash, SRAM, and peripheral address space) is defined to be secure
  accessible only.
- Secure boot.

## Programming and Debugging

The `nrf5340dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ (default) |  |  |  |  |

nRF5340 application core supports the Armv8-M Security Extension.
Applications built for the `nrf5340dk/nrf5340/cpuapp` board by default
boot in the Secure state.

nRF5340 network core does not support the Armv8-M Security Extension.
nRF5340 IDAU may configure bus accesses by the nRF5340 network core
to have Secure attribute set; the latter allows to build and run
Secure only applications on the nRF5340 SoC.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the nRF5340 may contain a Secure and a Non-Secure firmware
image for the application core. The Secure image can be built using either
Zephyr or [Trusted Firmware M](https://www.trustedfirmware.org/projects/tf-m/) [[4]](#id9) (TF-M). Non-Secure firmware
images are always built using Zephyr. The two alternatives are described below.

Note

By default the Secure image for nRF5340 application core is built
using TF-M.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for the application core using `-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

   > - Build the Non-Secure firmware image as a regular Zephyr application
   > - Build a TF-M (secure) firmware image
   > - Merge the output image binaries together
   > - Optionally build a bootloader image (MCUboot)

Note

Depending on the TF-M configuration, an application DTS overlay may be
required, to adjust the Non-Secure image Flash and SRAM starting address
and sizes.

2. Build the application firmware for the network core using
   `-DBOARD=nrf5340dk/nrf5340/cpunet`.

#### Building the Secure firmware using Zephyr

The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for the application core
   using `-DBOARD=nrf5340dk/nrf5340/cpuapp` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for the application core
   using `-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`.
3. Merge the two binaries together.
4. Build the application firmware for the network core using
   `-DBOARD=nrf5340dk/nrf5340/cpunet`.

When building a Secure/Non-Secure application for the nRF5340 application core,
the Secure application will have to set the IDAU (SPU) configuration to allow
Non-Secure access to all CPU resources utilized by the Non-Secure application
firmware. SPU configuration shall take place before jumping to the Non-Secure
application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=nrf5340dk/nrf5340/cpuapp` for
the firmware running on the nRF5340 application core, and using
`-DBOARD=nrf5340dk/nrf5340/cpunet` for the firmware running
on the nRF5340 network core.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then you can build and flash
applications as usual ([Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Warning

The nRF5340 has a flash read-back protection feature. When flash read-back
protection is active, you will need to recover the chip before reflashing.
If you are flashing with [west](../../../../develop/west/build-flash-debug.md#west-build-flash-debug), run
this command for more details on the related `--recover` option:

```shell
west flash -H -r nrfutil --skip-rebuild
```

Note

Flashing and debugging applications on the nRF5340 DK requires
upgrading the nRF Command Line Tools to version 10.12.0. Further
information on how to install the nRF Command Line Tools can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application running on the
nRF5340 application core.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF5340 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic
boards with a Segger IC.

## Testing the LEDs and buttons in the nRF5340 DK

There are 2 samples that allow you to test that the buttons (switches) and
LEDs on the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/nordic/nrf5340dk/nrf5340\_cpuapp\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi).

## References

[[1](#id3)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[[2](#id5)]

[https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF5340-DK](https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF5340-DK)

[3]
([1](#id7),[2](#id8))

[https://docs.nordicsemi.com/bundle/ps\_nrf5340/page/keyfeatures\_html5.html](https://docs.nordicsemi.com/bundle/ps_nrf5340/page/keyfeatures_html5.html)

[[4](#id10)]

[https://www.trustedfirmware.org/projects/tf-m/](https://www.trustedfirmware.org/projects/tf-m/)
