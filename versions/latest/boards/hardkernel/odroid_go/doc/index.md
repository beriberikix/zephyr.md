---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/hardkernel/odroid_go/doc/index.html
original_path: boards/hardkernel/odroid_go/doc/index.html
---

# ODROID-GO

Board Overview

[![../../../../_images/odroid_go.jpg](https://docs.zephyrproject.org/4.2.0/_images/odroid_go.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/odroid_go.jpg)

ODROID-GO

Name:
:   `odroid_go`

Vendor:
:   Hardkernel Co., Ltd

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/hardkernel/odroid_go/doc/index.rst/../..)

## Overview

ODROID-GO Game Kit is a “Do it yourself” (“DIY”) portable game console by
HardKernel. It features a custom ESP32-WROVER with 16 MB flash and it operates
from 80 MHz - 240 MHz [[1]](#id2).

The features include the following:

- Dual core Xtensa microprocessor (LX6), running at 80 - 240MHz
- 4 MB of PSRAM
- 802.11b/g/n/e/i
- Bluetooth v4.2 BR/EDR and BLE
- 2.4 inch 320x240 TFT LCD
- Speaker
- Micro SD card slot
- Micro USB port (battery charging and USB\_UART data communication
- Input Buttons (Menu, Volume, Select, Start, A, B, Direction Pad)
- Expansion port (I2C, GPIO, SPI)
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)

### External Connector

| PIN # | Signal Name | ESP32-WROVER Functions |
| --- | --- | --- |
| 1 | GND | GND |
| 2 | VSPI.SCK (IO18) | GPIO18, VSPICLK |
| 3 | IO12 | GPIO12 |
| 4 | IO15 | GPIO15, ADC2\_CH3 |
| 5 | IO4 | GPIO4, ADC2\_CH0 |
| 6 | P3V3 | 3.3 V |
| 7 | VSPI.MISO (IO19) | GPIO19, VSPIQ |
| 8 | VSPI.MOSI (IO23) | GPIO23, VSPID |
| 9 | N.C | N/A |
| 10 | VBUS | USB VBUS (5V) |

### Supported Features

The `odroid_go` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `odroid_go/esp32/appcpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L30) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L518) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L71) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L435) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L97) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif,esp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L191) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L444) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L454) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L508) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif,esp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L76) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif,esp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L200) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L305) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L339) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L361) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L331) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L157) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L169) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L84) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif,esp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L135) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L206) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L92) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L264) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L272) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L389) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L538) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L547) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L255) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L228) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L413) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L147) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L395)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L404) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L66) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `odroid_go/esp32/procpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L30) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L518) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L71) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L435) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L97) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif,esp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L191) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L444) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L454) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L508) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif,esp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Display | on-board | Ilitek ILI9341 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/hardkernel/odroid_go/odroid_go_procpu.dts?plain=1#L92) | [`ilitek,ili9341`](../../../../build/dts/api/bindings/display/ilitek,ili9341.md#std-dtcompatible-ilitek-ili9341) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L76) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif,esp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L200) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L305) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L339)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L350) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L361) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L331) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/hardkernel/odroid_go/odroid_go_procpu.dts?plain=1#L35) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L157) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/hardkernel/odroid_go/odroid_go_procpu.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L169) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L84) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif,esp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L135) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L206) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L92) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L264) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L272) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| Regulator | on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/hardkernel/odroid_go/odroid_go_procpu.dts?plain=1#L69) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L389) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L538) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L547) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L255) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L228)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L237) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L424)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L413) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L147) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L395)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L404) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L66) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

## System requirements

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

The `odroid_go` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **esp32** | ✅ (default) |  |

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
west build -b odroid_go --sysbuild samples/hello_world
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
west build -b odroid_go/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `odroid_go` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world
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
Hello World! odroid_go
```

## Debugging

As with much custom hardware, the ESP32 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[2]](#id4).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world
west debug
```

## References

[[2](#id5)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)

[[1](#id1)]

[https://wiki.odroid.com/odroid\_go/odroid\_go](https://wiki.odroid.com/odroid_go/odroid_go)
