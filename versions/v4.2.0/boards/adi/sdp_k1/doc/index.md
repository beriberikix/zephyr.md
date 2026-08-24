---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/sdp_k1/doc/index.html
original_path: boards/adi/sdp_k1/doc/index.html
---

# SDP-K1

Board Overview

[![../../../../_images/adi_sdp_k1.webp](https://docs.zephyrproject.org/4.2.0/_images/adi_sdp_k1.webp)
](https://docs.zephyrproject.org/4.2.0/_images/adi_sdp_k1.webp)

SDP-K1

Name:
:   `adi_sdp_k1`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   stm32f469xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/sdp_k1/doc/index.rst/../..)

## Overview

The EVAL-SDP-CK1Z (SDP-K1) controller board is a system demonstration platform
(SDP) from Analog Devices designed to connect to evaluation shields containing
ADI components.

- STM32 microcontroller in BGA216 package
- USB 2.0 device with USB-C connector
- USB debug interface supporting CMSIS-DAP through a NXP Freescale
  microcontroller
- Flexible board power supply
  :   - USB VBUS 5 V max. 500 mA
      - 5.5mm DC power jack 7 - 12 V min. 300 mA
      - VIN from Arduino\* compatible connectors
      - VIN from 120-pin connector 5 V min. 300 mA
- 3 color LEDs (green, orange, red) and 1 status LED
- One push-buttons: RESET
- 16MB SDRAM
- Arduino UNO and 120-pin SDP connectors

More information about the board can be found on the [ADI SDP-K1 website](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html).

## Hardware

ADI SDP-K1 provides the following hardware components:

- STM32F469NIH6 in BGA216 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 180 MHz max CPU frequency
- VDD of 1.8 V or 3.3 V
- 2 MB Flash
- 384 KB SRAM
- GPIO with external interrupt capability
- LCD parallel interface, 8080/6800 modes
- LCD TFT controller supporting up to XGA resolution
- MIPI® DSI host controller supporting up to 720p 30Hz resolution
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer
- General Purpose Timers (17)
- Watchdog Timers (2)
- USART/UART (8)
- I2C (3)
- SPI (6)
- 1xSAI (serial audio interface)
- SDIO
- 2xCAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- 8- to 14-bit parallel camera
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F469NI can be found here:
:   - [STM32F469NI product page](https://www.st.com/en/microcontrollers/stm32f469ni.html)
    - [STM32F469 reference manual](https://www.st.com/resource/en/reference_manual/dm00127514.pdf)

### Supported Features

The `adi_sdp_k1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `adi_sdp_k1/stm32f469xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L34) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32F4 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L543) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st,stm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L244) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L208) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L127) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L62) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L82)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F4 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L89) | [`st,stm32f4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f4-pll-clock.md#std-dtcompatible-st-stm32f4-pll-clock) |
| on-chip | STM32F4 PLL I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L11) | [`st,stm32f4-plli2s-clock`](../../../../build/dts/api/bindings/clock/st,stm32f4-plli2s-clock.md#std-dtcompatible-st-stm32f4-plli2s-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L97) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L364) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L278) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f429.dtsi?plain=1#L22) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L560) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L13) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | ST STM32 Ethernet MAC, a child node of the Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L19) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L109) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L159) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on a Analog devices SDP interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/sdp_k1/arduino_r3_connector.dtsi?plain=1#L8) | [`adi,sdp-120`](../../../../build/dts/api/bindings/gpio/adi,sdp-120.md#std-dtcompatible-adi-sdp-120) |
| on-board | GPIO pins exposed on a Digilent Pmod interface[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/sdp_k1/adi_sdp_120pin_connector.dtsi?plain=1#L66) | [`digilent,pmod`](../../../../build/dts/api/bindings/gpio/digilent,pmod.md#std-dtcompatible-digilent-pmod) |
| I2C | on-chip | STM32 I2C V1 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L265) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| I2S | on-chip | STM32 I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L51) | [`st,stm32-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32-i2s.md#std-dtcompatible-st-stm32-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L138) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/sdp_k1/adi_sdp_k1.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L30) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L536) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f427.dtsi?plain=1#L89) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f427.dtsi?plain=1#L95) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L579) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32F4 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L117) | [`st,stm32f4-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32f4-nv-flash.md#std-dtcompatible-st-stm32f4-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L632) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| on-board | This binding is to be used by all the usb transceivers which are an external ULPI phy[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/sdp_k1/adi_sdp_k1.dts?plain=1#L45) | [`usb-ulpi-phy`](../../../../build/dts/api/bindings/phy/usb-ulpi-phy.md#std-dtcompatible-usb-ulpi-phy) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L153) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L590) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L335) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L132) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L228) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L526) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 quadrature decoder[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L341) | [`st,stm32-qdec`](../../../../build/dts/api/bindings/sensor/st,stm32-qdec.md#std-dtcompatible-st-stm32-qdec) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L606) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L617) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L625) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L238) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L64)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L55) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L637) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f427.dtsi?plain=1#L66)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L301) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st,stm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L325) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L311) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L194) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L224) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L230) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

For more details please refer to [EVAL-SDP-CK1Z User Guide](https://www.analog.com/media/en/technical-documentation/user-guides/EVAL-SDP-CK1Z-UG-1539.pdf).

#### Arduino UNO headers

![ADI SDP-K1 Arduino UNO headers pinout](https://docs.zephyrproject.org/4.2.0/_images/adi_sdp_k1_arduino.webp)

ADI SDP-K1 (Credit: Analog Devices, Inc.)

#### 120-pin SDP connector

![ADI SDP-K1 120-pin SDP connector pinout](https://docs.zephyrproject.org/4.2.0/_images/adi_sdp_k1_120pin.webp)

ADI SDP-K1 (Credit: Analog Devices, Inc.)

#### Default Zephyr Peripheral Mapping:

- UART\_5 TX/RX : P2 (DAPLink USB-C)
- UART\_5 TX/RX : P8 (DAPLink two position through hole)
- LED1 : DS6 (Red)
- LED2 : DS5 (Orange)
- LED3 : DS4 (Green)
- LED4 : DS4 (Status)

## Programming and Debugging

The `adi_sdp_k1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The ADI SDP-K1 be programmed over USB using the DAPLink firmware running on an
embedded NXP Freescale microcontroller or a 10-pin `DEBUG` header connected
to a STLINK debugger.

DAPLink exposes a storage device, as well as USB HID and CDC Endpoints, to the
host. For more details please refer to the [Official DAPLink website](https://daplink.io/).

### Flashing

#### Flashing an application with a STLINK debugger

First, connect the STLINK debugger to your host computer using the Micro-USB port.
Then attach the debugger to the 10-pin `DEBUG` header on the SDP-K1. Finally
connect the SDP-K1 to your host computer using the USB-C port.

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/serial/by-id/usb-ARM_DAPLink_CMSIS-DAP_<...>
```

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b adi_sdp_k1 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! adi_sdp_k1
```

### Debugging
