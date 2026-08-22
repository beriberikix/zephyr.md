---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx8mn_evk/doc/index.html
original_path: boards/nxp/imx8mn_evk/doc/index.html
---

# i.MX8MN EVK (Cortex-A53)

Board Overview

Name:
:   `imx8mn_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64

SoC:
:   mimx8mn6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx8mn_evk/doc/index.rst/../..)

## Overview

i.MX8M Nano LPDDR4 EVK board is based on NXP i.MX8M Nano applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M7 core.
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
    - MicroUSB for UART debug, two COM ports for A53 and M7

More information about the board can be found at the
[NXP website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-8m-nano-applications-processor:8MNANOD4-EVK).

### Supported Features

The `imx8mn_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx8mn_evk/mimx8mn6/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L45)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L27) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L183) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L266) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L273) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Qualcomm Atheros AR8031 Ethernet PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mn_evk/imx8mn_evk_mimx8mn6_a53.dts?plain=1#L59) | [`qca,ar8031`](../../../../build/dts/api/bindings/ethernet/phy/qca%2Car8031.md#std-dtcompatible-qca-ar8031) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L288) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L75)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L89) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | PCA6416 I2C-based GPIO expander[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mn_evk/imx8mn_evk_mimx8mn6_a53.dts?plain=1#L83) | [`nxp,pca6416`](../../../../build/dts/api/bindings/gpio/nxp%2Cpca6416.md#std-dtcompatible-nxp-pca6416) |
| I2C | on-chip | NXP II2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L237)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L213) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L66) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L282) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L261) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp%2Crdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L168) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L172) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L201)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L189) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L53) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L146) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |

#### `imx8mn_evk/mimx8mn6/a53/smp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L39)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L27) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L183) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L266) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L273) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Qualcomm Atheros AR8031 Ethernet PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mn_evk/imx8mn_evk_mimx8mn6_a53_smp.dts?plain=1#L59) | [`qca,ar8031`](../../../../build/dts/api/bindings/ethernet/phy/qca%2Car8031.md#std-dtcompatible-qca-ar8031) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L288) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L75) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L213) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L66) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L282) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L261) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp%2Crdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L168) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L172) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Power management CPU operations | on-board | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mn_evk/imx8mn_evk_mimx8mn6_a53_smp.dts?plain=1#L32) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L201)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L189) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L53) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mn_a53.dtsi?plain=1#L146) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 8 MHz.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART4.

## Programming and Debugging

The `imx8mn_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

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
west build -b imx8mn_evk/mimx8mn6/a53 samples/hello_world
west flash
```

Then the following log could be found on UART4 console:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
Hello World! imx8mn_evk/mimx8mn6/a53
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mn_evk/mimx8mn6/a53 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “cpu” command is used to load and kick Zephyr to Cortex-A secondary Core, Currently
it has been supported in latest U-Boot version by [patch serials](https://patchwork.ozlabs.org/project/uboot/list/?series=417536&archive=both&state=*).

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

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx8mn_evk/mimx8mn6/a53 samples/synchronization
```

This will build an image with the synchronization sample app, boot it and
display the following ram console output:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
thread_a: Hello World from cpu 0 on mimx8mn_evk!
thread_b: Hello World from cpu 0 on mimx8mn_evk!
thread_a: Hello World from cpu 0 on mimx8mn_evk!
thread_b: Hello World from cpu 0 on mimx8mn_evk!
thread_a: Hello World from cpu 0 on mimx8mn_evk!
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
