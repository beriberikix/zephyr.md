---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/01space/esp32c3_042_oled/doc/index.html
original_path: boards/01space/esp32c3_042_oled/doc/index.html
---

# ESP32C3 0.42 OLED

Board Overview

[![../../../../_images/esp32c3_042_oled.webp](https://docs.zephyrproject.org/4.1.0/_images/esp32c3_042_oled.webp)
](https://docs.zephyrproject.org/4.1.0/_images/esp32c3_042_oled.webp)

ESP32C3 0.42 OLED

Name:
:   `esp32c3_042_oled`

Vendor:
:   01Space

Architecture:
:   riscv

SoC:
:   esp32c3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/01space/esp32c3_042_oled/doc/index.rst/../..)

## Overview

ESP32C3 0.42 OLED is a mini development board based on the [Espressif ESP32-C3](https://www.espressif.com/en/products/socs/esp32-c3) [[1]](#id3)
RISC-V WiFi/Bluetooth dual-mode chip.

For more details see the [01space ESP32C3 0.42 OLED](https://github.com/01Space/ESP32-C3-0.42LCD) [[2]](#id5) Github repo.

## Hardware

This board is based on the ESP32-C3-FH4 with WiFi and BLE support.
It features:

- RISC-V SoC @ 160MHz with 4MB flash and 400kB RAM
- WS2812B RGB serial LED
- 0.42-inch OLED over I2C
- Qwiic I2C connector
- One pushbutton
- Onboard ceramic chip antenna
- On-chip USB-UART converter

Note

The RGB led is not supported on this Zephyr board yet.

Note

The ESP32-C3 does not have native USB, it has an on-chip USB-serial converter
instead.

### Supported Features

The `esp32c3_042_oled` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `esp32c3_042_oled/esp32c3` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L34) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif,riscv.md#std-dtcompatible-espressif-riscv) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L304) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L72) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L259) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L112) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L130) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L231) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| Display | on-board | SSD1306 128x64 dot-matrix display controller on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/01space/esp32c3_042_oled/esp32c3_042_oled.dts?plain=1#L50) | [`solomon,ssd1306fb`](../../../../build/dts/api/compatibles/solomon,ssd1306fb.md#std-dtcompatible-solomon-ssd1306fb) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L314) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L139) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L154) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L169) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L180) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L95) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L146) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x0_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L62) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L213) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L253) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L297) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L203)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L194) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L222) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L268) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Timer | on-chip | ESP32 System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L104) | [`espressif,esp32-systimer`](../../../../build/dts/api/bindings/timer/espressif,esp32-systimer.md#std-dtcompatible-espressif-esp32-systimer) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L121) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L279)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L288) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L67) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

### Connections and IOs

See the following image:

![01space ESP32C3 0.42 OLED Pinout](https://docs.zephyrproject.org/4.1.0/_images/esp32c3_042_oled_pinout.webp)

01space ESP32C3 0.42 OLED Pinout

It also features a 0.42 inch OLED display, driven by a SSD1306-compatible chip.
It is connected over I2C: SDA on GPIO5, SCL on GPIO6.

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs. Run the command below to
retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Programming and Debugging

### Standalone application

The board can be loaded using a single binary image, without 2nd stage bootloader.
It is the default option when building the application without additional configuration.

Note

This mode does not provide any security features nor OTA updates.

Use the following command to build a sample hello\_world application:

```shell
# From the root of the zephyr repository
west build -b esp32c3_042_oled samples/hello_world
```

### Sysbuild

[Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild) makes it possible to build and flash all necessary images needed to
bootstrap the board.

By default, the ESP32 sysbuild configuration creates bootloader (MCUboot) and
application images.

To build the sample application using sysbuild, use this command:

```shell
west build -b esp32c3_042_oled --sysbuild samples/hello_world
```

### Flashing

For the `Hello, world!` application, follow the instructions below.
Assuming the board is connected to `/dev/ttyACM0` on Linux.

```shell
# From the root of the zephyr repository
west build -b esp32c3_042_oled samples/hello_world
west flash --esp-device /dev/ttyACM0
```

Since the Zephyr console is by default on the `usb_serial` device, we use
the espressif monitor utility to connect to the console.

```shell
$ west espressif monitor -p /dev/ttyACM0
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! esp32c3_042_oled
```

## References

[[1](#id4)]

[https://www.espressif.com/en/products/socs/esp32-c3](https://www.espressif.com/en/products/socs/esp32-c3)

[[2](#id6)]

[https://github.com/01Space/ESP32-C3-0.42LCD](https://github.com/01Space/ESP32-C3-0.42LCD)
