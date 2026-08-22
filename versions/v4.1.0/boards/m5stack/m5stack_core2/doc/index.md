---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/m5stack/m5stack_core2/doc/index.html
original_path: boards/m5stack/m5stack_core2/doc/index.html
---

# Core2

Board Overview

[![../../../../_images/m5stack_core2.webp](../../../../_images/m5stack_core2.webp)
](../../../../_images/m5stack_core2.webp)

Core2

Name:
:   `m5stack_core2`

Vendor:
:   M5Stack

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/m5stack/m5stack_core2/doc/index.rst/../..)

## Overview

M5Stack Core2 is an ESP32-based development board from M5Stack. It is the successor for the Core module.

M5Stack Core2 features the following integrated components:

- ESP32-D0WDQ6-V3 chip (240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi)
- PSRAM 8MB
- Flash 16MB
- LCD IPS TFT 2”, 320x240 px screen (ILI9342C)
- Touch screen (FT6336U)
- PMU AXP192
- Audio NS4168 amplifier (1W-092 speaker)
- Vibration motor
- RTC BM8563
- USB CP2104
- SD-Card slot
- Grove connector
- IMO 6-axis IMU MPU6886
- MIC SPM1423
- Battery 390mAh 3,7V

## Functional Description

The following table below describes the key components, interfaces, and controls
of the M5Stack Core2 board.

