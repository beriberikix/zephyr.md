---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/sipeed/longan_nano/doc/index.html
original_path: boards/sipeed/longan_nano/doc/index.html
---

# Longan Nano

Board Overview

[![../../../../_images/longan_nano.jpg](../../../../_images/longan_nano.jpg)
](../../../../_images/longan_nano.jpg)

Longan Nano

Name:
:   `longan_nano`

Vendor:
:   Shenzhen Sipeed Technology Co., Ltd.

Architecture:
:   riscv

SoC:
:   gd32vf103

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sipeed/longan_nano/doc/index.rst/../..)

## Overview

The Sipeed Longan Nano and Longan Nano Lite is an simple and tiny development board with
an GigaDevice GD32VF103 SoC that based on N200 RISC-V IP core by Nuclei system technology.
More information can be found on:

- [Sipeed Longan website](https://longan.sipeed.com/en/)
- [GD32VF103 datasheet](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103 user manual](https://www.gd32mcu.com/data/documents/userManual/GD32VF103_User_Manual_Rev1.4.pdf)
- [Nuclei website](https://www.nucleisys.com/download.php)
- [Nuclei Bumblebee core documents](https://github.com/nucleisys/Bumblebee_Core_Doc)
- [Nuclei ISA Spec](https://doc.nucleisys.com/nuclei_spec/)

## Hardware

- 4 x universal 16-bit timer
- 2 x basic 16-bit timer
- 1 x advanced 16-bit timer
- Watchdog timer
- RTC
- Systick
- 3 x USART
- 2 x I2C
- 3 x SPI
- 2 x I2S
- 2 x CAN
- 1 x USBFS(OTG)
- 2 x ADC(10 channel)
- 2 x DAC

### Supported Features

The `longan_nano` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

The microSD card reader in Longan Nano board is connected to SPI1.

### Serial Port

USART0 is on the opposite end of the USB.
Connect to TX0 (PA9) and RX0 (PA10).

## Programming and debugging

### Building & Flashing

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west flash
```

When using a custom toolchain it should be enough to have the downloaded
version of the binary in your `PATH`.

The default runner tries to flash the board via an external programmer using openocd.
To flash via the USB port, select the DFU runner when flashing:

```shell
west flash --runner dfu-util
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b longan_nano samples/basic/blinky
west debug
```
