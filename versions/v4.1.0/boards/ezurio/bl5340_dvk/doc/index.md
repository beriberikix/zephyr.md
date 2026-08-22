---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ezurio/bl5340_dvk/doc/index.html
original_path: boards/ezurio/bl5340_dvk/doc/index.html
---

# BL5340 DVK

Board Overview

[![../../../../_images/bl5340_dvk_top.jpg](../../../../_images/bl5340_dvk_top.jpg)
](../../../../_images/bl5340_dvk_top.jpg)

BL5340 DVK

Name:
:   `bl5340_dvk`

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/bl5340_dvk/doc/index.rst/../..)

## Overview

The BL5340 Development Kit provides support for the Ezurio
BL5340 module which is powered by a dual-core Nordic Semiconductor
nRF5340 ARM Cortex-M33F CPU. The nRF5340 inside the BL5340 module is a
dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running
  at a fixed 64 MHz, referred to as the **network core**.

The `bl5340_dvk/nrf5340/cpuapp` build target provides support for the application
core on the BL5340 module. The `bl5340_dvk/nrf5340/cpunet` build target provides
support for the network core on the BL5340 module. If ARM TrustZone is
used then the `bl5340_dvk/nrf5340/cpuapp` build target provides support for the
non-secure partition of the application core on the BL5340 module.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- IDAU
- I2C
- I2S
- MPU
- NVIC
- PWM
- QSPI
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- USB
- WDT

