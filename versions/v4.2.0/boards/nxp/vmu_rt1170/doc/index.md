---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/vmu_rt1170/doc/index.html
original_path: boards/nxp/vmu_rt1170/doc/index.html
---

# VMU RT1170

Board Overview

[![../../../../_images/vmu_rt1170.jpg](../../../../_images/vmu_rt1170.jpg)
](../../../../_images/vmu_rt1170.jpg)

VMU RT1170

Name:
:   `vmu_rt1170`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1176

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/vmu_rt1170/doc/index.rst/../..)

## Overview

The VMU RT1170 features an i.MX RT1176 dual core MCU with the
Cortex-M7 core at 1 GHz and a Cortex-M4 at 400 MHz.
The i.MX RT1176 MCU offers support over a wide temperature range
and is qualified for consumer, industrial and automotive markets.
The VMU RT1170 is the default VMU for CogniPilot’s Cerebri, a
Zephyr RTOS based Autopilot.

## Hardware

- MIMXRT1176DVMAA MCU

  - 1GHz Cortex-M7 & 400Mhz Cortex-M4
  - 2MB SRAM with 512KB of TCM for Cortex-M7 and 256KB of TCM for Cortex-M4
- Memory

  - 512 Mbit Octal Flash
  - TF socket for SD card
- Ethernet

  - 2 wire 100BASE-T1
- USB

  - USB 2.0 connector
- Power

  - Redundant dual picoflex power ports
- Debug

  - 10 pin debug and shell adapter board to 20 Pin JTAG debugger and USB-C shell
- Sensor

  - BMI088 6-axis IMU
  - BMM150 Magnetometer
  - Dual BMP388 Barometer
  - Dual ICM-42688 6-axis IMU
  - IST8310 3-axis Magnetometer
  - U-blox NEO-M8N GNSS module
- UART JST-GH connectors
- I2C JST-GH connectors
- CAN bus JST-GH connectors
- RC IN

  - RC input connector for SBUS compatible RC receivers

For more information about the MIMXRT1176 SoC and VMU RT1170 board, see
these references:

