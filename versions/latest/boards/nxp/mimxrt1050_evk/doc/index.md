---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt1050_evk/doc/index.html
original_path: boards/nxp/mimxrt1050_evk/doc/index.html
---

# MIMXRT1050-EVK

Board Overview

[![../../../../_images/mimxrt1050_evk.jpg](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1050_evk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1050_evk.jpg)

MIMXRT1050-EVK

Name:
:   `mimxrt1050_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1052

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1050_evk/doc/index.rst/../..)

## Overview

The i.MX RT1050 is a new processor family featuring NXP’s advanced
implementation of the ARM Cortex-M7 Core. It provides high CPU performance and
real-time response.

The i.MX RT1050 provides various memory interfaces, including SDRAM, Raw NAND
FLASH, NOR FLASH, SD/eMMC, Quad SPI, HyperBus and a wide range of other
interfaces for connecting peripherals, such as WLAN, Bluetooth™, GPS, displays,
and camera sensors. As with other i.MX processors, i.MX RT1050 also has rich
audio and video features, including LCD display, basic 2D graphics, camera
interface, SPDIF, and I2S audio interface.

## Hardware

- MIMXRT1052DVL6A MCU (600 MHz, 512 KB TCM)
- Memory

  - 256 KB SDRAM
  - 64 Mbit QSPI Flash
  - 512 Mbit Hyper Flash
- Display

  - LCD connector
  - Touch connector
- Ethernet

  - 10/100 Mbit/s Ethernet PHY
- USB

  - USB 2.0 OTG connector
  - USB 2.0 host connector
- Audio

  - 3.5 mm audio stereo headphone jack
  - Board-mounted microphone
  - Left and right speaker out connectors
- Power

  - 5 V DC jack
- Debug

  - JTAG 20-pin connector
  - OpenSDA with DAPLink
- Sensor

  - FXOS8700CQ 6-axis e-compass
  - CMOS camera sensor interface
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1050 SoC and MIMXRT1050-EVK board, see
these references:

- [i.MX RT1050 Website](https://www.nxp.com/products/microcontrollers-and-processors/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1050-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1050)
- [i.MX RT1050 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1050CEC.pdf)
- [i.MX RT1050 Reference Manual](https://www.nxp.com/docs/en/reference-manual/IMXRT1050RM.pdf)
- [MIMXRT1050-EVK Website](https://www.nxp.com/products/microcontrollers-and-processors/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1050-evaluation-kit:MIMXRT1050-EVK)
- [MIMXRT1050-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=IMXRT1050EVKBHUG)
- [MIMXRT1050-EVK Schematics](https://www.nxp.com/webapp/Download?colCode=MIMXRT1050-EVK-DESIGNFILES)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| IS42S16160J | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| S26KS512SDPBHI020 | FLEXSPI | Enabled via flash configuration block, which sets up FLEXSPI at boot time. |

### Supported Features

The `mimxrt1050_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt1050_evk/mimxrt1052/hyperflash` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L596) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp,mcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1116) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L929) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L949) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L279) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed factor clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L285) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX CCM Fractional PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L303) | [`nxp,imx-ccm-fnpll`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L973) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L171) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp,imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L176) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp,imx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1148) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1158) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Cryptographic accelerator | on-chip | NXP Data Co-Processor (DCP) Crypto accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1135) | [`nxp,mcux-dcp`](../../../../build/dts/api/bindings/crypto/nxp,mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L43) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L450) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L910) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L986) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L790) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L794) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L194) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L808) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on NXP LCD interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L47) | [`nxp,parallel-lcd-connector`](../../../../build/dts/api/bindings/gpio/nxp,parallel-lcd-connector.md#std-dtcompatible-nxp-parallel-lcd-connector) |
| on-board | GPIO pins exposed on NXP LCD touch controller interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L60) | [`nxp,i2c-tsc-fpc`](../../../../build/dts/api/bindings/gpio/nxp,i2c-tsc-fpc.md#std-dtcompatible-nxp-i2c-tsc-fpc) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L86) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L396)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L407) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L994) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L77) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L69) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L802) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L147) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1183) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI HyperFlash[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk_mimxrt1052_hyperflash.dts?plain=1#L29) | [`nxp,imx-flexspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-hyperflash.md#std-dtcompatible-nxp-imx-flexspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk_mimxrt1052_hyperflash.dts?plain=1#L47) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L980) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L606) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L611) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp,imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L879)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L891) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L140) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1088) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1142) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp,tempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L516) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L123)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L135) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L458)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L470) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L156) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L163) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L829)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L839) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP EHCI USB host controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L849) | [`nxp,uhc-ehci`](../../../../build/dts/api/bindings/usb/nxp,uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L867) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L903) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L959)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L966) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

#### `mimxrt1050_evk/mimxrt1052/qspi` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L596) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp,mcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1116) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L929) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L949) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L279) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed factor clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L285) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX CCM Fractional PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L303) | [`nxp,imx-ccm-fnpll`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L973) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP MCUX Quad Timer (QTMR)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L171) | [`nxp,imx-qtmr`](../../../../build/dts/api/bindings/counter/nxp,imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr) |
| on-chip | NXP MCUX Quad Timer Channel[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L176) | [`nxp,imx-tmr`](../../../../build/dts/api/bindings/counter/nxp,imx-tmr.md#std-dtcompatible-nxp-imx-tmr) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1148) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1158) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Cryptographic accelerator | on-chip | NXP Data Co-Processor (DCP) Crypto accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1135) | [`nxp,mcux-dcp`](../../../../build/dts/api/bindings/crypto/nxp,mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L43) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L450) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L910) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L986) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L790) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L794) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L194) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L808) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on NXP LCD interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L47) | [`nxp,parallel-lcd-connector`](../../../../build/dts/api/bindings/gpio/nxp,parallel-lcd-connector.md#std-dtcompatible-nxp-parallel-lcd-connector) |
| on-board | GPIO pins exposed on NXP LCD touch controller interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L60) | [`nxp,i2c-tsc-fpc`](../../../../build/dts/api/bindings/gpio/nxp,i2c-tsc-fpc.md#std-dtcompatible-nxp-i2c-tsc-fpc) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L86) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L396)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L407) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L994) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L77) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L69) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L802) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L147) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1183) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk_mimxrt1052_qspi.dts?plain=1#L23) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk_mimxrt1052_qspi.dts?plain=1#L32) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L980) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L606) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L611) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp,imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L879)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L891) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1050_evk/mimxrt1050_evk.dtsi?plain=1#L140) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1088) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1142) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp,tempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L516) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L123)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L135) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L458)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L470) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L156) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L163) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L829)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L839) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP EHCI USB host controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L849) | [`nxp,uhc-ehci`](../../../../build/dts/api/bindings/usb/nxp,uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L867) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L903) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L959)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L966) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

Note

For additional features not yet supported, please also refer to the
[MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064_evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1050\_evk board.

### Connections and IOs

The MIMXRT1050 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_00 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_B0\_01 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_B0\_02 | LPSPI3\_SDI/LCD\_RST| SPI/LCD Display | |
| GPIO\_AD\_B0\_03 | LPSPI3\_PCS0 | SPI |
| GPIO\_AD\_B0\_05 | GPIO | SD Card |
| GPIO\_AD\_B0\_09 | GPIO/ENET\_RST | LED |
| GPIO\_AD\_B0\_10 | GPIO/ENET\_INT | GPIO/Ethernet |
| GPIO\_AD\_B0\_11 | GPIO | Touch Interrupt |
| GPIO\_AD\_B0\_12 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_13 | LPUART1\_RX | UART Console |
| GPIO\_AD\_B1\_00 | LPI2C1\_SCL | I2C |
| GPIO\_AD\_B1\_01 | LPI2C1\_SDA | I2C |
| GPIO\_AD\_B1\_06 | LPUART3\_TX | UART BT HCI |
| GPIO\_AD\_B1\_07 | LPUART3\_RX | UART BT HCI |
| GPIO\_AD\_B1\_11 | ADC | ADC1 channel 0 |
| WAKEUP | GPIO | SW0 |
| GPIO\_B0\_00 | LCD\_CLK | LCD Display |
| GPIO\_B0\_01 | LCD\_ENABLE | LCD Display |
| GPIO\_B0\_02 | LCD\_HSYNC | LCD Display |
| GPIO\_B0\_03 | LCD\_VSYNC | LCD Display |
| GPIO\_B0\_04 | LCD\_DATA00 | LCD Display |
| GPIO\_B0\_05 | LCD\_DATA01 | LCD Display |
| GPIO\_B0\_06 | LCD\_DATA02 | LCD Display |
| GPIO\_B0\_07 | LCD\_DATA03 | LCD Display |
| GPIO\_B0\_08 | LCD\_DATA04 | LCD Display |
| GPIO\_B0\_09 | LCD\_DATA05 | LCD Display |
| GPIO\_B0\_10 | LCD\_DATA06 | LCD Display |
| GPIO\_B0\_11 | LCD\_DATA07 | LCD Display |
| GPIO\_B0\_12 | LCD\_DATA08 | LCD Display |
| GPIO\_B0\_13 | LCD\_DATA09 | LCD Display |
| GPIO\_B0\_14 | LCD\_DATA10 | LCD Display |
| GPIO\_B0\_15 | LCD\_DATA11 | LCD Display |
| GPIO\_B1\_00 | LCD\_DATA12 | LCD Display |
| GPIO\_B1\_01 | LCD\_DATA13 | LCD Display |
| GPIO\_B1\_02 | LCD\_DATA14 | LCD Display |
| GPIO\_B1\_03 | LCD\_DATA15 | LCD Display |
| GPIO\_B1\_04 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_B1\_05 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_B1\_06 | ENET\_RX\_EN | Ethernet |
| GPIO\_B1\_07 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_B1\_08 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_B1\_09 | ENET\_TX\_EN | Ethernet |
| GPIO\_B1\_10 | ENET\_REF\_CLK | Ethernet |
| GPIO\_B1\_11 | ENET\_RX\_ER | Ethernet |
| GPIO\_B1\_12 | GPIO | SD Card |
| GPIO\_B1\_14 | USDHC1\_VSELECT | SD Card |
| GPIO\_B1\_15 | BACKLIGHT\_CTL | LCD Display |
| GPIO\_EMC\_40 | ENET\_MDC | Ethernet |
| GPIO\_EMC\_41 | ENET\_MDIO | Ethernet |
| GPIO\_AD\_B0\_09 | ENET\_RST | Ethernet |
| GPIO\_AD\_B0\_10 | ENET\_INT | Ethernet |
| GPIO\_SD\_B0\_00 | USDHC1\_CMD/LPSPI1\_SCK | SD Card/SPI | |
| GPIO\_SD\_B0\_01 | USDHC1\_CLK/LPSPI1\_PCS0 | SD Card/SPI | |
| GPIO\_SD\_B0\_02 | USDHC1\_DATA0/LPSPI1\_SDO | SD Card/SPI | |
| GPIO\_SD\_B0\_03 | USDHC1\_DATA1/LPSPI1\_SDI | SD Card/SPI | |
| GPIO\_SD\_B0\_04 | USDHC1\_DATA2 | SD Card |
| GPIO\_SD\_B0\_05 | USDHC1\_DATA3 | SD Card |
| GPIO\_AD\_B1\_02 | 1588\_EVENT2\_OUT | 1588 |
| GPIO\_AD\_B1\_03 | 1588\_EVENT2\_IN | 1588 |

Note

In order to use the SPI peripheral on this board, resistors R278,
R279, R280, and R281 must be populated with zero ohm resistors

### System Clock

The MIMXRT1050 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1050 SoC has eight UARTs. `LPUART1` is configured for the console,
`LPUART3` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

### USB

The RT1050 SoC has two USB OTG (USBOTG) controllers that supports both
device and host functions through its micro USB connectors.
Only USB device function is supported in Zephyr at the moment.

## Board Targets

This board has two variants that can be targeted,
depending on which flash to set as `zephyr,flash`:

- `mimxrt1050_evk/mimxrt1052/hyperflash` is the default variant for the out of box
  setup of the board using hyperflash.
- `mimxrt1050_evk/mimxrt1052/qspi` is for a board that has been reworked to use the
  qspi flash instead of hyperflash.

## Programming and Debugging

The `mimxrt1050_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Note

Newer revisions of this board use [LPC-LINK2 Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpc-link2-onboard-debug-probe),
while older revisions use the [OpenSDA Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-onboard-debug-probe).
Schematic revisions A/A1 use the K20 OpenSDA probe, and B/B1 use the
LPC-Link2 LPC4322 probe.

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in [Configuring a Debug Probe
(Schematic A/A1)](#configuring-a-debug-probe-schematic-a-a1) or [Configuring a Debug Probe (Schematic B/B1)](#configuring-a-debug-probe-schematic-b-b1),
depending on board schematic revision to configure the board appropriately.

- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) (Default, NXP Supported)
- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) (NXP Supported)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details).

### Configuring a Debug Probe (Schematic A/A1)

For the RT1050 Schematic Rev A, J32/J33 are the SWD isolation jumpers, SW4 is
the reset button, and J21 is the 20 pin JTAG/SWD header.

A debug probe is used for both flashing and debugging the board. This board has
an [OpenSDA Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-onboard-debug-probe). The default firmware present on this
probe is the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Based on the host tool installed, please use the following instructions
to setup your debug probe:

- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools): [Using J-Link on NXP OpenSDA Boards](#using-j-link-on-nxp-opensda-boards)
- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools): [Using DAPLink on NXP OpenSDA Boards](#using-daplink-on-nxp-opensda-boards)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools): [Using DAPLink on NXP OpenSDA Boards](#using-daplink-on-nxp-opensda-boards)

#### Using DAPLink on NXP OpenSDA Boards

1. If the debug firmware has been modified, follow the instructions provided at
   [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are populated

#### Using J-Link on NXP OpenSDA Boards

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
board.

To update the onboard debug circuit, please do the following:

1. If the debug firmware has been modified, follow the instructions provided at
   [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are removed.

To attach an external J-Link probe, ensure the SWD isolation jumpers are
removed, and connect the external probe to the JTAG/SWD header.

### Configuring a Debug Probe (Schematic B/B1)

For the RT1050 Schematic Rev B, J47/J48 are the SWD isolation jumpers, J42 is
the DFU mode jumper, and J21 is the 20 pin JTAG/SWD header.

A debug probe is used for both flashing and debugging the board. This board has
an [LPC-LINK2 Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpc-link2-onboard-debug-probe). The default firmware present on this
probe is the [LPC-Link2 DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-daplink-onboard-debug-probe).

Based on the host tool installed, please use the following instructions
to setup your debug probe:

- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools):
  [Using J-Link with LPC-Link2 Probe](#using-j-link-with-lpc-link2-probe)
- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools):
  [Using CMSIS-DAP with LPC-Link2 Probe](#using-cmsis-dap-with-lpc-link2-probe)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools):
  [Using CMSIS-DAP with LPC-Link2 Probe](#using-cmsis-dap-with-lpc-link2-probe)

#### Using CMSIS-DAP with LPC-Link2 Probe

1. Follow the instructions provided at
   [LPC-LINK2 CMSIS DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-cmsis-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are populated

#### Using J-Link with LPC-Link2 Probe

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK.

To update the onboard debug circuit, please do the following:

1. Switch the power source for the EVK to a different source than the
   debug USB, as the J-Link firmware does not power the EVK via the
   debug USB.
2. Follow the instructions provided at
   [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
3. Ensure the SWD isolation jumpers are populated.

To attach an external J-Link probe, ensure the SWD isolation jumpers are
removed, then connect the probe to the external JTAG/SWD header

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J30 and J31 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J28.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1050_evk//hyperflash samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW4 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk//hyperflash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1050_evk//hyperflash samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk//hyperflash
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the boot header in HyperFlash is invalid or corrupted. The boot header is
configured by [`CONFIG_NXP_IMXRT_BOOT_HEADER`](../../../../kconfig.md#CONFIG_NXP_IMXRT_BOOT_HEADER "CONFIG_NXP_IMXRT_BOOT_HEADER").

```shell
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

You can fix it by erasing and reprogramming the HyperFlash with the following
steps:

1. Set the SW7 DIP switches to ON-ON-ON-OFF to prevent booting from HyperFlash.
2. Reset by pressing SW4
3. Run `west debug` or `west flash` again with a known working Zephyr
   application.
4. Set the SW7 DIP switches to OFF-ON-ON-OFF to boot from HyperFlash.
5. Reset by pressing SW4

## Board Revisions

The original MIMXRT1050-EVK (rev A0) board was updated with a newer
MIMXRT1050-EVKB (rev A1) board, with these major hardware differences:

- SoC changed from MIMXRT1052DVL6**A** to MIMXRT1052DVL6**B**
- Hardware bug fixes for: power, interfaces, and memory
- Arduino headers included

For more details, please see the following [NXP i.MXRT1050 A0 to A1 Migration Guide](https://www.nxp.com/docs/en/nxp/application-notes/AN12146.pdf).

Current Zephyr build supports the new MIMXRT1050-EVKB

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
