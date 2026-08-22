---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rza2m_evk/doc/index.html
original_path: boards/renesas/rza2m_evk/doc/index.html
---

# RZ/A2M Evaluation Kit

Board Overview

[![../../../../_images/rza2m_evkit.webp](../../../../_images/rza2m_evkit.webp)
](../../../../_images/rza2m_evkit.webp)

RZ/A2M Evaluation Kit

Name:
:   `rza2m_evk`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7s921053vcbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rza2m_evk/doc/index.rst/../..)

## Overview

The RZ/A2M Evaluation Board Kit is a best evaluation board kit to evaluate RZ/A2M.

- On-board device: RZ/A2M (R7S921053VCBG: with DRP function, without encryption function, internal
  RAM 4MB) Evaluation of DRP (Dynamically Reconfigurable Processor) is possible.
- MIPI Camera Module (MIPI CSI) is bundled and image recognition processing etc. can be used with
  images input with MIPI camera.
- HyperMCP (Multi-chip package), in which HyperFlash and HyperRAM are installed in one package,
  is mounted. HyperFlash and HyperRAM can be evaluated.
- A Display Output Board is included and the graphic output is possible by connecting it to the
  external display.
- It is possible to evaluate 2ch Ethernet communication.
- Other peripheral functions such as SDHI and USB can also be evaluated.
- Allows for safe and secure connection to the AWS cloud.
  HyperFlash and HyperRAM are trademarks of Cypress Semiconductor Corporation of the U.S.

## Hardware

The Renesas RZ/A2M MPU documentation can be found at [RZ/A2M Group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram) [[1]](#id3)

[![RZ/A2M group feature](../../../../_images/rza2m_block_diagram.webp)
](../../../../_images/rza2m_block_diagram.webp)

RZ/A2M block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZ/A2M-EVK Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit) [[2]](#id5)

### Supported Features

The `rza2m_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rza2m_evk/r7s921053vcbg` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| Clock control | on-chip | RZ/A2M Clock Pulse Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L55) | [`renesas,rza2m-cpg`](../../../../build/dts/api/bindings/clock/renesas%2Crza2m-cpg.md#std-dtcompatible-renesas-rza2m-cpg) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L61) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| GPIO & Headers | on-chip | Renesas RZ/A2M GPIO Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L105) | [`renesas,rza2m-gpio-int`](../../../../build/dts/api/bindings/gpio/renesas%2Crza2m-gpio-int.md#std-dtcompatible-renesas-rza2m-gpio-int) |
| on-chip | Renesas RZ/A2M GPIO Controller[22 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L144) | [`renesas,rza2m-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crza2m-gpio.md#std-dtcompatible-renesas-rza2m-gpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L41) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rza2m_evk/rza2m_evk.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rza2m_evk/rza2m_evk.dts?plain=1#L44) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas RZ/A2M pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L101) | [`renesas,rza2m-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crza2m-pinctrl.md#std-dtcompatible-renesas-rza2m-pinctrl) |
| Serial controller | on-chip | Renesas RZ/A2M UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L378)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L322) | [`renesas,rza2m-scif-uart`](../../../../build/dts/api/bindings/serial/renesas%2Crza2m-scif-uart.md#std-dtcompatible-renesas-rza2m-scif-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L50) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Renesas RZ/A2M OS timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L77)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rza/r7s9210.dtsi?plain=1#L85) | [`renesas,rza2m-ostm`](../../../../build/dts/api/bindings/timer/renesas%2Crza2m-ostm.md#std-dtcompatible-renesas-rza2m-ostm) |

## Programming and Debugging

The `rza2m_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rza2m_evk` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Console

The UART port is accessed by USB-Serial port (CN5).

### Building & Flashing

Here is an example for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rza2m_evk samples/hello_world
west flash
```

## References

[[1](#id4)]

[https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit)