- [VMU RT1170 Schematics](https://github.com/CogniPilot/NXP-VMU_RT117x-HW)
- [i.MX RT1170 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1170CEC.pdf)
- [i.MX RT1170 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1170RM)

### Supported Features

VMU-RT1170 is a “Vehicle Management Unit” based on the general i.MX RT1170
family of processors.

The `vmu_rt1170` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `vmu_rt1170/mimxrt1176/cm7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L16) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L973)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L959) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1203) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp%2Cmcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN CANFD controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L904) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L175) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed factor clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L187) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1017) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L989) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1222) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1232) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP MCUX DAC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L58) | [`nxp,dac12`](../../../../build/dts/api/bindings/dac/nxp%2Cdac12.md#std-dtcompatible-nxp-dac12) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L369) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp%2Cimx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1024)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1043) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1062) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp%2Cpxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L757) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L788)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L761) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L775) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L783) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-board | TJA1103 PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170.dtsi?plain=1#L112) | [`nxp,tja1103`](../../../../build/dts/api/bindings/ethernet/phy/nxp%2Ctja1103.md#std-dtcompatible-nxp-tja1103) |
| GPIO & Headers | on-chip | i.MX GPIO[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L194) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP LPI2C controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L281)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L314) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1076) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp%2Cmcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Futaba SBUS[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L188) | [`futaba,sbus`](../../../../build/dts/api/bindings/input/futaba%2Csbus.md#std-dtcompatible-futaba-sbus) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L43) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L114) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp%2Cimx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170.dtsi?plain=1#L18) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L128) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L796)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L769) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L87) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp%2Cimx-semc.md#std-dtcompatible-nxp-imx-semc) |
| on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L51) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp%2Cflexram.md#std-dtcompatible-nxp-flexram) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L377) | [`nxp,imx-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/nxp%2Cimx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L741) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp%2Cflexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L25) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI MX25UM51345G[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170.dtsi?plain=1#L200) | [`nxp,imx-flexspi-mx25um51345g`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170.dtsi?plain=1#L211) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L347) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L351) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L357) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L363) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP QTMR PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L143)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L151) | [`nxp,qtmr-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cqtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm) |
| on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L557) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cflexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L562)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L592) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| Regulator | on-board | Fixed voltage regulators[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L53) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | IMX CAAM (Cryptographic Acceleration and Assurance Module)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L41) | [`nxp,imx-caam`](../../../../build/dts/api/bindings/rng/nxp%2Cimx-caam.md#std-dtcompatible-nxp-imx-caam) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L842)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L854) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | iSentek ist8310 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L330) | [`isentek,ist8310`](../../../../build/dts/api/bindings/sensor/istentek%2Cist8310.md#std-dtcompatible-isentek-ist8310) |
| on-board | Bosch BMP388 pressure sensor accessed through I2C bus[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L355) | [`bosch,bmp388`](../../../../build/dts/api/compatibles/bosch%2Cbmp388.md#std-dtcompatible-bosch-bmp388) |
| on-board | Bosch BMM150 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L370) | [`bosch,bmm150`](../../../../build/dts/api/compatibles/bosch%2Cbmm150.md#std-dtcompatible-bosch-bmm150) |
| on-board | ICM-42688 motion tracking device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L252) | [`invensense,icm42688`](../../../../build/dts/api/bindings/sensor/invensense%2Cicm42688.md#std-dtcompatible-invensense-icm42688) |
| on-board | BMI08X Accel inertial measurement unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L298) | [`bosch,bmi08x-accel`](../../../../build/dts/api/compatibles/bosch%2Cbmi08x-accel.md#std-dtcompatible-bosch-bmi08x-accel) |
| on-board | BMI08X Gyro inertial measurement unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7.dts?plain=1#L311) | [`bosch,bmi08x-gyro`](../../../../build/dts/api/compatibles/bosch%2Cbmi08x-gyro.md#std-dtcompatible-bosch-bmi08x-gyro) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1175) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp%2Cmcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| Serial controller | on-chip | NXP LPUART[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L461)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L469) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L67)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L77) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L389)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L425) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L96) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cgpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L103) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L810)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L820) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L830) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L866) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp%2Cimx-csi.md#std-dtcompatible-nxp-imx-csi) |
| on-chip | NXP MIPI CSI-2 Rx interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L879) | [`nxp,mipi-csi2rx`](../../../../build/dts/api/bindings/video/nxp%2Cmipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L934) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Cimx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

### Connections and I/Os

The MIMXRT1170 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_00 | FLEXCAN2\_TX | CAN2\_TX |
| GPIO\_AD\_01 | FLEXCAN2\_RX | CAN2\_RX |
| GPIO\_AD\_02 | LPUART8\_TXD | UART8\_TX\_TELEM2 |
| GPIO\_AD\_03 | LPUART8\_RXD | UART8\_RX\_TELEM2 |
| GPIO\_AD\_04 | LPUART8\_CTS\_B | UART8\_CTS\_TELEM2 |
| GPIO\_AD\_05 | LPUART8\_RTS\_B | UART8\_RTS\_TELEM2 |
| GPIO\_AD\_06 | FLEXCAN1\_TX | CAN1\_TX |
| GPIO\_AD\_07 | FLEXCAN1\_RX | CAN1\_RX |
| GPIO\_AD\_08 | LPI2C1\_SCL | I2C1\_SCL\_GPS1 |
| GPIO\_AD\_09 | LPI2C1\_SDA | I2C1\_SDA\_GPS1 |
| GPIO\_AD\_10 | LPADC1\_CH2A | SCALED\_VDD\_3V3\_SENSORS1 |
| GPIO\_AD\_11 | LPADC1\_CH2B | SCALED\_VDD\_3V3\_SENSORS2 |
| GPIO\_AD\_12 | LPADC1\_CH3A | SCALED\_VDD\_3V3\_SENSORS3 |
| GPIO\_AD\_13 | LPADC1\_CH3B | SCALED\_V5 |
| GPIO\_AD\_14 | LPADC1\_CH4A | ADC\_6V6 |
| GPIO\_AD\_15 | LPUART10\_TXD | UART10\_TX\_TELEM3 |
| GPIO\_AD\_16 | LPADC1\_CH5A | ADC\_3V3 |
| GPIO\_AD\_17 | LPADC1\_CHB | SCALED\_VDD\_3V3\_SENSORS4 |
| GPIO\_AD\_18 | LPI2C2\_SCL | I2C2\_SCL\_GPS2 |
| GPIO\_AD\_19 | LPI2C2\_SDA | I2C2\_SDA\_GPS2 |
| GPIO\_AD\_20 | GPIO3\_IO19 | SPI1\_DRDY1\_SENSOR1 |
| GPIO\_AD\_21 | GPIO3\_IO20 | SPI3\_DRDY1\_SENSOR3 |
| GPIO\_AD\_22 | LPADC2\_CH2A | HW\_VER\_SENSE |
| GPIO\_AD\_23 | LPADC2\_CH2B | HW\_REV\_SENSE |
| GPIO\_AD\_24 | LPSPI2\_SCK | SPI2\_SCK\_SENSOR2 |
| GPIO\_AD\_25 | LPSPI2\_PCS0 | SPI2\_nCS0\_SENSOR2 |
| GPIO\_AD\_26 | LPSPI2\_SOUT | SPI2\_MOSI\_SENSOR2 |
| GPIO\_AD\_27 | LPSPI2\_SIN | SPI2\_MISO\_SENSOR2 |
| GPIO\_AD\_28 | LPUART5\_TXD | UART5\_TX\_GPS2 |
| GPIO\_AD\_29 | LPUART5\_RXD | UART5\_RX\_GPS2 |
| GPIO\_AD\_30 | LPUART3\_TXD | UART3\_TX\_GPS1 |
| GPIO\_AD\_31 | LPUART3\_RXD | UART3\_RX\_GPS1 |
| GPIO\_AD\_32 | USDHC1\_CD\_B | USDHC1\_CD |
| GPIO\_AD\_33 | LPUART10\_RXD | UART10\_RX\_TELEM3 |
| GPIO\_AD\_34 | LPUART10\_CTS\_B | UART10\_CTS\_TELEM3 |
| GPIO\_AD\_35 | LPUART10\_RTS\_B | UART10\_RTS\_TELEM3 |
| GPIO\_DISP\_B1\_00 | ENET\_1G\_RX\_EN | ETH\_CRS\_DV |
| GPIO\_DISP\_B1\_01 | ENET\_1G\_RX\_ER | ETH\_RX\_ER |
| GPIO\_DISP\_B1\_02 | LPUART1\_TXD | UART1\_TX\_DEBUG |
| GPIO\_DISP\_B1\_03 | LPUART1\_RXD | UART1\_RX\_DEBUG |
| GPIO\_DISP\_B1\_04 | LPUART4\_RXD | UART4\_RX\_TELEM1 |
| GPIO\_DISP\_B1\_05 | LPUART4\_CTS\_B | UART4\_CTS\_TELEM1 |
| GPIO\_DISP\_B1\_06 | LPUART4\_TXD | UART4\_TX\_TELEM1 |
| GPIO\_DISP\_B1\_07 | LPUART4\_RTS\_B | UART4\_RTS\_TELEM1 |
| GPIO\_DISP\_B1\_08 | ENET\_1G\_TDATA1 | ETH\_TXD1 |
| GPIO\_DISP\_B1\_09 | ENET\_1G\_TDATA0 | ETH\_TXD0 |
| GPIO\_DISP\_B1\_10 | ENET\_1G\_TX\_EN | ETH\_TX\_EN |
| GPIO\_DISP\_B1\_11 | ENET\_1G\_REF\_CLK | ETH\_REF\_CLK |
| GPIO\_DISP\_B2\_00 | GPIO5\_IO01 | nLED\_RED |
| GPIO\_DISP\_B2\_01 | GPIO5\_IO02 | nLED\_GREEN |
| GPIO\_DISP\_B2\_02 | ARM\_TRACE0 | TRACED0 |
| GPIO\_DISP\_B2\_03 | ARM\_TRACE1 | TRACED1 |
| GPIO\_DISP\_B2\_04 | ARM\_TRACE2 | TRACED2 |
| GPIO\_DISP\_B2\_05 | ARM\_TRACE3 | TRACED3 |
| GPIO\_DISP\_B2\_06 | ARM\_TRACE\_CLK | TRACECLK |
| GPIO\_DISP\_B2\_07 | ARM\_TRACE\_SWO | TRACESWO |
| GPIO\_DISP\_B2\_08 | GPIO5\_IO09 | ETH\_POWER\_EN |
| GPIO\_DISP\_B2\_09 | GPIO5\_IO10 | ETH\_PHY\_nINT |
| GPIO\_DISP\_B2\_10 | LPI2C3\_SCL | I2C3\_SCL\_FMU |
| GPIO\_DISP\_B2\_11 | LPI2C3\_SDA | I2C3\_SDA\_FMU |
| GPIO\_DISP\_B2\_12 | LPSPI4\_SCK | SPI4\_SCK\_SENSOR4 |
| GPIO\_DISP\_B2\_13 | LPSPI4\_SIN | SPI4\_MISO\_SENSOR4 |
| GPIO\_DISP\_B2\_14 | LPSPI4\_SOUT | SPI4\_MOSI\_SENSOR4 |
| GPIO\_DISP\_B2\_15 | LPSPI4\_PCS0 | SPI4\_nCS0\_SENSOR4 |
| GPIO\_EMC\_B1\_00 | FLEXPWM4\_PWM0\_A + FLEXIO1\_IO00 | FMU\_CH11 |
| GPIO\_EMC\_B1\_01 | GPIO1\_IO01 | VDD\_3V3\_SD\_CARD\_EN |
| GPIO\_EMC\_B1\_02 | FLEXPWM4\_PWM1\_A + FLEXIO1\_IO02 | FMU\_CH12 |
| GPIO\_EMC\_B1\_03 | GPIO1\_IO03 | FMU\_nSAFETY\_SWITCH\_LED\_OUT |
| GPIO\_EMC\_B1\_04 | GPIO1\_IO04 | NFC\_GPIO |
| GPIO\_EMC\_B1\_05 | GPIO1\_IO05 | SPI6\_DRDY1\_EXTERNAL1 |
| GPIO\_EMC\_B1\_06 | FLEXPWM2\_PWM0\_A + FLEXIO1\_IO06 | FMU\_CH4 |
| GPIO\_EMC\_B1\_07 | GPIO1\_IO07 | SPI6\_DRDY2\_EXTERNAL1 |
| GPIO\_EMC\_B1\_08 | FLEXPWM2\_PWM1\_A + FLEXIO1\_IO08 | FMU\_CH5 |
| GPIO\_EMC\_B1\_09 | GPT5\_CAPTURE1 | FMU\_PPM\_INPUT |
| GPIO\_EMC\_B1\_10 | FLEXPWM2\_PWM2\_A + FLEXIO1\_IO10 | FMU\_CH6 |
| GPIO\_EMC\_B1\_11 | GPIO1\_IO11 | SPI6\_nRESET\_EXTERNAL1 |
| GPIO\_EMC\_B1\_12 | GPIO1\_IO12 | VDD\_5V\_HIPOWER\_nOC |
| GPIO\_EMC\_B1\_13 | GPIO1\_IO13 | nLED\_BLUE |
| GPIO\_EMC\_B1\_14 | GPIO1\_IO14 | VDD\_3V3\_SENSORS3\_EN |
| GPIO\_EMC\_B1\_15 | GPIO1\_IO15 | VDD\_5V\_PERIPH\_nOC |
| GPIO\_EMC\_B1\_16 | GPIO1\_IO16 | SPI4\_DRDY1\_SENSOR4 |
| GPIO\_EMC\_B1\_17 | GPIO1\_IO17 | nARMED |
| GPIO\_EMC\_B1\_18 | TMR2\_TIMER0 | SPIX\_SYNC |
| GPIO\_EMC\_B1\_19 | FLEXPWM2\_PWM3\_A + FLEXIO1\_IO19 | FMU\_CH7 |
| GPIO\_EMC\_B1\_20 | TMR4\_TIMER0 | FMU\_CAP1 |
| GPIO\_EMC\_B1\_21 | FLEXPWM3\_PWM3\_A + FLEXIO1\_IO21 | FMU\_CH10 |
| GPIO\_EMC\_B1\_22 | GPIO1\_IO22 | VDD\_3V3\_SENSORS2\_EN |
| GPIO\_EMC\_B1\_23 | FLEXPWM1\_PWM0\_A | FMU\_CH1 |
| GPIO\_EMC\_B1\_24 | GPIO1\_IO24 | FMU\_SAFETY\_SWITCH\_IN |
| GPIO\_EMC\_B1\_25 | FLEXPWM1\_PWM1\_A + FLEXIO1\_IO25 | FMU\_CH2 |
| GPIO\_EMC\_B1\_26 | GPIO1\_IO26 | HW\_VER\_REV\_DRIVE |
| GPIO\_EMC\_B1\_27 | FLEXPWM1\_PWM2\_A + FLEXIO1\_IO27 | FMU\_CH3 |
| GPIO\_EMC\_B1\_28 | GPIO1\_IO28 | nPOWER\_IN\_A |
| GPIO\_EMC\_B1\_29 | FLEXPWM3\_PWM0\_A + FLEXIO1\_IO29 | FMU\_CH8 |
| GPIO\_EMC\_B1\_30 | GPIO1\_IO30 | nPOWER\_IN\_B |
| GPIO\_EMC\_B1\_31 | FLEXPWM3\_PWM1\_A + FLEXIO1\_IO31 | FMU\_CH9 |
| GPIO\_EMC\_B1\_32 | GPIO2\_IO00 | nPOWER\_IN\_C |
| GPIO\_EMC\_B1\_33 | GPIO2\_IO01 | VDD\_3V3\_SENSORS1\_EN |
| GPIO\_EMC\_B1\_34 | GPIO2\_IO02 | VDD\_5V\_PERIPH\_nEN |
| GPIO\_EMC\_B1\_35 | GPIO2\_IO03 | I2C2\_DRDY1 |
| GPIO\_EMC\_B1\_36 | GPIO2\_IO04 | VDD\_3V3\_SENSORS4\_EN |
| GPIO\_EMC\_B1\_37 | GPIO2\_IO05 | VDD\_5V\_HIPOWER\_nEN |
| GPIO\_EMC\_B1\_38 | GPIO2\_IO06 | VDD\_3V3\_SPEKTRUM\_POWER\_EN |
| GPIO\_EMC\_B1\_39 | GPIO2\_IO07 | SPI2\_DRDY1\_SENSOR2 |
| GPIO\_EMC\_B1\_40 | LPUART6\_TXD | UART6\_TX\_TO\_IO\_\_RC\_INPUT |
| GPIO\_EMC\_B1\_41 | LPUART6\_RXD | UART6\_RX\_FROM\_IO\_\_NC |
| GPIO\_EMC\_B2\_00 | LPSPI1\_SCK | SPI1\_SCK\_SENSOR1 |
| GPIO\_EMC\_B2\_01 | LPSPI1\_PCS0 | SPI1\_nCS0\_SENSOR1 |
| GPIO\_EMC\_B2\_02 | LPSPI1\_SOUT | SPI1\_MOSI\_SENSOR1 |
| GPIO\_EMC\_B2\_03 | LPSPI1\_SIN | SPI1\_MISO\_SENSOR1 |
| GPIO\_EMC\_B2\_04 | LPSPI3\_SCK | SPI3\_SCK\_SENSOR3 |
| GPIO\_EMC\_B2\_05 | LPSPI3\_PCS0 | SPI3\_nCS0\_SENSOR3 |
| GPIO\_EMC\_B2\_06 | LPSPI3\_SOUT | SPI3\_MOSI\_SENSOR3 |
| GPIO\_EMC\_B2\_07 | LPSPI3\_SIN | SPI3\_MISO\_SENSOR3 |
| GPIO\_EMC\_B2\_08 | LPSPI3\_PCS1 | SPI3\_nCS1\_SENSOR3 |
| GPIO\_EMC\_B2\_09 | TMR1\_TIMER0 | BUZZER\_1 |
| GPIO\_EMC\_B2\_10 | FLEXSPI2\_A\_SCLK | FLEXSPI2\_SCK\_FRAM |
| GPIO\_EMC\_B2\_11 | FLEXSPI2\_A\_SS0\_B | FLEXSPI2\_nCS0\_FRAM |
| GPIO\_EMC\_B2\_12 | GPIO2\_IO22 | GPIO\_EMC\_B2\_12 |
| GPIO\_EMC\_B2\_13 | FLEXSPI2\_A\_DATA0 | FLEXSPI2\_DATA0\_FRAM |
| GPIO\_EMC\_B2\_14 | FLEXSPI2\_A\_DATA1 | FLEXSPI2\_DATA1\_FRAM |
| GPIO\_EMC\_B2\_15 | ENET\_1G\_RDATA0 | ETH\_RXD0 |
| GPIO\_EMC\_B2\_16 | ENET\_1G\_RDATA1 | ETH\_RXD1 |
| GPIO\_EMC\_B2\_17 | TMR3\_TIMER0 | HEATER |
| GPIO\_EMC\_B2\_18 | GPIO2\_IO28 | SPI3\_DRDY2\_SENSOR3 |
| GPIO\_EMC\_B2\_19 | ENET\_1G\_MDC | ETH\_MDC |
| GPIO\_EMC\_B2\_20 | ENET\_1G\_MDIO | ETH\_MDIO |
| GPIO\_LPSR\_00 | FLEXCAN3\_TX | CAN3\_TX |
| GPIO\_LPSR\_01 | FLEXCAN3\_RX | CAN3\_RX |
| GPIO\_LPSR\_02 | SRC\_BOOT\_MODE00 | BT\_MODE0 |
| GPIO\_LPSR\_03 | SRC\_BOOT\_MODE01 | BT\_MODE1 |
| GPIO\_LPSR\_04 | LPUART11\_TXD | UART11\_TX\_EXTERNAL2 |
| GPIO\_LPSR\_05 | LPUART11\_RXD | UART11\_RX\_EXTERNAL2 |
| GPIO\_LPSR\_06 | LPI2C6\_SDA | I2C6\_SDA\_EXTERNAL2 |
| GPIO\_LPSR\_07 | LPI2C6\_SCL | I2C6\_SCL\_EXTERNAL2 |
| GPIO\_LPSR\_08 | LPSPI6\_PCS1 | SPI6\_nCS1\_EXTERNAL1 |
| GPIO\_LPSR\_09 | LPSPI6\_PCS0 | SPI6\_nCS0 |
| GPIO\_LPSR\_10 | LPSPI6\_SCK | SPI6\_SCK\_EXTERNAL1 |
| GPIO\_LPSR\_11 | LPSPI6\_SOUT | SPI6\_MOSI\_EXTERNAL1 |
| GPIO\_LPSR\_12 | LPSPI6\_SIN | SPI6\_MISO\_EXTERNAL1 |
| GPIO\_LPSR\_13 | JTAG\_MOD | NC\_JTAG\_MOD\_PD |
| GPIO\_LPSR\_14 | SWD\_CLK | FMU\_SWCLK |
| GPIO\_LPSR\_15 | SWD\_DIO | FMU\_SWDIO |
| GPIO\_SD\_B1\_00 | USDHC1\_CMD | USDHC1\_CMD |
| GPIO\_SD\_B1\_01 | USDHC1\_CLK | USDHC1\_CLK |
| GPIO\_SD\_B1\_02 | USDHC1\_DATA0 | USDHC1\_DATA0 |
| GPIO\_SD\_B1\_03 | USDHC1\_DATA1 | USDHC1\_DATA1 |
| GPIO\_SD\_B1\_04 | USDHC1\_DATA2 | USDHC1\_DATA2 |
| GPIO\_SD\_B1\_05 | USDHC1\_DATA3 | USDHC1\_DATA3 |
| GPIO\_SD\_B2\_00 | FLEXSPI1\_B\_DATA3 | FLEXSPI1\_DATA7\_HYPERFLASH |
| GPIO\_SD\_B2\_01 | FLEXSPI1\_B\_DATA2 | FLEXSPI1\_DATA6\_HYPERFLASH |
| GPIO\_SD\_B2\_02 | FLEXSPI1\_B\_DATA1 | FLEXSPI1\_DATA5\_HYPERFLASH |
| GPIO\_SD\_B2\_03 | FLEXSPI1\_B\_DATA0 | FLEXSPI1\_DATA4\_HYPERFLASH |
| GPIO\_SD\_B2\_04 | FLEXSPI1\_B\_SCLK | FLEXSPI1\_nSCK\_HYPERFLASH |
| GPIO\_SD\_B2\_05 | FLEXSPI1\_A\_DQS | FLEXSPI1\_DQS\_HYPERFLASH |
| GPIO\_SD\_B2\_06 | FLEXSPI1\_A\_SS0\_B | FLEXSPI1\_nCS0\_HYPERFLASH |
| GPIO\_SD\_B2\_07 | FLEXSPI1\_A\_SCLK | FLEXSPI1\_SCK\_HYPERFLASH |
| GPIO\_SD\_B2\_08 | FLEXSPI1\_A\_DATA0 | FLEXSPI1\_DATA0\_HYPERFLASH |
| GPIO\_SD\_B2\_09 | FLEXSPI1\_A\_DATA0 | FLEXSPI1\_DATA1\_HYPERFLASH |
| GPIO\_SD\_B2\_10 | FLEXSPI1\_A\_DATA2 | FLEXSPI1\_DATA2\_HYPERFLASH |
| GPIO\_SD\_B2\_11 | FLEXSPI1\_A\_DATA3 | FLEXSPI1\_DATA3\_HYPERFLASH |
| USB1\_DN | USB\_OG1\_DN | USB\_D\_N |
| USB1\_DP | USB\_OTG1\_DP | USB\_D\_P |
| USB1\_VBUS | USB\_OTG1\_VBUS | VBUS |

### Serial Port

The MIMXRT1170 SoC has 12 UARTs.

## Programming and Debugging

The `vmu_rt1170` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board.

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Connect the J-Link debugger through the debug adapter board.

### Configuring a Console

Use the USB-C from the debug adapter board to access the console with
the following settings for your serial terminal of choice (screen, minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b vmu_rt1170 samples/hello_world
west flash
```

You should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! vmu_rt1170
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b vmu_rt1170 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! vmu_rt1170
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
