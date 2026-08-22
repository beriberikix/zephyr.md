---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/lpcxpresso55s06/doc/index.html
original_path: boards/nxp/lpcxpresso55s06/doc/index.html
---

# LPCXpresso55S06

Board Overview

[![../../../../_images/lpcxpress55s06.jpg](../../../../_images/lpcxpress55s06.jpg)
](../../../../_images/lpcxpress55s06.jpg)

LPCXpresso55S06

Name:
:   `lpcxpresso55s06`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc55s06

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso55s06/doc/index.rst/../..)

## Overview

The LPCXpresso55S06 board provides the ideal platform for evaluation
of the LPC55S0x/LPC550x MCU family, based on the Arm® Cortex®-M33
architecture. Arduino® UNO compatible shield connectors are included,
with additional expansion ports around the Arduino footprint, along
with a PMod/host interface port and MikroElektronika Click module
site.

## Hardware

- LPC55S06 Arm® Cortex®-M33 microcontroller running at up to 96 MHz
- 256 KB flash and 96 KB SRAM on-chip
- LPC-Link2 debug high speed USB probe with VCOM port
- MikroElektronika Click expansion option
- LPCXpresso expansion connectors compatible with Arduino UNO
- PMod compatible expansion / host connector
- Reset, ISP, wake, and user buttons for easy testing of software functionality
- Tri-color LED
- UART header for external serial to USB cable
- CAN Transceiver
- NXP FXOS8700CQ accelerometer

For more information about the LPC55S06 SoC and LPCXPresso55S06 board, see:

- [LPC55S06 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
- [LPC55S06 User Manual](https://www.nxp.com/docs/en/user-guide/UM11424.pdf)
- [LPCXpresso55S06 Website](https://www.nxp.com/design/development-boards/lpcxpresso-boards/lpcxpresso-development-board-for-lpc55s0x-0x-family-of-mcus:LPC55S06-EVK)
- [LPCXpresso55S06 User Manual](https://www.nxp.com/docs/en/user-guide/LPCXpresso55S06UM.pdf)
- [LPCXpresso55S06 Development Board Design Files](https://www.nxp.com/downloads/en/design-support/LPCXPRESSSO55S06-DESIGN-FILES.zip)

### Supported Features

The `lpcxpresso55s06` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `lpcxpresso55s06/lpc55s06` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ARM architecture | on-chip | LPC Flexcomm node[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L163) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| CAN | on-chip | NXP LPC SoC series MCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L237) | [`nxp,lpc-mcan`](../../../../build/dts/api/bindings/can/nxp%2Clpc-mcan.md#std-dtcompatible-nxp-lpc-mcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L68) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Flash controller | on-chip | NXP (In-Application Programming) flash memory controller for the lpc55xxx family, except lpc553x[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L78) | [`nxp,iap-fmc55`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ciap-fmc55.md#std-dtcompatible-nxp-iap-fmc55) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L120) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L125) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Mikro BUS headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s06/lpcxpresso55s06_common.dtsi?plain=1#L70) | [`mikro-bus`](../../../../build/dts/api/bindings/gpio/mikro-bus.md#std-dtcompatible-mikro-bus) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s06/lpcxpresso55s06_common.dtsi?plain=1#L93) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L98) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s06/lpcxpresso55s06_common.dtsi?plain=1#L51) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L142) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s06/lpcxpresso55s06_common.dtsi?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L24) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L85)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L92) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s06/lpcxpresso55s06_common.dtsi?plain=1#L122) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L109) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | LPC pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L115) | [`nxp,lpc-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L72) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp%2Clpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RNG | on-chip | LPC RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L248) | [`nxp,lpc-rng`](../../../../build/dts/api/bindings/rng/nxp%2Clpc-rng.md#std-dtcompatible-nxp-lpc-rng) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L154) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L226) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S0x_common.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

Note

For additional features not yet supported, please also refer to the
[LPCXPRESSO55S69](../../lpcxpresso55s69/doc/index.md#lpcxpresso55s69) , which is the superset board in NXP’s LPC55xx series.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the lpcxpresso55s69 board may have additional features
already supported, which can also be re-used on this lpcxpresso55s06 board:

### Connections and IOs

The LPC55S06 SoC has IOCON registers, which can be used to configure
the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_5 | GPIO | ISP SW4 |
| PIO0\_29 | USART | USART RX |
| PIO0\_30 | USART | USART TX |
| PIO1\_4 | GPIO | RED LED |
| PIO1\_6 | GPIO | BLUE\_LED |
| PIO1\_7 | GPIO | GREEN LED |
| PIO1\_9 | GPIO | USR SW3 |
| PIO1\_18 | GPIO | Wakeup SW1 |

### System Clock

The LPC55S06 SoC is configured to use the internal FRO at 96MHz as a
source for the system clock. Other sources for the system clock are
provided in the SOC, depending on your system requirements.

### Serial Port

The LPC55S06 SoC has 8 FLEXCOMM interfaces for serial
communication. One is configured as USART for the console
and the remaining are not used.

## Programming and Debugging

The `lpcxpresso55s06` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

LinkServer is the default runner for this board.
A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the integrated [MCU-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-onboard-debug-probe)
in the CMSIS-DAP mode. To use this probe with Zephyr, you need to install the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging) for additional
information.

The integrated MCU-Link hardware can also be used as a J-Link probe with a
firmware update, as described in [MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
The [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) should be available in this case.

### Configuring a Console

Connect a USB cable from your PC to J1 (LINK2), and use the serial
terminal of your choice (minicom, putty, etc.) with the following
settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s06 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.0.0 *****
Hello World! lpcxpresso55s06
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s06 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v3.0.0 *****
Hello World! lpcxpresso55s06
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
