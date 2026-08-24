---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/witte/linum/doc/index.html
original_path: boards/witte/linum/doc/index.html
---

# Linum Board

Board Overview

[![../../../../_images/linum-stm32h753bi-top.jpg](https://docs.zephyrproject.org/4.1.0/_images/linum-stm32h753bi-top.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/linum-stm32h753bi-top.jpg)

Linum Board

Name:
:   `linum`

Vendor:
:   Witte Technology

Architecture:
:   arm

SoC:
:   stm32h753xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/witte/linum/doc/index.rst/../..)

## Overview

Linum is a development board released by Witte Tenology in 2023, and it was developed around the
STM32H753BI microcontroller. The board has 2 expansion connectors used by the LCD display with
touchscreen and another for access to other peripherals of microcontroller. Also it brings plenty
of communications interfaces like UART with RS232 and RS485 capabillities, CAN bus compatible to
FD standard, and networking over Ethernet.

## Hardware

The board features:
:   - 8 to 52V power supply
    - SWD Pins for use as STLink (Pin header) and TC2030-IDC 6-Pin Tag-Connect Plug-of-Nails™ Connector
    - Crystal for HS 25MHz
    - Crystal for RTC 32.768KHz
    - 1 UART serial for debug
    - 1 Led RGB
    - 1 Buzzer without internal oscillator
    - 1 Mono audio up to 3W
    - 1 Ethernet 10/100
    - 1 MicroSD connector supporting 1 or 4-bit bus
    - 1 USB 2.0 Host/Device
    - 1 EEPROM memory with 512K bits
    - 1 External SRAM memory with 8MB
    - 1 NOR memory with 16MB
    - 2 On-board RS232 Transceiver with RTS/CTS
    - 2 On-board RS485 Transceiver
    - 2 On-board CAN-FD Transceiver

Expansion connector 1 features:
:   - 1 Display RBG 888
    - 1 Capacitive Touchscreen sensor

Expansion connector 2 features.
:   - 1 SPI
    - 1 I2C
    - 1 One Wire
    - 2 DACs
    - 6 PWM Channels
    - 10 ADCs

More information about the board, can be found at the [Witte Linum website](https://wittetech.com/).

### Supported Features

The `linum` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `linum/stm32h753xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L35) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L852)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L869) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32H7 series FDCAN CAN FD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L526) | [`st,stm32h7-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) |
| Clock control | on-chip | STM32H7 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L153) | [`st,stm32h7-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-rcc.md#std-dtcompatible-st-stm32h7-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L66) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L74)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L81) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L88) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7 main PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L103)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L117) | [`st,stm32h7-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-pll-clock.md#std-dtcompatible-st-stm32h7-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L124) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L132) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L581) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L921) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L46) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L929) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| on-chip | STM32 BDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L955) | [`st,stm32-bdma`](../../../../build/dts/api/bindings/dma/st%2Cstm32-bdma.md#std-dtcompatible-st-stm32-bdma) |
| on-chip | STM32 DMAMUX controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L968) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Ethernet | on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1028) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L248) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/microchip%2Cksz8081.md#std-dtcompatible-microchip-ksz8081) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L144) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L397)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L373) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L484) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st%2Cstm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L164) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1038) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st%2Cstm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L57) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-chip | STM32H7 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1046) | [`st,stm32h7-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32h7-fmc.md#std-dtcompatible-st-stm32h7-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1052) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1008)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1018) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L42) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L15) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L355) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L111) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L712)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L558) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1068) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st%2Cstm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L158) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1000) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L362) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1088) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1100) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1106) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L288) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L312)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L320) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L353) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1114) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L421)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L432) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L66) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L702)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L548) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L834) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h743.dtsi?plain=1#L32) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1078) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st%2Cstm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L274) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L280) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

#### Default Zephyr Peripheral Mapping:

#### BOARD-LEDs

The LINUM-STM32H753BI has 3 software controllable LEDs.

> | LED RGB | PINS |
> | --- | --- |
> | LED\_R | PG2 |
> | LED\_G | PG3 |
> | LED\_B | PB2 |

#### UART/USART

The LINUM-STM32H753BI used the USART1 for serial console.

#### USART1

> | USART1 | PINS |
> | --- | --- |
> | TX | PB14 |
> | RX | PB15 |

The LINUM-STM32H753BI board has two on-board RS-232 transceiver connected to USART2 and USART3.

> | USART2 | PINS |
> | --- | --- |
> | TXD | PD5 |
> | RXD | PD6 |
> | CTS | PD3 |
> | RTS | PD4 |
>
> | USART3 | PINS |
> | --- | --- |
> | TXD | PB10 |
> | RXD | PB11 |
> | CTS | PD11 |
> | RTS | PD12 |

The LINUM-STM32H753BI board has two on-board RS-485 transceiver connected to USART4 and USART6.

> | UART4 | PINS |
> | --- | --- |
> | TXD | PB9 |
> | RXD | PB8 |
> | DE | PA15 |
>
> | USART6 | PINS |
> | --- | --- |
> | TXD | PC6 |
> | RXD | PC7 |
> | DE | PG12 |

#### SDMMC

The LINUM-STM32H753BI has one SDCard slot connected as below:

> | SDMMC1 | PINS |
> | --- | --- |
> | SDMMC\_D0 | PC8 |
> | SDMMC\_D1 | PC9 |
> | SDMMC\_D2 | PC10 |
> | SDMMC\_D3 | PC11 |
> | SDMMC\_DK | PC12 |
>
> | GPIO | PINS |
> | --- | --- |
> | SDCARD\_DETECTED | PG7 |
> | SDCARD\_PWR\_EN | PD7 |

