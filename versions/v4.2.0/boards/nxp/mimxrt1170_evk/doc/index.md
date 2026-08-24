---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt1170_evk/doc/index.html
original_path: boards/nxp/mimxrt1170_evk/doc/index.html
---

# MIMXRT1170-EVK/EVKB

Board Overview

[![../../../../_images/mimxrt1170_evk.jpg](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1170_evk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1170_evk.jpg)

MIMXRT1170-EVK/EVKB

Name:
:   `mimxrt1170_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1176

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1170_evk/doc/index.rst/../..)

## Overview

The dual core i.MX RT1170 runs on the Cortex-M7 core at 1 GHz and on the Cortex-M4
at 400 MHz. The i.MX RT1170 MCU offers support over a wide temperature range
and is qualified for consumer, industrial and automotive markets. Zephyr
supports the initial revision of this EVK, as well as rev EVKB.

## Hardware

- MIMXRT1176DVMAA MCU

  - 1GHz Cortex-M7 & 400Mhz Cortex-M4
  - 2MB SRAM with 512KB of TCM for Cortex-M7 and 256KB of TCM for Cortex-M4
- Memory

  - 512 Mbit SDRAM
  - 128 Mbit QSPI Flash
  - 512 Mbit Octal Flash
  - 2 Gbit raw NAND flash
  - 64 Mbit LPSPI flash
  - TF socket for SD card
- Display

  - MIPI LCD connector
- Ethernet

  - 10/100 Mbit/s Ethernet PHY
  - 10/100/1000 Mbit/s Ethernet PHY
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
  - on-board debugger
- Sensor

  - FXOS8700CQ 6-axis e-compass
  - MIPI camera sensor connector
- Expansion port

  - Arduino interface
  - M.2 WIFI/BT interface
- CAN bus connector

For more information about the MIMXRT1170 SoC and MIMXRT1170-EVK board, see
these references:

- [i.MX RT1170 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170)
- [i.MX RT1170 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1170CEC.pdf)
- [i.MX RT1170 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1170RM)
- [MIMXRT1170-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1170-evaluation-kit:MIMXRT1170-EVK)
- [MIMXRT1170-EVKB Board Hardware User’s Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1170EVKBHUG)
- [MIMXRT1170-EVK Board Hardware User’s Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1170EVKHUG)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| W9825G6KH SDRAM | SEMC | Enabled via device configuration data (DCD) block, which sets up the SEMC at boot time |
| IS25WP128 QSPI flash (RT1170 EVK) | FLEXSPI | Enabled via flash configuration block (FCB), which sets up the FLEXSPI at boot time. |
| W25Q512NWEIQ QSPI flash (RT1170 EVKB) | FLEXSPI | Enabled via flash configuration block (FCB), which sets up the FLEXSPI at boot time. Supported for XIP only. |

### Supported Features

NXP considers the MIMXRT1170-EVK as the superset board for the i.MX RT11xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT11xx family.

The `mimxrt1170_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt1170_evk@A/mimxrt1176/cm4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L11) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | LPC LPADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L959) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1203) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN CANFD controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L904) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L175) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed factor clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L187) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1017) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L989) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp,kinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1222) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1232) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP MCUX DAC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L58) | [`nxp,dac12`](../../../../build/dts/api/bindings/dac/nxp,dac12.md#std-dtcompatible-nxp-dac12) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L369) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1043)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1024) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1062) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L757) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L761)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L788) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L149) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L775)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L802) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L783) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L178) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX GPIO[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L194) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L53) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L281)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L292) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1076)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1099) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L69) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L769)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L796) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L87) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L377) | [`nxp,imx-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L741) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L20) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L256) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L266) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L347) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L351) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L357) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L363) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP QTMR PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L143) | [`nxp,qtmr-pwm`](../../../../build/dts/api/bindings/pwm/nxp,qtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm) |
| on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L557) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L582)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L562) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| SDHC | on-chip | NXP imx USDHC controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L842) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L93) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1175) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L461)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L469) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L67)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L77) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L389) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L96) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L103) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L810) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L830) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L866) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| on-chip | NXP MIPI CSI-2 Rx interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L879) | [`nxp,mipi-csi2rx`](../../../../build/dts/api/bindings/video/nxp,mipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L934) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

