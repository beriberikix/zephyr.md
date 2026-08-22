---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/eval_adin1110ebz/doc/index.html
original_path: boards/adi/eval_adin1110ebz/doc/index.html
---

# EVAL-ADIN1110EVB Evaluation board

Board Overview

[![../../../../_images/adi_eval_adin1110ebz.webp](../../../../_images/adi_eval_adin1110ebz.webp)
](../../../../_images/adi_eval_adin1110ebz.webp)

EVAL-ADIN1110EVB Evaluation board

Name:
:   `adi_eval_adin1110ebz`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   stm32l4s5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/eval_adin1110ebz/doc/index.rst/../..)

## Overview

The EVAL-ADIN1110EBZ is a flexible platform enabling quick evaluation of the ADIN1110, robust,
low power 10BASE-T1L MAC-PHY. It provides 10Mbit per second Single Pair Ethernet (SPE) connections
with devices across 1.7km of cable.

The evaluation board offers two modes of operation for maximum flexibility. Connected to a PC
via USB port, the full set of ADIN1110 register settings and features such as link quality
monitoring and diagnostics can be accessed over the USB using serial command interface.
The board also provides an Arduino interface.

Alternatively, the board can operate in stand-alone mode where it is configured by setting hardware
configuration links and switches. On-board LEDs provide status indication.

The SPI interface provides configuration and data access to the ADIN1110.

A small prototyping area and test points are provided for experimentation with alternative cable
connection topologies including isolation transformers and/or power coupling inductors.

Important

S201 DIP switches are shipped in Open Alliance SPI mode. The current Zephyr
default board configuration is set to work as “Generic SPI, CRC enabled”,
so the S201 DIP switches must be set as `SPI_CFG0 OFF` and `SPI_CFG1 ON`.
An inconsistent S201 DIP switches configuration will halt the boot.

## Hardware

The ADI EVAL-ADIN1110EBZ hardware features list is available here:

[https://wiki.analog.com/resources/eval/user-guides/eval-adin1110ebz-user-guide](https://wiki.analog.com/resources/eval/user-guides/eval-adin1110ebz-user-guide)

### Supported Features

The `adi_eval_adin1110ebz` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `adi_eval_adin1110ebz/stm32l4s5xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L397) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L295) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L136) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L102) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L110) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L320) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32L4 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4s5.dtsi?plain=1#L13) | [`st,stm32l4-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32l4-aes.md#std-dtcompatible-st-stm32l4-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L372) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L429)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L439) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L326) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Ethernet | on-board | ADIN1110 standalone 10BASE-T1L Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L207) | [`adi,adin1110`](../../../../build/dts/api/bindings/ethernet/phy/adi%2Cadin1110.md#std-dtcompatible-adi-adin1110) |
| on-board | ADIN2111 PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L225) | [`adi,adin2111-phy`](../../../../build/dts/api/bindings/ethernet/phy/adi%2Cadin2111-phy.md#std-dtcompatible-adi-adin2111-phy) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 OSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L272) | [`st,stm32-ospi-nor`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L168) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L242)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L124) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L147) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-board | ADIN2111 MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L220) | [`adi,adin2111-mdio`](../../../../build/dts/api/bindings/mdio/adi%2Cadin2111-mdio.md#std-dtcompatible-adi-adin2111-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4r5.dtsi?plain=1#L29) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-board | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L61) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-board | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L66) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L350) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L106) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L380)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L394) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L409) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L162) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L483) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L314)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L297) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L471) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L386) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | ADT7420 16-Bit digital I2C temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin1110ebz/adi_eval_adin1110ebz.dts?plain=1#L184) | [`adi,adt7420`](../../../../build/dts/api/bindings/sensor/adi%2Cadt7420.md#std-dtcompatible-adi-adt7420) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L517) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L528) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L536) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L215)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L224) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L233) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L106) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L543) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L148)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L276) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L304)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L287) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L449) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L304) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L338) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st%2Cstm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L201) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L207) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

ADI ADIN1110EBZ evaluation board has 7 GPIO controllers (from A to G). These controllers are
responsible for pin muxing, input/output, pull-up, etc.

For mode details please refer to [EVAL-ADIN1110EBZ User Guide](https://wiki.analog.com/resources/eval/user-guides/eval-adin1110ebz-user-guide).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10 (UART to FT232)
- UART\_4 TX/RX : PA0/PA1 (Arduino Serial)
- I2C1 SCL/SDA : PG14/PG13 (Arduino I2C)
- I2C3 SCL/SDA : PG7/PG8 (Sensor I2C bus)
- SPI1 SCK/MISO/MOSI : PA5/PA6/PA7 (Simple SPI to nor Flash)
- SPI2 SCK/MISO/MOSI : PB13/PB14/PB15 (ADIN1110)
- SPI3 SCK/MISO/MOSI : PC10/PC11/PC12 (Arduino SPI)
- LD1 : PC13 (Green LED)
- LD2 : PE2 (Red LED)
- LD3 : PE6 (Yellow LED)
- LD4 : PG15 (Blue LED)
- PSRAMPE0/PE1/PF0-PF15/PG0-PG5/PD11-PD13/PE3/PE4
  :   PD14/PD15/PD9/PD1/PE7-PE15/PD8-PD10

#### System Clock

EVAL-ADIN1110EBZ System Clock could be driven by an internal or external oscillator, as well as
the main PLL clock. By default the System clock is driven by the PLL clock at 80MHz, driven by the
16MHz high speed internal oscillator.

#### Serial Port

EVAL-ADIN1110EBZ has 2 U(S)ARTs. The Zephyr console output is assigned to UART1 that is connected
to a FT232, so available through Micro USB connector. Default settings are 115200 8N1.

## Programming and Debugging

The `adi_eval_adin1110ebz` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

EVAL-ADIN1110EBZ includes an ST-LINK/V2-1 JTAG/SWD 10 or 20 pin connector. This interface is
supported by the openocd version included in Zephyr SDK.

#### Flashing an application to Discovery kit

Connect the EVAL-ADIN1110EBZ to your host computer using the USB port, then run a serial host
program to connect with your ADI board. For example:

```shell
$ minicom -D /dev/serial/by-id/usb-ADI_EVAL-ADIN1110EBZ_AVAS_XXXXXX-if00-port0
```

where XXXXXX is the serial number of the connected device.
Then, build and flash in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b adi_eval_adin1110ebz samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! adi_eval_adin1110ebz
```

### Debugging

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b adi_eval_adin1110ebz samples/hello_world
west debug
```
