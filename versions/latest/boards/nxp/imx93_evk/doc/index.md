---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx93_evk/doc/index.html
original_path: boards/nxp/imx93_evk/doc/index.html
---

# i.MX93 EVK

Board Overview

Name:
:   `imx93_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64, arm

SoC:
:   mimx9352

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx93_evk/doc/index.rst/../..)

## Overview

The i.MX93 Evaluation Kit (MCIMX93-EVK board) is a platform designed to show
the most commonly used features of the i.MX 93 Applications Processor in a
small and low cost package. The MCIMX93-EVK board is an entry-level development
board, which helps developers to get familiar with the processor before
investing a large amount of resources in more specific designs.

i.MX93 MPU is composed of one cluster of 2x Cortex®-A55 cores and a single
Cortex®-M33 core. Zephyr OS is ported on Cortex®-A55 core and Cortex®-M33
core.

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
  - Ethernet
  - PCI-E M.2
  - Connectors:

    - 40-Pin Dual Row Header
  - LEDs:

    - 1x Power status LED
    - 2x UART LED
  - Debug

    - JTAG 20-pin connector
    - MicroUSB for UART debug, two COM ports for A55 and M33

### Supported Features

The `imx93_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx93_evk/mimx9352/a55` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L29)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L23) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm,cortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L341)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L329) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L79) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| Counter | on-chip | NXP Timer/PWM Module (TPM) used as timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L434) | [`nxp,tpm-timer`](../../../../build/dts/api/bindings/counter/nxp,tpm-timer.md#std-dtcompatible-nxp-tpm-timer) |
| DAI | on-chip | NXP Synchronous Audio Interface (SAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L364) | [`nxp,dai-sai`](../../../../build/dts/api/bindings/dai/nxp,dai-sai.md#std-dtcompatible-nxp-dai-sai) |
| DMA | on-chip | NXP enhanced Direct Memory Access (eDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L353) | [`nxp,edma`](../../../../build/dts/api/bindings/dma/nxp,edma.md#std-dtcompatible-nxp-edma) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L404) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L410) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L109) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L425) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX RGPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L85) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| on-board | ADP5585 GPIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L151) | [`adi,adp5585-gpio`](../../../../build/dts/api/bindings/gpio/adi,adp5585-gpio.md#std-dtcompatible-adi-adp5585-gpio) |
| on-board | NXP PCAL6524 I2C GPIO expander[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L166) | [`nxp,pcal6524`](../../../../build/dts/api/bindings/gpio/nxp,pcal6524.md#std-dtcompatible-nxp-pcal6524) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L157)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L145) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L57) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L55) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L419) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Multi-Function Device | on-board | Analog ADP5585 GPIO/keypad/PWM chip[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L146) | [`adi,adp5585`](../../../../build/dts/api/bindings/mfd/adi,adp5585.md#std-dtcompatible-adi-adp5585) |
| Miscellaneous | on-board | The i.MX 93 EVK boards has a series of MUXes that selects between 2 pin functions[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L73) | `imx93evk-exp-sel` |
| PHY | on-board | Simple GPIO controlled CAN transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_a55.dts?plain=1#L83) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L64) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L68) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Power management CPU operations | on-chip | Power State Coordination Interface (PSCI) version 1.1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L50) | [`arm,psci-1.1`](../../../../build/dts/api/bindings/pm_cpu_ops/arm,psci-1.1.md#std-dtcompatible-arm-psci-1.1) |
| SDHC | on-chip | NXP imx USDHC controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L378) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L135)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L125) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L241) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L37) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx93_evk/mimx9352/m33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L17) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L33) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L38) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L53) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| GPIO & Headers | on-chip | i.MX RGPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L59) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_m33.dts?plain=1#L48) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx93_evk/imx93_evk_mimx9352_m33.dts?plain=1#L32) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L43) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L47) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx93_m33.dtsi?plain=1#L91) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 24 MHz.
Cortex-A55 Core runs up to 1.7 GHz.
Cortex-M33 Core runs up to 200MHz in which SYSTICK runs on same frequency.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART2 for A55 core and M33 core.

#### uSDHC (SD or eMMC Interface on A55)

i.MX 93 processor has three ultra secured digital host controller (uSDHC) modules
for SD/eMMC interface support. On the MCIMX93-EVK board, the uSDHC2 interface of
the processor connects to the MicroSD card slot (J1002), and uSDHC1 interface connects
to the eMMC memory (located at the SOM board). DTS overlay file “usdhc1.overlay” and
“usdhc2.overlay” are provided to enable specified the uSDHC controller.

Currently it rely on U-boot or Linux to boot Zephyr on Cortex-A Core, so Zephyr need
to use different uSDHC controller from U-boot or Linux to avoid resource conflict.
For example, if EVK board boots from SD Card which uses uSDHC2, Zephyr can use MMC
which uses uSDHC1 for testing:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 tests/subsys/sd/mmc -- -DEXTRA_DTC_OVERLAY_FILE=usdhc1.overlay
```