#### `mimxrt1170_evk@A/mimxrt1176/cm7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L16) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L959)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L973) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1203) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L924)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L904) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L175) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed factor clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L187) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1017) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L989) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp,kinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1222) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1232) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP MCUX DAC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L58) | [`nxp,dac12`](../../../../build/dts/api/bindings/dac/nxp,dac12.md#std-dtcompatible-nxp-dac12) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L369) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1024)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1043) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1062) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L757) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L761)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L788) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L149) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L775)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L802) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L783) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L178) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX GPIO[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L194) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L53) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on NXP 44-pin board-to-board camera connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7.dts?plain=1#L70) | [`nxp,cam-44pins-connector`](../../../../build/dts/api/bindings/gpio/nxp,cam-44pins-connector.md#std-dtcompatible-nxp-cam-44pins-connector) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L325)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L281) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1076)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1099) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L114) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L769)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L796) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L87) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L51) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L377) | [`nxp,imx-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L741) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L25) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L256) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L266) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L347) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L351) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L357) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L363) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP QTMR PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L143) | [`nxp,qtmr-pwm`](../../../../build/dts/api/bindings/pwm/nxp,qtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm) |
| on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L557) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L582)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L562) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | IMX CAAM (Cryptographic Acceleration and Assurance Module)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L41) | [`nxp,imx-caam`](../../../../build/dts/api/bindings/rng/nxp,imx-caam.md#std-dtcompatible-nxp-imx-caam) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L842)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L854) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L93) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1175) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L461)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L469) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L67)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L77) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L389)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L401) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L96) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L103) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L810)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L820) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L830)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L836) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L866) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| on-chip | NXP MIPI CSI-2 Rx interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L879) | [`nxp,mipi-csi2rx`](../../../../build/dts/api/bindings/video/nxp,mipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L934) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

#### `mimxrt1170_evk@B/mimxrt1176/cm4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L11) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | LPC LPADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L959) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1203) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| CAN | on-chip | NXP FlexCAN CANFD controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L904) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L175) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed factor clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L187) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1017) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L989) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp,kinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1222) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1232) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP MCUX DAC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L58) | [`nxp,dac12`](../../../../build/dts/api/bindings/dac/nxp,dac12.md#std-dtcompatible-nxp-dac12) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L369) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1043)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1024) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1062) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L757) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L761)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L788) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L149) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L775)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L802) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L783) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L178) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX GPIO[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L194) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L53) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L281)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L292) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1076)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1099) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L69) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L769)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L796) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L87) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L377) | [`nxp,imx-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L741) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L20) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm4_B.overlay?plain=1#L24) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm4_B.overlay?plain=1#L34) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L347) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L351) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L357) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L363) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP QTMR PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L143) | [`nxp,qtmr-pwm`](../../../../build/dts/api/bindings/pwm/nxp,qtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm) |
| on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L557) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L582)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L562) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| SDHC | on-chip | NXP imx USDHC controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L842) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1175) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L461)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L469) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L67)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L77) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L389)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L401) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm4.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L96) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L103) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L810) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L830) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L866) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| on-chip | NXP MIPI CSI-2 Rx interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L879) | [`nxp,mipi-csi2rx`](../../../../build/dts/api/bindings/video/nxp,mipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L934) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

