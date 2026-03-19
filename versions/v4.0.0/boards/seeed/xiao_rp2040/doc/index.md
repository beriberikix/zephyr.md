---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/seeed/xiao_rp2040/doc/index.html
original_path: boards/seeed/xiao_rp2040/doc/index.html
---

# XIAO RP2040

Board Overview

[![../../../../_images/xiao_rp2040.webp](../../../../_images/xiao_rp2040.webp)
](../../../../_images/xiao_rp2040.webp)

XIAO RP2040

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   rp2040

## Overview

The XIAO RP2040 is an IoT mini development board from Seeed Studio.
It is equipped with an RP2040 SoC, an on-board WS2812 addressable
LED, and USB connector. The USB bootloader allows it
to be flashed without any adapter, in a drag-and-drop manner.

For more details see the [Seeed Studio XIAO RP2040](https://wiki.seeedstudio.com/XIAO-RP2040/) [[1]](#id3) wiki page.

## Hardware

The Seeed Studio XIAO RP2040 is a low-power microcontroller that
carries the powerful Dual-core RP2040 processor with a flexible
clock running up to 133 MHz. There is also 264KB of SRAM, and 2MB of
on-board Flash memory.

There are 14 GPIO PINs on Seeed Studio XIAO RP2040, on which there
are 11 digital pins, 4 analog pins, 11 PWM Pins,1 I2C interface,
1 UART interface, 1 SPI interface, 1 SWD Bonding pad interface.

### Supported Features

The `xiao_rp2040` board target supports the following hardware
features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| NVIC | N/A | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| UART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| GPIO | [`CONFIG_GPIO`](../../../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi%2Cpico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| ADC | [`CONFIG_ADC`](../../../../kconfig.md#CONFIG_ADC "CONFIG_ADC") | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi%2Cpico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| I2C | [`CONFIG_I2C`](../../../../kconfig.md#CONFIG_I2C "CONFIG_I2C") | [`snps,designware-i2c`](../../../../build/dts/api/bindings/i2c/snps%2Cdesignware-i2c.md#std-dtcompatible-snps-designware-i2c) |
| SPI | [`CONFIG_SPI`](../../../../kconfig.md#CONFIG_SPI "CONFIG_SPI") | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| USB Device | [`CONFIG_USB_DEVICE_STACK`](../../../../kconfig.md#CONFIG_USB_DEVICE_STACK "CONFIG_USB_DEVICE_STACK") | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi%2Cpico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| HWINFO | [`CONFIG_HWINFO`](../../../../kconfig.md#CONFIG_HWINFO "CONFIG_HWINFO") | N/A |
| Watchdog Timer (WDT) | [`CONFIG_WATCHDOG`](../../../../kconfig.md#CONFIG_WATCHDOG "CONFIG_WATCHDOG") | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi%2Cpico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |
| PWM | [`CONFIG_PWM`](../../../../kconfig.md#CONFIG_PWM "CONFIG_PWM") | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi%2Cpico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Flash | [`CONFIG_FLASH`](../../../../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi%2Cpico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| Clock controller | [`CONFIG_CLOCK_CONTROL`](../../../../kconfig.md#CONFIG_CLOCK_CONTROL "CONFIG_CLOCK_CONTROL") | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| UART (PIO) | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`raspberrypi,pico-uart-pio`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart-pio.md#std-dtcompatible-raspberrypi-pico-uart-pio) |

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C1\_SDA : P6
- I2C1\_SCL : P7
- SPI0\_RX : P4
- SPI0\_SCK : P2
- SPI0\_TX : P3

### Connections and IOs

The board uses a standard XIAO pinout, the default pin mapping is the following:

![XIAO RP2040 Pinout](../../../../_images/xiao_rp2040_pinout.webp)

XIAO RP2040 Pinout

## Programming and Debugging

### Flashing

#### Using UF2

You can flash the Xiao RP2040 with a UF2 file.
By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the Xiao RP2040 is powered on with
the `BOOTSEL` button pressed, it will appear on the host as a mass storage
device. The UF2 file should be copied to the device, which will
flash the Xiao RP2040.

## References

[[1](#id4)]

[https://wiki.seeedstudio.com/XIAO-RP2040/](https://wiki.seeedstudio.com/XIAO-RP2040/)
