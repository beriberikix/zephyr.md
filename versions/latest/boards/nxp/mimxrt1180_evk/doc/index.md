---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt1180_evk/doc/index.html
original_path: boards/nxp/mimxrt1180_evk/doc/index.html
---

# MIMXRT1180-EVK

Board Overview

[![../../../../_images/mimxrt1180_evk.webp](../../../../_images/mimxrt1180_evk.webp)
](../../../../_images/mimxrt1180_evk.webp)

MIMXRT1180-EVK

Name:
:   `mimxrt1180_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1189

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1180_evk/doc/index.rst/../..)

## Overview

The dual core i.MX RT1180 runs on the Cortex-M33 core at 240 MHz and on the
Cortex-M7 at 792 MHz. The i.MX RT1180 MCU offers support over a wide
temperature range and is qualified for consumer, industrial and automotive
markets.

## Hardware

- MIMXRT1189CVM8B MCU

  - 240MHz Cortex-M33 with 256KB TCM and 16 KB caches
  - 792Mhz Cortex-M7 with 512KB TCM and 32 KB caches
  - 1.5MB SRAM
- Memory

  - 512 Mbit SDRAM
  - 128 Mbit QSPI Flash
  - 512 Mbit HYPER RAM
  - TF socket for SD card
- Ethernet

  - 1000 Mbit/s Ethernet PHY
- USB

  - 2\* USB 2.0 OTG connector
- Audio

  - 3.5 mm audio stereo headphone jack
  - Board-mounted microphone
  - Left and right speaker out connectors
- Power

  - 5 V DC jack
- Debug

  - JTAG 20-pin connector
  - MCU-Link with DAPLink
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1180 SoC and MIMXRT1180-EVK board, see
these references:

- [i.MX RT1180 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1180-crossover-mcu-with-tsn-switch-and-edgelock:i.MX-RT1180)
- [MIMXRT1180-EVK Website](https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/i-mx-rt1180-evaluation-kit:MIMXRT1180-EVK)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| W9825G6KH | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| W25Q128JWSIQ | FLEXSPI | Enabled via flash configuration block, which sets up FLEXSPI at boot time. |

### Supported Features

NXP considers the MIMXRT1180-EVK as the superset board for the i.MX RT118x
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT118x family. NXP prioritizes enabling
this board with new support for Zephyr features.

The `mimxrt1180_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt1180_evk/mimxrt1189/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L22) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L375)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L389) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L709)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L689) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L84) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L89) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L347) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L405) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[32 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L410) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L719)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L730) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DMA | on-chip | NXP MCUX EDMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1046) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| DSA | on-chip | NXP NETC ethernet switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L653) | [`nxp,netc-switch`](../../../../build/dts/api/bindings/dsa/nxp%2Cnetc-switch.md#std-dtcompatible-nxp-netc-switch) |
| Ethernet | on-chip | NXP i.MX NETC Physical Station Interface (PSI)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L627) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cimx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-board | Generic MII PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L48) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-board | Realtek RTL8211F Ethernet PHY device[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L54) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek%2Crtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX RGPIO[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L216) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L264) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1009)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L996) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L26) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L18) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L35) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm33.dtsi?plain=1#L58) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L644) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cimx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L31) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L187) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L197) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L69) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L72) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L78) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L752) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cflexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L813)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L757) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | MCUX Timer/PWM Module (TPM)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L936) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1022)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1034) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L96)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L106) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1115)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1091) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm33.dtsi?plain=1#L39)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm33.dtsi?plain=1#L43) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L339)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L330) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1213) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1233) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | NXP RT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1163)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1173) | [`nxp,rtwdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Crtwdog.md#std-dtcompatible-nxp-rtwdog) |

#### `mimxrt1180_evk/mimxrt1189/cm7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L36) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L375)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L389) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L709)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L689) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L84) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L89) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L347) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L405) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[32 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L410) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L719)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L730) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DMA | on-chip | NXP MCUX EDMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1046) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| DSA | on-chip | NXP NETC ethernet switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L653) | [`nxp,netc-switch`](../../../../build/dts/api/bindings/dsa/nxp%2Cnetc-switch.md#std-dtcompatible-nxp-netc-switch) |
| Ethernet | on-chip | NXP i.MX NETC Physical Station Interface (PSI)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L627) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cimx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-board | Generic MII PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L48) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-board | Realtek RTL8211F Ethernet PHY device[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L54) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek%2Crtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX RGPIO[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L216) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L264) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1009)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L996) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L26) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L18) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L35) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm7.dtsi?plain=1#L51) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L644) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cimx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L45) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L187) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L197) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L69) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L72) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L78) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L752) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cflexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L813)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L757) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | MCUX Timer/PWM Module (TPM)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L936) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1022)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1034) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L96)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L106) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1115)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1091) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm7.dtsi?plain=1#L32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x_cm7.dtsi?plain=1#L36) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L339)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L330) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1213) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1233) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | NXP RT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1163)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt118x.dtsi?plain=1#L1173) | [`nxp,rtwdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Crtwdog.md#std-dtcompatible-nxp-rtwdog) |

