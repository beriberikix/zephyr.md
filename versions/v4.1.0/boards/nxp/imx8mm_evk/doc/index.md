---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/imx8mm_evk/doc/index.html
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

The Zephyr imx8mm\_evk board for Cortex-A53 configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC-v3 | on-chip | interrupt controller |
| ARM TIMER | on-chip | system clock |
| CLOCK | on-chip | clock\_control |
| PINMUX | on-chip | pinmux |
| RDC | on-chip | Resource Domain Controller |
| UART | on-chip | serial port |
| GPT | on-chip | timer |
| ENET | on-chip | ethernet port |
| GPIO | on-chip | GPIO ports |
| I2C | on-chip | I2C bus |

The Zephyr imx8mm\_evk board for Cortex-M4 supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| CLOCK | on-chip | clock\_control |
| PINMUX | on-chip | pinmux |
| UART | on-chip | serial port-polling; serial port-interrupt |
| GPIO | on-chip | GPIO output GPIO input |

The default configuration can be found in the defconfig file:
[boards/nxp/imx8mm\_evk/imx8mm\_evk\_mimx8mm6\_m4\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_m4_defconfig)

It is recommended to disable peripherals used by the M4 core on the Linux host.

Other hardware features are not currently supported by the port.

### Devices

#### System Clock

This board configuration uses a system clock frequency of 8 MHz.

The M4 Core is configured to run at a 400 MHz clock speed.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART4. This is used for the M4 and A53 core targets.

## Programming and Debugging (A53)

U-Boot “cpu” command is used to load and kick Zephyr to Cortex-A secondary Core, Currently
it is supported in : [Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot) (use the branch “uboot\_vxxxx.xx-y.y.y,
xxxx.xx is uboot version and y.y.y is Real-Time Edge Software version, for example
“uboot\_v2023.04-2.9.0” branch is U-Boot v2023.04 used in Real-Time Edge Software release
v2.9.0), and pre-build images and user guide can be found at [Real-Time Edge Software](https://www.nxp.com/rtedge).

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin to Cortex-A53 Core0:

```shell
fatload mmc 1:1 0x93c00000 zephyr.bin; dcache flush; icache flush; go 0x93c00000
```

Or kick zephyr.bin to the other Cortex-A53 Core, for example Core2:

```shell
fatload mmc 1:1 0x93c00000 zephyr.bin; dcache flush; icache flush; cpu 2 release 0x93c00000
```

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx8mm_evk/mimx8mm6/a53 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it and
display the following ram console output:

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-3575-g44dd713bd883  ***
thread_a: Hello World from cpu 0 on mimx8mm_evk_a53!
thread_b: Hello World from cpu 0 on mimx8mm_evk_a53!
thread_a: Hello World from cpu 0 on mimx8mm_evk_a53!
thread_b: Hello World from cpu 0 on mimx8mm_evk_a53!
thread_a: Hello World from cpu 0 on mimx8mm_evk_a53!
```

Use Jailhouse hypervisor, after root cell linux is up:

```shell
#jailhouse enable imx8mm.cell
#jailhouse cell create imx8mm-zephyr.cell
#jailhouse cell load 1 zephyr.bin -a 0x93c00000
#jailhouse cell start 1
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

### References
