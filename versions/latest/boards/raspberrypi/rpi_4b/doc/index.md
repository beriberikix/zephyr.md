---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/raspberrypi/rpi_4b/doc/index.html
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

#### `rpi_4b/bcm2711` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A72 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L18) | [`arm,cortex-a72`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| GPIO & Headers | on-chip | BCM2711 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L74)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L62) | [`brcm,bcm2711-gpio`](../../../../build/dts/api/bindings/gpio/brcm%2Cbcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L46) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v2.md#std-dtcompatible-arm-gic-v2) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Serial controller | on-chip | BCM2711 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L86) | [`brcm,bcm2711-aux-uart`](../../../../build/dts/api/bindings/serial/brcm%2Cbcm2711-aux-uart.md#std-dtcompatible-brcm-bcm2711-aux-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L27) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

## Programming and Debugging

The `rpi_4b` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

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
