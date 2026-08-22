---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gardena/sgrm/doc/index.html
original_path: boards/gardena/sgrm/doc/index.html
---

# Smart Garden Radio Module

Board Overview

[![../../../../_images/sgrm.webp](../../../../_images/sgrm.webp)
](../../../../_images/sgrm.webp)

Smart Garden Radio Module

Name:
:   `sgrm`

Vendor:
:   GARDENA GmbH

Architecture:
:   arm

SoC:
:   sim3u167

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gardena/sgrm/doc/index.rst/../..)

## Overview

This is a SoM that is used as a radio module by the GARDENA smart gateway ([manual](https://content.tdr.dss.husqvarnagroup.net/pub000094159/doc000240276), [FOSS parts](https://github.com/husqvarnagroup/smart-garden-gateway-public)).

## Hardware

- Silicon Labs [SiM3U167-B-GM](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.SiM3U167-B-GQ?tab=specs) SoC
- Silicon Labs [Si4467](https://www.silabs.com/wireless/proprietary/ezradiopro-sub-ghz-ics/device.si4467?tab=specs) transceiver (via SPI)
- Controls an RGB LED via high drive pins. It’s expected to mirror the state of 3 low-drive pins
  coming from the Linux SoC.
- UART is connected to the Linux SoC. Usually it’s used for PPP, but it can also be used for
  debugging when PPP is not active.

### Supported Features

The `sgrm` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sgrm/sim3u167` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L20) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| Clock control | on-chip | Silabs Si32 PLL clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L41) | [`silabs,si32-pll`](../../../../build/dts/api/bindings/clock/silabs%2Csi32-pll.md#std-dtcompatible-silabs-si32-pll) |
| on-chip | Silabs Si32 AHB clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L48) | [`silabs,si32-ahb`](../../../../build/dts/api/bindings/clock/silabs%2Csi32-ahb.md#std-dtcompatible-silabs-si32-ahb) |
| on-chip | Silabs Si32 APB clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L54) | [`silabs,si32-apb`](../../../../build/dts/api/bindings/clock/silabs%2Csi32-apb.md#std-dtcompatible-silabs-si32-apb) |
| Cryptographic accelerator | on-chip | Si32 AES node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L76) | [`silabs,si32-aes`](../../../../build/dts/api/bindings/crypto/silabs%2Csi32-aes.md#std-dtcompatible-silabs-si32-aes) |
| DMA | on-chip | Si32 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L64) | [`silabs,si32-dma`](../../../../build/dts/api/bindings/dma/silabs%2Csi32-dma.md#std-dtcompatible-silabs-si32-dma) |
| Flash controller | on-chip | Silabs Si32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L87) | [`silabs,si32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/silabs%2Csi32-flash-controller.md#std-dtcompatible-silabs-si32-flash-controller) |
| GPIO & Headers | on-chip | Si32 GPIO node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L116) | [`silabs,si32-gpio`](../../../../build/dts/api/bindings/gpio/silabs%2Csi32-gpio.md#std-dtcompatible-silabs-si32-gpio) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L94) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gardena/sgrm/sgrm.dts?plain=1#L77) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Si32 pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L32) | [`silabs,si32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/silabs%2Csi32-pinctrl.md#std-dtcompatible-silabs-si32-pinctrl) |
| Serial controller | on-chip | Si32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L100) | [`silabs,si32-usart`](../../../../build/dts/api/bindings/serial/silabs%2Csi32-usart.md#std-dtcompatible-silabs-si32-usart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

| Pin | Name | Note |
| --- | --- | --- |
| PB0.0 | TX (O) | Serial connection to the Linux SoM |
| PB0.1 | RX (I) |
| PB0.2 | RTS (O) |
| PB0.3 | CTS (I) |
| PB0.4 | LED red (I) | Controlled by the Linux SoM |
| PB0.5 | LED green (I) |
| PB0.6 | LED blue (I) |
| PB0.13 | TX (O) | UART1 for debugging (no connection to Linux SoM) |
| PB0.14 | RX (I) |
| PB4.0 | LED red (O) | Mirrors PB0.4 |
| PB4.1 | LED green (O) | Mirrors PB0.5 |
| PB4.2 | LED blue (O) | Mirrors PB0.6 |

## Programming and Debugging

### Flashing

The easiest way is to do this via SSH from the Linux SoM that’s connected to the SiM3U SoM.

On your building machine:

```shell
scp -O build/zephyr/zephyr.hex root@IP:/tmp/
```

On the gateway:

```shell
openocd -f board/gardena_radio.cfg -c 'program /tmp/zephyr.hex verify exit'
reset-rm
```

### Debugging

The easiest way is to do this via SSH from the Linux gateway as well:

```shell
openocd -f board/gardena_radio.cfg -c init
```