| Key Component | Description | Status |
| --- | --- | --- |
| ESP32-D0WDQ6-V2 module | This [MPU-ESP32](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/esp32_datasheet_en_v3.9.pdf) module provides complete Wi-Fi and Bluetooth functionalities and integrates a 16-MB SPI flash. | supported |
| 32.768 kHz RTC | External precision 32.768 kHz crystal oscillator serves as a clock with low-power consumption while the chip is in Deep-sleep mode. | supported |
| Status LED | One user LED connected to the GPIO pin. | supported |
| USB Port | USB interface. Power supply for the board as well as the communication interface between a computer and the board. Contains: TypeC x 1, GROVE(I2C+I/O+UART) x 1 | supported |
| Reset button | Reset button | supported |
| Power Switch | Power on/off button. | supported |
| LCD screen | Built-in LCD TFT display ([LCD-ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf), 2”, 320x240 px) controlled via SPI interface | supported |
| SD-Card slot | SD-Card connection via SPI-mode. | supported |
| 6-axis IMU MPU6886 | The [MPU-6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf) is a 6-axis motion tracker (6DOF IMU) device that combines a 3-axis gyroscope and a 3-axis accelerometer. For details please refer to [M5Stack-Core2 base shield](../../../shields/m5stack_core2_ext/doc/index.md#m5stack-core2-ext) | supported |
| Grove port | Note: Grove port requires 5V to be enabled via `bus_5v` regulator | supported |
| Built-in microphone | The [SPM-1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf) I2S driven microphone. | todo |
| Built-in speaker | 1W speaker for audio output via I2S interface. | todo |
| Battery-support | Power supply via battery is supported automatically. But there is no possibility to query current battery status. | todo |

### Power supply

M5Stack Core2 module is equipped with the feature-rich power management IC
([`x-powers,axp192-regulator`](../../../../build/dts/api/bindings/regulator/x-powers%2Caxp192-regulator.md#std-dtcompatible-x-powers-axp192-regulator)).
Following regulators are utilized on this module:

- **vdd\_mcu**:
  Main power supply for the MCU.
- **lcd\_bg**:
  Display backlight voltage.
- **v\_peri**:
  Periphal supply. This regulator controls supply for the display, SD-Card.
- **vib\_motor**:
  Vibration motor regulator.
- **bus\_5v**
  BUS\_5V supply for Grove port.
  Note: This fixed regulator supply is disabled by default.

These voltages can be controlled via regulator api.

### Supported Features

The `m5stack_core2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `m5stack_core2/esp32/appcpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L29) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif%2Cxtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L471) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L70) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif%2Cesp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L408) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif%2Cesp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L192) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L417) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L461) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif%2Cesp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L75) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif%2Cesp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L201) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif%2Cesp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L306) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif%2Cesp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L340) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L332) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif%2Cesp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L173) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L148) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif%2Cesp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L160) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif%2Cmbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L83) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif%2Cesp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L126) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif%2Cesp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L207) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L91) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L265) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L273) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L362) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif%2Cesp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L491) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif%2Cesp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L500) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif%2Cesp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L256) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif%2Cesp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L229) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L386) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L138) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L368)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L377) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L65) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `m5stack_core2/esp32/procpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX6 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L29) | [`espressif,xtensa-lx6`](../../../../build/dts/api/bindings/cpu/espressif%2Cxtensa-lx6.md#std-dtcompatible-espressif-xtensa-lx6) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L471) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L70) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif%2Cesp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L408) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L182) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif%2Cesp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L192) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L417) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L461) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif%2Cesp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Display | on-board | ILI9342C 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L65) | [`ilitek,ili9342c`](../../../../build/dts/api/bindings/display/ilitek%2Cili9342c.md#std-dtcompatible-ilitek-ili9342c) |
| Ethernet | on-chip | ESP32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L75) | [`espressif,esp32-eth`](../../../../build/dts/api/bindings/ethernet/espressif%2Cesp32-eth.md#std-dtcompatible-espressif-esp32-eth) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L201) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif%2Cesp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L306) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif%2Cesp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| on-board | AXP192 GPIO Controller AX192 features 5 native GPIOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L167) | [`x-powers,axp192-gpio`](../../../../build/dts/api/bindings/gpio/x-powers%2Caxp192-gpio.md#std-dtcompatible-x-powers-axp192-gpio) |
| on-board | GPIO pins exposed on Grove 4 pins headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/grove_connectors.dtsi?plain=1#L8) | [`grove-header`](../../../../build/dts/api/bindings/gpio/grove-header.md#std-dtcompatible-grove-header) |
| on-board | GPIO pins exposed on M5Stack M-Bus headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_mbus_connectors.dtsi?plain=1#L7) | [`m5stack,mbus-header`](../../../../build/dts/api/bindings/gpio/m5stack%2Cmbus-header.md#std-dtcompatible-m5stack-mbus-header) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L340)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L351) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L332) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif%2Cesp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L190) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech%2Cft5336.md#std-dtcompatible-focaltech-ft5336) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L173) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| IPM | on-chip | ESP32 soft inter processor message[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L148) | [`espressif,esp32-ipm`](../../../../build/dts/api/bindings/ipm/espressif%2Cesp32-ipm.md#std-dtcompatible-espressif-esp32-ipm) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L42) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | ESP32 soft mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L160) | [`espressif,mbox-esp32`](../../../../build/dts/api/bindings/mbox/espressif%2Cmbox-esp32.md#std-dtcompatible-espressif-mbox-esp32) |
| MDIO | on-chip | ESP32 MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L83) | [`espressif,esp32-mdio`](../../../../build/dts/api/bindings/mdio/espressif%2Cesp32-mdio.md#std-dtcompatible-espressif-esp32-mdio) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L126) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif%2Cesp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| Multi-Function Device | on-board | X-Powers AXP192[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L130) | [`x-powers,axp192`](../../../../build/dts/api/bindings/mfd/x-powers%2Caxp192.md#std-dtcompatible-x-powers-axp192) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L207) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x1000_amp_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L91) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L265) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L273) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| Regulator | on-board | AXP192 PMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L135) | [`x-powers,axp192-regulator`](../../../../build/dts/api/bindings/regulator/x-powers%2Caxp192-regulator.md#std-dtcompatible-x-powers-axp192-regulator) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L78) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L362) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif%2Cesp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| RTC | on-board | NXP PCF8563 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/m5stack/m5stack_core2/m5stack_core2_procpu.dts?plain=1#L124) | [`nxp,pcf8563`](../../../../build/dts/api/bindings/rtc/nxp%2Cpcf8563.md#std-dtcompatible-nxp-pcf8563) |
| SDHC | on-chip | ESP32 SDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L491) | [`espressif,esp32-sdhc`](../../../../build/dts/api/bindings/sdhc/espressif%2Cesp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc) |
| on-chip | ESP32 SDHC controller slot[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L500) | [`espressif,esp32-sdhc-slot`](../../../../build/dts/api/bindings/sdhc/espressif%2Cesp32-sdhc-slot.md#std-dtcompatible-espressif-esp32-sdhc-slot) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L256) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif%2Cesp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L229)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L238) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L397)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L386) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L138) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L368)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L377) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32/esp32_common.dtsi?plain=1#L65) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

## Start Application Development

Before powering up your M5Stack Core2, please make sure that the board is in good
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

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b m5stack_core2/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `m5stack_core2` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b m5stack_core2/esp32/procpu samples/hello_world
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
Hello World! m5stack_core2
```

#### Debugging

M5Stack Core2 debugging is not supported due to pinout limitations.

## Related Documents

- [M5Stack-Core2 schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/CORE2_V1.0_SCH.pdf) (PDF)
- [ESP32-PICO-D4 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf) (PDF)
- [M5Stack-Core2 docs](https://docs.m5stack.com/en/core/core2)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) (PDF)
- [ESP32 Hardware Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html)
