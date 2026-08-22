---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx91_evk/doc/index.html
original_path: boards/nxp/imx91_evk/doc/index.html
---

# i.MX91 EVK

Board Overview

Name:
:   `imx91_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64

SoC:
:   mimx9131

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx91_evk/doc/index.rst/../..)

## Overview

The i.MX 91 Evaluation Kit (MCIMX91-EVK board) is a platform designed
to display the most commonly used features of the i.MX 91 applications
processor. The MCIMX91-EVK board is an entry-level development board
with a small and low-cost package. The board can be used by developers
to get familiar with the processor before investing a large amount of
resources in more specific designs.

The i.MX 91 applications processor features an Arm Cortex-A55 core
that can operate at speeds of up to 1.4 GHz.

- Board features:

  - RAM: 2GB LPDDR4
  - Storage:

    - SanDisk 16GB eMMC5.1
    - microSD Socket
  - Wireless:

    - Murata Type-2EL (SDIO+UART+SPI) module. It is based on NXP IW612 SoC,
      which supports dual-band (2.4 GHz /5 GHz) 1x1 Wi-Fi 6, Bluetooth 5.2,
      and 802.15.4
  - USB:

    - Two USB 2.0 Type C connectors
  - Ethernet:

    - ENET: 10/100/1000 Mbit/s RGMII Ethernet connected with external PHY
      RTL8211
    - ENET\_QoS: 10/100/1000 Mbit/s RGMII Ethernet supporting TSN connected
      with external PHY RTL8211
  - PCIe:

    - One M.2/NGFF Key E mini card 75-pin connector
  - Connectors:

    - 40-Pin Dual Row Header
  - LEDs:

    - 1x Power status LED
    - 2x UART LED
  - Debug:

    - JTAG 20-pin connector
    - MicroUSB for UART debug

### Supported Features

The `imx91_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx91_evk/mimx9131` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L23) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L72) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| Counter | on-chip | NXP Timer/PWM Module (TPM) used as timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L253)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L242) | [`nxp,tpm-timer`](../../../../build/dts/api/bindings/counter/nxp%2Ctpm-timer.md#std-dtcompatible-nxp-tpm-timer) |
| GPIO & Headers | on-chip | i.MX RGPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L90)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L78) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L146)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L170) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx91_evk/imx91_evk_mimx9131.dts?plain=1#L50) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L48) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx91_evk/imx91_evk_mimx9131.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L57) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L61) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 1.1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L43) | [`arm,psci-1.1`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.md#std-dtcompatible-arm-psci-1.1) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L126)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L136) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx91.dtsi?plain=1#L30) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 24 MHz.
Cortex-A55 Core runs up to 1.4 GHz.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART1 for A55 core.

## Programming and Debugging

The `imx91_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

There are multiple methods to program and debug Zephyr

### Option 1. Boot Zephyr by Using JLink Runner

The default runner for the board is JLink, connect the EVK board’s JTAG connector to
the host computer using a J-Link debugger, power up the board and stop the board at
U-Boot command line.

Then use “west flash” or “west debug” command to load the zephyr.bin
image from the host computer and start the Zephyr application on A55 core0.

#### Flash and Run

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx91_evk/mimx9131 samples/hello_world
west flash
```

Then the following log could be found on UART1 console:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g2c7ef313ac38 ***
Hello World! imx91_evk/mimx9131
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx91_evk/mimx9131 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “go” command is used to load and kick Zephyr to Cortex-A55 Core.

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin to Cortex-A55 Core:

```shell
fatload mmc 1:1 0x80000000 zephyr.bin; dcache flush; icache flush; go 0x80000000
```

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx91_evk/mimx9131 samples/synchronization
```

This will build an image with the synchronization sample app, boot it and
display the following console output:

```shell
*** Booting Zephyr OS build v4.0.0-3277-g69f43115c9a8 ***
thread_a: Hello World from cpu 0 on imx91_evk!
thread_b: Hello World from cpu 0 on imx91_evk!
thread_a: Hello World from cpu 0 on imx91_evk!
thread_b: Hello World from cpu 0 on imx91_evk!
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