### Connections and I/Os

The MIMXRT1180 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AON\_04 | GPIO | SW8 |
| GPIO\_AD\_27 | GPIO | LED |
| GPIO\_AON\_08 | LPUART1\_TX | UART Console M33 core |
| GPIO\_AON\_09 | LPUART1\_RX | UART Console M33 core | |
| GPIO\_AON\_19 | LPUART12\_TX | UART Console M7 core | |
| GPIO\_AON\_20 | LPUART12\_RX | UART Console M7 core |
| GPIO\_SD\_B1\_00 | SPI1\_CS0 | spi | |
| GPIO\_SD\_B1\_01 | SPI1\_CLK | spi | |
| GPIO\_SD\_B1\_02 | SPI1\_SDO | spi | |
| GPIO\_SD\_B1\_03 | SPI1\_SDI | spi | |

UART for M7 core is connected to USB-to-UART J60 connector.
Or user can use open JP7 Jumper to enable second UART on MCU LINK J53 connector.

### System Clock

The MIMXRT1180 SoC is configured to use SysTick as the system clock source,
running at 240MHz. When targeting the M7 core, SysTick will also be used,
running at 792MHz

### Serial Port

The MIMXRT1180 SoC has 12 UARTs. LPUART1 is configured for the CM33 console, the LPUART12 is
configured for the CM7 console core and the remaining are not used.

### Ethernet

NETC Ethernet driver supports to manage the Physical Station Interface (PSI).
NETC DSA driver supports to manage switch ports. Current DSA support is with
limitation that only switch function is available without management via
DSA master port. DSA master port support is TODO work.

```text
                +--------+                  +--------+
                | ENETC1 |                  | ENETC0 |
                |        |                  |        |
                | Pseudo |                  |  1G    |
                |  MAC   |                  |  MAC   |
                +--------+                  +--------+
                    | zero copy interface       |
+-------------- +--------+----------------+     |
|               | Pseudo |                |     |
|               |  MAC   |                |     |
|               |        |                |     |
|               | Port 4 |                |     |
|               +--------+                |     |
|           SWITCH       CORE             |     |
+--------+ +--------+ +--------+ +--------+     |
| Port 0 | | Port 1 | | Port 2 | | Port 3 |     |
|        | |        | |        | |        |     |
|  1G    | |  1G    | |  1G    | |  1G    |     |
|  MAC   | |  MAC   | |  MAC   | |  MAC   |     |
+--------+-+--------+-+--------+-+--------+     |
    |          |          |          |          |
NETC External Interfaces (4 switch ports, 1 end-point port)
```

## Programming and Debugging

The `mimxrt1180_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

LinkServer is the default runner for this board.
A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe).
The [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board. Use one of the other supported debug probes
below.

#### Using J-Link

Please ensure to use a version of JLINK above V7.94g and jumper JP5 is installed if using
external jlink plus on J37 as debugger.

When debugging cm33 core, need to ensure the SW5 on “0100” mode.
When debugging cm7 core, need to ensure the SW5 on “0001” mode.
(Only support run cm7 image when debugging due to default boot core on board is cm33 core)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK.

#### Using Linkserver

Please ensure to use a version of Linkserver above V1.5.30 and jumper JP5 is uninstalled (default setting).

When debugging cm33 core, need to ensure the SW5 on “0100” mode.
When debugging cm7 core, need to ensure the SW5 on “0001” mode.
(Only support run cm7 image when debugging due to default boot core on board is cm33 core)

## Dual Core samples Debugging

When debugging dual core samples, need to ensure the SW5 on “0100” mode.
The CM33 core is responsible for copying and starting the CM7.
To debug the CM7 it is useful to put infinite while loop either in reset vector or
into main function and attach via debugger to CM7 core.

CM7 core can be started again only after reset, so after flashing ensure to reset board.

### Configuring a Console

Regardless of your choice in debug probe, we will use the MCU-Link
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers JP5 and JP3 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the MCU-Link microcontroller.

Connect a USB cable from your PC to J53.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application on cm33 core.

Before power on the board, make sure SW5 is set to 0100b

```shell
# From the root of the zephyr repository
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/hello_world
west flash
```

Power off the board, then power on the board and
open a serial terminal, reset the board (press the SW3 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.7.0-xxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1180_evk/mimxrt1189/cm33
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.7.0-xxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1180_evk/mimxrt1189/cm33
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
