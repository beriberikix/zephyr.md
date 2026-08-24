---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/weact/stm32h5_core/doc/index.html
original_path: boards/weact/stm32h5_core/doc/index.html
---

# STM32H5 Core Board

Board Overview

Name:
:   `weact_stm32h5_core`

Vendor:
:   WeAct Studio

Architecture:
:   arm

SoC:
:   stm32h562xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/weact/stm32h5_core/doc/index.rst/../..)

## Overview

The `weact_stm32h5_core` board is a compact development board equipped with
an STM32H562RGT6 microcontroller. It features basic set of peripherals:
user LED and button, microSD™ card slot, and combined SWD & UART header.

Key Features

- STM32 microcontroller in LQFP64 package
- USB OTG or full-speed device
- 1 user LED
- User, boot, and reset push-buttons
- 32.768 kHz and 8MHz HSE crystal oscillators
- Board connectors:

  > - microSD™ card
  > - USB Type-C Connector
  > - SWD & UART header for external debugger
  > - 2x 30-pin GPIO connector

More information about the board can be found on the [WeAct GitHub](https://github.com/WeActStudio/WeActStudio.STM32H5_64Pin_CoreBoard).

## Hardware

The `weact_stm32h5_core` board provides the following hardware components:

> - STM32H562RGT6 in LQFP64 package
> - ARM 32-bit Cortex-M33 CPU with FPU
> - CORDIC for trigonometric functions acceleration
> - FMAC (filter mathematical accelerator)
> - CRC calculation unit
> - 240 MHz max CPU frequency
> - VDD from 1.71 V to 3.6 V
> - 1MB Flash, 2 banks read-while-write
> - 640kB SRAM
> - 4 Kbytes of backup SRAM available in the lowest power modes
> - 2x watchdogs
> - 2x SysTick timer
> - 32-bit timers (2)
> - 16-bit advanced motor control timers (2)
> - 16-bit low power timers (6)
> - 16-bit timers (10)
> - 1x USB Type-C / USB power-delivery controller
> - 1x USB 2.0 full-speed host and device
> - 4x I2C FM+ interfaces (SMBus/PMBus)
> - 1x I3C interface
> - 12x U(S)ARTS (ISO7816 interface, LIN, IrDA, modem control)
> - 1x LP UART
> - 6x SPIs including 3 muxed with full-duplex I2S
> - 2x SAI
> - 1x FDCAN
> - Flexible external memory controller with up to 16-bit data bus: SRAM, PSRAM, FRAM, SDRAM/LPSDR SDRAM, NOR/NAND memories
> - 1x OCTOSPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
> - 1x SD/SDIO/MMC interfaces
> - 1x HDMI-CEC
> - 2x 12-bit ADC with up to 5 MSPS in 12-bit
> - 1x 12-bit D/A with 2 channels
> - 1x Digital temperature sensor

More information about STM32H562RG can be found here:

- [STM32H562RG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h562rg.html)
- [STM32H562 reference manual](https://www.st.com/resource/en/reference_manual/rm0481-stm32h52333xx-stm32h56263xx-and-stm32h573xx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `weact_stm32h5_core` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `weact_stm32h5_core/stm32h562xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L29) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L309) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L520)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L483) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st,stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L149) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st,stm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L54) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L60) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L90)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L82) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L97)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L103) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L111) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L368) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L474) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L301) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L559) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st,stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Ethernet | on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L541) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L123) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L188) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L437) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L583) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| I3C | on-chip | STM32H5 I3C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L461) | [`st,stm32-i3c`](../../../../build/dts/api/bindings/i3c/st,stm32-i3c.md#std-dtcompatible-st-stm32-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/weact/stm32h5_core/weact_stm32h5_core.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L161) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/weact/stm32h5_core/weact_stm32h5_core.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L551) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L505) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L495) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L131) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/weact/stm32h5_core/weact_stm32h5_core.dts?plain=1#L146) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L681) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L182) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L346) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L155) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L531) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L326) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Digital Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L644) | [`st,stm32-digi-temp`](../../../../build/dts/api/bindings/sensor/st,stm32-digi-temp.md#std-dtcompatible-st-stm32-digi-temp) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L654) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L666) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L674) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L251)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L260) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L278) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L126) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L686) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L487)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L498) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L93)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L229) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L337) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L631) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L287) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L293) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| xSPI | on-chip | STM32 XSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L261) | [`st,stm32-xspi`](../../../../build/dts/api/bindings/xspi/st,stm32-xspi.md#std-dtcompatible-st-stm32-xspi) |

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

The `weact_stm32h5_core` board is configured as follows

- USER\_LED : PB2
- USER\_PB : PC13
- SDMMC1 CLK/DCMD/CD/D0/D1/D2/D3 : PC12/PD2/PD4/PC8/PC9/PC10/PC11 (microSD card)
- USB DM/DP : PA11/PA12 (USB CDC ACM)
- UART on debug header : RX/TX - pA10/PA9

### System Clock

The STM32H562RG System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock is driven
by the PLL clock at 240MHz. PLL clock is fed by a 8MHz external clock.

### Serial Port (USB CDC ACM)

The Zephyr console output is assigned to the USB CDC ACM virtual serial port.
Virtual COM port interface. Default communication settings are 115200 8N1.

## Programming and Debugging

The `weact_stm32h5_core` board facilitates firmware flashing via the USB DFU
bootloader. This method simplifies the process of updating images, although
it doesn’t provide debugging capabilities. However, the board provides header
pins for the Serial Wire Debug (SWD) interface, which can be used to connect
an external debugger, such as ST-Link.

### Flashing

To activate the bootloader, follow these steps:

1. Press and hold the BOOT0 key.
2. While still holding the BOOT0 key, press and release the RESET key.
3. Wait for 0.5 seconds, then release the BOOT0 key.

Upon successful execution of these steps, the device will transition into
bootloader mode and present itself as a USB DFU Mode device. You can program
the device using the west tool or the STM32CubeProgrammer.

#### Flashing an application to `weact_stm32h5_core`

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, put the board in bootloader mode as described above. Then build and flash
the application in the usual way. Just add `CONFIG_BOOT_DELAY=5000` to the
configuration, so that USB CDC ACM is initialized before any text is printed,
as below:

```shell
# From the root of the zephyr repository
west build -b weact_stm32h5_core samples/hello_world -- -DCONFIG_BOOT_DELAY=5000
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D <tty_device> -b 115200
```

Then, press the RESET button, you should see the following message after few seconds:

```shell
Hello World! weact_stm32h5_core
```

Replace `<tty_device>` with the port where the board can be found.
For example, under Linux, `/dev/ttyACM0`.

#### Debugging

This current Zephyr port does not support debugging.

## Testing the LEDs in the `weact_stm32h5_core`

There is a sample that allows to test that LED on the board are working
properly with Zephyr:

```shell
# From the root of the zephyr repository
west build -b weact_stm32h5_core samples/basic/blinky -- -DCONFIG_BOOT_DELAY=5000
west flash
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The LED definitions can be found in
[boards/weact/stm32h5\_core/weact\_stm32h5\_core.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/weact/stm32h5_core/weact_stm32h5_core.dts).

## Testing shell over USB in the `weact_stm32h5_core`

There is a sample that allows to test shell interface over USB CDC ACM interface
with Zephyr:

```shell
# From the root of the zephyr repository
west build -b weact_stm32h5_core samples/subsys/shell/shell_module -- -DCONFIG_BOOT_DELAY=5000
west flash
```
