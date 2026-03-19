---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/raspberrypi/rpi_4b/doc/index.html
original_path: boards/raspberrypi/rpi_4b/doc/index.html
---

# Raspberry Pi 4 Model B (Cortex-A72)

Board Overview

Name:
:   `rpi_4b`

Vendor:
:   Raspberry Pi Foundation

Architecture:
:   arm64

SoC:
:   bcm2711

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_4b/doc/index.rst/../..)

## Overview

see <[https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)>

## Hardware

see <[https://www.raspberrypi.com/documentation/computers/raspberry-pi.html](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)>

### Supported Features

The `rpi_4b` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

### TF Card

Prepare a TF card with MBR and FAT32. In the root directory of the TF card:

1. Download and place these firmware files:

   - [bcm2711-rpi-4-b.dtb](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bcm2711-rpi-4-b.dtb)
   - [bootcode.bin](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bootcode.bin)
   - [start4.elf](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/start4.elf)
2. Copy `build/zephyr/zephyr.bin`
3. Create a `config.txt`:

   ```text
   kernel=zephyr.bin
   arm_64bit=1
   enable_uart=1
   uart_2ndstage=1
   ```

Insert the card and power on the board. You should see the following output on
the serial console (GPIO 14/15):

```text
*** Booting Zephyr OS build XXXXXXXXXXXX  ***
Hello World! Raspberry Pi 4 Model B!
```
