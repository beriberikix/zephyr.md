---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/madmachine/mm_feather/doc/index.html
original_path: boards/madmachine/mm_feather/doc/index.html
---

# SwiftIO Feather

Board Overview

[![../../../../_images/mm_feather.jpg](https://docs.zephyrproject.org/4.1.0/_images/mm_feather.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/mm_feather.jpg)

SwiftIO Feather

Name:
:   `mm_feather`

Vendor:
:   Shenzhen FeiKaiTe Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   mimxrt1062

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/madmachine/mm_feather/doc/index.rst/../..)

## Overview

The SwiftIO Feather board, designed by MadMachine is
designed with support for the modern [Swift language](https://docs.swift.org/swift-book/). Zephyr provides basic
low-level capabilities for the SwiftIO Feather board. Swift application would
run on top of Zephyr. More information about the board can be found
at:

- [MadMachine Homepage](https://madmachine.io)
- [SwiftIO API Reference](https://madmachineio.github.io/SwiftIO/documentation/swiftio/)

## Hardware

- MIMXRT1062DVL6B MCU (Cortex-M7 at 600MHz, 2048KB on-chip memory)
- Memory

  > - 8MB QSPI Flash
  > - 32MB SDRAM
  > - TF socket for SD card
- USB

  > - USB-C 2.0 OTG connector
- Power

  > - 5V USB power
  > - 4.2V DC jack
- Debug

  > - SWD connector
- RGB LED

### Supported Features

The `mm_feather` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mm_feather/mimxrt1062` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp%2Cmcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1099) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp%2Cmcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L912) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L932) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L279) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed factor clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L285) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX CCM Fractional PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L303) | [`nxp,imx-ccm-fnpll`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L956) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L171) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L176) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp%2Cimx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1131) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1141) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Cryptographic accelerator | on-chip | NXP Data Co-Processor (DCP) Crypto accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1118) | [`nxp,mcux-dcp`](../../../../build/dts/api/bindings/crypto/nxp%2Cmcux-dcp.md#std-dtcompatible-nxp-mcux-dcp) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L43) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L450) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp%2Cimx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L892) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L969) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp%2Cpxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L790) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L794) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L808) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO node[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L396)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L407) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L977) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp%2Cmcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/madmachine/mm_feather/mm_feather.dts?plain=1#L38) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L802) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP FlexRAM on-chip ram controller If the flexram,bank-spec property is specified, then the flexram will be dynamically reconfigured to the configuration specified at runtime[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp%2Cflexram.md#std-dtcompatible-nxp-flexram) |
| on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L147) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp%2Cimx-semc.md#std-dtcompatible-nxp-imx-semc) |
| Miscellaneous | on-chip | NXP FlexIO controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1166) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp%2Cflexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/madmachine/mm_feather/mm_feather.dts?plain=1#L60) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L963) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L606) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cflexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L641)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L611) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Cimx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L861)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L873) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1071) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp%2Cmcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1125) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp%2Ctempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L546) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L123) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L482)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L458) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L156) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cgpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L163) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L829)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L839) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB high speed phy that is used on NXP RTxxxx, RTxxx, MCX, LPC and Kinetis platforms if high speed usb is supported on these platforms[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L849) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L885) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp%2Cimx-csi.md#std-dtcompatible-nxp-imx-csi) |
| Watchdog | on-chip | imxRT watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L942) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Cimx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

### Connections and IOs

Note:
The following SwiftIO Feather pinout diagram is used for Swift programming.
The Swift ID is not the same as the Zephyr driver ID.

| Name | | GPIO | | Other peripherals | |
| --- | --- | --- | --- | --- | --- |
| Swift ID | Pin name | Swift ID | Zephyr driver | Swift ID | Zephyr driver |
| P0 | GPIO\_AD\_B1\_04 | D0 | GPIO1\_IO20 |  |  |
| P1 | GPIO\_AD\_B1\_08 | D1 | GPIO1\_IO24 |  |  |
| P2 | GPIO\_AD\_B1\_09 | D2 | GPIO1\_IO25 |  |  |
| P3 | GPIO\_AD\_B1\_10 | D3 | GPIO1\_IO26 | UART1 | UART\_8 |
| P4 | GPIO\_AD\_B1\_11 | D4 | GPIO1\_IO27 |
| P5 | GPIO\_AD\_B1\_12 | D5 | GPIO1\_IO28 |  |  |
| P6 | GPIO\_AD\_B1\_15 | D6 | GPIO1\_IO31 | SPI0 | SPI\_3 |
| P7 | GPIO\_AD\_B1\_14 | D7 | GPIO1\_IO30 |
| P8 | GPIO\_AD\_B1\_13 | D8 | GPIO1\_IO29 |
| P9 | GPIO\_AD\_B1\_03 | D9 | GPIO1\_IO19 | UART0 | UART\_2 |
| P10 | GPIO\_AD\_B1\_02 | D10 | GPIO1\_IO18 |
| P11 | GPIO\_AD\_B1\_05 | D11 | GPIO1\_IO21 |  |  |
| P12 | GPIO\_AD\_B0\_14 | D12 | GPIO1\_IO14 | CAN0 | CAN\_3 |
| P13 | GPIO\_AD\_B0\_15 | D13 | GPIO1\_IO15 |
| P14 | GPIO\_B0\_00 | D14 | GPIO2\_IO00 |  |  |
| P15 | GPIO\_B1\_03 | D15 | GPIO2\_IO19 |  |  |
| P16 | GPIO\_B1\_02 | D16 | GPIO2\_IO18 |  |  |
| P17 | GPIO\_B1\_01 | D17 | GPIO2\_IO17 | UART2 | UART\_4 |
| P18 | GPIO\_B1\_00 | D18 | GPIO2\_IO16 |
| P19 | GPIO\_B1\_15 | D19 | GPIO2\_IO31 |  |  |
| P20 | GPIO\_B1\_14 | D20 | GPIO2\_IO30 |  |  |
| P21 | GPIO\_B0\_03 | D21 | GPIO2\_IO03 | SPI1 | SPI\_4 |
| P22 | GPIO\_B0\_02 | D22 | GPIO2\_IO02 |
| P23 | GPIO\_B0\_01 | D23 | GPIO2\_IO01 |
| P24 | GPIO\_B0\_04 | D24 | GPIO2\_IO04 |  |  |
| P25 | GPIO\_B0\_05 | D25 | GPIO2\_IO05 |  |  |
| P26 | GPIO\_B0\_06 | D26 | GPIO2\_IO06 |  |  |
| P27 | GPIO\_B0\_07 | D27 | GPIO2\_IO07 |  |  |
| P28 | GPIO\_B0\_08 | D28 | GPIO2\_IO08 |  |  |
| P29 | GPIO\_B0\_09 | D29 | GPIO2\_IO09 |  |  |
| P30 | GPIO\_B0\_10 | D30 | GPIO2\_IO10 |  |  |
| P31 | GPIO\_B0\_11 | D31 | GPIO2\_IO11 |  |  |
| P32 | GPIO\_B0\_12 | D32 | GPIO2\_IO12 |  |  |
| P33 | GPIO\_B0\_13 | D33 | GPIO2\_IO13 |  |  |
| P34 | GPIO\_B0\_14 | D34 | GPIO2\_IO14 |  |  |
| P35 | GPIO\_B0\_15 | D35 | GPIO2\_IO15 |  |  |
|  | GPIO\_AD\_B1\_07 |  | GPIO1\_IO23 | I2C0 | I2C\_3 |
|  | GPIO\_AD\_B1\_06 |  | GPIO1\_IO22 |
|  | GPIO\_AD\_B1\_00 |  | GPIO1\_IO16 | I2C1 | I2C\_1 |
|  | GPIO\_AD\_B1\_00 |  | GPIO1\_IO17 |

## Programming and Flash

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Console

Connect a USB-to-serial adapter from your PC to corresponding UART pins of SwiftIO Feather.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect a DAPLink debugger from your PC to corresponding SWD pins of SwiftIO Feather.

```shell
# From the root of the zephyr repository
west build -b mm_feather samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the “reset” button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1-301-gd9c666a5abf8  ***
Hello World! mm_feather
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mm_feather samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1-301-gd9c666a5abf8  ***
Hello World! mm_feather
```
