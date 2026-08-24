---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt1062_fmurt6/doc/index.html
original_path: boards/nxp/mimxrt1062_fmurt6/doc/index.html
---

# FMURT6

Board Overview

[![../../../../_images/mimxrt1062_fmurt6.webp](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1062_fmurt6.webp)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1062_fmurt6.webp)

FMURT6

Name:
:   `mimxrt1062_fmurt6`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1062

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1062_fmurt6/doc/index.rst/../..)

## Overview

The MIMXRT1062\_FMURT6 adds to the industry’s crossover
processor series and expands the i.MX RT series to three scalable families.

The i.MX RT1062 doubles the On-Chip SRAM to 1MB while keeping pin-to-pin
compatibility with i.MX RT1050. This series introduces additional features
ideal for real-time applications such as High-Speed GPIO, CAN FD, and
synchronous parallel NAND/NOR/PSRAM controller. The i.MX RT1062 runs on the
Arm® Cortex-M7® core up to 600 MHz.

## Hardware

- MIMXRT1062DVL6B MCU (600 MHz, 1024 KB on-chip memory)
- Memory

  - 256 Mbit SDRAM
  - 512 Mbit Hyper Flash
  - TF socket for SD card
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

  - BMI088 6-axis e-compass
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1062 SoC and MIMXRT1062-FMURT6 board, see
these references:

