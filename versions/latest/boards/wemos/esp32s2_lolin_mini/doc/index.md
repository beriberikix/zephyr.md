---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wemos/esp32s2_lolin_mini/doc/index.html
original_path: boards/wemos/esp32s2_lolin_mini/doc/index.html
---

# ESP32-S2 Lolin Mini

Board Overview

[![../../../../_images/esp32_s2_lolin_mini.jpg](../../../../_images/esp32_s2_lolin_mini.jpg)
](../../../../_images/esp32_s2_lolin_mini.jpg)

ESP32-S2 Lolin Mini

Name:
:   `esp32s2_lolin_mini`

Vendor:
:   WEMOS Electronics

Architecture:
:   xtensa

SoC:
:   esp32s2

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wemos/esp32s2_lolin_mini/doc/index.rst/../..)

## Overview

ESP32-S2 is a highly integrated, low-power, single-core Wi-Fi Microcontroller SoC, designed to be secure and
cost-effective, with a high performance and a rich set of IO capabilities. [[1]](#id2)

The features include the following:

- RSA-3072-based secure boot
- AES-XTS-256-based flash encryption
- Protected private key and device secrets from software access
- Cryptographic accelerators for enhanced performance
- Protection against physical fault injection attacks
- Various peripherals:

  - 43x programmable GPIOs
  - 14x configurable capacitive touch GPIOs
  - USB OTG
  - LCD interface
  - camera interface
  - SPI
  - I2S
  - UART
  - ADC
  - DAC
  - LED PWM with up to 8 channels

## Hardware

### Supported Features

The `esp32s2_lolin_mini` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `esp32s2_lolin_mini/esp32s2` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif Xtensa LX7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L34) | [`espressif,xtensa-lx7`](../../../../build/dts/api/bindings/cpu/espressif%2Cxtensa-lx7.md#std-dtcompatible-espressif-xtensa-lx7) |
| ADC | on-chip | ESP32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L397) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L66) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif%2Cesp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L417) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L76) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif%2Cesp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 general-purpose timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L272) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L282) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DAC | on-chip | ESP32 Digital to Analog converter (DAC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L381) | [`espressif,esp32-dac`](../../../../build/dts/api/bindings/dac/espressif%2Cesp32-dac.md#std-dtcompatible-espressif-esp32-dac) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L151) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif%2Cesp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L203) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif%2Cesp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L236) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L258) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif%2Cesp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-chip | ESP32 touch sensor input[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L228) | [`espressif,esp32-touch`](../../../../build/dts/api/bindings/input/espressif%2Cesp32-touch-sensor.md#std-dtcompatible-espressif-esp32-touch) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wemos/esp32s2_lolin_mini/esp32s2_lolin_mini.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L124) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wemos/esp32s2_lolin_mini/esp32s2_lolin_mini.dts?plain=1#L32) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | ESP32 pseudo-static RAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L112) | [`espressif,esp32-psram`](../../../../build/dts/api/bindings/memory-controllers/espressif%2Cesp32-psram.md#std-dtcompatible-espressif-esp32-psram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L158) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x1000_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L71) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L194) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L335) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif%2Cesp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Sensors | on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L185) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif%2Cesp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L390) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif%2Cesp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L166)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L175) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L341) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L133) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L363)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L372) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/espressif/esp32s2/esp32s2_common.dtsi?plain=1#L61) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

## System requirements

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

### Building & Flashing

The `esp32s2_lolin_mini` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **esp32** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b esp32s2_lolin_mini samples/hello_world
```

The usual `flash` target will work with the `esp32s2_lolin_mini` board
configuration after putting the board into bootloader mode by holding the ‘0’
button then pressing ‘RST’ and releasing the ‘RST’ button.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32s2_lolin_mini samples/hello_world
west flash
```

Open a serial port using e.g. screen

```shell
screen /dev/ttyUSB0 115200
```

After the board has been manually reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! esp32s2_lolin_mini
```

## References

[[1](#id1)]

[https://www.espressif.com/en/products/socs/esp32-s2](https://www.espressif.com/en/products/socs/esp32-s2)
