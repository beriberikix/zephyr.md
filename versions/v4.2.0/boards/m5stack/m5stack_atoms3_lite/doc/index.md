---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/m5stack/m5stack_atoms3_lite/doc/index.html
original_path: boards/m5stack/m5stack_atoms3_lite/doc/index.html
---

# AtomS3 Lite

Board Overview

[![../../../../_images/m5stack_atoms3_lite.webp](https://docs.zephyrproject.org/4.2.0/_images/m5stack_atoms3_lite.webp)
](https://docs.zephyrproject.org/4.2.0/_images/m5stack_atoms3_lite.webp)

AtomS3 Lite

Name:
:   `m5stack_atoms3_lite`

Vendor:
:   M5Stack

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/m5stack/m5stack_atoms3_lite/doc/index.rst/../..)

## Overview

M5Stack AtomS3 Lite is an ESP32-based development board from M5Stack.

It features the following integrated components:

- ESP32-S3FN8 chip (240MHz dual core, Wi-Fi/BLE 5.0)
- 512KB of SRAM
- 384KB of ROM
- 8MB of Flash
- RGB Status-LED

### Supported Features

The `m5stack_atoms3_lite` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `m5stack_atoms3_lite/esp32s3/appcpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX7 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L32) | [`espressif,xtensa-lx7`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx7.md#std-dtcompatible-espressif-xtensa-lx7) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L361) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L73) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L381) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L83) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif,esp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 general-purpose timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L456)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L408) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L418) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L532) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L194) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L248) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L282) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L304) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L274) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L167) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L142) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L154) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L108) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L200) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x0_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L78) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L495) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L503) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L489) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L554) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L563) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L354) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L523) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L208) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L399) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L332) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L132) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Video | on-chip | ESP32 LCD CAM Peripheral interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L390) | [`espressif,esp32-lcd-cam`](../../../../build/dts/api/bindings/video/espressif,esp32-cam.md#std-dtcompatible-espressif-esp32-lcd-cam) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L176) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L471) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L68) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `m5stack_atoms3_lite/esp32s3/procpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX7 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L32) | [`espressif,xtensa-lx7`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx7.md#std-dtcompatible-espressif-xtensa-lx7) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L361) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L73) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L381) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L83) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif,esp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 general-purpose timers[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L408)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L440) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L418) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L532) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L194) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L248) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L282) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L304) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L274) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_atoms3_lite/m5stack_atoms3_lite_procpu.dts?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L167) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L142) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| LED strip | on-board | Worldsemi WS2812 LED strip, SPI binding[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_atoms3_lite/m5stack_atoms3_lite_procpu.dts?plain=1#L84) | [`worldsemi,ws2812-spi`](../../../../build/dts/api/bindings/led_strip/worldsemi,ws2812-spi.md#std-dtcompatible-worldsemi-ws2812-spi) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L154) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L108) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L200) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x0_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L78) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L495) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L503) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L489) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L554) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L563) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L354) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L523) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L208)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L217) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L399) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L343)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L332) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L132) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Video | on-chip | ESP32 LCD CAM Peripheral interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L390) | [`espressif,esp32-lcd-cam`](../../../../build/dts/api/bindings/video/espressif,esp32-cam.md#std-dtcompatible-espressif-esp32-lcd-cam) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L176) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L471)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L480) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s3/esp32s3_common.dtsi?plain=1#L68) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

## Start Application Development

Before powering up your M5Stack AtomS3 Lite, please make sure that the board is in good
condition with no obvious signs of damage.

### System requirements

#### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

#### Building & Flashing

The `m5stack_atoms3_lite` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **esp32** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b m5stack_atoms3_lite/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `m5stack_atoms3_lite` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b m5stack_atoms3_lite/esp32s3/procpu samples/hello_world
west flash
```

The baud rate of 921600bps is set by default. If experiencing issues when flashing,
try using different values by using `--esp-baud-rate <BAUD>` option during
`west flash` (e.g. `west flash --esp-baud-rate 115200`).

You can also open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! m5stack_atoms3_lite
```

#### Debugging

M5Stack AtomS3 Lite debugging is not supported due to pinout limitations.

## Related Documents

- [M5Stack AtomS3 Lite schematic](https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3%20Lite/img-4061fdd4-6954-4709-a7e7-b0f50e5ba52e.webp)
- [ESP32S3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)
