---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32f769i_disco/doc/index.html
original_path: boards/st/stm32f769i_disco/doc/index.html
---

# STM32F769I Discovery

Board Overview

[![../../../../_images/stm32f769i_disco.jpg](https://docs.zephyrproject.org/4.2.0/_images/stm32f769i_disco.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/stm32f769i_disco.jpg)

STM32F769I Discovery

Name:
:   `stm32f769i_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f769xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f769i_disco/doc/index.rst/../..)

## Overview

The discovery kit enables a wide diversity of applications taking benefit
from audio, multi-sensor support, graphics, security, security, video,
and high-speed connectivity features. Important board features include:

- STM32F769NIH6 microcontroller featuring 2 Mbytes of Flash memory and 512 Kbytes of RAM, in BGA216 package
- On-board ST-LINK/V2-1 supporting USB reenumeration capability
- USB ST-LINK functions: virtual COM port, mass storage, debug port
- Five power supply options:

  - ST LINK/V2-1
  - USB HS connector
  - 5 V from RJ45 (Power Over Ethernet)
  - 5 V from Arduino™ or external connector
  - USB charger
- 4-inch capacitive touch LCD display with MIPI-DSI connector
- SAI audio codec
- Two audio line jacks, one for input and one for output
- Stereo speaker outputs
- Four ST MEMS microphones on DFSDM inputs
- Two SPDIF RCA input and output connectors
- Two push-buttons (user and reset)
- 512-Mbit Quad-SPI Flash memory
- 128-Mbit SDRAM
- Connector for microSD card
- Wi-Fi or Ext-EEP daughterboard connector
- USB OTG HS with Micro-AB connector
- Ethernet connector compliant with IEEE-802.3-2002
- Power Over Ethernet based on IEEE 802.3af (Powered Device, 48 V to 5 V, 3 W)
- Power supply output for external applications: 3.3 V or 5 V
- Arduino Uno V3 connectors
- Comprehensive free software including a variety of examples, part of the STM32Cube package
- Supported by a wide choice of integrated development environments

More information about the board can be found at the [32F769I-DISCO website](https://www.st.com/en/evaluation-tools/32f769idiscovery.html).

## Hardware

The STM32F769I Discovery kit provides the following hardware components:

- STM32F769NIH6 in BGA216 package
- ARM® 32-bit Cortex® -M7 CPU with FPU
- 216 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 2 MB Flash
- 512 + 16 + 4 KB SRAM
- Flexible external memory controller with up to 32-bit data bus
- Dual mode Quad-SPI
- Chrom-ART Accelerator(DMA2D), graphical hardware accelerator enabling enhanced graphical user interface
- Hardware JPEG codec
- LCD-TFT controller supporting up to XGA resolution
- MIPI® DSI host controller supporting up to 720p 30Hz resolution
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- DMA Controller
- General Purpose Timers (15)
- Watchdog Timers (2)
- I2C (4)
- USART/UART (8)
- SPI (6)
- SAI (2)
- CAN (3)
- SDMMC (2)
- SPDIFRX interface
- HDMI-CEC
- MDIO slave interface
- USB 2.0 full-speed device/host/OTG controller with on-chip PHY
- USB 2.0 high-speed/full-speed device/host/OTG controller with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA: supports IEEE 1588v2 hardware, MII/RMII
- 8- to 14-bit camera interface up to 54 Mbyte/s
- True random number generator
- CRC calculation unit
- RTC: sub-second accuracy, hardware calendar
- 96-bit unique ID

More information about STM32F769NIH6 can be found here:

- [STM32F769NIH6 on www.st.com](https://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32-high-performance-mcus/stm32f7-series/stm32f7x9/stm32f769ni.html)
- [STM32F76xxx reference manual](https://www.st.com/resource/en/reference_manual/dm00224583.pdf)

### Supported Features

The `stm32f769i_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32f769i_disco/stm32f769xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L34) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32F4 ADC[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L752) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st,stm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L412) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L135) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L56) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L62) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L69) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F7 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L84) | [`st,stm32f7-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f7-pll-clock.md#std-dtcompatible-st-stm32f7-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L92) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L454) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L803) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f767.dtsi?plain=1#L15) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L811) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f765.dtsi?plain=1#L71) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | ST STM32 Ethernet MAC, a child node of the Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f765.dtsi?plain=1#L77) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L175) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L118) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 QSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L198) | [`st,stm32-qspi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L167) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L326)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L338) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L143) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech,ft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L60) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L146) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f765.dtsi?plain=1#L88) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L104) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L110) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L745) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f765.dtsi?plain=1#L96)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L839) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L41) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L205) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L894) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| on-board | This binding is to be used by all the usb transceivers which are an external ULPI phy[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f769i_disco/stm32f769i_disco.dts?plain=1#L36) | [`usb-ulpi-phy`](../../../../build/dts/api/bindings/phy/usb-ulpi-phy.md#std-dtcompatible-usb-ulpi-phy) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L161) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L431) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L857) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L140) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L830) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L735) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L868) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L879) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L887) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L254)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L263) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L281) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L904) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L372)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L362) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L421) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L707) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L721) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L240) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L246) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

STM32F769I Discovery kit has 9 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [32F769I-DISCO board User Manual](https://www.st.com/resource/en/user_manual/dm00276557.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10 (ST-Link Virtual Port Com)
- UART\_6 TX/RX : PC6/PC7 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C4 SCL/SDA : PD12/PB7 (Touchscreen FT6202, PI13 Interrupt Pin)
- SPI2 SCK/MISO/MOSI : PA12/PB14/PB15 (Arduino SPI)
- ETH : PA1, PA2, PA7, PC1, PC4, PC5, PG11, PG13, PG14
- LD1 : PJ13
- LD2 : PJ5
- LD3 : PA12
- LD4 : PD4

### System Clock

The STM32F769I System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock is driven by the PLL
clock at 216MHz, driven by a 25MHz high speed external clock.

### Serial Port

The STM32F769I Discovery kit has up to 8 UARTs. The Zephyr console output is assigned to UART1
which connected to the onboard ST-LINK/V2 Virtual COM port interface. Default communication
settings are 115200 8N1.

## Programming and Debugging

The `stm32f769i_disco` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

STM32F769I Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f769i_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32F769I

First, connect the STM32F769I Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f769i_disco samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f769i_disco samples/hello_world
west debug
```
