---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/lpcxpresso51u68/doc/index.html
original_path: boards/nxp/lpcxpresso51u68/doc/index.html
---

# LPCXPRESSO51U68

Board Overview

[![../../../../_images/lpcxpresso51u68.jpg](../../../../_images/lpcxpresso51u68.jpg)
](../../../../_images/lpcxpresso51u68.jpg)

LPCXPRESSO51U68

Name:
:   `lpcxpresso51u68`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc51u68

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso51u68/doc/index.rst/../..)

## Overview

The LPCXpresso51u68 development board uses an NXP LPC51U68 MCU based
on an ARM CORTEX-M0+ core.

## Hardware

- LPC51U68 M0+ running at up to 150 MHz
- Memory

  - 256KB of flash memory
  - 96KB of SRAM
- On-board high-speed USB based debug probe with CMSIS-DAP and J-Link protocol
  support, can debug the on-board LPC51U68 or an external target
- External debug probe option
- Tri-color LED, target reset, ISP & interrupt/user buttons for easy testing of
  software functionality
- Expansion options based on Arduino UNO and PMOD™, plus additional expansion
  port pins
- FTDI UART Connector

More information can be found here:

- [LPC51U68 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/high-performance-power-efficient-and-cost-sensitive-arm-cortex-m0-plus-mcus:LPC51U68)
- [LPC51U68 Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC51U68.pdf)

### Supported Features

The `lpcxpresso51u68` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The IOCON controller can be used to configure the LPC51U68 pins.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_0 | UART | USART RX |
| PIO0\_1 | UART | USART TX |
| PIO1\_10 | GPIO | GREEN LED |
| PIO0\_29 | GPIO | RED LED |
| PIO1\_9 | GPIO | BLUE\_LED |
| PIO0\_25 | I2C | I2C SCL |
| PIO0\_26 | I2C | I2C SDA |
| PIO0\_18 | SPI | SPI MISO |
| PIO0\_19 | SPI | SPI SCK |
| PIO0\_20 | SPI | SPI MOSI |
| PIO1\_1 | SPI | SPI SSEL2 |

## Programming and Debugging

The `lpcxpresso51u68` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the LPC-Link2 CMSIS-DAP Onboard Debug Probe,
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not support this probe so you must
reconfigure the board for one of the following debug probes instead.

#### [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to program
the J-Link firmware.

### Configuring a Console

Connect a USB to FTDI RX, TX & GND pins to P3 Connector.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso51u68 samples/hello_world
west flash
```

```shell
***** Booting Zephyr OS build zephyr-v2.6.0-934-g4c438c0c7d13 *****
Hello World! lpcxpresso51u68
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso51u68 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS build zephyr-v2.6.0-934-g4c438c0c7d13 *****
Hello World! lpcxpresso51u68
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
