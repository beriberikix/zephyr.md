---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/madmachine/mm_swiftio/doc/index.html
original_path: boards/madmachine/mm_swiftio/doc/index.html
---

# SwiftIO

Board Overview

[![../../../../_images/mm_swiftio.jpg](https://docs.zephyrproject.org/4.1.0/_images/mm_swiftio.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/mm_swiftio.jpg)

SwiftIO

Name:
:   `mm_swiftio`

Vendor:
:   Shenzhen FeiKaiTe Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   mimxrt1052

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/madmachine/mm_swiftio/doc/index.rst/../..)

## Overview

The SwiftIO board, designed by MadMachine is the world’s first board
designed with support for the modern [Swift language](https://docs.swift.org/swift-book/). Zephyr provides basic
low-level capabilities for the SwiftIO board. Swift application would
run on top of Zephyr. More information about the board can be found
at:

- [MadMachine Homepage](https://madmachine.io)
- [SwiftIO API Reference](https://madmachineio.github.io/SwiftIO/documentation/swiftio/)

## Hardware

- i.MX RT1052 Cortex-M7 processor at 600MHz
- 8MB QSPI Flash, 32MB SDRAM
- On-board DAPLink debugger with serial port
- User RGB LED, USB 2.0 Connector, microSD slot

### Supported Features

The `mm_swiftio` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mm_swiftio/mimxrt1052` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp,mcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1099) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L912) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L932) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L279) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed factor clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L285) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX CCM Fractional PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L303) | [`nxp,imx-ccm-fnpll`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L956) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L171) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp,imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L176) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp,imx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1131) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1141) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Cryptographic accelerator | on-chip | NXP Data Co-Processor (DCP) Crypto accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1118) | [`nxp,mcux-dcp`](../../../../build/dts/api/bindings/crypto/nxp,mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L43) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L450) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L892) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L969) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L790) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L794) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L808) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L396)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L407) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L977) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/madmachine/mm_swiftio/mm_swiftio.dts?plain=1#L38) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L802) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP FlexRAM on-chip ram controller If the flexram,bank-spec property is specified, then the flexram will be dynamically reconfigured to the configuration specified at runtime[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L147) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1166) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/madmachine/mm_swiftio/mm_swiftio.dts?plain=1#L60) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L963) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L606) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L641)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L611) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp,imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L861)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L873) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1071) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1125) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp,tempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L526) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L123) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L482)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L458) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L156) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L163) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L829)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L839) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB high speed phy that is used on NXP RTxxxx, RTxxx, MCX, LPC and Kinetis platforms if high speed usb is supported on these platforms[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L849) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-board | OV7725 CMOS video sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/madmachine/mm_swiftio/mm_swiftio.dts?plain=1#L109) | [`ovti,ov7725`](../../../../build/dts/api/bindings/video/ovti,ov7725.md#std-dtcompatible-ovti-ov7725) |
| on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L885) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| Watchdog | on-chip | imxRT watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L942) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

### Connections and IOs

Note:
The following SwiftIO pinout diagram is used for Swift programming.
The Swift ID is not the same as the Zephyr driver ID.

| Name | | GPIO | | Other peripherals | |
| --- | --- | --- | --- | --- | --- |
| Swift ID | Pin name | Swift ID | Zephyr driver | Swift ID | Zephyr driver |
| P0 | GPIO\_AD\_B1\_03 | D0 | GPIO1\_IO19 | UART0 | UART\_2 |
| P1 | GPIO\_AD\_B1\_02 | D1 | GPIO1\_IO18 |
| P2 | GPIO\_AD\_B0\_03 | D2 | GPIO1\_IO03 | UART1 | UART\_6 |
| P3 | GPIO\_AD\_B0\_02 | D3 | GPIO1\_IO02 |
| P4 | GPIO\_B1\_14 | D4 | GPIO2\_IO30 |  |  |
| P5 | GPIO\_B1\_15 | D5 | GPIO2\_IO31 |  |  |
| P6 | GPIO\_B0\_03 | D6 | GPIO2\_IO03 | SPI0 | SPI\_4 |
| P7 | GPIO\_B0\_02 | D7 | GPIO2\_IO02 |
| P8 | GPIO\_B0\_01 | D8 | GPIO2\_IO01 |
| P9 | GPIO\_B0\_00 | D9 | GPIO2\_IO00 |
| P10 | GPIO\_B1\_03 | D10 | GPIO2\_IO19 |  |  |
| P11 | GPIO\_B1\_02 | D11 | GPIO2\_IO18 |  |  |
| P12 | GPIO\_B1\_01 | D12 | GPIO2\_IO17 | UART2 | UART\_4 |
| P13 | GPIO\_B1\_00 | D13 | GPIO2\_IO16 |
| P14 | GPIO\_AD\_B1\_15 | D14 | GPIO1\_IO31 | SPI1 | SPI\_3 |
| P15 | GPIO\_AD\_B1\_14 | D15 | GPIO1\_IO30 |
| P16 | GPIO\_AD\_B1\_13 | D16 | GPIO1\_IO29 |
| P17 | GPIO\_AD\_B1\_12 | D17 | GPIO1\_IO28 |
| P18 | GPIO\_AD\_B1\_11 | D18 | GPIO1\_IO27 | UART3 | UART\_8 |
| P19 | GPIO\_AD\_B1\_10 | D19 | GPIO1\_IO26 |
| P20 | GPIO\_AD\_B1\_09 | D20 | GPIO1\_IO25 |  |  |
| P21 | GPIO\_AD\_B1\_08 | D21 | GPIO1\_IO24 |  |  |
| P22 | GPIO\_AD\_B1\_05 | D22 | GPIO1\_IO21 |  |  |
| P23 | GPIO\_AD\_B1\_04 | D23 | GPIO1\_IO20 |  |  |
| P24 | GPIO\_AD\_B0\_15 | D24 | GPIO1\_IO15 |  |  |
| P25 | GPIO\_AD\_B0\_14 | D25 | GPIO1\_IO14 |  |  |
| P26 | GPIO\_B0\_04 | D26 | GPIO2\_IO04 |  |  |
| P27 | GPIO\_B0\_05 | D27 | GPIO2\_IO05 |  |  |
| P28 | GPIO\_B0\_06 | D28 | GPIO2\_IO06 |  |  |
| P29 | GPIO\_B0\_07 | D29 | GPIO2\_IO07 |  |  |
| P30 | GPIO\_B0\_08 | D30 | GPIO2\_IO08 |  |  |
| P31 | GPIO\_B0\_09 | D31 | GPIO2\_IO09 |  |  |
| P32 | GPIO\_B0\_10 | D32 | GPIO2\_IO10 |  |  |
| P33 | GPIO\_B0\_11 | D33 | GPIO2\_IO11 |  |  |
| P34 | GPIO\_B0\_12 | D34 | GPIO2\_IO12 |  |  |
| P35 | GPIO\_B0\_13 | D35 | GPIO2\_IO13 |  |  |
| P36 | GPIO\_B0\_14 | D36 | GPIO2\_IO14 |  |  |
| P37 | GPIO\_B0\_15 | D37 | GPIO2\_IO15 |  |  |
| P38 | GPIO\_B1\_11 | D38 | GPIO2\_IO27 |  |  |
| P39 | GPIO\_B1\_10 | D39 | GPIO2\_IO26 |  |  |
| P40 | GPIO\_B1\_9 | D40 | GPIO2\_IO25 |  |  |
| P41 | GPIO\_B1\_8 | D41 | GPIO2\_IO24 |  |  |
| P42 | GPIO\_B1\_7 | D42 | GPIO2\_IO23 |  |  |
| P43 | GPIO\_B1\_6 | D43 | GPIO2\_IO22 |  |  |
| P44 | GPIO\_B1\_5 | D44 | GPIO2\_IO21 |  |  |
| P45 | GPIO\_B1\_4 | D45 | GPIO2\_IO20 |  |  |
|  | GPIO\_AD\_B1\_07 |  |  | I2C0 | I2C\_3 |
|  | GPIO\_AD\_B1\_06 |  |  |
|  | GPIO\_AD\_B1\_00 |  |  | I2C1 | I2C\_1 |
|  | GPIO\_AD\_B1\_01 |  |  |

## Programming and Flash

Build applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Configuring a Debug Probe

This board is configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must flash the device by copying files

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a USB-to-serial adapter for the serial console.

Connect a USB cable from your PC to Serial of SwiftIO.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect a USB cable from your PC to “Serial” port of SwiftIO.
On Ubuntu, DAPLink debug probes appear on the host
computer as a USB disk mounted to `/media/<user>/SWIFTIODBGR/`,
where `<user>` is your login name.

```shell
west build -b mm_swiftio samples/hello_world
cp build/zephyr/zephyr.bin /media/<user>/SWIFTIODBGR/
```

Open a serial terminal, reset the board (press the “reset” button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.1.0-rc1 *****
Hello World! mm_swiftio
```