#### `mimxrt1170_evk@B/mimxrt1176/cm7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L16) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L959)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L973) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1203) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| Audio | on-board | WM8962 audio codec[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_B.overlay?plain=1#L114) | [`wolfson,wm8962`](../../../../build/dts/api/bindings/audio/wolfson,wm8962.md#std-dtcompatible-wolfson-wm8962) |
| Bluetooth | on-board | Bluetooth module that uses NXP’s Bluetooth Module (e.g[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_B.overlay?plain=1#L90) | [`nxp,bt-hci-uart`](../../../../build/dts/api/bindings/bluetooth/nxp,bt-hci-uart.md#std-dtcompatible-nxp-bt-hci-uart) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L924)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L904) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM Rev2 (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L175) | [`nxp,imx-ccm-rev2`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2) |
| on-chip | Generic fixed factor clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L187) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1017) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L51) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L989) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp,kinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1222) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1232) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP MCUX DAC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L58) | [`nxp,dac12`](../../../../build/dts/api/bindings/dac/nxp,dac12.md#std-dtcompatible-nxp-dac12) |
| Display | on-chip | NXP i.MX eLCDIF (Enhanced LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L369) | [`nxp,imx-elcdif`](../../../../build/dts/api/bindings/display/nxp,imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1024)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1043) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1062) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L757) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L761)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L788) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_B.overlay?plain=1#L75) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L775)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L802) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L783) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L178) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| GPIO & Headers | on-chip | i.MX GPIO[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L194) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L53) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on NXP 44-pin board-to-board camera connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7.dts?plain=1#L70) | [`nxp,cam-44pins-connector`](../../../../build/dts/api/bindings/gpio/nxp,cam-44pins-connector.md#std-dtcompatible-nxp-cam-44pins-connector) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L325)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L281) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1076)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1099) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L114) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk.dtsi?plain=1#L45) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L769)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L796) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Memory controller | on-chip | NXP Smart External Memory Controller (SEMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L87) | [`nxp,imx-semc`](../../../../build/dts/api/bindings/memory-controllers/nxp,imx-semc.md#std-dtcompatible-nxp-imx-semc) |
| on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L51) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L377) | [`nxp,imx-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi) |
| Miscellaneous | on-chip | NXP FlexIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L741) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L25) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_B.overlay?plain=1#L28) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_B.overlay?plain=1#L38) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L347) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L351) | [`nxp,mcux-rt11xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L357) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L363) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP QTMR PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L143) | [`nxp,qtmr-pwm`](../../../../build/dts/api/bindings/pwm/nxp,qtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm) |
| on-chip | NXP eFLEX PWM module with mcux-pwm submodules[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L557) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L582)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L562) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | IMX CAAM (Cryptographic Acceleration and Assurance Module)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx_cm7.dtsi?plain=1#L41) | [`nxp,imx-caam`](../../../../build/dts/api/bindings/rng/nxp,imx-caam.md#std-dtcompatible-nxp-imx-caam) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L842)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L854) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp,imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L1175) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L461)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L477) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L67)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L77) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L389)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L401) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L96) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L103) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L810)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L820) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L830)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L836) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Video | on-chip | NXP MCUX CMOS sensor interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L866) | [`nxp,imx-csi`](../../../../build/dts/api/bindings/video/nxp,imx-csi.md#std-dtcompatible-nxp-imx-csi) |
| on-chip | NXP MIPI CSI-2 Rx interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L879) | [`nxp,mipi-csi2rx`](../../../../build/dts/api/bindings/video/nxp,mipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt11xx.dtsi?plain=1#L934) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

### Connections and I/Os

The MIMXRT1170 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| WAKEUP | GPIO | SW7 |
| GPIO\_AD\_04 | GPIO | LED |
| GPIO\_AD\_24 | LPUART1\_TX | UART Console |
| GPIO\_AD\_25 | LPUART1\_RX | UART Console |
| GPIO\_LPSR\_00 | CAN3\_TX | flexcan |
| GPIO\_LPSR\_01 | CAN3\_RX | flexcan |
| GPIO\_AD\_29 | SPI1\_CS0 | spi |
| GPIO\_AD\_28 | SPI1\_CLK | spi |
| GPIO\_AD\_30 | SPI1\_SDO | spi |
| GPIO\_AD\_31 | SPI1\_SDI | spi |
| GPIO\_AD\_08 | LPI2C1\_SCL | i2c |
| GPIO\_AD\_09 | LPI2C1\_SDA | i2c |
| GPIO\_LPSR\_05 | LPI2C5\_SCL | i2c |
| GPIO\_LPSR\_04 | LPI2C5\_SDA | i2c |
| GPIO\_AD\_04 | FLEXPWM1\_PWM2 | pwm |
| GPIO\_AD\_32 | ENET\_MDC | Ethernet |
| GPIO\_AD\_33 | ENET\_MDIO | Ethernet |
| GPIO\_DISP\_B2\_02 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_03 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_04 | ENET\_TX\_EN | Ethernet |
| GPIO\_DISP\_B2\_05 | ENET\_REF\_CLK | Ethernet |
| GPIO\_DISP\_B2\_06 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_07 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_08 | ENET\_RX\_EN | Ethernet |
| GPIO\_DISP\_B2\_09 | ENET\_RX\_ER | Ethernet |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI\_MCLK | SAI |
| GPIO\_AD\_21\_SAI1\_TX\_DATA00 | SAI1\_TX\_DATA | SAI |
| GPIO\_AD\_22\_SAI1\_TX\_BCLK | SAI1\_TX\_BCLK | SAI |
| GPIO\_AD\_23\_SAI1\_TX\_SYNC | SAI1\_TX\_SYNC | SAI |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI1\_MCLK | SAI |
| GPIO\_AD\_20\_SAI1\_RX\_DATA00 | SAI1\_RX\_DATA00 | SAI |
| GPIO\_DISP\_B2\_10 | LPUART2\_TX | M.2 BT HCI |
| GPIO\_DISP\_B2\_11 | LPUART2\_RX | M.2 BT HCI |
| GPIO\_DISP\_B2\_12 | LPUART2\_CTS\_B | M.2 BT HCI |
| GPIO\_DISP\_B2\_13 | LPUART1\_RTS\_B | M.2 BT HCI |

## Dual Core samples

| Core | Boot Address | Comment |
| --- | --- | --- |
| Cortex M7 | 0x30000000[630K] | primary core |
| Cortex M4 | 0x20020000[96k] | boots from OCRAM |

| Memory | Address[Size] | Comment |
| --- | --- | --- |
| flexspi1 | 0x30000000[16M] | Cortex M7 flash |
| sdram0 | 0x80030000[64M] | Cortex M7 ram |
| ocram | 0x20020000[512K] | Cortex M4 “flash” |
| sram1 | 0x20000000[128K] | Cortex M4 ram |
| ocram2 | 0x200C0000[512K] | Mailbox/shared memory |

Only the first 16K of ocram2 has the correct MPU region attributes set to be
used as shared memory

### System Clock

The MIMXRT1170 SoC is configured to use SysTick as the system clock source,
running at 996MHz. When targeting the M4 core, SysTick will also be used,
running at 400MHz

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1170 SoC has 12 UARTs. `LPUART1` is configured for the console,
`LPUART2` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

### Fetch Binary Blobs

The board Bluetooth/WiFi module requires fetching some binary blob files, to do
that run the command:

```shell
west blobs fetch hal_nxp
```

Note

Only Bluetooth functionality is currently supported.

## Programming and Debugging

The `mimxrt1170_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Building a Dual-Core Image

Dual core samples load the M4 core image from flash into the shared `ocram`
region. The M7 core then sets the M4 boot address to this region. The only
sample currently enabled for dual core builds is the `openamp` sample.
To flash a dual core sample, the M4 image must be flashed first, so that it is
written to flash. Then, the M7 image must be flashed. The openamp sysbuild
sample will do this automatically by setting the image order.

The secondary core can be debugged normally in single core builds
(where the target is `mimxrt1170_evk/mimxrt1176/cm4`). For dual core builds, the
secondary core should be placed into a loop, then a debugger can be attached
(see [AN13264](https://www.nxp.com/docs/en/application-note/AN13264.pdf), section 4.2.3 for more information)

### Launching Images Targeting M4 Core

If building targeting the M4 core, the M7 core must first run code to launch
the M4 image, by copying it into the `ocram` region then kicking off the M4
core. When building using sysbuild targeting the M4 core, a minimal “launcher”
image will be built and flashed to the M7 core, which loads and kicks off
the M4 core. Therefore when developing an application intended to run
standalone on the M4 core, it is recommended to build with sysbuild, like
so:

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm4 --sysbuild samples/hello_world
west flash
```

If desired, this behavior can be disabled by building with
`-DSB_CONFIG_SECOND_CORE_MCUX_LAUNCHER=n`

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. The on-board
debugger listed below works with the LinkServer runner by default, or can be
reprogrammed with JLink firmware.

- MIMXRT1170-EVKB: [MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe)
- MIMXRT1170-EVK: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe)

