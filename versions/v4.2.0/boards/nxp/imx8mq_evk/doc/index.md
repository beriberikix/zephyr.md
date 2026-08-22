---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx8mq_evk/doc/index.html
original_path: boards/nxp/imx8mq_evk/doc/index.html
---

# MIMX8MQ EVK

Board Overview

[![../../../../_images/mimx8mq_evk.jpg](../../../../_images/mimx8mq_evk.jpg)
](../../../../_images/mimx8mq_evk.jpg)

MIMX8MQ EVK

Name:
:   `imx8mq_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimx8mq6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx8mq_evk/doc/index.rst/../..)

## Overview

i.MX8MQ EVK board is based on NXP i.MX8MQ applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M4 core.
Zephyr OS is ported to run on the Cortex®-M4 core.

- Board features:

  - RAM: 3GB LPDDR4
  - Storage:

    - 16GB eMMC5.0
    - 32MB QSPI NOR
    - microSD Socket
  - Wireless:

    - WiFi: 2.4/5GHz IEEE 802.11 a/b/g/n/ac
    - Bluetooth: v4.1
  - USB:

    - OTG - 1x type C
    - HOST - 1x type A
  - Ethernet
  - PCI-E M.2
  - LEDs:

    - 1x Power status LED
    - 1x UART LED
  - Debug

    - JTAG 10-pin connector
    - MicroUSB for UART debug, two COM ports for A53 and M4

More information about the board can be found at the
[NXP website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-8m-applications-processor:MCIMX8M-EVK).

### Supported Features

The `imx8mq_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx8mq_evk/mimx8mq6/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L18) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L26) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L31) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L133) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L58) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L201) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp%2Cimx-mu.md#std-dtcompatible-nxp-imx-mu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L123) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L127) | [`nxp,imx8m-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8m-pinctrl.md#std-dtcompatible-nxp-imx8m-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L177)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L169) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L139) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

MIMX8MQ EVK board was tested with the following pinmux controller
configuration.

| Board Name | SoC Name | Usage |
| --- | --- | --- |
| UART2 RXD | UART2\_TXD | UART Console |
| UART2 TXD | UART2\_RXD | UART Console |

### System Clock

The M4 Core is configured to run at a 266 MHz clock speed.

### Serial Port

The i.MX8MQ SoC has four UARTs. UART\_2 is configured for the console and
the remaining are not used/tested.

## Programming and Debugging

The `imx8mq_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The MIMX8MQ EVK board doesn’t have QSPI flash for the M4 and it needs
to be started by the A53 core. The A53 core is responsible to load the M4 binary
application into the RAM, put the M4 in reset, set the M4 Program Counter and
Stack Pointer, and get the M4 out of reset. The A53 can perform these steps at
bootloader level or after the Linux system has booted.

The M4 can use up to 3 different RAMs. These are the memory mapping for A53 and M4:

| Region | Cortex-A53 | Cortex-M4 (System Bus) | Cortex-M4 (Code Bus) | Size |
| --- | --- | --- | --- | --- |
| OCRAM | 0x00900000-0x0091FFFF | 0x20200000-0x2021FFFF | 0x00900000-0x0091FFFF | 128KB |
| TCMU | 0x00800000-0x0081FFFF | 0x20000000-0x2001FFFF |  | 128KB |
| TCML | 0x007E0000-0x007FFFFF |  | 0x1FFE0000-0x1FFFFFFF | 128KB |
| OCRAM\_S | 0x00180000-0x00187FFF | 0x20180000-0x20187FFF | 0x00180000-0x00187FFF | 32KB |

For more information about memory mapping see the
[i.MX 8M Applications Processor Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMX8MDQLQRM) (section 2.1.2 and 2.1.3)

At compilation time you have to choose which RAM will be used. This
configuration is done in the file [boards/nxp/imx8mq\_evk/imx8mq\_evk\_mimx8mq6\_m4.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mq_evk/imx8mq_evk_mimx8mq6_m4.dts)
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

Load and run Zephyr on M4 from A53 using u-boot.

From an SD cardFrom serial

Copy the compiled `zephyr.bin` to the first FAT partition of the
SD card and plug the SD card into the board. Power it up and stop the u-boot
execution at prompt.

Load the M4 binary onto the desired memory and start its execution using:

```shell
fatload mmc 0:1 0x40480000 zephyr.bin
cp.b 0x40480000 0x7e0000 0x8000
bootaux 0x7e0000
```

This procedure requires `screen` and `lrzsz` to be installed.

Start `screen`, power up the board, and stop the u-boot execution at prompt:

```shell
screen <tty-device> 115200
```

Start `loadx` with offset `7e0000`:

```shell
loadx 7e0000 115200
```

Send the compiled `zephyr.bin` with `sx` by pressing `Ctrl`-`a` followed by `:`
and write:

```shell
exec !! sx </full/path/to/zephyr.bin>
```

Start execution:

```shell
bootaux 0x7e0000
```

### Debugging

MIMX8MQ EVK board can be debugged by connecting an external JLink
JTAG debugger to the J401 debug connector and to the PC. Then
the application can be debugged using the usual way.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mq_evk/mimx8mq6/m4 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS build zephyr-v2.6.99-30942-g6ee70bd22058 *****
Hello World! imx8mq_evk
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