More information about the module can be found on the
[BL5340 homepage](https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules) [[2]](#id5).

The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
contains the processor’s information and the datasheet.

## Hardware

The BL5340 DVK has two external oscillators. The frequency of
the slow clock is 32.768KHz. The frequency of the main clock
is 32MHz.

### Supported Features

The `bl5340_dvk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `bl5340_dvk/nrf5340/cpuapp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L16) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L284) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L49) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L96) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L102) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L374) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L491) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L546) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| on-chip | Nordic SPU (System Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L72) | [`nordic,nrf-spu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-spu.md#std-dtcompatible-nordic-nrf-spu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L448) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L63) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L363) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L293) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | ARM TrustZone CryptoCell 312[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L101) | [`arm,cryptocell-312`](../../../../build/dts/api/bindings/crypto/arm%2Ccryptocell-312.md#std-dtcompatible-arm-cryptocell-312) |
| DAC | on-board | Microchip MCP4725 12-bit DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L202) | [`microchip,mcp4725`](../../../../build/dts/api/bindings/dac/microchip%2Cmcp4725.md#std-dtcompatible-microchip-mcp4725) |
| Debug | on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L23) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Display | on-board | ILI9340 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L120) | [`ilitek,ili9340`](../../../../build/dts/api/bindings/display/ilitek%2Cili9340.md#std-dtcompatible-ilitek-ili9340) |
| Ethernet | on-board | ENC424J600 standalone 100BASE-T Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L232) | [`microchip,enc424j600`](../../../../build/dts/api/bindings/ethernet/microchip%2Cenc424j600.md#std-dtcompatible-microchip-enc424j600) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L474) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L530) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-board | TCA9538 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L214) | [`ti,tca9538`](../../../../build/dts/api/bindings/gpio/ti%2Ctca9538.md#std-dtcompatible-ti-tca9538) |
| on-chip | NRF5 GPIO node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L559) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L84)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L93) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L85) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L148)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L108) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L455) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L580) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L191) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech%2Cft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L24) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L57) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L464) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L42) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L343) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L29) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | I2C EEPROMs compatible with Atmel’s AT24 family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L176) | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel%2Cat24.md#std-dtcompatible-atmel-at24) |
| on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L298) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic%2Cqspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L357) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L539) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L484) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L70) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L523) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L553) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L416)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L424) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L32) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L39) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L55) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L79) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-board | Microchip MCP7940N I2C RTC with battery-backed SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L208) | [`microchip,mcp7940n`](../../../../build/dts/api/bindings/rtc/microchip%2Cmcp7940n.md#std-dtcompatible-microchip-mcp7940n) |
| on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L323) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | STMicroelectronics LIS2DH 3-axis accelerometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L185) | [`st,lis2dh`](../../../../build/dts/api/compatibles/st%2Clis2dh.md#std-dtcompatible-st-lis2dh) |
| on-board | The BME680 is an integrated environmental sensor that measures temperature, pressure, humidity and air quality[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L197) | [`bosch,bme680`](../../../../build/dts/api/compatibles/bosch%2Cbme680.md#std-dtcompatible-bosch-bme680) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L497) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L141)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L182) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L189)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L124) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L511) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic%2Cnrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L349)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L356) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `bl5340_dvk/nrf5340/cpuapp/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L284) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L96) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L102) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L374) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L491) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L546) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L448) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L63) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L363) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L293) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| DAC | on-board | Microchip MCP4725 12-bit DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L202) | [`microchip,mcp4725`](../../../../build/dts/api/bindings/dac/microchip%2Cmcp4725.md#std-dtcompatible-microchip-mcp4725) |
| Display | on-board | ILI9340 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L120) | [`ilitek,ili9340`](../../../../build/dts/api/bindings/display/ilitek%2Cili9340.md#std-dtcompatible-ilitek-ili9340) |
| Ethernet | on-board | ENC424J600 standalone 100BASE-T Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L232) | [`microchip,enc424j600`](../../../../build/dts/api/bindings/ethernet/microchip%2Cenc424j600.md#std-dtcompatible-microchip-enc424j600) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L474) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L530) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-board | TCA9538 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L214) | [`ti,tca9538`](../../../../build/dts/api/bindings/gpio/ti%2Ctca9538.md#std-dtcompatible-ti-tca9538) |
| on-chip | NRF5 GPIO node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L559) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L58) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L85) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L148)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L108) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L455) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L580) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L191) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech%2Cft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L24) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L57) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L464) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L343) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | I2C EEPROMs compatible with Atmel’s AT24 family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L176) | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel%2Cat24.md#std-dtcompatible-atmel-at24) |
| on-board | QSPI NOR flash supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L298) | [`nordic,qspi-nor`](../../../../build/dts/api/bindings/mtd/nordic%2Cqspi-nor.md#std-dtcompatible-nordic-qspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L357) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L539) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L484) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L70) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L523) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L553) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L416)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L424) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L32) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L39) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L55) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L79) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-board | Microchip MCP7940N I2C RTC with battery-backed SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L208) | [`microchip,mcp7940n`](../../../../build/dts/api/bindings/rtc/microchip%2Cmcp7940n.md#std-dtcompatible-microchip-mcp7940n) |
| on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L323) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-board | STMicroelectronics LIS2DH 3-axis accelerometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L185) | [`st,lis2dh`](../../../../build/dts/api/compatibles/st%2Clis2dh.md#std-dtcompatible-st-lis2dh) |
| on-board | The BME680 is an integrated environmental sensor that measures temperature, pressure, humidity and air quality[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpuapp_common.dtsi?plain=1#L197) | [`bosch,bme680`](../../../../build/dts/api/compatibles/bosch%2Cbme680.md#std-dtcompatible-bosch-bme680) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L497) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L141)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L182) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L189)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L124) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L511) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic%2Cnrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L349)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L356) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `bl5340_dvk/nrf5340/cpunet` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L21) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L43) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L234) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family SWI (Software Interrupt)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L269) | [`nordic,nrf-swi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| on-chip | Nordic nRF family ACL (Access Control List)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L297) | [`nordic,nrf-acl`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-acl.md#std-dtcompatible-nordic-nrf-acl) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L58) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L136) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L146) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L153) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L303) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L121) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L325) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L193) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L100) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L183) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L36) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L162) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L312) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl5340_dvk/bl5340_dvk_nrf5340_cpunet_common.dtsi?plain=1#L38) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L90) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L65) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L319) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L73) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L114) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic%2Cnrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L175) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L168) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L227) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L210) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L49) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L129) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

See [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
for a complete list of hardware features.

### Connections and IOs

An eight-pin GPIO port expander is used to provide additional inputs
and outputs to the BL5340 module.

Refer to the [TI TCA9538 datasheet](https://www.ti.com/lit/gpn/TCA9538) [[4]](#id10) for further details.

#### LEDs

- LED1 (blue) = via TCA9538 port expander channel P4 (active low)
- LED2 (blue) = via TCA9538 port expander channel P5 (active low)
- LED3 (blue) = via TCA9538 port expander channel P6 (active low)
- LED4 (blue) = via TCA9538 port expander channel P7 (active low)

#### Push buttons

- BUTTON1 = SW1 = via TCA9538 port expander channel P0 (active low)
- BUTTON2 = SW2 = via TCA9538 port expander channel P1 (active low)
- BUTTON3 = SW3 = via TCA9538 port expander channel P2 (active low)
- BUTTON4 = SW4 = via TCA9538 port expander channel P3 (active low)
- BOOT = boot (active low)

### External Memory

Several external memory sources are available for the BL5340 DVK. These
are described as follows.

#### Flash Memory

A Macronix MX25R6435FZNIL0 8MB external QSPI Flash memory part is
incorporated for application image storage and large datasets.

Refer to the [Macronix MX25R6435FZNIL0 datasheet](https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf) [[5]](#id12) for further details.

#### EEPROM Memory

A 32KB Giantec GT24C256C-2GLI-TR EEPROM is available via I2C for
storage of infrequently updated data and small datasets.

Refer to the [Giantec GT24C256C-2GLI-TR datasheet](https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C_DS_Cu.pdf) [[6]](#id14) for further details.

#### External Memory

An on-board micro SD card slot is available for use with micro SD cards.

### Sensors

The BL5340 DVK incorporates two sensors for user application testing.
These are described as follows.

#### Temperature, Pressure, Humidity & Air Quality Sensor

A Bosch BME680 Temperature, Pressure, Humidity & Air Quality sensor is
available via I2C for environmental measurement applications.

Refer to the [Bosch BME680 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf) [[7]](#id16) for further details.

#### 3-Axis Accelerometer

An ST Microelectronics LIS3DH 3-Axis Accelerometer is available via I2C
for vibration and motion detection applications.

Refer to the [ST Microelectronics LIS3DH datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf) [[8]](#id18) for further details.

### Ethernet

Cabled 10/100 Base-T Ethernet Connectivity is available via a Microchip
ENC424J600 Ethernet controller.

Refer to the [Microchip ENC424J600 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf) [[9]](#id20) for further details.

### TFT Display & Capacitive Touch Screen Controller

A 2.8 inch, 240 x 320 pixel TFT display with capacitive touch
controller is included with the BL5340 DVK for user interface
application features.

Refer to the [ER\_TFTM028\_4 datasheet](https://www.buydisplay.com/download/manual/ER-TFTM028-4_Datasheet.pdf) [[10]](#id22) for a high level overview of the
display.

An ILI9341 TFT controller is incorporated in the TFT module and
acts as the main controller, controlled via SPI.

Refer to the [ILI9341 datasheet](https://www.buydisplay.com/download/ic/ILI9341.pdf) [[11]](#id24) for further details.

An FT6206 Capacitive Touch Controller, controlled via I2C is
also incorporated in the TFT module.

Refer to the [FT6206 datasheet](https://www.buydisplay.com/download/ic/FT6206.pdf) [[12]](#id26) for further details.

### Real-Time Clock

A real-time clock is available for accurate time data availability.

Refer to the [Microchip MCP7940N datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf) [[13]](#id28) for further details.

### DAC

A 10-bit Digital to Analog Converter is incorporated for generation of
variable voltages.

Refer to the [Microchip MCP4725 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf) [[14]](#id30) for further details.

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id3)) on the application
  core. The IDAU is implemented with the System Protection Unit and is
  used to define secure and non-secure memory maps. By default, all of
  the memory space (Flash, SRAM, and peripheral address space) is
  defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

The BL5340’s application core supports the Armv8-M Security Extension.
Applications built for the `bl5340_dvk/nrf5340/cpuapp` board by default
boot in the Secure state.

The BL5340’s network core does not support the Armv8-M Security
Extension. The IDAU may configure bus accesses by the network core to
have Secure attribute set; the latter allows to build and run Secure
only applications on the BL5340 module.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the BL5340 module may contain a Secure and a Non-Secure
firmware image for the application core. The Secure image can be built
using either Zephyr or [Trusted Firmware M](https://www.trustedfirmware.org/projects/tf-m/) [[15]](#id32) (TF-M). Non-Secure
firmware images are always built using Zephyr. The two alternatives are
described below.

Note

By default the Secure image for BL5340’s application core is
built using TF-M.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the
Non-Secure firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for the application core using `-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

   > - Build the Non-Secure firmware image as a regular Zephyr application
   > - Build a TF-M (secure) firmware image
   > - Merge the output image binaries together
   > - Optionally build a bootloader image (MCUboot)

Note

Depending on the TF-M configuration, an application DTS overlay may
be required, to adjust the Non-Secure image Flash and SRAM starting
address and sizes.

2. Build the application firmware for the network core using
   `-DBOARD=bl5340_dvk/nrf5340/cpunet`.

#### Building the Secure firmware using Zephyr

The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for the application core
   using `-DBOARD=bl5340_dvk/nrf5340/cpuapp` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for the application core
   using `-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`.
3. Merge the two binaries together.
4. Build the application firmware for the network core using
   `-DBOARD=bl5340_dvk/nrf5340/cpunet`.

When building a Secure/Non-Secure application for the BL5340’s
application core, the Secure application will have to set the IDAU
(SPU) configuration to allow Non-Secure access to all CPU resources
utilized by the Non-Secure application firmware. SPU configuration
shall take place before jumping to the Non-Secure application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=bl5340_dvk/nrf5340/cpuapp` for
the firmware running on the BL5340’s application core, and using
`-DBOARD=bl5340_dvk/nrf5340/cpunet` for the firmware running
on the BL5340’s network core.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then you can build and flash
applications as usual ([Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Warning

The BL5340 has a flash read-back protection feature. When flash
read-back protection is active, you will need to recover the chip
before reflashing. If you are flashing with
[west](../../../../develop/west/build-flash-debug.md#west-build-flash-debug), run this command for more
details on the related `--recover` option:

```shell
west flash -H -r nrfjprog --skip-rebuild
```

Note

Flashing and debugging applications on the BL5340 DVK requires
upgrading the nRF Command Line Tools to version 10.12.0 or newer.
Further information on how to install the nRF Command Line Tools can
be found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application running on the
BL5340’s application core.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BL5340 DVK board
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpuapp samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging
boards with a Segger IC.

## Testing Bluetooth on the BL5340 DVK

Many of the Bluetooth examples will work on the BL5340 DVK.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

## References

[[1](#id4)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[[2](#id6)]

[https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules](https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl5340-series-multi-core-bluetooth-52-802154-nfc-modules)

[3]
([1](#id8),[2](#id9))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[4](#id11)]

[https://www.ti.com/lit/gpn/TCA9538](https://www.ti.com/lit/gpn/TCA9538)

[[5](#id13)]

[https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf](https://www.macronix.com/Lists/Datasheet/Attachments/8868/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.6.pdf)

[[6](#id15)]

[https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C\_DS\_Cu.pdf](https://www.giantec-semi.com/juchen1123/uploads/pdf/GT24C256C_DS_Cu.pdf)

[[7](#id17)]

[https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf)

[[8](#id19)]

[https://www.st.com/resource/en/datasheet/lis3dh.pdf](https://www.st.com/resource/en/datasheet/lis3dh.pdf)

[[9](#id21)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf)

[[10](#id23)]

[https://www.buydisplay.com/download/manual/ER-TFTM028-4\_Datasheet.pdf](https://www.buydisplay.com/download/manual/ER-TFTM028-4_Datasheet.pdf)

[[11](#id25)]

[https://www.buydisplay.com/download/ic/ILI9341.pdf](https://www.buydisplay.com/download/ic/ILI9341.pdf)

[[12](#id27)]

[https://www.buydisplay.com/download/ic/FT6206.pdf](https://www.buydisplay.com/download/ic/FT6206.pdf)

[[13](#id29)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/20005010H.pdf)

[[14](#id31)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/22039d.pdf)

[[15](#id33)]

[https://www.trustedfirmware.org/projects/tf-m/](https://www.trustedfirmware.org/projects/tf-m/)