#### Using LinkServer

Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
search path. LinkServer works with the default CMSIS-DAP firmware included in
the on-board debugger.

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK. See [Using J-Link with MIMXRT1170-EVKB](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1170-EVKB/ta-p/1715138) or
[Using J-Link with MIMXRT1160-EVK or MIMXRT1170-EVK](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1160-EVK-or-MIMXRT1170-EVK/ta-p/1529760) for more details.

Use the `-r jlink` option with West to use the jlink runner.

```shell
west flash -r jlink
```

Alternatively, pyOCD can be used to flash and debug the board by using the
`-r pyocd` option with West. pyOCD is installed when you complete the
[Get Zephyr and install Python dependencies](../../../../develop/getting_started/index.md#gs-python-deps) step in the Getting Started Guide. The runners supported
by NXP are LinkServer and JLink. pyOCD is another potential option, but NXP
does not test or support the pyOCD runner.

### Configuring a Console

We will use the on-board debugger
microcontroller as a usb-to-serial adapter for the serial console. The following
jumper settings are default on these boards, and are required to connect the
UART signals to the USB bridge circuit:

- MIMXRT1170-EVKB: JP2 open (default)
- MIMXRT1170-EVK: J31 and J32 shorted (default)

Connect a USB cable from your PC to the on-board debugger USB port:

- MIMXRT1170-EVKB: J86
- MIMXRT1170-EVK: J11

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Before powering the board, make sure SW1 is set to 0001b

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 samples/hello_world
west flash
```

Power off the board, and change SW1 to 0010b. Then power on the board and
open a serial terminal, reset the board (press the SW4 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1170_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1170_evk
```

### ENET1G Driver

Current default of ethernet driver is to use 100M Ethernet instance ENET.
To use the 1G Ethernet instance ENET1G, include the overlay to west build with
the option `-DEXTRA_DTC_OVERLAY_FILE=nxp,enet1g.overlay` instead.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
