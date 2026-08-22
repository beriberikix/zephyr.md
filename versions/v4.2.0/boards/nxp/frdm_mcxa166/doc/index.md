---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxa166/doc/index.html
original_path: boards/nxp/frdm_mcxa166/doc/index.html
---

# FRDM-MCXA166

Board Overview

[![../../../../_images/frdm_mcxa166.webp](../../../../_images/frdm_mcxa166.webp)
](../../../../_images/frdm_mcxa166.webp)

FRDM-MCXA166

Name:
:   `frdm_mcxa166`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxa166

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxa166/doc/index.rst/../..)

## Overview

FRDM-MCXA166 are compact and scalable development boards for rapid prototyping of
MCX A16X MCUs. They offer industry standard headers for easy access to the MCUs I/Os,
integrated open-standard serial interfaces and an on-board MCU-Link debugger.
MCX A Series are high-performance, low-power microcontrollers with MAU,SmartDMA and performance efficiency.

## Hardware

- MCX-A166 Arm Cortex-M33 microcontroller running at 180 MHz
- 1MB dual-bank on chip Flash
- 256 KB RAM
- 1x FlexCAN with FD, 1x RGB LED, 3x SW buttons
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-A166 SoC and FRDM-MCXA166 board, see:

- [MCX-A166 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-a-series-microcontrollers/mcx-a13x-14x-15x-mcus-with-arm-cortex-m33-scalable-device-options-low-power-and-intelligent-peripherals:MCX-A13X-A14X-A15X)
- [MCX-A166 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXAP100M96FS6.pdf)
- [MCX-A166 Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXAP100M96FS6RM)
- [FRDM-MCXA166 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-a144-5-6-a154-5-6-mcus:FRDM-MCXA166)
- [FRDM-MCXA166 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxa166:GS-FRDM-MCXA166)
- [FRDM-MCXA166 Board User Manual](https://www.nxp.com/docs/en/user-manual/UM12121.pdf)
- [FRDM-MCXA166 Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-90841)

### Supported Features

The `frdm_mcxa166` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The MCX-A166 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO2\_3 | UART | UART RX |
| PIO2\_2 | UART | UART TX |

### System Clock

The MCX-A166 SoC is configured to use FRO running at 180MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXA166 SoC has 6 LPUART interfaces for serial communication.
LPUART 2 is configured as UART for the console.

## Programming and Debugging

The `frdm_mcxa166` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using LinkServer

Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `ISP mode` to program the firmware,
short jumper JP4.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `ISP mode`
by shortening the jumper JP4.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J14) of the board. Additionally, the jumper JP6 must
be shorted.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J15, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa166 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa166/mcxa166
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa166/mcxa166 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa166/mcxa166
```

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