And if EVK board boots from MMC which uses uSDHC1, Zephyr can use SD Card which uses
uSDHC2 for testing:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 tests/subsys/sd/sdmmc -- -DEXTRA_DTC_OVERLAY_FILE=usdhc2.overlay
```

#### Board MUX Control

This board configuration uses a series of digital multiplexers to switch between
different board functions. The multiplexers are controlled by a GPIO signal called
`EXP_SEL` from onboard GPIO expander ADP5585. It can be configured to select
function set “A” or “B” by dts configuration if board control module is enabled.
The following dts node is defined:

```dts
board_exp_sel: board-exp-sel {
    compatible = "imx93evk-exp-sel";
    mux-gpios = <&gpio_exp0 4 GPIO_ACTIVE_HIGH>;
    mux = "A";
};
```

Following steps are required to configure the `EXP_SEL` signal:

1. Enable Kconfig option `CONFIG_BOARD_MIMX93_EVK_EXP_SEL_INIT`.
2. Select `mux="A";` or `mux="B";` in `&board_exp_sel` devicetree node.

Kconfig option `CONFIG_BOARD_MIMX93_EVK_EXP_SEL_INIT` is enabled if a board
function that requires configuring the mux is enabled. The MUX option is
automatically selected if certain board function is enabled, and takes precedence
over dts config. For instance, if `CONFIG_CAN` is enabled, MUX A is selected
even if `mux="B";` is configured in dts, and an warning would be reported in
the log.

#### User Button GPIO Option

The user buttons RFU\_BTN1 and RFU\_BTN2 is connected to i.MX 93 GPIO by default,
but can be changed to connect to onboard GPIO expander PCAL6524 with on-board DIP
switches. To do this, switch SW1006 to 0000, then switch SW1005 to 0101. An devicetree
overlay is included to support this.

Run following command to test user buttons on PCAL6524:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 samples/basic/button -- -DEXTRA_DTC_OVERLAY_FILE=imx93_evk_mimx9352_exp_btn.overlay
```

Run the app, press RFU\_BTN1 and the red LED turns on accordingly.

Note: The overlay only supports `mimx9352/a55`, but can be extended to support
`mimx9352/m33` if I2C and PCAL6524 is enabled.

## Programming and Debugging (A55)

The `imx93_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

There are multiple method to program and debug Zephyr on the A55 core:

### Option 1. Boot Zephyr by Using JLink Runner

The default runner for the board is JLink, connect the EVK board’s JTAG connector to
the host computer using a J-Link debugger, power up the board and stop the board at
U-Boot command line, execute the following U-boot command to disable D-Cache:

```shell
dcache off
```

then use “west flash” or “west debug” command to load the zephyr.bin
image from the host computer and start the Zephyr application on A55 core0.

#### Flash and Run

Here is an example for the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") application.

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 samples/synchronization
west flash
```

Then the following log could be found on UART2 console:

```shell
*** Booting Zephyr OS build Booting Zephyr OS build v3.7.0-2055-g630f27a5a867  ***
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “go” command can be used to start Zephyr on A55 core0 and U-Boot “cpu” command
is used to load and kick Zephyr to the other A55 secondary Cores. Currently “cpu” command
is supported in : [Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot) (use the branch “uboot\_vxxxx.xx-y.y.y,
xxxx.xx is uboot version and y.y.y is Real-Time Edge Software version, for example
“uboot\_v2023.04-2.9.0” branch is U-Boot v2023.04 used in Real-Time Edge Software release
v2.9.0), and pre-build images and user guide can be found at [Real-Time Edge Software](https://www.nxp.com/rtedge).

#### Step 1: Download Zephyr Image into DDR Memory

Firstly need to download Zephyr binary image into DDR memory, it can use tftp:

```shell
tftp 0xd0000000 zephyr.bin
```

Or copy the Zephyr image `zephyr.bin` SD card and plug the card into the board, for example
if copy to the FAT partition of the SD card, use the following U-Boot command to load the image
into DDR memory (assuming the SD card is dev 1, fat partition ID is 1, they could be changed
based on actual setup):

```shell
fatload mmc 1:1 0xd0000000 zephyr.bin;
```

#### Step 2: Boot Zephyr

Then use the following command to boot Zephyr on the core0:

```shell
dcache off; icache flush; go 0xd0000000;
```

Or use “cpu” command to boot from secondary Core, for example Core1:

```shell
dcache flush; icache flush; cpu 1 release 0xd0000000
```

### Option 3. Boot Zephyr by Using Remoteproc under Linux

When running Linux on the A55 core, it can use the remoteproc framework to load and boot Zephyr,
refer to Real-Time Edge user guide for more details. Pre-build images and user guide can be found
at [Real-Time Edge Software](https://www.nxp.com/rtedge).

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 samples/synchronization
```

