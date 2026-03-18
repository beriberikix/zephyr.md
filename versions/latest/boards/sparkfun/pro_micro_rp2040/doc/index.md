---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/sparkfun/pro_micro_rp2040/doc/index.html
original_path: boards/sparkfun/pro_micro_rp2040/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SparkFun Pro Micro RP2040

## Overview

The SparkFun Pro Micro RP2040 is a small, low-cost, versatile board from
SparkFun. It is equipped with an RP2040 SoC, an on-board WS2812 addressable
LED, a USB connector, and a Qwiic connector. The USB bootloader allows it
to be flashed without any adapter, in a drag-and-drop manner.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
- 18 GPIO pins
- 4 Analog inputs
- 1 UART peripherals
- 1 SPI controllers
- 2 I2C controllers (one via Qwiic connector)
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board RGB LED
- 1 Watchdog timer peripheral

![SparkFun Pro Micro RP2040](../../../../_images/sparkfun_pro_micro_rp2040.jpg)

SparkFun Pro Micro RP2040 (Image courtesy of SparkFun)

### Supported Features

The sparkfun\_pro\_micro\_rp2040 board configuration supports the following
hardware features:

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
| Flash | [`CONFIG_FLASH`](../../../../kconfig.md#CONFIG_FLASH "CONFIG_FLASH") | `raspberrypi,pico-flash` |
| Clock controller | [`CONFIG_CLOCK_CONTROL`](../../../../kconfig.md#CONFIG_CLOCK_CONTROL "CONFIG_CLOCK_CONTROL") | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| UART (PIO) | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`raspberrypi,pico-uart-pio`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart-pio.md#std-dtcompatible-raspberrypi-pico-uart-pio) |

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C1\_SDA : P2
- I2C1\_SCL : P3
- SPI0\_RX : P20
- SPI0\_SCK : P18
- SPI0\_TX : P19

## Programming and Debugging

### Flashing

#### Using UF2

The Pro Micro board does make the SWD pins available on pads on the
underside of the board. You can solder to these pins, and use a JTag
debugger. You can also flash the SparkFun ProMicro RP2040 with a UF2 file.
By default, building an app for this board will generate a
build/zephyr/zephyr.uf2 file. If the Pro Micro RP2040 is powered on with
the BOOTSEL button pressed, it will appear on the host as a mass storage
device. The UF2 file should be copied to the device, which will
flash the Pro Micro RP2040.
