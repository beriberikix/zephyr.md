---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/npcm400_evb/doc/index.html
original_path: boards/nuvoton/npcm400_evb/doc/index.html
---

# NPCM400\_EVB

Board Overview

[![../../../../_images/npcm400_evb.webp](https://docs.zephyrproject.org/4.1.0/_images/npcm400_evb.webp)
](https://docs.zephyrproject.org/4.1.0/_images/npcm400_evb.webp)

NPCM400\_EVB

Name:
:   `npcm400_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npcm400

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npcm400_evb/doc/index.rst/../..)

## Overview

The NPCM400\_EVB kit is a development platform to evaluate the
Nuvoton NPCM4 series microcontrollers. This board needs to be mated with
part number NPCM400 Satellite Management Controller (SMC).

## Hardware

- ARM Cortex-M4F Processor
- Core clock up to 100 MHz
- 1MB Integrated Flash
- 32KB cache for XIP and Data
- 768 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- I2C/I3C
- RMII
- USB2.0 Device
- USB1.1 Host
- Secure Boot is supported

### Supported Features

The `npcm400_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `npcm400_evb/npcm400` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcm/npcm.dtsi?plain=1#L18) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| Clock control | on-chip | Nuvoton, NPCM PCC (Power and Clock Controller) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcm/npcm.dtsi?plain=1#L38) | [`nuvoton,npcm-pcc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnpcm-pcc.md#std-dtcompatible-nuvoton-npcm-pcc) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcm400.dtsi?plain=1#L16) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcm/npcm.dtsi?plain=1#L26) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

Nuvoton to provide the schematic for this board.

### Serial Port

UART0 is configured for serial logs. The default serial setup is 115200 8N1.

## Programming and Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG-only sessions.

### Flashing

If the correct headers are installed, this board supports J-TAG.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b npcm400_evb samples/hello_world
west flash
```

Open a serial terminal, and you should see the following message in the terminal:

```shell
Hello World! npcm400_evb/npcm400
```

### Debugging

Use JTAG/SWD with a J-Link

## References
