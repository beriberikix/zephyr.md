---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/sensortile_box/doc/index.html
original_path: boards/st/sensortile_box/doc/index.html
---

# SensorTile.box

Board Overview

[![../../../../_images/sensortile_box.jpg](../../../../_images/sensortile_box.jpg)
](../../../../_images/sensortile_box.jpg)

SensorTile.box

Name:
:   `sensortile_box`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l4r9xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/sensortile_box/doc/index.rst/../..)

## Overview

The STEVAL-MKSBOX1V1 (SensorTile.box) is a ready-to-use box kit for wireless
IoT and wearable sensor platforms to help you use and develop apps based on
remote motion and environmental sensor data.
The SensorTile.box board fits into a small plastic box with a long-life rechargeable
battery, and communicates with a standard smartphone through its Bluetooth interface,
providing data coming from the sensors.

More information about the board can be found at the [SensorTile.box website](https://www.st.com/en/evaluation-tools/steval-mksbox1v1.html) [[1]](#id2).

## Hardware

SensorTile.box provides the following hardware components:

- Ultra low-power STM32L4R9ZI System on Chip

  - LQFP144 package
  - Core: ARM® 32-bit Cortex®-M4 CPU with FPU, adaptive
    real-time accelerator (ART Accelerator) allowing 0-wait-state
    execution from Flash memory, frequency up to 120 MHz, MPU, 150
    DMIPS/1.25 DMIPS/MHz (Dhrystone 2.1), and DSP instructions
  - Clock Sources:

    - 16 MHz crystal oscillator
    - 32 kHz crystal oscillator for RTC (LSE)
- Communication

  - Bluetooth Smart connectivity v4.2 (SPBTLE-1S)
  - 1 x USB OTG FS (SoC) with micro-B connector
    (USB device role only)
- Internal Buses

  - 3 x SPI bus
  - 3 x I2C bus
- micro-SD connector
- On board sensors:

  - Digital temperature sensor (STTS751)
  - 6-axis inertial measurement unit (LSM6DSOX)
  - 3-axis accelerometers (LIS2DW12 and LIS3DHH)
  - 3-axis magnetometer (LIS2MDL)
  - Altimeter / pressure sensor (LPS22HH)
  - Microphone / audio sensor (MP23ABS1)
  - Humidity sensor (HTS221)
- HCP602535ZC LI-ion rechargeable battery (3.7V 500mAh)
- FTSH107 connector for SWD debugging and UART Tx/Rx

### Supported Features

The SensorTile.box provides motion, environmental, and audio
sensor data through either the BLE or USB protocols to a host application running
on a smartphone/PC to implement applications such as:

- Pedometer optimized for belt positioning
- Baby crying detection with Cloud AI learning
- Barometer / environmental monitoring
- Vehicle / goods tracking
- Vibration monitoring
- Compass and inclinometer
- Sensor data logger

The `sensortile_box` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sensortile_box/stm32l4r9xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L397) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V2 compatible with BlueNRG-1 and successor devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L175) | [`st,hci-spi-v2`](../../../../build/dts/api/bindings/bluetooth/st%2Chci-spi-v2.md#std-dtcompatible-st-hci-spi-v2) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L295) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L136) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L95)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L102) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L110) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L320) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L372) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4r9.dtsi?plain=1#L15) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L429) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L326) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L168) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L242)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L124) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L147) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4r5.dtsi?plain=1#L29) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L350) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L215) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L380) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L409) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L162) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L483) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L297) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L471) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L386) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics HTS221 humidity and temperature sensor on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L111) | [`st,hts221`](../../../../build/dts/api/compatibles/st%2Chts221.md#std-dtcompatible-st-hts221) |
| on-board | STMicroelectronics LPS22HH pressure and temperature sensor connected to I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L117) | [`st,lps22hh`](../../../../build/dts/api/compatibles/st%2Clps22hh.md#std-dtcompatible-st-lps22hh) |
| on-board | STMicroelectronics STTS751 temperature sensor connected to I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L130) | [`st,stts751`](../../../../build/dts/api/bindings/sensor/st%2Cstts751-i2c.md#std-dtcompatible-st-stts751) |
| on-board | STMicroelectronics LIS2DW12 3-axis accelerometer accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L146) | [`st,lis2dw12`](../../../../build/dts/api/compatibles/st%2Clis2dw12.md#std-dtcompatible-st-lis2dw12) |
| on-board | STMicroelectronics LSM6DSO 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L153) | [`st,lsm6dso`](../../../../build/dts/api/compatibles/st%2Clsm6dso.md#std-dtcompatible-st-lsm6dso) |
| on-board | STMicroelectronics IIS3DHHC 3-axis accelerometer accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L161) | [`st,iis3dhhc`](../../../../build/dts/api/bindings/sensor/st%2Ciis3dhhc-spi.md#std-dtcompatible-st-iis3dhhc) |
| on-board | STMicroelectronics LIS2MDL magnetometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box/sensortile_box.dts?plain=1#L195) | [`st,lis2mdl`](../../../../build/dts/api/compatibles/st%2Clis2mdl.md#std-dtcompatible-st-lis2mdl) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L517) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L528) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L536) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L215)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L97) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L233) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L106) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L543) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L276) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L287) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L449) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L304) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L338) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st%2Cstm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L201) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L207) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

#### LED

- Blue LED = PB15
- Green LED = PF2

#### Push buttons

- BUTTON = BOOT
  (used to let the SensorTile.box enter DFU mode. See [Programming and Debugging](#programming-and-debugging)
  section)
- BUTTON = PWR
  (used to Power on/off the board when battery is connected)

### System Clock

SensorTile.box System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default, the System clock is
driven by the PLL clock at 80MHz, driven by the 16MHz external oscillator.
The system clock can be boosted to 120MHz.
The internal AHB/APB1/APB2 AMBA buses are all clocked at 80MHz.

### Serial Port

There are two possible options for Zephyr console output:

- using USART1 which is available on FTSH107 connector. In this case a JTAG adapter
  can be used to connect SensorTile.box to STLINK-V2 and have both SWD and console lines
  available on PC.
- using the USB connector, which may be used to make the console available on PC as
  USB CDC class.

Console default settings are 115200 8N1.

### USB interface

SensorTile.box can be connected as a USB device to a PC host through its micro-B connector.
The final application may use it to declare SensorTile.box device as belonging to a
certain standard or vendor class, e.g. a CDC, a mass storage or a composite device with both
functions.

## Programming and Debugging

The `sensortile_box` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **dfu-util** | ✅ (default) |  |

There are 2 main entry points for flashing STM32FL4Rx SoCs, one using the ROM
bootloader, and another by using the SWD debug port (which requires additional
hardware) on FTSH107 connector.
Flash using the ROM bootloader by powering on the board
while keeping the BOOT0 button pressed.
The ROM bootloader supports flashing via USB (DFU), UART, I2C and SPI.
You can read more about how to enable and use the ROM bootloader by checking
the application note [AN2606](https://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf) [[2]](#id4) (STM32L4Rx section).

### Flashing

#### Installing dfu-util

It is recommended to use at least v0.8 of dfu-util. The package available in
Debian and Ubuntu can be quite old, so you might have to build dfu-util from source.
Information about how to get the source code and how to build it can be found
at the [DFU-UTIL website](http://dfu-util.sourceforge.net/) [[3]](#id6)

#### Flashing an Application to SensorTile.box

While pressing the BOOT0 button, connect the
micro-USB cable to the USB OTG SensorTile.box
port and to your computer. The board should be
forced to enter DFU mode.

Confirm that the board is in DFU mode:

```shell
$ sudo dfu-util -l
dfu-util 0.9

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2019 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=2, name="@OTP Memory /0x1FFF7000/01*0001Ke", serial="204A325D574D"
Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=1, name="@Option Bytes  /0x1FF00000/01*040 e/0x1FF01000/01*040 e", serial="204A325D574D"
Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=0, name="@Internal Flash  /0x08000000/512*0004Kg", serial="204A325D574D"
```

You should see following confirmation on your Linux host:

```shell
$ dmesg
usb 2-2: new full-speed USB device number 74 using xhci_hcd
usb 2-2: New USB device found, idVendor=0483, idProduct=df11
usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 2-2: Product: STM32  BOOTLOADER
usb 2-2: Manufacturer: STMicroelectronics
usb 2-2: SerialNumber: 204A325D574D
```

You can build and flash the provided sample application
([SensorTile.box sensors](../../../../samples/boards/st/sensortile_box/README.md#sensortile_box_sensors "Read sensor data from the various SensorTile.box sensors.")) that reads sensors data and outputs
values on the console.

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/steval-mksbox1v1.html](https://www.st.com/en/evaluation-tools/steval-mksbox1v1.html)

[[2](#id5)]

[https://www.st.com/content/ccc/resource/technical/document/application\_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf](https://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf)

[[3](#id7)]

[http://dfu-util.sourceforge.net/](http://dfu-util.sourceforge.net/)
