---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/vcc-gnd/yd_esp32/doc/index.html
original_path: boards/vcc-gnd/yd_esp32/doc/index.html
---

# YD-ESP32

Board Overview

[![../../../../_images/yd_esp32.png](https://docs.zephyrproject.org/4.1.0/_images/yd_esp32.png)
](https://docs.zephyrproject.org/4.1.0/_images/yd_esp32.png)

YD-ESP32

Name:
:   `yd_esp32`

Vendor:
:   VCC-GND Studio

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/vcc-gnd/yd_esp32/doc/index.rst/../..)

## Overview

The YD-ESP32 development board is one of VCC-GND® Studio’s official boards.
This board is based on the ESP32-WROOM-32E module, with the ESP32 as the core.

### ESP32

ESP32 is a series of low cost, low power system on a chip microcontrollers
with integrated Wi-Fi & dual-mode Bluetooth. The ESP32 series employs a
Tensilica Xtensa LX6 microprocessor in both dual-core and single-core
variations. ESP32 is created and developed by Espressif Systems, a
Shanghai-based Chinese company, and is manufactured by TSMC using their 40nm
process.

The features include the following:

- Dual core Xtensa microprocessor (LX6), running at 160 or 240MHz
- 520KB of SRAM
- 802.11b/g/n/e/i
- Bluetooth v4.2 BR/EDR and BLE
- Various peripherals:

  - 12-bit ADC with up to 18 channels
  - 2x 8-bit DACs
  - 10x touch sensors
  - Temperature sensor
  - 4x SPI
  - 2x I2S
  - 2x I2C
  - 3x UART
  - SD/SDIO/MMC host
  - Slave (SDIO/SPI)
  - Ethernet MAC
  - CAN bus 2.0
  - IR (RX/TX)
  - Motor PWM
  - LED PWM with up to 16 channels
  - Hall effect sensor
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)
- 5uA deep sleep current

For more information, check the datasheet at [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf) [[3]](#id6).

### Supported Features

The `yd_esp32` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `yd_esp32/esp32/appcpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L29) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L471) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L70) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L408) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L192) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L417) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L461) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif,esp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L75) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif,esp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L201) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L306) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L340) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L332) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L173) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L148) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L160) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L83) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif,esp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L126) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L207) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L91) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L265) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L273) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L362) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L491) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L500) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L256) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L229) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L386) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L138) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L368)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L377) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L65) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `yd_esp32/esp32/procpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L29) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif,xtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L471) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L70) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L408) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L192) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L417) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L461) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif,esp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L75) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif,esp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L201) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L306) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L340)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L351) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L332) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif,esp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/vcc-gnd/yd_esp32/yd_esp32_procpu.dts?plain=1#L24) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L173) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L148) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif,esp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| LED strip | on-board | Worldsemi WS2812 LED strip, SPI binding[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/vcc-gnd/yd_esp32/yd_esp32_procpu.dts?plain=1#L95) | [`worldsemi,ws2812-spi`](../../../../build/dts/api/bindings/led_strip/worldsemi,ws2812-spi.md#std-dtcompatible-worldsemi-ws2812-spi) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L160) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif,mbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L83) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif,esp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L126) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif,esp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L207) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L91) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L265) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L273) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L362) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L491) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L500) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L256) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L229)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L238) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L386) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L138) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L368)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L377) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L65) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

### System requirements

#### Prerequisites

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
west build -b yd_esp32 --sysbuild samples/hello_world
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
west build -b yd_esp32/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `yd_esp32` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
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
Hello World! yd_esp32
```

### RGB LED

The board contains an addressable RGB LED ([XL-5050RGBC-WS2812B](http://www.xinglight.cn/index.php?c=show&id=947) [[1]](#id2)), driven by GPIO16.
Here is an example of how to test it using the [LED strip](../../../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/drivers/led/led_strip
west flash
```

## Debugging

ESP32 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[5]](#id10).

On the YD-ESP32 board, the JTAG pins are not run to a
standard connector (e.g. ARM 20-pin) and need to be manually connected
to the external programmer (e.g. a Flyswatter2):

| ESP32 pin | JTAG pin |
| --- | --- |
| 3V3 | VTRef |
| EN | nTRST |
| IO14 | TMS |
| IO12 | TDI |
| GND | GND |
| IO13 | TCK |
| IO15 | TDO |

Further documentation can be obtained from the SoC vendor in [JTAG debugging for ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html) [[4]](#id8).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
west debug
```

### Note on Debugging with GDB Stub

GDB stub is enabled on ESP32.

- When adding breakpoints, please use hardware breakpoints with command
  `hbreak`. Command `break` uses software breakpoints which requires
  modifying memory content to insert break/trap instructions.
  This does not work as the code is on flash which cannot be randomly
  accessed for modification.

## References

[[1](#id3)]

[http://www.xinglight.cn/index.php?c=show&id=947](http://www.xinglight.cn/index.php?c=show&id=947)

[[2](#id5)]

[https://www.espressif.com/sites/default/files/documentation/esp32\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)

[[3](#id7)]

[https://espressif.com/sites/default/files/documentation/esp32\_technical\_reference\_manual\_en.pdf](https://espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)

[[4](#id9)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html)

[[5](#id11)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
