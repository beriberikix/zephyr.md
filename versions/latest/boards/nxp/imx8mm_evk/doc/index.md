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

#### `imx8mm_evk/mimx8mm6/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L45)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L27) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L182) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L265) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L272) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Qualcomm Atheros AR8031 Ethernet PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_a53.dts?plain=1#L59) | [`qca,ar8031`](../../../../build/dts/api/bindings/ethernet/phy/qca%2Car8031.md#std-dtcompatible-qca-ar8031) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L287) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L75)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L89) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | PCA6416 I2C-based GPIO expander[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_a53.dts?plain=1#L83) | [`nxp,pca6416`](../../../../build/dts/api/bindings/gpio/nxp%2Cpca6416.md#std-dtcompatible-nxp-pca6416) |
| I2C | on-chip | NXP II2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L236)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L212) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L66) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L281) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L260) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp%2Crdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L167) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L171) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L200)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L188) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L53) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L145) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |

#### `imx8mm_evk/mimx8mm6/a53/smp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L39)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L27) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L182) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L265) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L272) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Qualcomm Atheros AR8031 Ethernet PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_a53_smp.dts?plain=1#L59) | [`qca,ar8031`](../../../../build/dts/api/bindings/ethernet/phy/qca%2Car8031.md#std-dtcompatible-qca-ar8031) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L287) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L75) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L212) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L66) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L281) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L260) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp%2Crdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L167) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L171) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Power management CPU operations | on-board | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mm_evk/imx8mm_evk_mimx8mm6_a53_smp.dts?plain=1#L32) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L200)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L188) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L53) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mm_a53.dtsi?plain=1#L145) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |

#### `imx8mm_evk/mimx8mm6/m4` target

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
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L127) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L193)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L169) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8m_m4.dtsi?plain=1#L139) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

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
