---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/sensortile_box_pro/doc/index.html
original_path: boards/st/sensortile_box_pro/doc/index.html
---

# SensorTile.box PRO

Board Overview

[![../../../../_images/sensortile_box_pro.jpg](https://docs.zephyrproject.org/4.2.0/_images/sensortile_box_pro.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sensortile_box_pro.jpg)

SensorTile.box PRO

Name:
:   `sensortile_box_pro`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u585xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/sensortile_box_pro/doc/index.rst/../..)

## Overview

The STEVAL-MKBOXPRO (SensorTile.box PRO) features an ARM Cortex-M33 based STM32U585AI MCU
and is a ready-to-use box kit for wireless IoT and wearable sensor platforms to help using
and developing apps based on remote motion and environmental sensor data.

The SensorTile.box PRO board fits into a small plastic box with a long-life rechargeable
battery, and communicates with a standard smartphone through its Bluetooth interface,
providing data coming from the sensors.

More information about the board can be found at the [SensorTile.box PRO website](https://www.st.com/en/evaluation-tools/steval-mkboxpro.html) [[1]](#id2).

## Supported Features

The SensorTile.box PRO provides motion, environmental, and audio
sensor data through either the BLE or USB protocols to a host application running
on a smartphone/PC to implement applications such as:

- Pedometer optimized for belt positioning
- Baby crying detection with Cloud AI learning
- Barometer / environmental monitoring
- Vehicle / goods tracking
- Vibration monitoring
- Compass and inclinometer
- Sensor data logger

(see [Motion and environmental sensors](#motion-and-environmental-sensors) section for the complete lists of available
sensors on board)

The `sensortile_box_pro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### `sensortile_box_pro/stm32u585xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L35) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L759) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V2 compatible with BlueNRG-1 and successor devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L161) | [`st,hci-spi-v2`](../../../../build/dts/api/bindings/bluetooth/st,hci-spi-v2.md#std-dtcompatible-st-hci-spi-v2) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L796) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st,stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L177) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st,stm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L83) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L96)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L89) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32U5 Multi Speed Internal Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L103)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L110) | [`st,stm32u5-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32u5-msi-clock.md#std-dtcompatible-st-stm32u5-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L117) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L132)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L138) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L152) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L558) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_crypt.dtsi?plain=1#L9) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L751) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L807) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st,stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L159) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L216) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L892) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L371)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L395) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32 SAI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L473) | [`st,stm32-sai`](../../../../build/dts/api/bindings/i2s/st,stm32-sai.md#std-dtcompatible-st-stm32-sai) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L47) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L189) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L44) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L50) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L741)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L34) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L43) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L167) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L335) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L696) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st,stm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_fs.dtsi?plain=1#L27) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L210) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L820) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L536)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L504) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L183) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L722) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L463) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics LSM6DSV16X 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L187) | [`st,lsm6dsv16x`](../../../../build/dts/api/compatibles/st,lsm6dsv16x.md#std-dtcompatible-st-lsm6dsv16x) |
| on-board | STMicroelectronics LIS2DU12 3-axis ultra-low power accelerometer sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L197) | [`st,lis2du12`](../../../../build/dts/api/compatibles/st,lis2du12.md#std-dtcompatible-st-lis2du12) |
| on-board | STMicroelectronics LPS22DF pressure and temperature sensor connected to I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L236) | [`st,lps22df`](../../../../build/dts/api/compatibles/st,lps22df.md#std-dtcompatible-st-lps22df) |
| on-board | STMicroelectronics LIS2MDL magnetometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L243) | [`st,lis2mdl`](../../../../build/dts/api/compatibles/st,lis2mdl.md#std-dtcompatible-st-lis2mdl) |
| on-board | STMicroelectronics STTS22H temperature sensor connected to I2C bus When setting the sampling-rate property in a .dts or .dtsi file you may include stts22h.h and use the macros defined there[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L250) | [`st,stts22h`](../../../../build/dts/api/bindings/sensor/st,stts22h-i2c.md#std-dtcompatible-st-stts22h) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L902) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L914)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L923) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L939)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L932) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L296)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L9) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L314)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L323) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L332) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L946) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L341)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L361) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L78) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L71) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st,stm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L419)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L430) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L527)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L495) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_fs.dtsi?plain=1#L12) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L273) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L279) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

## Hardware

The following is a summary of the main board features. More info can be find on [UM3133](https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf) [[2]](#id4)
and the [schematic](https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf) [[3]](#id6).

The STM32U585xx devices are an ultra-low-power microcontrollers family (STM32U5
Series) based on the high-performance Arm|reg| Cortex|reg|-M33 32-bit RISC core.
They operate at a frequency of up to 160 MHz.

- Ultra-low-power with FlexPowerControl (down to 300 nA Standby mode and 19.5 uA/MHz run mode)
- Core: ARM® 32-bit Cortex® -M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 1.5 DMPIS/MHz (Drystone 2.1)
  - 651 CoreMark® (4.07 CoreMark® /MHZ)
- Security and cryptography

  - Arm® TrustZone® and securable I/Os memories and peripherals
  - Flexible life cycle scheme with RDP (readout protection) and password protected debug
  - Root of trust thanks to unique boot entry and secure hide protection area (HDP)
  - Secure Firmware Installation thanks to embedded Root Secure Services
  - Secure data storage with hardware unique key (HUK)
  - Secure Firmware Update support with TF-M
  - 2 AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - Active tampers
  - True Random Number Generator NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte One-Time Programmable for user data
  - Active tampers
- Clock management:

  - 4 to 50 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - 2 internal multispeed 100 kHz to 48 MHz oscillators, including one auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 3 PLLs for system clock, USB, audio, ADC
  - Internal 48 MHz with clock recovery
- Power management

  - Embedded regulator (LDO)
  - Embedded SMPS step-down converter supporting switch on-the-fly and voltage scaling
- RTC with HW calendar and calibration
- Up to 136 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- Up to 17 timers and 2 watchdogs

  - 2x 16-bit advanced motor-control
  - 2x 32-bit and 5 x 16-bit general purpose
  - 4x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer
- ART accelerator

  - 8-Kbyte instruction cache allowing 0-wait-state execution from Flash and
    external memories: up to 160 MHz, MPU, 240 DMIPS and DSP
  - 4-Kbyte data cache for external memories
- Memories

  - 2-Mbyte Flash memory with ECC, 2 banks read-while-write, including 512 Kbytes with 100 kcycles
  - 786-Kbyte SRAM with ECC OFF or 722-Kbyte SRAM including up to 322-Kbyte SRAM with ECC ON
  - External memory interface supporting SRAM, PSRAM, NOR, NAND and FRAM memories
  - 2 Octo-SPI memory interfaces
- Rich analog peripherals (independent supply)

  - 14-bit ADC 2.5-Msps, resolution up to 16 bits with hardware oversampling
  - 12-bit ADC 2.5-Msps, with hardware oversampling, autonomous in Stop 2 mode
  - 12-bit DAC, low-power sample and hold
  - 2 operational amplifiers with built-in PGA
  - 2 ultra-low-power comparators
- Up to 22 communication interfaces

  - USB Type-C / USB power delivery controller
  - USB OTG 2.0 full-speed controller
  - 2x SAIs (serial audio interface)
  - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 6x USARTs (ISO 7816, LIN, IrDA, modem)
  - 3x SPIs (5x SPIs with dual OCTOSPI in SPI mode)
  - 1x FDCAN
  - 2x SDMMC interface
  - 16- and 4-channel DMA controllers, functional in Stop mode
  - 1 multi-function digital filter (6 filters)+ 1 audio digital filter with
    sound-activity detection
- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™
- True Random Number Generator (RNG)
- Graphic features

  - Chrom-ART Accelerator (DMA2D) for enhanced graphic content creation
  - 1 digital camera interface
- Mathematical co-processor

> - CORDIC for trigonometric functions acceleration
> - FMAC (filter mathematical accelerator)

More information about STM32U585AI can be found here:

- [STM32U585 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html) [[4]](#id8)
- [STM32U585 reference manual](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf) [[5]](#id10)

### Motion and environmental sensors

> - **LSM6DSV16X** 6-axis inertial measurement unit
>   ([lsm6dsv16x datasheet](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html) [[6]](#id12))
> - **LIS2MDL** 3-axis magnetometer
>   ([lis2mdl datasheet](https://www.st.com/en/mems-and-sensors/lis2mdl.html) [[7]](#id14))
> - **LPS22DF** Altimeter / pressure sensor
>   ([lps22df datasheet](https://www.st.com/en/mems-and-sensors/lps22df.html) [[8]](#id16))
> - **LIS2DU12** 3-axis accelerometer
>   ([lis2du12 datasheet](https://www.st.com/en/mems-and-sensors/lis2du12.html) [[9]](#id18))
> - **STTS22H** Digital temperature sensor
>   ([stts22hh datasheet](https://www.st.com/en/mems-and-sensors/stts22h.html) [[10]](#id20))
> - **MP23db01HP** Microphone / audio sensor
>   ([mp23db01hp datasheet](https://www.st.com/en/mems-and-sensors/mp23db01hp.html) [[11]](#id22))

### Connections and IOs

- 4x user LEDs

  - **led0** (Green)
  - **led1** (Red - shared with BLE)
  - **led2** (Yellow)
  - **led3** (Blue)
- 4x buttons/switch

  - **User BT1** button, available to user application
  - **User BT2** / **boot0** button, available to user application
    but useful to let the SensorTile.box PRO enter DFU mode
    if found pressed after h/w reset (see **rst** button and
    [Programming and Debugging](#programming-and-debugging) section)
  - **rst** button, used to reset the board (not available on case)
  - **power** switch, used to Power on/off the board

### System Clock

SensorTile.box PRO System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default, the System clock is
driven by the PLL clock at 80MHz, driven by the 16MHz external oscillator.
The system clock can be boosted to 120MHz.
The internal AHB/APB1/APB2 AMBA buses are all clocked at 80MHz.

### Serial Port

The SensorTile.box PRO has 4 U(S)ARTs. The UART4 is connected to JTAG/SWD connector
and may be used as console.

### USB interface

SensorTile.box PRO can be connected as a USB device to a PC host through its USB-C connector.
The final application may use it to declare SensorTile.box PRO device as belonging to a
certain standard or vendor class, e.g. a CDC, a mass storage or a composite device with both
functions.

### BlueNRG-LP chip

The board is equipped with an STMicroelectronics [BlueNRG-LP](https://www.st.com/en/wireless-connectivity/bluenrg-lp.html) [[12]](#id24) chip. Before running Zephyr Bluetooth samples
on SensorTile.box PRO, it is required to upgrade the BlueNRG chip with a Zephyr BLE stack compatible firmware.
The upgrade may be easily performed using the application provided in [SensorTile.box PRO BLE firmware upgrade package](https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble_fw_upg_app/README.rst) [[13]](#id26).
For more information about BLE binaries for SensorTile.box family, see [stsw-mkbox-bleco](https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html) [[14]](#id28).

### Console

There are two possible options for Zephyr console output:

- through common CDC ACM UART backend configuration for all boards
- through UART4 which is available on SWD connector (JP2). In this case a JTAG adapter
  can be used to connect SensorTile.box PRO and have both SWD and console lines available.

  To enable console and shell over UART:

  - in your prj.conf, override the board’s default configuration by setting `CONFIG_BOARD_SERIAL_BACKEND_CDC_ACM=n`
  - add an overlay file named `<board>.overlay`:

```dts
/ {
    chosen {
       zephyr,console = &uart4;
       zephyr,shell-uart = &uart4;
     };
  };
```

Console default settings are 115200 8N1.

## Programming and Debugging

The `sensortile_box_pro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **dfu-util** | ✅ (default) |  |

There are two alternative methods of flashing ST Sensortile.box Pro board:

1. Using DFU software tools

   This method requires to enter STM32U585 ROM bootloader DFU mode
   by powering up (or reset) the board while keeping the BOOT0 button pressed.
   No additional hardware is required except a USB-C cable. This method is fully
   supported by [Flash & Debug Host Tools](../../../../develop/flash_debug/host-tools.md#flash-debug-host-tools).
   You can read more about how to enable and use the ROM bootloader by checking
   the application note [AN2606](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf) [[15]](#id30) (STM32U585xx section).
2. Using SWD hardware tools

   This method requires to connect additional hardware, like a ST-LINK/V3
   embedded debug tool, to the board SWD connector.

### DFU flashing

#### Install dfu-util

It is recommended to use at least v0.9 of dfu-util. The package available in
Debian and Ubuntu can be quite old, so you might have to build dfu-util from source.
Information about how to get the source code and how to build it can be found
at the [DFU-UTIL website](http://dfu-util.sourceforge.net/) [[16]](#id32)

#### Flash an Application to SensorTile.box PRO

While pressing the BOOT0 button, connect the USB-C cable to the USB OTG SensorTile.box PRO
port and to your computer. The board should be forced to enter DFU mode.

Check that the board is indeed in DFU mode:

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
([SensorTile.box Pro sensors](../../../../samples/boards/st/sensortile_box_pro/sensors-on-board/README.md#sensortile_box_pro_sensors "Read sensor data from the various SensorTile.box Pro sensors.")) that reads sensors data and outputs
values on the console.

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/steval-mkboxpro.html](https://www.st.com/en/evaluation-tools/steval-mkboxpro.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/schematic\_pack/steval-mkboxpro-schematic.pdf](https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf)

[[4](#id9)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html)

[[5](#id11)]

[https://www.st.com/resource/en/reference\_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf)

[[6](#id13)]

[https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html)

[[7](#id15)]

[https://www.st.com/en/mems-and-sensors/lis2mdl.html](https://www.st.com/en/mems-and-sensors/lis2mdl.html)

[[8](#id17)]

[https://www.st.com/en/mems-and-sensors/lps22df.html](https://www.st.com/en/mems-and-sensors/lps22df.html)

[[9](#id19)]

[https://www.st.com/en/mems-and-sensors/lis2du12.html](https://www.st.com/en/mems-and-sensors/lis2du12.html)

[[10](#id21)]

[https://www.st.com/en/mems-and-sensors/stts22h.html](https://www.st.com/en/mems-and-sensors/stts22h.html)

[[11](#id23)]

[https://www.st.com/en/mems-and-sensors/mp23db01hp.html](https://www.st.com/en/mems-and-sensors/mp23db01hp.html)

[[12](#id25)]

[https://www.st.com/en/wireless-connectivity/bluenrg-lp.html](https://www.st.com/en/wireless-connectivity/bluenrg-lp.html)

[[13](#id27)]

[https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble\_fw\_upg\_app/README.rst](https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble_fw_upg_app/README.rst)

[[14](#id29)]

[https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html](https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html)

[[15](#id31)]

[http://www.st.com/content/ccc/resource/technical/document/application\_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf)

[[16](#id33)]

[http://dfu-util.sourceforge.net/](http://dfu-util.sourceforge.net/)