#### ETHERNET

The LINUM-STM32H753BI has a ethernet connection using the transceiver KSZ8081RNACA.

> | ETH | PINS |
> | --- | --- |
> | ETH\_REF\_CLK | PA1 |
> | ETH\_MDIO | PA2 |
> | ETH\_CRS\_DV | PA7 |
> | ETH\_MDC | PC1 |
> | ETH\_RXD0 | PC4 |
> | ETH\_RXD1 | PC5 |
> | ETH\_TX\_EN | PG11 |
> | ETH\_TXD0 | PG13 |
> | ETH\_TXD1 | PG14 |
> | ETH\_CLK | PA8 |
> | ETH\_RESET | PI4 |

#### CAN-FD

The LINUM-STM32H753BI board has two on-board CAN-FD transceiver connected to FDCAN1 and FDCAN2.

> | FDCAN1 | PINS |
> | --- | --- |
> | TXD | PH13 |
> | RXD | PH14 |
> | STD | PI2 |
>
> | FDCAN2 | PINS |
> | --- | --- |
> | TXD | PB13 |
> | RXD | PB12 |
> | STD | PE3 |

#### USB

The LINUM-STM32H753BI has one usb port.

> | USB | PINS |
> | --- | --- |
> | USB\_VBUS | PA9 |
> | USB\_N | PA11 |
> | USB\_P | PA12 |
> | USB\_EN | PI12 |
> | USB\_FLT | PI13 |

#### I2C3

The LINUM-STM32H753BI connects the EEPROM memory and the touchscreen sensor to I2C3.

> | I2C3 | PINS |
> | --- | --- |
> | SCL | PH7 |
> | SDA | PH8 |

#### External SDRAM

The LINUM-STM32H753BI has a external SDRAM with 8Mbytes connected to FMC peripheral.

> | FMC | PINS |
> | --- | --- |
> | FMC\_A0 | PF0 |
> | FMC\_A1 | PF1 |
> | FMC\_A2 | PF2 |
> | FMC\_A3 | PF3 |
> | FMC\_A4 | PF4 |
> | FMC\_A5 | PF5 |
> | FMC\_A6 | PF12 |
> | FMC\_A7 | PF13 |
> | FMC\_A8 | PF14 |
> | FMC\_A9 | PF15 |
> | FMC\_A10 | PG0 |
> | FMC\_A11 | PG1 |
> | FMC\_BA0 | PG4 |
> | FMC\_BA1 | PG5 |
> | FMC\_D0 | PD14 |
> | FMC\_D1 | PD15 |
> | FMC\_D2 | PD0 |
> | FMC\_D3 | PD1 |
> | FMC\_D4 | PE7 |
> | FMC\_D5 | PE8 |
> | FMC\_D6 | PE9 |
> | FMC\_D7 | PE10 |
> | FMC\_D8 | PE11 |
> | FMC\_D9 | PE12 |
> | FMC\_D10 | PE13 |
> | FMC\_D11 | PE14 |
> | FMC\_D12 | PE15 |
> | FMC\_D13 | PD8 |
> | FMC\_D14 | PD9 |
> | FMC\_D15 | PD10 |
> | FMC\_NBL0 | PE0 |
> | FMC\_NBL1 | PE1 |
> | FMC\_SDCKE0 | PC3 |
> | FMC\_SDCLK | PG8 |
> | FMC\_SDNCAS | PG15 |
> | FMC\_SDNEO | PC2 |
> | FMC\_SDNRAS | PF11 |
> | FMC\_SDNWE | PC0 |

#### LCD

The LINUM-STM32H753BI use the LTDC to support one LCD with RGB connection.

> | LTDC | PINS |
> | --- | --- |
> | LTDC\_B0 | PJ12 |
> | LTDC\_B1 | PJ13 |
> | LTDC\_B2 | PJ14 |
> | LTDC\_B3 | PJ15 |
> | LTDC\_B4 | PK3 |
> | LTDC\_B5 | PK4 |
> | LTDC\_B6 | PK5 |
> | LTDC\_B7 | PK6 |
> | LTDC\_CLK | PI14 |
> | LTDC\_DE | PK7 |
> | LTDC\_G0 | PJ7 |
> | LTDC\_G1 | PJ8 |
> | LTDC\_G2 | PJ9 |
> | LTDC\_G3 | PJ10 |
> | LTDC\_G4 | PJ11 |
> | LTDC\_G5 | PK0 |
> | LTDC\_G6 | PK1 |
> | LTDC\_G7 | PK2 |
> | LTDC\_HSYNC | PI10 |
> | LTDC\_R0 | PI15 |
> | LTDC\_R1 | PJ0 |
> | LTDC\_R2 | PJ1 |
> | LTDC\_R3 | PJ2 |
> | LTDC\_R4 | PJ3 |
> | LTDC\_R5 | PJ4 |
> | LTDC\_R6 | PJ5 |
> | LTDC\_R7 | PJ6 |
> | LTDC\_VSYNC | PI9 |
> | PWM\_BACKLIGHT | PH6 |

#### System Clock

Linum H753ZI System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 480MHz, driven by an 25MHz high-speed external clock.

## Programming and Debugging

Applications for the `linum` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Note

For debugging or programming Linum you will need to use an external debug
debug or flash tool and connect it to the SWD Connnector. JLink or ST-Link
probes are examples of out of the box compatible tools.

### Flashing

#### Flashing an application to the Linum board

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b linum samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! linum
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b linum samples/hello_world
west debug
```
