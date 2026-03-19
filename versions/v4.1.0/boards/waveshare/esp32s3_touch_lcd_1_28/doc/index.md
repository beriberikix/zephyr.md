---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/waveshare/esp32s3_touch_lcd_1_28/doc/index.html
original_path: boards/waveshare/esp32s3_touch_lcd_1_28/doc/index.html
---

# ESP32-S3-Touch-LCD-1.28

Board Overview

[![../../../../_images/esp32s3_touch_lcd_1_28.webp](../../../../_images/esp32s3_touch_lcd_1_28.webp)
](../../../../_images/esp32s3_touch_lcd_1_28.webp)

ESP32-S3-Touch-LCD-1.28

Name:
:   `esp32s3_touch_lcd_1_28`

Vendor:
:   Waveshare Electronics

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/waveshare/esp32s3_touch_lcd_1_28/doc/index.rst/../..)

## Overview

The ESP32-S3-Touch-LCD-1.28 is an ESP32S3 development board from Waveshare with a round LCD,
suitable to build watches or similar projects. This board integrates complete Wi-Fi and Bluetooth
Low Energy functions, an accelerometer and gyroscope, a battery charger and GPIO extension port.

## Hardware

ESP32-S3 is a low-power MCU-based system on a chip (SoC) with integrated 2.4 GHz Wi-Fi
and Bluetooth® Low Energy (Bluetooth LE). It consists of high-performance dual-core microprocessor
(Xtensa® 32-bit LX7), a low power coprocessor, a Wi-Fi baseband, a Bluetooth LE baseband,
RF module, and numerous peripherals.

ESP32-S3-Touch-LCD-1.28 includes the following features:

- Dual core 32-bit Xtensa Microprocessor (Tensilica LX7), running up to 240MHz
- Additional vector instructions support for AI acceleration
- 2MB of SRAM
- 16MB of FLASH
- Wi-Fi 802.11b/g/n
- Bluetooth LE 5.0 with long-range support and up to 2Mbps data rate
- Round 1.28” LCD with touchscreen controller
- Accelerometer/gyroscope
- Battery charger

Digital interfaces:

- 6 programmable GPIOs
- 2 open-drain outputs

Low Power:

- Power Management Unit with five power modes
- Ultra-Low-Power (ULP) coprocessors: ULP-RISC-V and ULP-FSM

Security:

- Secure boot
- Flash encryption
- 4-Kbit OTP, up to 1792 bits for users
- Cryptographic hardware acceleration: (AES-128/256, Hash, RSA, RNG, HMAC, Digital signature)

## Asymmetric Multiprocessing (AMP)

ESP32-S3 allows 2 different applications to be executed in ESP32-S3 SoC. Due to its dual-core
architecture, each core can be enabled to execute customized tasks in stand-alone mode
and/or exchanging data over OpenAMP framework. See [Inter-Processor Communication (IPC)](../../../../samples/subsys/ipc/ipc.md#ipc) folder as code reference.

For more information, check the datasheet at [ESP32-S3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf) [[1]](#id2) or the technical reference
manual at [ESP32-S3 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf) [[2]](#id4).

### Supported Features

The `esp32s3_touch_lcd_1_28` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

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

## References

[[1](#id3)]

[https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1\_mini-1u\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf)

[[2](#id5)]

[https://www.espressif.com/sites/default/files/documentation/esp32-s3\_technical\_reference\_manual\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)
