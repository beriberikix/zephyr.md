---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/steval_stwinbx1/doc/index.html
original_path: boards/st/steval_stwinbx1/doc/index.html
---

# STEVAL STWINBX1 Development kit

Board Overview

[![../../../../_images/steval_stwinbx1.jpg](https://docs.zephyrproject.org/4.1.0/_images/steval_stwinbx1.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/steval_stwinbx1.jpg)

STEVAL STWINBX1 Development kit

Name:
:   `steval_stwinbx1`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u585xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/steval_stwinbx1/doc/index.rst/../..)

## Overview

The STWIN.box (STEVAL-STWINBX1) is a development kit that features an Arm|reg| Cortex|reg|-M33 based STM32U585AI MCU
and is a reference design that simplifies prototyping and testing of advanced industrial sensing applications in
IoT contexts such as condition monitoring and predictive maintenance.

The STEVAL-STWINBX1 kit consists of an STWIN.box core system, a 480mAh LiPo battery, an adapter for the ST-LINK debugger,
a plastic case, an adapter board for DIL 24 sensors and a flexible cable.

More information about the board can be found at the [STEVAL-STWINBX1 Development kit website](https://www.st.com/en/evaluation-tools/steval-stwinbx1.html).

## Supported Features

The STEVAL-STWINBX1 provides motion, environmental, and audio
sensor data through either the built-in RS485 transceiver, BLE, Wi-Fi, and
NFC or USB protocols to a host application running on a smartphone/PC to implement applications such as:

- Multisensing wireless platform for vibration monitoring and ultrasound detection
- Baby crying detection with Cloud AI learning
- Barometer / environmental monitoring
- Vehicle / goods tracking
- Vibration monitoring
- Compass and inclinometer
- Sensor data logger

(see [Sensing](#sensing) section for the complete lists of available
sensors on board)

The `steval_stwinbx1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### `steval_stwinbx1/stm32u585xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L35) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L781) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V2 compatible with BlueNRG-1 and successor devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L187) | [`st,hci-spi-v2`](../../../../build/dts/api/bindings/bluetooth/st%2Chci-spi-v2.md#std-dtcompatible-st-hci-spi-v2) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L818) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L177) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L83) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L96)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L89) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32U5 Multi Speed Internal Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L103)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L110) | [`st,stm32u5-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-msi-clock.md#std-dtcompatible-st-stm32u5-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L117) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L132) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L152) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L561) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L725) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L773) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L837) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L159) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L216) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L936) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L408)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L396) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L189) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L36) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L850) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L856) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L753)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L763) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L43) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L167) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L300) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L699) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u575.dtsi?plain=1#L29) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L210) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L864) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L576)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L507) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L183) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L734) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L488) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics IIS2DLPC accelerometer accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L157) | [`st,iis2dlpc`](../../../../build/dts/api/compatibles/st%2Ciis2dlpc.md#std-dtcompatible-st-iis2dlpc) |
| on-board | STMicroelectronics ISM330DHCX 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L165) | [`st,ism330dhcx`](../../../../build/dts/api/compatibles/st%2Cism330dhcx.md#std-dtcompatible-st-ism330dhcx) |
| on-board | STMicroelectronics IIS2ICLX 2-axis accelerometer sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L173) | [`st,iis2iclx`](../../../../build/dts/api/compatibles/st%2Ciis2iclx.md#std-dtcompatible-st-iis2iclx) |
| on-board | STMicroelectronics STTS22H temperature sensor connected to I2C bus When setting the sampling-rate property in a .dts or .dtsi file you may include stts22h.h and use the macros defined there[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L205) | [`st,stts22h`](../../../../build/dts/api/bindings/sensor/st%2Cstts22h-i2c.md#std-dtcompatible-st-stts22h) |
| on-board | STMicroelectronics IIS2MDC magnetometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L212) | [`st,iis2mdc`](../../../../build/dts/api/compatibles/st%2Ciis2mdc.md#std-dtcompatible-st-iis2mdc) |
| on-board | STMicroelectronics LPS22DF pressure and temperature sensor connected to I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/steval_stwinbx1/steval_stwinbx1.dts?plain=1#L219) | [`st,ilps22qs`](../../../../build/dts/api/compatibles/st%2Cilps22qs.md#std-dtcompatible-st-ilps22qs) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L946) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L958)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L967) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L983)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L976) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L321)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L312) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L339) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L357) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L990) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L376)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L366) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L78) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L829) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L444)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L455) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L567)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L498) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u575.dtsi?plain=1#L14) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L289) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L295) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

## Hardware

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

- [STM32U585 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html)
- [STM32U585 reference manual](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf)

## Connectivity

> - **BlueNRG-M2SA** Bluetooth|reg| low energy v5.2 wireless technology module
>   ([BlueNRG-M2 datasheet](https://www.st.com/en/product/BlueNRG-M2))
> - **MXCHIP EMW3080** (802.11 b/g/n compliant Wi-Fi module)
> - **ST25DV64K** dynamic NFC/RFID tag IC with 64-Kbit EEPROM
>   ([st25dv64k datasheet](https://www.st.com/en/nfc/st25dv64k.html))
> - USB Type-C|trade| connector (power supply and data)
> - STDC14 programming connector for **STLINK-V3MINI**
>   ([stlink-v3mini](https://www.st.com/en/development-tools/stlink-v3mini.html))
> - microSD card socket

## Sensing

> - **ILPS22QS** MEMS pressure sensor
>   ([ilps22qs datasheet](https://www.st.com/en/mems-and-sensors/ilps22qs.html))
> - **STTS22H** Digital temperature sensor
>   ([stts22hh datasheet](https://www.st.com/en/mems-and-sensors/stts22h.html))
> - **TSV912** wide-bandwidth (8 MHz) rail-to-rail I/O op-amp
>   ([tsv912 datasheet](https://www.st.com/en/automotive-analog-and-power/tsv912.html))
> - **ISM330DHCX** iNEMO IMU, 3D accelerometer and 3D gyroscope with Machine Learning Core and Finite State Machine
>   ([ism330dhcx datasheet](https://www.st.com/en/mems-and-sensors/ism330dhcx.html))
> - **IIS3DWB** wide bandwidth accelerometer
>   ([iis3dwb datasheet](https://www.st.com/en/mems-and-sensors/iis3dwb.html))
> - **IIS2DLPC** high-performance ultra-low-power 3-axis accelerometer for industrial applications
>   ([iis2dlpc datasheet](https://www.st.com/en/mems-and-sensors/iis2dlpc.html))
> - **IIS2MDC** 3-axis magnetometer
>   ([iis2mdc datasheet](https://www.st.com/en/mems-and-sensors/iis2mdc.html))
> - **IIS2ICLX** high-accuracy, high-resolution, low-power, 2-axis digital inclinometer with Machine Learning Core
>   ([iis2iclx datasheet](https://www.st.com/en/mems-and-sensors/iis2iclx.html))
> - **IMP23ABSU** analog MEMS microphone
>   ([imp23absu datasheet](https://www.st.com/en/mems-and-sensors/imp23absu.html))
> - **IMP34DT05** digital MEMS microphone
>   ([imp34dt05 datasheet](https://www.st.com/en/mems-and-sensors/imp34dt05.html))

## Connections and IOs

- 2x user LEDs

  - **led0** (Green)
  - **led1** (Orange)
- 4x buttons/switch

  - **User** / **boot0** button, available to user application
    but useful to let the SensorTile.box PRO enter DFU mode
    if found pressed after h/w reset (see **rst** button and
    [Programming and Debugging](#programming-and-debugging) section)
  - **RESET** button, used to reset the board
  - **PWR** button, used to Power on/off the board

For more details please refer to [STEVAL-STWINBX1 board User Manual](https://www.st.com/resource/en/user_manual/um2965-getting-started-with-the-stevalstwinbx1-sensortile-wireless-industrial-node-development-kit-stmicroelectronics.pdf).

### System Clock

STEVAL-STWINBX1 System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default the System clock is driven by the PLL clock at 160MHz,
driven by 16MHz high speed external oscillator.
The internal AHB/APB1/APB2/APB3 AMBA buses are all clocked at 160MHz.

### Serial Port

The USART2 is connected to JTAG/SWD connector
and may be used as console.

### USB interface

STEVAL-STWINBX1 can be connected as a USB device to a PC host through its USB-C connector.
The final application may use it to declare STEVAL-STWINBX1 device as belonging to a
certain standard or vendor class, e.g. a CDC, a mass storage or a composite device with both
functions.

### Console

There are two possible options for Zephyr console output:

- through common CDC ACM UART backend configuration for all boards
- through USART2 which is available on SWD connector (CN4). In this case a JTAG adapter
  can be used to connect STEVAL-STWINBX1 and have both SWD and console lines available.

  To enable console and shell over UART:

  - in your prj.conf, override the board’s default configuration by setting `CONFIG_BOARD_SERIAL_BACKEND_CDC_ACM=n`
  - add an overlay file named `<board>.overlay`:

```dts
/ {
    chosen {
       zephyr,console = &usart2;
       zephyr,shell-uart = &usart2;
     };
  };
```

Console default settings are 115200 8N1.

### Programming and Debugging

There are two alternative methods of flashing ST Sensortile.box Pro board:

1. Using DFU software tools

   This method requires to enter STM32U585 ROM bootloader DFU mode
   by powering up (or reset) the board while keeping the USER (BOOT0) button pressed.
   No additional hardware is required except a USB-C cable. This method is fully
   supported by [Flash & Debug Host Tools](../../../../develop/flash_debug/host-tools.md#flash-debug-host-tools).
   You can read more about how to enable and use the ROM bootloader by checking
   the application note [AN2606](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf) (STM32U585xx section).
2. Using SWD hardware tools

   The STEVAL-STWINBX1 does not include a on-board debug probe.
   It requires to connect additional hardware, like a ST-LINK/V3
   embedded debug tool, to the board STDC14 connector (CN4) labeled `MCU-/SWD`.

### Install dfu-util

Note

Required only to use dfu-util runner.

It is recommended to use at least v0.9 of dfu-util. The package available in
Debian and Ubuntu can be quite old, so you might have to build dfu-util from source.
Information about how to get the source code and how to build it can be found
at the [DFU-UTIL website](http://dfu-util.sourceforge.net/)

### Install STM32CubeProgrammer

Note

Required to program over DFU (default) or SWD.

It is recommended to use the latest version of [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)

### Flash an Application to STEVAL-STWINBX1

There are two ways to enter DFU mode:

1. USB-C cable not connected

   While pressing the USER button, connect the USB-C cable to the USB OTG STEVAL-STWINBX1
   port and to your computer.
2. USB-C cable connected

   While pressing the USER button, press the RESET button and release it.

With both methods, the board should be forced to enter DFU mode.

Check that the board is indeed in DFU mode:

```shell
$ sudo dfu-util -l
dfu-util 0.9

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2019 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [0483:df11] ver=0200, devnum=58, cfg=1, intf=0, path="3-1", alt=2, name="@OTP Memory   /0x0BFA0000/01*512 e", serial="207136863530"
Found DFU: [0483:df11] ver=0200, devnum=58, cfg=1, intf=0, path="3-1", alt=1, name="@Option Bytes   /0x40022040/01*64 e", serial="207136863530"
Found DFU: [0483:df11] ver=0200, devnum=58, cfg=1, intf=0, path="3-1", alt=0, name="@Internal Flash   /0x08000000/256*08Kg", serial="207136863530"
```

You should see the following confirmation on your Linux host:

```shell
$ dmesg
usb 3-1: new full-speed USB device number 16 using xhci_hcd
usb 3-1: New USB device found, idVendor=0483, idProduct=df11, bcdDevice= 2.00
usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 3-1: Product: DFU in FS Mode
usb 3-1: Manufacturer: STMicroelectronics
usb 3-1: SerialNumber: 207136863530
```

You can build and flash the provided sample application
([STWIN.box sensors](../../../../samples/boards/st/steval_stwinbx1/sensors/README.md#stwinbx1_sensors "Read sensor data from the various STWIN SensorTile wireless industrial node sensors.")) that reads sensors data and outputs
values on the console.
