---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mcx_n9xx_evk/doc/index.html
original_path: boards/nxp/mcx_n9xx_evk/doc/index.html
---

# MCX-N9XX-EVK

Board Overview

[![../../../../_images/mcx_n9xx_evk.webp](https://docs.zephyrproject.org/4.2.0/_images/mcx_n9xx_evk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/mcx_n9xx_evk.webp)

MCX-N9XX-EVK

Name:
:   `mcx_n9xx_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxn947

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mcx_n9xx_evk/doc/index.rst/../..)

## Overview

MCX-N9XX-EVK is a full featured evaluation kit for prototyping of MCX N94 / N54
MCUs. They offer industry standard headers for access to the MCU’s I/Os,
integrated open-standard serial interfaces and an on-board MCU-Link debugger
with power measurement capability. MCX N Series are high-performance, low-power
microcontrollers with intelligent peripherals and accelerators providing
multi-tasking capabilities and performance efficiency.

## Hardware

- MCX-N947 Dual Arm Cortex-M33 microcontroller running at 150 MHz
- 2MB dual-bank on chip Flash
- 512 KB RAM
- External Quad SPI flash over FlexSPI
- USB high-speed (Host/Device) with on-chip HS PHY.
- USB full-speed (Host/Device) with on-chip FS PHY.
- 10x LP Flexcomms each supporting SPI, I2C, UART
- FlexCAN with FD, I3Cs, SAI
- 1x Ethernet with QoS
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, mikroBUS, M.2

For more information about the MCX-N947 SoC and MCX-N9XX-EVK board, see:

- [MCX-N947 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n94x-54x-highly-integrated-multicore-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N94X-N54X)
- [MCX-N947 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXNx4xDS.pdf)
- [MCX-N947 Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXNX4XRM)
- [MCX-N9XX-EVK Website](https://www.nxp.com/design/design-center/development-boards-and-designs/MCX-N9XX-EVK)
- [MCX-N9XX-EVK Board User Manual](https://www.nxp.com/webapp/Download?colCode=UM12036)
- [MCX-N9XX-EVK Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-55276)

### Supported Features

The `mcx_n9xx_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mcx_n9xx_evk/mcxn947/cpu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L19) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L836)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L851) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L906)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L77) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L73) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L734)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L746) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP LPTMR[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L916) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp,lptmr.md#std-dtcompatible-nxp-lptmr) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L974) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L985)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L991) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP MCUX LPDAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L648)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L10) | [`nxp,lpdac`](../../../../build/dts/api/bindings/dac/nxp,lpdac.md#std-dtcompatible-nxp-lpdac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L587)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L603) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP SmartDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L804) | [`nxp,smartdma`](../../../../build/dts/api/bindings/dma/nxp,smartdma.md#std-dtcompatible-nxp-smartdma) |
| Ethernet | on-chip | NXP ENET QOS IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L657) | [`nxp,enet-qos`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos.md#std-dtcompatible-nxp-enet-qos) |
| on-chip | NXP ENET QOS MAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L661) | [`nxp,enet-qos-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos-mac.md#std-dtcompatible-nxp-enet-qos-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L201) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L19) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp,msf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L119)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L169) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L60) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp,lcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L635) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp,lpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L296)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L208) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1038)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1021) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L949)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L936) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp,mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | NXP Mailbox Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L578) | [`nxp,mbox-mailbox`](../../../../build/dts/api/bindings/mbox/nxp,mbox-mailbox.md#std-dtcompatible-nxp-mbox-mailbox) |
| MDIO | on-chip | NXP ENET QOS MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L668) | [`nxp,enet-qos-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-qos-mdio.md#std-dtcompatible-nxp-enet-qos-mdio) |
| Multi-Function Device | on-chip | Low Power Flexcomm[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L218)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L179) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MIPI-DBI | on-chip | NXP FlexIO LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L968) | [`nxp,mipi-dbi-flexio-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L962) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L628) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L125) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L161) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| Pin control | on-chip | NXP PORT Pin Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L83) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L38) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L684) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L24)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L689) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L794) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L823) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp,vref.md#std-dtcompatible-nxp-vref) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L77) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp,lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RTC | on-chip | IRTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1010) | [`nxp,irtc`](../../../../build/dts/api/bindings/rtc/nxp,irtc.md#std-dtcompatible-nxp-irtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L813) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP low-power analog comparator (LPCMP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L69)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L890) | [`nxp,lpcmp`](../../../../build/dts/api/bindings/sensor/nxp,lpcmp.md#std-dtcompatible-nxp-lpcmp) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L272)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L190) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L238)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L197) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L24) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L63) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L641) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L865) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L875) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L884) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L676) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

#### `mcx_n9xx_evk/mcxn947/cpu0/qspi` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L19) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L836)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L851) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L906)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L77) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L73) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L734)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L746) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP LPTMR[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L916) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp,lptmr.md#std-dtcompatible-nxp-lptmr) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L974) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L985)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L991) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP MCUX LPDAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L648)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L10) | [`nxp,lpdac`](../../../../build/dts/api/bindings/dac/nxp,lpdac.md#std-dtcompatible-nxp-lpdac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L587)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L603) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP SmartDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L804) | [`nxp,smartdma`](../../../../build/dts/api/bindings/dma/nxp,smartdma.md#std-dtcompatible-nxp-smartdma) |
| Ethernet | on-chip | NXP ENET QOS IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L657) | [`nxp,enet-qos`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos.md#std-dtcompatible-nxp-enet-qos) |
| on-chip | NXP ENET QOS MAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L661) | [`nxp,enet-qos-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos-mac.md#std-dtcompatible-nxp-enet-qos-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L201) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L19) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp,msf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L119)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L169) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L60) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp,lcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L635) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp,lpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L296)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L208) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1038)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1021) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L949)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L936) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp,mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | NXP Mailbox Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L578) | [`nxp,mbox-mailbox`](../../../../build/dts/api/bindings/mbox/nxp,mbox-mailbox.md#std-dtcompatible-nxp-mbox-mailbox) |
| MDIO | on-chip | NXP ENET QOS MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L668) | [`nxp,enet-qos-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-qos-mdio.md#std-dtcompatible-nxp-enet-qos-mdio) |
| Multi-Function Device | on-chip | Low Power Flexcomm[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L218)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L179) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MIPI-DBI | on-chip | NXP FlexIO LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L968) | [`nxp,mipi-dbi-flexio-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L962) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L628) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L125) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L161) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| Pin control | on-chip | NXP PORT Pin Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L83) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L38) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L684) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L24)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L689) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L794) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L823) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp,vref.md#std-dtcompatible-nxp-vref) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L77) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp,lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RTC | on-chip | IRTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1010) | [`nxp,irtc`](../../../../build/dts/api/bindings/rtc/nxp,irtc.md#std-dtcompatible-nxp-irtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L813) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP low-power analog comparator (LPCMP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x_common.dtsi?plain=1#L69)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L890) | [`nxp,lpcmp`](../../../../build/dts/api/bindings/sensor/nxp,lpcmp.md#std-dtcompatible-nxp-lpcmp) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L272)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L190) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L238)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L197) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L24) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L63) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L641) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L865) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L875) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L884) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L676) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

