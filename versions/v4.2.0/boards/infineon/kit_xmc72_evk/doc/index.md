---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/kit_xmc72_evk/doc/index.html
original_path: boards/infineon/kit_xmc72_evk/doc/index.html
---

# XMC7200 Evaluation Kit

Board Overview

[![../../../../_images/kit_xmc72_evk.webp](https://docs.zephyrproject.org/4.2.0/_images/kit_xmc72_evk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/kit_xmc72_evk.webp)

XMC7200 Evaluation Kit

Name:
:   `kit_xmc72_evk`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc7200d\_e272k8384

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/kit_xmc72_evk/doc/index.rst/../..)

## Overview

The XMC7200 evaluation kit enables you to evaluate and develop your applications using the XMC7200D
microcontroller(hereafter called “XMC7200D”). The XMC7200D is designed for industrial applications
and it is a true programmable embedded system-on-chip, integrating up to two 350-MHz Arm® Cortex®-M7
as the primary application processor, a 100-MHz Arm® Cortex®-M0+ that supports the following:

- Low-power operations
- Up to 8 MB flash and 1 MB SRAM
- Gigabit Ethernet
- CAN FD
- Secure Digital Host Controller (SDHC) supporting SD/SDIO/eMMC interfaces
- Programmable analog and digital peripherals that allow faster time-to-market

The evaluation board has a M.2 interface connector for interfacing radio modules-based on
AIROC™ Wi-Fi & Bluetooth combos, SMIF dual header compatible with Digilent Pmod for interfacing
HYPERBUS™ memories, and headers compatible with Arduino for interfacing Arduino shields.
In addition, the board features an onboard programmer/debugger(KitProg3), a 512-Mbit QSPI NOR flash,
CAN FD transceiver, Gigabit Ethernet PHY transceiver with RJ45 connector interface, a micro-B
connector for USB device interface, three user LEDs, one potentiometer, and two push buttons.
The board supports operating voltages from 3.3 V to 5.0 V for XMC7200D.

## Hardware

For more information about XMC7200D and KIT\_XMC72\_EVK:

- [XMC7200D SoC Website](https://www.infineon.com/cms/en/product/microcontroller/32-bit-industrial-microcontroller-based-on-arm-cortex-m/32-bit-xmc7000-industrial-microcontroller-arm-cortex-m7/xmc7200d-e272k8384aa/) [[1]](#id2)
- [kit\_xmc72\_evk Board Website](https://www.infineon.com/cms/en/product/evaluation-boards/kit_xmc72_evk) [[2]](#id4)

### Kit Features

- Evaluation board for XMC7200D-E272K8384 in BGA package with 272 pins, dual-core Arm®Cortex® M7 CPUs running at 350-MHz and an Arm® Cortex® M0+ CPU running at 100-MHz
- Full-system approach on the board, featuring Gigabit Ethernet PHY and connector, CAN FD transceiver, user LEDs, buttons, and potentiometer
- M.2 interface connector for interfacing radio modules based on AIROC™ Wi-Fi & Bluetooth®combos (currently not - supported)
- Headers compatible with Arduino for interfacing Arduino shields
- Fully compatible with ModusToolbox™ v3.0
- KitProg3 on-board SWD programmer/debugger, USB-UART, and USB-I2C bridge functionality through USB connector
- Digilent dual PMOD SMIF header for interfacing HYPERBUS™ memories (currently not supported)
- A 512-Mbit external QSPI NOR flash
- Evaluation board supports operating voltages from 3.3 V to 5.0 V for XMC7200D

### Kit Contents

- XMC7200 evaluation board
- USB Type-A to Mirco-B cable
- 12V/3A DC power adapter with additional blades
- Six jumper wires (five inches each)
- Quick start guide

### Supported Features

The `kit_xmc72_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `kit_xmc72_evk/xmc7200d_e272k8384/m0p` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200_m0p.dtsi?plain=1#L15) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L371) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Clock control | on-chip | Generic fixed-rate clock provider[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L68)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L100) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L464) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2118) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L11) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L172)[29 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L55) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L17) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L43) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| PWM | on-chip | Infineon CAT1 PWM[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L1291) | [`infineon,cat1-pwm`](../../../../build/dts/api/bindings/pwm/infineon,cat1-pwm.md#std-dtcompatible-infineon-cat1-pwm) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2341) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon,cat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L389) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L37) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Infineon Cat1 low power timer[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L445) | [`infineon,cat1-lp-timer`](../../../../build/dts/api/bindings/timer/infineon,cat1-lp-timer.md#std-dtcompatible-infineon-cat1-lp-timer) |
| on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L438) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

#### `kit_xmc72_evk/xmc7200d_e272k8384/m7_0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200_m7.dtsi?plain=1#L15) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L371) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Clock control | on-chip | Generic fixed-rate clock provider[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L68)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L100) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L464) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2118) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L11) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L172)[29 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L55) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L17) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L43) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| PWM | on-chip | Infineon CAT1 PWM[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L1291) | [`infineon,cat1-pwm`](../../../../build/dts/api/bindings/pwm/infineon,cat1-pwm.md#std-dtcompatible-infineon-cat1-pwm) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2341) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon,cat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L389) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L37) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Infineon Cat1 low power timer[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L445) | [`infineon,cat1-lp-timer`](../../../../build/dts/api/bindings/timer/infineon,cat1-lp-timer.md#std-dtcompatible-infineon-cat1-lp-timer) |
| on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L438) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

#### `kit_xmc72_evk/xmc7200d_e272k8384/m7_1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200_m7.dtsi?plain=1#L15) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L371) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Clock control | on-chip | Generic fixed-rate clock provider[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L68)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/system_clocks.dtsi?plain=1#L100) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L464) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2118) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L11) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L172)[29 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L55) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_xmc72_evk/kit_xmc72_evk_common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L17) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L43) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| PWM | on-chip | Infineon CAT1 PWM[118 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L1291) | [`infineon,cat1-pwm`](../../../../build/dts/api/bindings/pwm/infineon,cat1-pwm.md#std-dtcompatible-infineon-cat1-pwm) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L2341) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon,cat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L389) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L37) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Infineon Cat1 low power timer[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L445) | [`infineon,cat1-lp-timer`](../../../../build/dts/api/bindings/timer/infineon,cat1-lp-timer.md#std-dtcompatible-infineon-cat1-lp-timer) |
| on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/xmc7200/xmc7200.dtsi?plain=1#L438) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

## Programming and Debugging

The `kit_xmc72_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Building

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b kit_xmc72_evk samples/basic/blinky
```

### Flashing

The KIT\_XMC72\_EVK includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3) [[6]](#id12)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [[3]](#id6) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [[4]](#id8) packages include Infineon OpenOCD.
Installing either of these packages will also install Infineon OpenOCD.

If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) [[5]](#id10) release for your system and manually extract the files to a location of your choice.

Note

Linux requires device access rights to be set up for KitProg3. This is handled automatically by the ModusToolbox and ModusToolbox Programming Tools installations. When doing a minimal installation, this can be done manually by executing the script `openocd/udev_rules/install_rules.sh`.

### West Commands

The path to the installed Infineon OpenOCD executable must be available to the `west` tool commands. There are multiple ways of doing this. The example below uses a permanent CMake argument to set the CMake variable `OPENOCD`.

> WindowsLinux
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd.exe
>
> # Do a pristine build once after setting CMake argument
> west build -b kit_xmc72_evk -p always samples/basic/blinky
>
> west flash
> west debug
> ```
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
>
> # Do a pristine build once after setting CMake argument
> west build -b kit_xmc72_evk -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/cms/en/product/microcontroller/32-bit-industrial-microcontroller-based-on-arm-cortex-m/32-bit-xmc7000-industrial-microcontroller-arm-cortex-m7/xmc7200d-e272k8384aa/](https://www.infineon.com/cms/en/product/microcontroller/32-bit-industrial-microcontroller-based-on-arm-cortex-m/32-bit-xmc7000-industrial-microcontroller-arm-cortex-m7/xmc7200d-e272k8384aa/)

[[2](#id5)]

[https://www.infineon.com/cms/en/product/evaluation-boards/kit\_xmc72\_evk](https://www.infineon.com/cms/en/product/evaluation-boards/kit_xmc72_evk)

[[3](#id7)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

[[4](#id9)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

[[5](#id11)]

[https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

[[6](#id13)]

[https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)
