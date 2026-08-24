---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt1010_evk/doc/index.html
original_path: boards/nxp/mimxrt1010_evk/doc/index.html
---

# MIMXRT1010-EVK

Board Overview

[![../../../../_images/mimxrt1010_evk.jpg](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1010_evk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt1010_evk.jpg)

MIMXRT1010-EVK

Name:
:   `mimxrt1010_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1011

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1010_evk/doc/index.rst/../..)

## Overview

The i.MX RT1010 offer a new entry-point into the i.MX RT crossover processor
series by providing the lowest-cost LQFP package option, combined with the
high performance and ease-of-use known throughout the entire i.MX RT series.
This device is fully supported by NXP’s MCUXpresso Software and Tools.

## Hardware

- MIMXRT1011DAE5A MCU
- Memory

  - 128 Mbit QSPI Flash
- Connectivity

  - Micro USB host and OTG connectors
  - Arduino interface
- Audio

  - Audio Codec
  - 4-pole audio headphone jack
  - External speaker connection
  - Microphone
- Debug

  - JTAG 10-pin connector
  - OpenSDA with DAPLink

For more information about the MIMXRT1010 SoC and MIMXRT1010-EVK board, see
these references:

- [i.MX RT1010 Website](https://www.nxp.com/imxrt1010)
- [i.MX RT1010 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1010CEC.pdf)
- [i.MX RT1010 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1010RM)
- [MIMXRT1010-EVK Website](https://www.nxp.com/MIMXRT1010-EVK)
- [MIMXRT1010-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1010EVKHUG)
- [MIMXRT1010-EVK Design Files](https://www.nxp.com/webapp/Download?colCode=IMXRT1010-EVK-DESIGN-FILES)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| AT25SF128A | FLEXSPI | Enabled via flash configuration block, which sets up FLEXSPI at boot time. |

### Supported Features

The `mimxrt1010_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt1010_evk/mimxrt1011` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L29) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | NXP MCUA 12B1MSPS SAR ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L586)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L596) | [`nxp,mcux-12b1msps-sar`](../../../../build/dts/api/bindings/adc/nxp,mcux-12b1msps-sar.md#std-dtcompatible-nxp-mcux-12b1msps-sar) |
| ARM architecture | on-chip | MCUX XBAR (Crossbar)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1116) | [`nxp,mcux-xbar`](../../../../build/dts/api/bindings/arm/nxp,mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L279) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed factor clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L291) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | i.MX CCM Fractional PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L303) | [`nxp,imx-ccm-fnpll`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll) |
| on-chip | i.MX ANATOP (Analog Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L973) | [`nxp,imx-anatop`](../../../../build/dts/api/bindings/clock/nxp,imx-anatop.md#std-dtcompatible-nxp-imx-anatop) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1148) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1158) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Cryptographic accelerator | on-chip | NXP Data Co-Processor (DCP) Crypto accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1135) | [`nxp,mcux-dcp`](../../../../build/dts/api/bindings/crypto/nxp,mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L43) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L910) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| on-chip | NXP PXP 2D DMA engine[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L986) | [`nxp,pxp`](../../../../build/dts/api/bindings/dma/nxp,pxp.md#std-dtcompatible-nxp-pxp) |
| GPIO & Headers | on-chip | i.MX GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L325) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L53) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L122)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L133) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L278) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | NXP FlexRAM on-chip RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L92) | [`nxp,flexram`](../../../../build/dts/api/bindings/memory-controllers/nxp,flexram.md#std-dtcompatible-nxp-flexram) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1183) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L38) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L94) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L104) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L440) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX RT SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L444) | [`nxp,mcux-rt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl) |
| on-chip | i.MX IOMUXC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L980) | [`nxp,imx-gpr`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-gpr.md#std-dtcompatible-nxp-imx-gpr) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L192) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L197) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L822) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP SNVS LP/HP RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L319) | [`nxp,imx-snvs-rtc`](../../../../build/dts/api/bindings/rtc/nxp,imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc) |
| Sensors | on-chip | NXP MCUX QDEC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1088) | [`nxp,mcux-qdec`](../../../../build/dts/api/bindings/sensor/nxp,mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec) |
| on-chip | NXP on-die temperature monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L1142) | [`nxp,tempmon`](../../../../build/dts/api/bindings/sensor/nxp,tempmon.md#std-dtcompatible-nxp-tempmon) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L506)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L516) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L103) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L154)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L166) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP MCUX General-Purpose HW Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L156) | [`nxp,gpt-hw-timer`](../../../../build/dts/api/bindings/timer/nxp,gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer) |
| on-chip | NXP MCUX General-Purpose Timer (GPT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L163) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| USB | on-chip | NXP EHCI USB host controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L849) | [`nxp,uhc-ehci`](../../../../build/dts/api/bindings/usb/nxp,uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci) |
| on-chip | NXP USB High Speed PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L867) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt1010.dtsi?plain=1#L247) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| Watchdog | on-chip | imxRT watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt10xx.dtsi?plain=1#L959) | [`nxp,imx-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,imx-wdog.md#std-dtcompatible-nxp-imx-wdog) |

Note

For additional features not yet supported, please also refer to the
[MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064_evk), which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1010\_evk board:

### Connections and I/Os

The MIMXRT1010 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_11 | GPIO | LED |
| GPIO\_SD\_05 | GPIO | SW4 |
| GPIO\_10 | LPUART1\_TX | UART Console |
| GPIO\_09 | LPUART1\_RX | UART Console |
| GPIO\_01 | LPI2C1\_SDA | I2C SDA |
| GPIO\_02 | LPI2C1\_CLK | I2C SCL |
| GPIO\_AD\_03 | LPSPI1\_SDI | SPI |
| GPIO\_AD\_04 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_05 | LPSPI1\_PCS0 | SPI |
| GPIO\_AD\_06 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_01 | ADC | ADC1 Channel 1 |
| GPIO\_AD\_02 | ADC | ADC1 Channel 2 |

### System Clock

The MIMXRT1010 SoC is configured to use SysTick as the system clock source,
running at 500MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1010 SoC has four UARTs. `LPUART1` is configured for the console,
and the remaining are not used.

## Programming and Debugging

The `mimxrt1010_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in [Configuring a Debug Probe](#configuring-a-debug-probe) to
configure the board appropriately.

- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) (Default, Supported by NXP)
- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) (Supported by NXP)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details).

### Configuring a Debug Probe

For the RT1010, J61/J62 are the SWD isolation jumpers, J22 is the DFU
mode jumper, and J16 is the 10 pin JTAG/SWD header.

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
jumpers J31 and J32 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J41.

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
west build -b mimxrt1010_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
Hello World! mimxrt1010_evk
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