#### `mcx_n9xx_evk/mcxn947/cpu1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L31) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | LPC LPADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L836) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L906) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L73) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L734) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP LPTMR[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L916) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp,lptmr.md#std-dtcompatible-nxp-lptmr) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L974) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L985) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP MCUX LPDAC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L648) | [`nxp,lpdac`](../../../../build/dts/api/bindings/dac/nxp,lpdac.md#std-dtcompatible-nxp-lpdac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L587)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L603) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP SmartDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L804) | [`nxp,smartdma`](../../../../build/dts/api/bindings/dma/nxp,smartdma.md#std-dtcompatible-nxp-smartdma) |
| Ethernet | on-chip | NXP ENET QOS IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L657) | [`nxp,enet-qos`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos.md#std-dtcompatible-nxp-enet-qos) |
| on-chip | NXP ENET QOS MAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L661) | [`nxp,enet-qos-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-qos-mac.md#std-dtcompatible-nxp-enet-qos-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L201) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L19) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp,msf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L119)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L169) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L60) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp,lcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L635) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp,lpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | NXP LPI2C controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L208) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1021) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| I3C | on-chip | NXP MCUX I3C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L936) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp,mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | NXP Mailbox Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L578) | [`nxp,mbox-mailbox`](../../../../build/dts/api/bindings/mbox/nxp,mbox-mailbox.md#std-dtcompatible-nxp-mbox-mailbox) |
| MDIO | on-chip | NXP ENET QOS MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L668) | [`nxp,enet-qos-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-qos-mdio.md#std-dtcompatible-nxp-enet-qos-mdio) |
| Multi-Function Device | on-chip | Low Power Flexcomm[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L262)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L179) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MIPI-DBI | on-chip | NXP FlexIO LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L968) | [`nxp,mipi-dbi-flexio-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L962) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L628) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L125) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk.dtsi?plain=1#L161) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| Pin control | on-chip | NXP PORT Pin Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L83) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L38) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L684) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L689) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L794) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L823) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp,vref.md#std-dtcompatible-nxp-vref) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L77) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp,lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RTC | on-chip | IRTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L1010) | [`nxp,irtc`](../../../../build/dts/api/bindings/rtc/nxp,irtc.md#std-dtcompatible-nxp-irtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L813) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP low-power analog comparator (LPCMP)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L890) | [`nxp,lpcmp`](../../../../build/dts/api/bindings/sensor/nxp,lpcmp.md#std-dtcompatible-nxp-lpcmp) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L272)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L190) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L197) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn94x.dtsi?plain=1#L24) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L63) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L641) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L865) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L875) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L884) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxnx4x_common.dtsi?plain=1#L676) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

### Shields for Supported Features

Some features in the table above are tested with Zephyr shields. These shields
are tested on this board:
- [NXP LCD\_PAR\_S035 TFT LCD Module](../../../shields/lcd_par_s035/doc/index.md#lcd-par-s035) - supports the Display interface. This board uses the
MIPI\_DBI interface of the shield, connected to the FlexIO on-chip peripheral.

## Dual Core samples

| Core | Boot Address | Comment |
| --- | --- | --- |
| CPU0 | 0x10000000[1856K] | primary core flash |
| CPU1 | 0x101d0000[192K] | secondary core flash |

| Memory | Address[Size] | Comment |
| --- | --- | --- |
| srama | 0x20000000[320k] | CPU0 ram |
| sramg | 0x20050000[64k] | CPU1 ram |
| sramh | 0x20060000[32k] | Shared memory |

### Targets available

The default configuration file
[boards/nxp/mcx\_n9xx\_evk/mcx\_n9xx\_evk\_mcxn947\_cpu0\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_n9xx_evk/mcx_n9xx_evk_mcxn947_cpu0_defconfig)
only enables the first core. CPU0 is the only target that can run standalone.

CPU1 does not work without CPU0 enabling it.

To enable CPU1, create System Build application project and enable the
second core with config [`CONFIG_SECOND_CORE_MCUX`](../../../../kconfig.md#CONFIG_SECOND_CORE_MCUX "CONFIG_SECOND_CORE_MCUX").

Please have a look at some already enabled samples:

- [IPC service: static vrings backend](../../../../samples/subsys/ipc/ipc_service/static_vrings/README.md#ipc-static-vrings "Send messages between two cores using the IPC service and static vrings backend.")
- [OpenAMP](../../../../samples/subsys/ipc/openamp/README.md#openamp "Send messages between two cores using OpenAMP.")
- [MBOX](../../../../samples/drivers/mbox/README.md#mbox "Perform inter-processor mailbox communication using the MBOX API.")
- [MBOX Data](../../../../samples/drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.")

### Connections and IOs

The MCX-N947 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| P0\_PIO1\_8 | UART | UART RX cpu0 |
| P1\_PIO1\_9 | UART | UART TX cpu0 |
| P4\_PIO4\_3 | UART | UART RX cpu1 |
| P4\_PIO4\_2 | UART | UART TX cpu1 |

### System Clock

The MCX-N947 SoC is configured to use PLL0 running at 150MHz as a source for
the system clock.

### Serial Port

The MCX-N9XX-EVK SoC has 10 FLEXCOMM interfaces for serial communication.
Flexcomm 4 is configured as UART for the console.

### Ethernet

To use networking samples with the Ethernet jack, change jumper JP13 to pins 2-3.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using LinkServer

LinkServer is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `ISP mode` to program the firmware,
short jumper JP24.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `ISP mode`
by shortening the jumper JP24.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
20-pin SWD connector (J11) of the board. Additionally, the jumper JP6 must
be shorted.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J5, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mcx_n9xx_evk/mcxn947/cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build vX.X.X ***
Hello World! mcx_n9xx_evk/mcxn947/cpu0
```

### Building a dual-core image

The dual-core samples are run using `mcx_n9xx_evk/mcxn947/cpu0` target.

Images built for `mcx_n9xx_evk/mcxn947/cpu1` will be loaded from flash
and executed on the second core when [`CONFIG_SECOND_CORE_MCUX`](../../../../kconfig.md#CONFIG_SECOND_CORE_MCUX "CONFIG_SECOND_CORE_MCUX") is selected.

For an example of building for both cores with System Build, see
[IPC service: static vrings backend](../../../../samples/subsys/ipc/ipc_service/static_vrings/README.md#ipc-static-vrings "Send messages between two cores using the IPC service and static vrings backend.")

Here is an example for the [MBOX Data](../../../../samples/drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.") application.

```shell
west build -b mcx_n9xx_evk/mcxn947/cpu0 --sysbuild zephyr/samples/drivers/mbox_data
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mcx_n9xx_evk/mcxn947/cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build vX.X.X ***
Hello World! mcx_n9xx_evk/mcxn947/cpu0
```

#### Debugging a dual-core image

For dual core builds, the secondary core should be placed into a loop,
then a debugger can be attached.
As a reference please see ([AN13264](https://www.nxp.com/docs/en/application-note/AN13264.pdf), section 4.2.3 for more information).
The reference is for the RT1170 but similar technique can be also used here.

### Using QSPI board variant

The MCX-N9XX-EVK board includes an external QSPI flash. The MCXN947 can boot and
XIP directly from this flash using the FlexSPI interface. The QSPI variant
enables building applications and code to execute from the QSPI.

#### Programming the ROM bootloader for external QSPI

By default, the MCXN947 bootloader in ROM will boot using internal flash. But
the MCU can be programmed to boot from external memory on the FlexSPI interface.
Before using the QSPI board variant, the board should be programmed to boot from
QSPI using the steps below.

To configure the ROM bootloader, the Protected Flash Region (PFR) must be
programmed. Programming the PFR is done using NXP’s ROM bootloader tools.
Some simple steps are provided in NXP’s
[MCUXpresso SDK example hello\_world\_qspi\_xip readme](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/mcxn9xxevk/demo_apps/hello_world_qspi_xip/example_board_readme.md). The binary to program
with blhost is found at [bootfromflexspi.bin](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/mcxn9xxevk/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflexspi.bin). A much more detailed explanation
is available at this post [Running code from external memory with MCX N94x](https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/Running-code-from-external-memory-with-MCX-N94x/ta-p/1792204).
The steps below program the MCX-N9XX-EVK board. Note that these steps interface
to the ROM bootloader through the UART serial port, but USB is another option.

1. Disconnect any terminal from the UART serial port, since these steps use that
   serial port.
2. Connect a micro USB cable to the host computer and J5 on the board, in the
   upper left corner. This powers the board, connects the debug probe, and
   connects the UART serial port used for the `blhost` command.
3. Place the MCU in ISP mode. On the MCX-N9XX-EVK board, the ISP button
   can be used for this. Press and hold the ISP button SW3, on the bottom right
   corner of the board. Press and release the Reset button SW1 on the lower left
   corner of the board. The MCU has booted into ISP mode. Release the ISP
   button.
4. Run the `blhost` command:

UbuntuWindows

This step assumes the MCU serial port is connected to /dev/ttyACM0

```shell
blhost -t 2000 -p /dev/ttyACM0,115200 -j -- write-memory 0x01004000 bootfromflexspi.bin
```

Change COMxx to match the COM port number connected to the MCU serial port.

```shell
blhost -t 2000 -p COMxx -j -- write-memory 0x01004000 bootfromflexspi.bin
```

Successful programming should look something like this:

```shell
$ blhost -t 2000 -p /dev/ttyACM0,115200 -j -- write-memory 0x01004000 bootfromflexspi.bin
{
   "command": "write-memory",
   "response": [
      256
   ],
   "status": {
      "description": "0 (0x0) Success.",
      "value": 0
   }
}
```

5. Reset the board with SW1 to exit ISP mode. Now the MCU is ready to boot from
   QSPI.

The ROM bootloader can be configured to boot from internal flash again. Repeat
the steps above to program the PFR, and program the file [bootfromflash.bin](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/mcxn9xxevk/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflash.bin).

#### Build, flash, and debug with the QSPI variant

Once the PFR is programmed to boot from QSPI, the normal Zephyr steps to build,
flash, and debug can be used with the QSPI board variant. Here are some examples.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application:

```shell
west build -b mcx_n9xx_evk//cpu0/qspi zephyr/samples/hello_world
west flash
```

MCUboot can also be used with the QSPI variant. By default, this places the
MCUboot bootloader in the `boot-partition` in QSPI flash, with the application
images. The ROM bootloader will boot first and load MCUboot in the QSPI, which
will load the app. This example builds and loads the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
sample with MCUboot using Sysbuild:

```shell
west build -b mcx_n9xx_evk//cpu0/qspi --sysbuild zephyr/samples/basic/blinky -- -DSB_CONFIG_BOOTLOADER_MCUBOOT=y
west flash
```

Open a serial terminal, reset the board with the SW1 button, and the console
will print:

```shell
*** Booting MCUboot vX.Y.Z ***
*** Using Zephyr OS build vX.Y.Z ***
I: Starting bootloader
I: Image index: 0, Swap type: none
I: Bootloader chainload address offset: 0x14000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build vX.Y.Z ***
LED state: OFF
LED state: ON
```

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
