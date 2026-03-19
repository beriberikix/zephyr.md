---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/raspberrypi/rpi_4b/doc/index.html
original_path: boards/raspberrypi/rpi_4b/doc/index.html
---

# Raspberry Pi 4 Model B (Cortex-A72)

Board Overview

Vendor:
:   Raspberry Pi Foundation

Architecture:
:   arm64

SoC:
:   bcm2711

## Overview

see <[https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)>

## Hardware

see <[https://www.raspberrypi.com/documentation/computers/raspberry-pi.html](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)>

### Supported Features

The Raspberry Pi 4 Model B board configuration supports the following
hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| GIC-400 | N/A | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`brcm,bcm2711-gpio`](../../../../build/dts/api/bindings/gpio/brcm%2Cbcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio) |
| UART (Mini UART) | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`brcm,bcm2711-aux-uart`](../../../../build/dts/api/bindings/serial/brcm%2Cbcm2711-aux-uart.md#std-dtcompatible-brcm-bcm2711-aux-uart) |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in
[boards/raspberrypi/rpi\_4b/rpi\_4b\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b_defconfig)

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
