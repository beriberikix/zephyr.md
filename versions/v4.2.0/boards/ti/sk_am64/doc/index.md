---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/sk_am64/doc/index.html
original_path: boards/ti/sk_am64/doc/index.html
---

# SK-AM64

Board Overview

[![../../../../_images/sk_am64.webp](https://docs.zephyrproject.org/4.2.0/_images/sk_am64.webp)
](https://docs.zephyrproject.org/4.2.0/_images/sk_am64.webp)

SK-AM64

Name:
:   `sk_am64`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   am6442

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/sk_am64/doc/index.rst/../..)

## Overview

The SK-AM64 board configuration is used by Zephyr applications that run on
the Cortex-M4F MCU core and the Cortex-R5F cores on TI AM64x platform.

The board configuration also enables support for the semihosting debugging console.

See the [TI AM64 Product Page](https://www.ti.com/product/AM6442) for details.

## Hardware

The SK-AM64 EVM features the AM64 SoC, which is composed of a dual Cortex-A53
cluster and a single Cortex-M4 core in the MCU domain. Zephyr is ported to run on
the M4F core and the following listed hardware specifications are used:

- Low-power ARM Cortex-M4F
  :   - 256KB of SRAM
- 2x ARM Dual-Core Cortex-R5F
  :   - 64KB of SRAM each
- Memory
  :   - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Supported Features

The `sk_am64` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sk_am64/am6442/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L21) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L38) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L56)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_m4.dts?plain=1#L54) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L276)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L14)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L20)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | TI Dual-Mode Timer[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

#### `sk_am64/am6442/r5f0_0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L22) | [`arm,cortex-r5`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5.md#std-dtcompatible-arm-cortex-r5) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | TI Vectored Interrupt Manager is a external interrupt controller (TI specific IP) which is compatible with R5F VIC port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L52) | [`ti,vim`](../../../../build/dts/api/bindings/interrupt-controller/ti%2Cvim.md#std-dtcompatible-ti-vim) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L244)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_r5f0_0.dts?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | TI Dual-Mode Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L86)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

#### `sk_am64/am6442/r5f0_1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L22) | [`arm,cortex-r5`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5.md#std-dtcompatible-arm-cortex-r5) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | TI Vectored Interrupt Manager is a external interrupt controller (TI specific IP) which is compatible with R5F VIC port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L52) | [`ti,vim`](../../../../build/dts/api/bindings/interrupt-controller/ti%2Cvim.md#std-dtcompatible-ti-vim) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L244)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_r5f0_1.dts?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | TI Dual-Mode Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L92)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

#### `sk_am64/am6442/r5f1_0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L22) | [`arm,cortex-r5`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5.md#std-dtcompatible-arm-cortex-r5) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | TI Vectored Interrupt Manager is a external interrupt controller (TI specific IP) which is compatible with R5F VIC port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L52) | [`ti,vim`](../../../../build/dts/api/bindings/interrupt-controller/ti%2Cvim.md#std-dtcompatible-ti-vim) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L260)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_r5f1_0.dts?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | TI Dual-Mode Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L98)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

#### `sk_am64/am6442/r5f1_1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L22) | [`arm,cortex-r5`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5.md#std-dtcompatible-arm-cortex-r5) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | TI Vectored Interrupt Manager is a external interrupt controller (TI specific IP) which is compatible with R5F VIC port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L52) | [`ti,vim`](../../../../build/dts/api/bindings/interrupt-controller/ti%2Cvim.md#std-dtcompatible-ti-vim) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L260)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_r5f1_1.dts?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | TI Dual-Mode Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L104)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 400 MHz.

#### DDR RAM

The board has 2GB of DDR RAM available. This board configuration
allocates Zephyr:

- 1MB for IPC (VirtIO / Vrings)
- 4KB for Linux RemoteProc resource table
- 15MB for general usage

#### Serial Port

This board configuration uses a single serial communication channel with the
MCU domain UART (MCU\_UART0).

#### GPIO

The SK-AM64 has a heartbeat LED connected to MCU\_GPIO0\_6. It’s configured
to build and run the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.

## SD Card

Download TI’s official [WIC](https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-yXgchBCk98/10.01.10.04/tisdk-default-image-am64xx-evm-10.01.10.04.rootfs.wic.xz) and flash the WIC file with an etching software
onto an SD card. This will boot Linux on the A53 application cores of the EVM.
These cores will then load the zephyr binary on the M4 core using remoteproc.

The default configuration can be found in
[boards/ti/sk\_am64/sk\_am64\_am6442\_m4\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am64/sk_am64_am6442_m4_defconfig)

## Flashing

The board can using remoteproc, and uses the OpenAMP resource table to accomplish this.

The testing requires the binary to be copied to the SD card to allow the A53 cores to load it while booting using remoteproc.

To test the M4F core, we build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample with the following command.

```shell
# From the root of the Zephyr repository
west build -p -b sk_am64/am6442/m4 samples/hello_world
```

This builds the program and the binary is present in the `build/zephyr` directory as
`zephyr.elf`.

We now copy this binary onto the SD card in the `/lib/firmware` directory and name it as
`am64-mcu-m4f0_0-fw`.

```shell
# Mount the SD card at sdcard for example
sudo mount /dev/sdX sdcard
# copy the elf to the /lib/firmware directory
sudo cp --remove-destination zephyr.elf sdcard/lib/firmware/am64-mcu-m4f0_0-fw
```

The SD card can now be used for booting. The binary will now be loaded onto the M4F core on boot.

To allow the board to boot using the SD card, set the boot pins to the SD Card boot mode. Refer to [SK-AM64B EVM User’s Guide](https://www.ti.com/lit/ug/spruj64/spruj64.pdf).

After changing the boot mode, the board should go through the boot sequence on powering up.
The binary will run and print Hello world to the MCU\_UART0 port.

## References