This will build an image with the synchronization sample app, boot it and
display the following console output:

```shell
*** Booting Zephyr OS build Booting Zephyr OS build v3.7.0-2055-g630f27a5a867  ***
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
```

### System Reboot (A55)

Currently i.MX93 only support cold reboot and doesn’t support warm reboot.
Use this configuratiuon to verify cold reboot with [Custom Shell module](../../../../samples/subsys/shell/shell_module/README.md#shell-module "Register shell commands using the Shell API")
sample:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/a55 samples/subsys/shell/shell_module
```

This will build an image with the shell sample app, boot it and execute
kernel reboot command in shell command line:

```shell
uart:~$ kernel reboot cold
```

## Programming and Debugging (M33)

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin to Cortex-M33 Core:

### Boot with code from TCM

```shell
load mmc 1:1 0x80000000 zephyr.bin;cp.b 0x80000000 0x201e0000 0x30000;bootaux 0x1ffe0000 0
```

### Boot with code from DDR

```shell
load mmc 1:1 0x84000000 zephyr.bin;dcache flush;bootaux 0x84000000 0
```

Note: Cortex M33 need execute permission to run code from DDR memory. In order
to enable this, [imx-atf](https://github.com/nxp-imx/imx-atf) can to be modified in “plat/imx/imx93/trdc\_config.h”.

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/m33 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it and
display the following console output:

```shell
*** Booting Zephyr OS build v3.7.0-684-g71a7d05ba60a ***
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
thread_a: Hello World from cpu 0 on imx93_evk!
thread_b: Hello World from cpu 0 on imx93_evk!
```

To make a container image flash.bin with `zephyr.bin` for SD/eMMC programming and booting
from BootROM. Refer to user manual of i.MX93 [MCUX SDK release](https://mcuxpresso.nxp.com/).

### References

More information can refer to NXP official website:
[NXP website](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-processors/i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93).

## Using the SOF-specific variant

### Purpose

Since this board doesn’t have a DSP, an alternative for people who might be interested
in running SOF on this board had to be found. The alternative consists of running SOF
on an A55 core using Jailhouse as a way to “take away” one A55 core from Linux and
assign it to Zephyr with [SOF](https://github.com/thesofproject/sof).

### What is Jailhouse?

Jailhouse is a light-weight hypervisor that allows the partitioning of hardware resources.
For more details on how this is done and, generally, about Jailhouse, please see: [1](https://lwn.net/Articles/578295/),
[2](https://lwn.net/Articles/578852/) and [3](http://events17.linuxfoundation.org/sites/events/files/slides/ELCE2016-Jailhouse-Tutorial.pdf). The GitHub repo can be found [here](https://github.com/siemens/jailhouse).

### How does it work?

Firstly, we need to explain a few Jailhouse concepts that will be referred to later on:

- **Cell**: refers to a set of hardware resources that the OS assigned to this
  cell can utilize.
- **Root cell**: refers to the cell in which Linux is running. This is the main cell which
  will contain all the hardware resources that Linux will utilize and will be used to assign
  resources to the inmates. The inmates CANNOT use resources such as the CPU that haven’t been
  assigned to the root cell.
- **Inmate**: refers to any other OS that runs alongside Linux. The resources an inmate will
  use are taken from the root cell (the cell Linux is running in).

SOF+Zephyr will run as an inmate, alongside Linux, on core 1 of the board. This means that
said core will be taken away from Linux and will only be utilized by Zephyr.

The hypervisor restricts inmate’s/root’s access to certain hardware resources using
the second-stage translation table which is based on the memory regions described in the
configuration files. Please consider the following scenario:

> Root cell wants to use the **UART** which let’s say has its registers mapped in
> the **[0x0 - 0x42000000]** region. If the inmate wants to use the same **UART** for
> some reason then we’d need to also add this region to inmate’s configuration
> file and add the **JAILHOUSE\_MEM\_ROOTSHARED** flag. This flag means that the inmate
> is allowed to share this region with the root. If this region is not set in
> the inmate’s configuration file and Zephyr (running as an inmate here) tries
> to access this region this will result in a second stage translation fault.

Notes:

- Linux and Zephyr are not aware that they are running alongside each other.
  They will only be aware of the cores they have been assigned through the config
  files (there’s a config file for the root and one for each inmate).

### Architecture overview

The architecture overview can be found at this [location](https://github.com/thesofproject/sof/issues/7192). (latest status update as of now
and the only one containing diagrams).

### How to use this board?

This board has been designed for SOF so it’s only intended to be used with SOF.

TODO: document the SOF build process for this board. For now, the support for
i.MX93 is still in review and has yet to merged on SOF side.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
