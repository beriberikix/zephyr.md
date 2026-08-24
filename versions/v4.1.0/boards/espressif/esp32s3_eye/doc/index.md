---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/espressif/esp32s3_eye/doc/index.html
original_path: boards/espressif/esp32s3_eye/doc/index.html
---

# ESP32-S3-EYE

Board Overview

[![../../../../_images/esp32s3_eye.webp](https://docs.zephyrproject.org/4.1.0/_images/esp32s3_eye.webp)
](https://docs.zephyrproject.org/4.1.0/_images/esp32s3_eye.webp)

ESP32-S3-EYE

Name:
:   `esp32s3_eye`

Vendor:
:   Espressif Systems

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/espressif/esp32s3_eye/doc/index.rst/../..)

## Overview

The ESP32-S3-EYE is a small-sized AI development board produced by [Espressif](https://espressif.com).
It is based on the [ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3) SoC.
It features a 2-Megapixel camera, an LCD display, and a microphone, which are used for image
recognition and audio processing. ESP32-S3-EYE offers plenty of storage, with an 8 MB Octal PSRAM
and a 8 MB flash.

## Hardware

The ESP32-S3-EYE board consists of two parts: the main board (ESP32-S3-EYE-MB) that integrates the
ESP32-S3-WROOM-1 module, camera, SD card slot, digital microphone, USB port, and function buttons;
and the sub board (ESP32-S3-EYE-SUB) that contains an LCD display.
The main board and sub board are connected through pin headers.

### Supported Features

The `esp32s3_eye` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `esp32s3_eye/esp32s3/appcpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX7 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L32) | [`espressif,xtensa-lx7`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx7.md#std-dtcompatible-espressif-xtensa-lx7) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L362) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L73) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L382) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L168) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L186) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L442)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L409) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L513) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L195) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L249) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L283) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L305) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L275) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L159) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L134) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L146) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L100) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L201) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x0_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L78) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L476) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L484) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L470) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L535) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L544) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L355) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L504) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L209) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L400) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L333) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L124) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Video | on-chip | ESP32 LCD CAM Peripheral interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L391) | [`espressif,esp32-lcd-cam`](../../../../build/dts/api/bindings/video/espressif,esp32-cam.md#std-dtcompatible-espressif-esp32-lcd-cam) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L177) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L452) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L68) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `esp32s3_eye/esp32s3/procpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX7 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L32) | [`espressif,xtensa-lx7`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx7.md#std-dtcompatible-espressif-xtensa-lx7) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L362)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L372) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L73) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L382) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L168) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L186) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L409)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L431) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| Display | on-board | ST7789V 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32s3_eye/esp32s3_eye_procpu.dts?plain=1#L89) | [`sitronix,st7789v`](../../../../build/dts/api/bindings/display/sitronix,st7789v.md#std-dtcompatible-sitronix-st7789v) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L513) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L195) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L249) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L294)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L283) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L305) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L275) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32s3_eye/esp32s3_eye_procpu.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| on-board | Input driver for ADC attached resistor ladder buttons[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32s3_eye/esp32s3_eye_procpu.dts?plain=1#L46) | [`adc-keys`](../../../../build/dts/api/bindings/input/adc-keys.md#std-dtcompatible-adc-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L159) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L134) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32s3_eye/esp32s3_eye_procpu.dts?plain=1#L73) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L146) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L100) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L201) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x0_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L78) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L476) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L484) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L470) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L535) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L544) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L355) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L504) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L209) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L400) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L344)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L333) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L124) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Video | on-board | OV2640 CMOS video sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32s3_eye/esp32s3_eye_procpu.dts?plain=1#L126) | [`ovti,ov2640`](../../../../build/dts/api/bindings/video/ovti,ov2640.md#std-dtcompatible-ovti-ov2640) |
| on-chip | ESP32 LCD CAM Peripheral interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L391) | [`espressif,esp32-lcd-cam`](../../../../build/dts/api/bindings/video/espressif,esp32-cam.md#std-dtcompatible-espressif-esp32-lcd-cam) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L177) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L452)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L461) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L68) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

### Block Diagram

The block diagram below presents main components of the ESP32-S3-EYE-MB main board (on the left)
and the ESP32-S3-EYE-SUB sub board (on the right), as well as the interconnections between
components.

![ESP32-S3-EYE Block Diagram](https://docs.zephyrproject.org/4.1.0/_images/ESP32-S3-EYE_20210913_V03_SystemBlock.webp)

### Components on the ESP32-S3-EYE-MB Main Board

![ESP32-S3-EYE_MB](https://docs.zephyrproject.org/4.1.0/_images/ESP32-S3-EYE_MB-annotated-photo.webp)

Key Components MB

| No. | Key Component | Description |
| --- | --- | --- |
| 1 | Camera | The camera OV2640 with 2 million pixels has a 66.5° field of view and a maximum resolution of 1600x1200. You can change the resolution when developing applications. |
| 2 | Module Power LED | The LED (green) turns on when USB power is connected to the board. If it is not turned on, it indicates either the USB power is not supplied, or the 5 V to 3.3 V LDO is broken. Software can configure GPIO3 to set different LED statuses (turned on/off, flashing) for different statuses of the board. Note that GPIO3 must be set up in open-drain mode. Pulling GPIO3 up may burn the LED. |
| 3 | Pin Headers | Connect the female headers on the sub board. |
| 4 | 5 V to 3.3 V LDO | Power regulator that converts a 5 V supply into a 3.3 V output for the module. |
| 5 | Digital Microphone | The digital I2S MEMS microphone features 61 dB SNR and –26 dBFS sensitivity, working at 3.3 V. |
| 6 | FPC Connector | Connects the main board and the sub board. |
| 7 | Function Button | There are six function buttons on the board. Users can configure any functions as needed except for the RST button. |
| 8 | ESP32-S3-WROOM-1 | The ESP32-S3-WROOM-1 module embeds the ESP32-S3R8 chip variant that provides Wi-Fi and Bluetooth 5 (LE) connectivity, as well as dedicated vector instructions for accelerating neural network computing and signal processing. On top of the integrated 8 MB Octal SPI PSRAM offered by the SoC, the module also comes with 8 MB flash, allowing for fast data access. ESP32-S3-WROOM-1U module is also supported. |
| 9 | MicroSD Card Slot | Used for inserting a MicroSD card to expand memory capacity. |
| 10 | 3.3 V to 1.5 V LDO | Power regulator that converts a 3.3 V supply into a 1.5 V output for the camera. |
| 11 | 3.3 V to 2.8 V LDO | Power regulator that converts a 3.3 V supply into a 2.8 V output for the camera. |
| 12 | USB Port | A Micro-USB port used for 5 V power supply to the board, as well as for communication with the chip via GPIO19 and GPIO20. |
| 13 | Battery Soldering Points | Used for soldering a battery socket to connect an external Li-ion battery that can serve as an alternative power supply to the board. If you use an external battery, make sure it has built-in protection circuit and fuse. The recommended specifications of the battery: capacity > 1000 mAh, output voltage 3.7 V, input voltage 4.2 V – 5 V. |
| 14 | Battery Charger Chip | 1 A linear Li-ion battery charger (ME4054BM5G-N) in ThinSOT package. The power source for charging is the **USB Port**. |
| 15 | Battery Red LED | When the USB power is connected to the board and a battery is not connected, the red LED blinks. If a battery is connected and being charged, the red LED turns on. When the battery is fully charged, it turns off. |
| 16 | Accelerometer | Three-axis accelerometer (QMA7981) for screen rotation, etc. |

### Components on the ESP32-S3-EYE-SUB Sub Board

![ESP32-S3-EYE_SUB](https://docs.zephyrproject.org/4.1.0/_images/ESP32-S3-EYE_SUB-annotated-photo.webp)

Key Components SUB

| Key Component | Description |
| --- | --- |
| LCD Display | 1.3” LCD display, connected to ESP32-S3 over the SPI bus. |
| Strapping Pins | Four strapping pins led out from the main board. They can be used as testing points. |
| Female Headers | Used for mounting onto the pin headers on the main board. |
| LCD FPC Connector | Connects the sub board and the LCD display. |
| LCD\_RST | LCD\_RST testing point. You can use it to reset the LCD display with control signals. |

## Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

### Simple boot

The board could be loaded using the single binary image, without 2nd stage bootloader.
It is the default option when building the application without additional configuration.

Note

Simple boot does not provide any security features nor OTA updates.

### MCUboot bootloader

User may choose to use MCUboot bootloader instead. In that case the bootloader
must be built (and flashed) at least once.

There are two options to be used when building an application:

1. Sysbuild
2. Manual build

Note

User can select the MCUboot bootloader by adding the following line
to the board default configuration file.

```cfg
CONFIG_BOOTLOADER_MCUBOOT=y
```

### Sysbuild

The sysbuild makes possible to build and flash all necessary images needed to
bootstrap the board with the ESP32 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b esp32s3_eye/esp32s3/procpu --sysbuild samples/hello_world
```

By default, the ESP32 sysbuild creates bootloader (MCUboot) and application
images. But it can be configured to create other kind of images.

Build directory structure created by sysbuild is different from traditional
Zephyr build. Output is structured by the domain subdirectories:

```text
build/
├── hello_world
│   └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
├── mcuboot
│    └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
└── domains.yaml
```

Note

With `--sysbuild` option the bootloader will be re-build and re-flash
every time the pristine build is used.

For more information about the system build please read the [Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild) documentation.

### Manual build

During the development cycle, it is intended to build & flash as quickly possible.
For that reason, images can be built one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b esp32s3_eye/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `esp32s3_eye/esp32s3/procpu` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32s3_eye/esp32s3/procpu samples/hello_world
west flash
```

Open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! esp32s3_eye/esp32s3/procpu
```

## Debugging

ESP32-S3 modules require patches to OpenOCD that are not upstreamed yet.
Espressif maintains their own fork of the project. The custom OpenOCD can be obtained at
[OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases)

The Zephyr SDK uses a bundled version of OpenOCD by default.
You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp32s3_eye/esp32s3/procpu samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32s3_eye/esp32s3/procpu samples/hello_world
west debug
```
