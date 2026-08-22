---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nordic/nrf54l20pdk/doc/index.html
original_path: boards/nordic/nrf54l20pdk/doc/index.html
---

# nRF54L20 PDK

Board Overview

Name:
:   `nrf54l20pdk`

Vendor:
:   Nordic Semiconductor

Architecture:
:   arm, riscv

SoC:
:   nrf54l20

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/nrf54l20pdk/doc/index.rst/../..)

## Overview

Note

All software for the nRF54L20 SoC is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The nRF54L20 Preview Development Kit hardware provides
support for the Nordic Semiconductor nRF54L20 Arm Cortex-M33 CPU and
the following devices:

- CLOCK
- RRAM
- GPIO
- GRTC
- NVIC
- UARTE

## Hardware

nRF54L20 PDK has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

### Supported Features

The `nrf54l20pdk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nrf54l20pdk/nrf54l20/cpuapp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L26) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L512) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L99) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L241) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L471) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF54L series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L63) | [`nordic,nrf54l-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf54l-lfxo.md#std-dtcompatible-nordic-nrf54l-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF54L series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L69) | [`nordic,nrf54l-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf54l-hfxo.md#std-dtcompatible-nordic-nrf54l-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L759) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L716) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L201) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Debug | on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L34) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Flash controller | on-chip | Nordic RRAMC (Resistive random access memory controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L809) | [`nordic,rram-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Crram-controller.md#std-dtcompatible-nordic-rram-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L191) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L546) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L297) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic TDM (Time division multiplexed audio interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L576) | [`nordic,nrf-tdm`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-tdm.md#std-dtcompatible-nordic-nrf-tdm) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L259) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L48) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L835) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L10) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L34) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic VEVIF (VPR Event Interface) - EVENT RX MODE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf54l20_enga_cpuapp.dtsi?plain=1#L32) | [`nordic,nrf-vevif-event-rx`](../../../../build/dts/api/bindings/mbox/nordic%2Cnrf-vevif-event-rx.md#std-dtcompatible-nordic-nrf-vevif-event-rx) |
| on-chip | Nordic VEVIF (VPR Event Interface) - TASK TX MODE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf54l20_enga_cpuapp.dtsi?plain=1#L42) | [`nordic,nrf-vevif-task-tx`](../../../../build/dts/api/bindings/mbox/nordic%2Cnrf-vevif-task-tx.md#std-dtcompatible-nordic-nrf-vevif-task-tx) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L93) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L125) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| on-chip | Nordic PPIB (Programmable Peripheral Interconnect Bridge)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L131) | [`nordic,nrf-ppib`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ppib.md#std-dtcompatible-nordic-nrf-ppib) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L816) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20_cpuapp_common.dtsi?plain=1#L48) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L248) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L521) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L766) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L485)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L494) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF54L[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L792) | [`nordic,nrf54l-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf54l-regulators.md#std-dtcompatible-nordic-nrf54l-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L799) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L775) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RISC-V architecture | on-chip | VPR coprocessor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L143) | [`nordic,nrf-vpr-coprocessor`](../../../../build/dts/api/bindings/riscv/nordic%2Cnrf-vpr-coprocessor.md#std-dtcompatible-nordic-nrf-vpr-coprocessor) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L528) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L553) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L327)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L181) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L162) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L104) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Nordic GRTC (Global RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L567) | [`nordic,nrf-grtc`](../../../../build/dts/api/bindings/timer/nordic%2Cnrf-grtc.md#std-dtcompatible-nordic-nrf-grtc) |
| on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L844) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L727) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `nrf54l20pdk/nrf54l20/cpuflpr` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Nordic Semiconductor RISC-V VPR CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L41) | [`nordic,vpr`](../../../../build/dts/api/bindings/cpu/nordic%2Cvpr.md#std-dtcompatible-nordic-vpr) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L512) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L99) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L241) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L471) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF54L series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L63) | [`nordic,nrf54l-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf54l-lfxo.md#std-dtcompatible-nordic-nrf54l-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF54L series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L69) | [`nordic,nrf54l-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf54l-hfxo.md#std-dtcompatible-nordic-nrf54l-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L759) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L716) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L201) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Flash controller | on-chip | Nordic RRAMC (Resistive random access memory controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L809) | [`nordic,rram-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Crram-controller.md#std-dtcompatible-nordic-rram-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L191) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L546) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L297) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic TDM (Time division multiplexed audio interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L576) | [`nordic,nrf-tdm`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-tdm.md#std-dtcompatible-nordic-nrf-tdm) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L259) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L48) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | Nordic VPR CLIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L152) | [`nordic,nrf-clic`](../../../../build/dts/api/bindings/interrupt-controller/nordic%2Cnrf-clic.md#std-dtcompatible-nordic-nrf-clic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L10) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20-common.dtsi?plain=1#L34) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic VEVIF (VPR Event Interface) - TASK RX MODE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/nordic/nrf54l20_enga_cpuflpr.dtsi?plain=1#L26) | [`nordic,nrf-vevif-task-rx`](../../../../build/dts/api/bindings/mbox/nordic%2Cnrf-vevif-task-rx.md#std-dtcompatible-nordic-nrf-vevif-task-rx) |
| on-chip | Nordic VEVIF (VPR Event Interface) - EVENT TX MODE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/nordic/nrf54l20_enga_cpuflpr.dtsi?plain=1#L44) | [`nordic,nrf-vevif-event-tx`](../../../../build/dts/api/bindings/mbox/nordic%2Cnrf-vevif-event-tx.md#std-dtcompatible-nordic-nrf-vevif-event-tx) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L93) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L125) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| on-chip | Nordic PPIB (Programmable Peripheral Interconnect Bridge)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L131) | [`nordic,nrf-ppib`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ppib.md#std-dtcompatible-nordic-nrf-ppib) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L823) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf54l20pdk/nrf54l20pdk_nrf54l20_cpuflpr.dts?plain=1#L29) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L248) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L521) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L766) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L485)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L494) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF54L[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L792) | [`nordic,nrf54l-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf54l-regulators.md#std-dtcompatible-nordic-nrf54l-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L799) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L775) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RISC-V architecture | on-chip | VPR coprocessor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L143) | [`nordic,nrf-vpr-coprocessor`](../../../../build/dts/api/bindings/riscv/nordic%2Cnrf-vpr-coprocessor.md#std-dtcompatible-nordic-nrf-vpr-coprocessor) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L528) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L553) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L707)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L181) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L162) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L112) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Nordic GRTC (Global RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L567) | [`nordic,nrf-grtc`](../../../../build/dts/api/bindings/timer/nordic%2Cnrf-grtc.md#std-dtcompatible-nordic-nrf-grtc) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf54l20.dtsi?plain=1#L727) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

## Programming and Debugging

The `nrf54l20pdk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfutil** | ✅ (default) |  |  |  |  |

Applications for the `nrf54l20pdk/nrf54l20/cpuapp` board target can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Applications for the `nrf54l20pdk/nrf54l20/cpuflpr` board target need
to be built using sysbuild to include the `vpr_launcher` image for the application core.

Enter the following command to compile `hello_world` for the FLPR core::
:   west build -p -b nrf54l20pdk/nrf54l20/cpuflpr –sysbuild

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

To build and program the sample to the nRF54L20 PDK, complete the following steps:

First, connect the nRF54L20 PDK to you computer using the IMCU USB port on the PDK.
Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b nrf54l20pdk/nrf54l20/cpuapp samples/hello_world
west flash
```

## Testing the LEDs and buttons in the nRF54L20 PDK

Test the nRF54L20 PDK with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
