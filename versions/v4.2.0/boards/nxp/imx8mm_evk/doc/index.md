---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx8mm_evk/doc/index.html
original_path: boards/nxp/imx8mm_evk/doc/index.html
---

# i.MX8MM EVK

Board Overview

Name:
:   `imx8mm_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64, arm

SoC:
:   mimx8mm6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx8mm_evk/doc/index.rst/../..)

## Overview

i.MX8M Mini LPDDR4 EVK board is based on NXP i.MX8M Mini applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M4 core.
Zephyr OS is ported to run on the Cortex®-A53 core.

- Board features:

  - RAM: 2GB LPDDR4
  - Storage:

    - SanDisk 16GB eMMC5.1
    - Micron 32MB QSPI NOR
    - microSD Socket
  - Wireless:

    - WiFi: 2.4/5GHz IEEE 802.11b/g/n
    - Bluetooth: v4.1
  - USB:

    - OTG - 2x type C
  - Ethernet
  - PCI-E M.2
  - Connectors:

    - 40-Pin Dual Row Header
  - LEDs:

    - 1x Power status LED
    - 1x UART LED
  - Debug

    - JTAG 20-pin connector
    - MicroUSB for UART debug, two COM ports for A53 and M4

More information about the board can be found at the
[NXP website](https://www.nxp.com/design/development-boards/i.mx-evaluation-and-development-boards/evaluation-kit-for-thebr-i.mx-8m-mini-applications-processor:8MMINILPD4-EVK).

### Supported Features

The `imx8mm_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

It is recommended to disable peripherals used by the M4 core on the Linux host.

### Devices

#### System Clock

This board configuration uses a system clock frequency of 8 MHz.

The M4 Core is configured to run at a 400 MHz clock speed.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART4. This is used for the M4 and A53 core targets.

## Programming and Debugging (A53)

The `imx8mm_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

There are multiple methods to program and debug Zephyr on the A53 core:

### Option 1. Boot Zephyr by Using JLink Runner

The default runner for the board is JLink, connect the EVK board’s JTAG connector to
the host computer using a J-Link debugger, power up the board and stop the board at
U-Boot command line.

Then use “west flash” or “west debug” command to load the zephyr.bin
image from the host computer and start the Zephyr application on A53 core0.

#### Flash and Run

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mm_evk/mimx8mm6/a53 samples/hello_world
west flash
```

Then the following log could be found on UART4 console:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
Hello World! imx8mm_evk/mimx8mm6/a53
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mm_evk/mimx8mm6/a53 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “cpu” command is used to load and kick Zephyr to Cortex-A secondary Core, Currently
it is supported in : [Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot) (use the branch “uboot\_vxxxx.xx-y.y.y,
xxxx.xx is uboot version and y.y.y is Real-Time Edge Software version, for example
“uboot\_v2023.04-2.9.0” branch is U-Boot v2023.04 used in Real-Time Edge Software release
v2.9.0), and pre-build images and user guide can be found at [Real-Time Edge Software](https://www.nxp.com/rtedge).

#### Step 1: Download Zephyr Image into DDR Memory

Firstly need to download Zephyr binary image into DDR memory, it can use tftp:

```shell
tftp 0x93c00000 zephyr.bin
```

Or copy the Zephyr image `zephyr.bin` SD card and plug the card into the board, for example
if copy to the FAT partition of the SD card, use the following U-Boot command to load the image
into DDR memory (assuming the SD card is dev 1, fat partition ID is 1, they could be changed
based on actual setup):

```shell
fatload mmc 1:1 0x93c00000 zephyr.bin;
```

#### Step 2: Boot Zephyr

Then use the following command to boot Zephyr on the core0:

```shell
dcache off; icache flush; go 0x93c00000;
```

Or use “cpu” command to boot from secondary Core, for example Core1:

```shell
dcache flush; icache flush; cpu 1 release 0x93c00000
```

### Option 3. Boot Zephyr by Using Remoteproc under Linux

When running Linux on the A55 core, it can use the remoteproc framework to load and boot Zephyr,
refer to Real-Time Edge user guide for more details. Pre-build images and user guide can be found
at [Real-Time Edge Software](https://www.nxp.com/rtedge).

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx8mm_evk/mimx8mm6/a53 samples/synchronization
```

This will build an image with the synchronization sample app, boot it and
display the following console output:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
thread_a: Hello World from cpu 0 on mimx8mm_evk!
thread_b: Hello World from cpu 0 on mimx8mm_evk!
thread_a: Hello World from cpu 0 on mimx8mm_evk!
thread_b: Hello World from cpu 0 on mimx8mm_evk!
thread_a: Hello World from cpu 0 on mimx8mm_evk!
```

## Programming and Debugging (M4)

The MIMX8MM EVK board doesn’t have QSPI flash for the M4 and it needs
to be started by the A53 core. The A53 core is responsible to load the M4 binary
application into the RAM, put the M4 in reset, set the M4 Program Counter and
Stack Pointer, and get the M4 out of reset. The A53 can perform these steps at
bootloader level or after the Linux system has booted.

The M4 can use up to 3 different RAMs. These are the memory mapping for A53 and M4:

| Region | Cortex-A53 | Cortex-M4 (System Bus) | Cortex-M4 (Code Bus) | Size |
| --- | --- | --- | --- | --- |
| OCRAM | 0x00900000-0x0093FFFF | 0x20200000-0x2023FFFF | 0x00900000-0x0093FFFF | 256KB |
| TCMU | 0x00800000-0x0081FFFF | 0x20000000-0x2001FFFF |  | 128KB |
| TCML | 0x007E0000-0x007FFFFF |  | 0x1FFE0000-0x1FFFFFFF | 128KB |
| OCRAM\_S | 0x00180000-0x00187FFF | 0x20180000-0x20187FFF | 0x00180000-0x00187FFF | 32KB |

For more information about memory mapping see the
[i.MX 8M Applications Processor Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMX8MMRM) (section 2.1.2 and 2.1.3)

At compilation time you have to choose which RAM will be used. This
configuration is done in the file
[boards/nxp/imx8mm\_evk/imx8mm\_evk\_mimx8mm6\_m4.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_m4.dts)
with “zephyr,flash” (when CONFIG\_XIP=y) and “zephyr,sram” properties.
The available configurations are:

```text
"zephyr,flash"
- &tcml_code
- &ocram_code
- &ocram_s_code

"zephyr,sram"
- &tcmu_sys
- &ocram_sys
- &ocram_s_sys
```

Load and run Zephyr on M4 from A53 using u-boot by copying the compiled
`zephyr.bin` to the first FAT partition of the SD card and plug the SD
card into the board. Power it up and stop the u-boot execution at prompt.

Load the M4 binary onto the desired memory and start its execution using:

```shell
fatload mmc 0:1 0x7e0000 zephyr.bin;bootaux 0x7e0000
```

### Debugging

MIMX8MM EVK board can be debugged by connecting an external JLink
JTAG debugger to the J902 debug connector and to the PC. Then
the application can be debugged using the usual way.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mm_evk/mimx8mm6/m4 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS build zephyr-v2.0.0-1859-g292afe8533c0 *****
Hello World! imx8mm_evk
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
