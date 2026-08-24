---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html
original_path: boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html
---

# SiM3U1xx 32-bit MCU USB Development Kit

Board Overview

[![../../../../../_images/sim3u1xx_dk.webp](https://docs.zephyrproject.org/4.2.0/_images/sim3u1xx_dk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/sim3u1xx_dk.webp)

SiM3U1xx 32-bit MCU USB Development Kit

Name:
:   `sim3u1xx_dk`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   sim3u167

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sim3u1xx_dk/doc/index.rst/../..)

## Overview

This is a [development kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit) [[3]](#id6) that is used to develop software for the SiM3U1xx MCUs.

## Hardware

- Silicon Labs SiM3U167-B-GM SoC
- CPU core: ARM Cortex®-M3
- Flash memory: 256 kB
- RAM: 32 kB
- IO:

  - 2x user LEDs
  - 2x user push buttons
  - 2x power LEDs
  - Reset push button
  - Potentiometer
  - Analog terminals
  - Capacitive sensing slider and button
  - USB virtual COM port

For more information about the SiM3U167 SoC and the SiM3U1xx board, refer to these documents:

- Silicon Labs [SiM3U1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx) [[1]](#id2)
- Silicon Labs [SiM3U167-B-GM](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm) [[2]](#id4)
- Silicon Labs [SiM3U1xx-B-DK](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit) [[3]](#id6)
- Silicon Labs SiM3U1xx-B-DK MCU card [user’s guide](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf) [[4]](#id8)
- Silicon Labs SiM3U1xx and SiM3C1xx Revision B [Errata](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf) [[5]](#id10)

### Supported Features

The `sim3u1xx_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sim3u1xx_dk/sim3u167` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L20) | [`arm,cortex-m3`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| Clock control | on-chip | Silabs Si32 PLL clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L41) | [`silabs,si32-pll`](../../../../../build/dts/api/bindings/clock/silabs,si32-pll.md#std-dtcompatible-silabs-si32-pll) |
| on-chip | Silabs Si32 AHB clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L48) | [`silabs,si32-ahb`](../../../../../build/dts/api/bindings/clock/silabs,si32-ahb.md#std-dtcompatible-silabs-si32-ahb) |
| on-chip | Silabs Si32 APB clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L54) | [`silabs,si32-apb`](../../../../../build/dts/api/bindings/clock/silabs,si32-apb.md#std-dtcompatible-silabs-si32-apb) |
| Cryptographic accelerator | on-chip | Si32 AES node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L76) | [`silabs,si32-aes`](../../../../../build/dts/api/bindings/crypto/silabs,si32-aes.md#std-dtcompatible-silabs-si32-aes) |
| DMA | on-chip | Si32 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L64) | [`silabs,si32-dma`](../../../../../build/dts/api/bindings/dma/silabs,si32-dma.md#std-dtcompatible-silabs-si32-dma) |
| Flash controller | on-chip | Silabs Si32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L87) | [`silabs,si32-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,si32-flash-controller.md#std-dtcompatible-silabs-si32-flash-controller) |
| GPIO & Headers | on-chip | Si32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L116) | [`silabs,si32-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,si32-gpio.md#std-dtcompatible-silabs-si32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sim3u1xx_dk/sim3u1xx_dk.dts?plain=1#L45) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sim3u1xx_dk/sim3u1xx_dk.dts?plain=1#L31) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L94) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sim3u1xx_dk/sim3u1xx_dk.dts?plain=1#L99) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Si32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L32) | [`silabs,si32-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,si32-pinctrl.md#std-dtcompatible-silabs-si32-pinctrl) |
| Serial controller | on-chip | Si32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L100)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L108) | [`silabs,si32-usart`](../../../../../build/dts/api/bindings/serial/silabs,si32-usart.md#std-dtcompatible-silabs-si32-usart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L28) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

| Pin | Name | Note |
| --- | --- | --- |
| PB1.12 | TX (O) | Serial connection to host via USB virtual COM port |
| PB1.13 | RX (I) |
| PB1.14 | RTS (O) |
| PB1.15 | CTS (I) |
| PB2.8 | Push button switch (SW2) |  |
| PB2.9 | Push button switch (SW3) |  |
| PB2.10 | Red LED (DS3) |  |
| PB2.11 | Yellow LED (DS4) |  |
| PB1.5 | Potentiometer |  |
| PB2.12 | Potentiometer bias |  |

## Programming and Debugging

The `sim3u1xx_dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example. Build the Zephyr kernel and
application:

```shell
# From the root of the zephyr repository
west build -b sim3u1xx_dk samples/hello_world
```

Connect the sim3u1xx\_dk to your host computer using both USB port and you should see a USB serial
connection.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! sim3u1xx_dk/sim3u167
```

## References

[[1](#id3)]

[https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx)

[[2](#id5)]

[https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm)

[3]
([1](#id7),[2](#id12))

[https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)

[[4](#id9)]

[https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf)

[[5](#id11)]

[https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf)