- [i.MX RT1060 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060)
- [i.MX RT1060 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1060RM)
- [MIMXRT1062-FMURT6 User Guide](https://docs.px4.io/master/en/)
- [MIMXRT1062-FMURT6 Schematics](https://github.com/NXPHoverGames/NXP-FMUMRT6)

### Supported Features

The `mimxrt1062_fmurt6` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt1062_fmurt6/mimxrt1062` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L596) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp,mcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1116) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L929)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L939) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
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
| Ethernet | on-chip | NXP ENET IP Module[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L790) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1060.dtsi?plain=1#L38)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L794) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L808) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L407) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| GPIO & Headers | on-chip | i.MX GPIO[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP LPI2C controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L396)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L418) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L994) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1060.dtsi?plain=1#L46)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L802) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L147) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| Miscellaneous | on-chip | NXP FlexIO controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1183) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI HyperFlash[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L188) | [`nxp,imx-flexspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-hyperflash.md#std-dtcompatible-nxp-imx-flexspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L206) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L980) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L606) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L657)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L611) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| Regulator | on-board | Fixed voltage regulators[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L54) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp,imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L879)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L891) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | Bosch BMP388 pressure sensor accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L247) | [`bosch,bmp388`](../../../../build/dts/api/compatibles/bosch,bmp388.md#std-dtcompatible-bosch-bmp388) |
| on-board | Bosch BMM150 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L259) | [`bosch,bmm150`](../../../../build/dts/api/compatibles/bosch,bmm150.md#std-dtcompatible-bosch-bmm150) |
| on-board | STMicroelectronics ISM330DHCX 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L313) | [`st,ism330dhcx`](../../../../build/dts/api/compatibles/st,ism330dhcx.md#std-dtcompatible-st-ism330dhcx) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1088) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1142) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp,tempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L516)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
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
already supported, which can also be re-used on this mimxrt1060\_evk board.

### Connections and I/Os

The MIMXRT1062 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B1\_08 | FLEXCAN1 TX | CAN |
| GPIO\_B0\_03 | FLEXCAN1 RX | CAN |
| GPIO\_AD\_B0\_06 | PWM2A0 | PWM |
| GPIO\_EMC\_08 | PWM2A1 | PWM |
| GPIO\_EMC\_10 | PWM2A2 | PWM |
| GPIO\_AD\_B0\_09 | PWM2A3 | PWM |
| GPIO\_EMC\_31 | LPUART7\_TX | UART Console |
| GPIO\_EMC\_32 | LPUART7\_RX | UART Console |
| GPIO\_B0\_04 | LPI2C2\_SCL | I2C |
| GPIO\_B0\_05 | LPI2C2\_SDA | I2C |
| GPIO\_AD\_B1\_00 | LPI2C1\_SCL | I2C |
| GPIO\_AD\_B1\_01 | LPI2C1\_SDA | I2C |
| GPIO\_AD\_B0\_12 | LPI2C4\_SCL | I2C |
| GPIO\_AD\_B0\_13 | LPI2C4\_SDA | I2C |
| WAKEUP | GPIO | SW0 |
| GPIO\_B1\_01 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_B1\_02 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_B1\_03 | ENET\_RX\_EN | Ethernet |
| GPIO\_B0\_12 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_B0\_13 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_B0\_14 | ENET\_TX\_EN | Ethernet |
| GPIO\_B0\_15 | ENET\_REF\_CLK | Ethernet |
| GPIO\_B1\_00 | ENET\_RX\_ER | Ethernet |
| GPIO\_B1\_12 | GPIO | SD Card |
| GPIO\_B1\_14 | USDHC1\_VSELECT | SD Card |
| GPIO\_EMC\_40 | ENET\_MDC | Ethernet |
| GPIO\_B0\_01 | ENET\_MDIO | Ethernet |
| GPIO\_SD\_B0\_00 | USDHC1\_CMD | SD Card |
| GPIO\_SD\_B0\_01 | USDHC1\_CLK | SD Card |
| GPIO\_SD\_B0\_02 | USDHC1\_DATA0 | SD Card |
| GPIO\_SD\_B0\_03 | USDHC1\_DATA1 | SD Card |
| GPIO\_SD\_B0\_04 | USDHC1\_DATA2 | SD Card |
| GPIO\_SD\_B0\_05 | USDHC1\_DATA3 | SD Card |
| GPIO\_EMC\_27 | LPSPI1\_SCK | SPI |
| GPIO\_EMC\_28 | LPSPI1\_SDO | SPI |
| GPIO\_EMC\_29 | LPSPI1\_SDI | SPI |
| GPIO\_EMC\_00 | LPSPI2\_SCK | SPI |
| GPIO\_EMC\_02 | LPSPI2\_SDO | SPI |
| GPIO\_EMC\_03 | LPSPI2\_SDI | SPI |
| GPIO\_AD\_B1\_15 | LPSPI3\_SCK | SPI |
| GPIO\_AD\_B1\_14 | LPSPI3\_SDO | SPI |
| GPIO\_AD\_B1\_13 | LPSPI3\_SDI | SPI |
| GPIO\_AD\_B1\_11 | ADC | ADC1 Channel 0 |
| GPIO\_AD\_B1\_09 | ADC | ADC1 Channel 14 |
| GPIO\_AD\_B0\_15 | ADC | ADC1 Channel 4 |
| GPIO\_AD\_B1\_02 | UART2\_TX\_GPS1 | UART GPS |
| GPIO\_AD\_B1\_03 | UART2\_RX\_GPS1 | UART GPS |

### System Clock

The MIMXRT1062 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1062 SoC has eight UARTs. `LPUART7` is configured for the console,
`LPUART8 and 2` for GPS/MAG, `LPUART3 and 4` for Telemetry and the remaining are not used.

## Programming and Debugging

The `mimxrt1062_fmurt6` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must reconfigure the board for one of the
following debug probes instead.

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

For Hyperflash support on i.MxRT106x use JLink\_V780 or above.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
FMURT6 on J23 FMU Debug Port.
Run JLink.exe and choose device / core as MIMXRT106A-ALEXA.

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to PixHawk debug adapter.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

#### Using SWO

SWO can be used as a logging backend, by setting `CONFIG_LOG_BACKEND_SWO=y`.
Your SWO viewer should be configured with a CPU frequency of 132MHz, and
SWO frequency of 7500KHz.

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

### Troubleshooting

If the west flash or debug commands fail, and the command hangs while executing
runners.jlink, confirm the J-Link debug probe is configured, powered, and
connected to the FMURT6 properly.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
