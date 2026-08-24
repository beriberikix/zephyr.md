---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/waveshare/rp2040_plus/doc/index.html
original_path: boards/waveshare/rp2040_plus/doc/index.html
---

# RP2040-Plus

Board Overview

[![../../../../_images/rp2040_plus.webp](https://docs.zephyrproject.org/4.2.0/_images/rp2040_plus.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rp2040_plus.webp)

RP2040-Plus

Name:
:   `rp2040_plus`

Vendor:
:   Waveshare Electronics

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/waveshare/rp2040_plus/doc/index.rst/../..)

## Overview

RP2040-Plus, a low-cost, high-performance Pico-like MCU board based on Raspberry Pi microcontroller RP2040
including a battery charger.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 4MB/16MB on-board QSPI flash with XIP capabilities
- 26 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 SPI controllers
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- on-board battery charger

### Supported Features

The `rp2040_plus` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rp2040_plus/rp2040` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L35) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Raspberry Pi Pico ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L308) | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi,pico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| Clock control | on-chip | Raspberry Pi Pico clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L219) | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| on-chip | The representation of Raspberry Pi Pico’s clock[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L47)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L174) | [`raspberrypi,pico-clock`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock.md#std-dtcompatible-raspberrypi-pico-clock) |
| on-chip | The representation of Raspberry Pi Pico’s PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L128) | [`raspberrypi,pico-pll`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-pll.md#std-dtcompatible-raspberrypi-pico-pll) |
| on-chip | The representation of Raspberry Pi Pico ring oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L150) | [`raspberrypi,pico-rosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc) |
| on-chip | The representation of Raspberry Pi Pico external oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L168) | [`raspberrypi,pico-xosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc) |
| Counter | on-chip | Raspberry Pi Pico timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L372) | [`raspberrypi,pico-timer`](../../../../build/dts/api/bindings/counter/raspberrypi,pico-timer.md#std-dtcompatible-raspberrypi-pico-timer) |
| DMA | on-chip | Raspberry Pi Pico DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L388) | [`raspberrypi,pico-dma`](../../../../build/dts/api/bindings/dma/raspberrypi,pico-dma.md#std-dtcompatible-raspberrypi-pico-dma) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi,pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L241) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| on-chip | Raspberry Pi Pico GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L254) | [`raspberrypi,pico-gpio-port`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port) |
| on-board | GPIO pins exposed on Raspberry Pi Pico headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_plus/rp2040_plus.dts?plain=1#L30) | [`raspberrypi,pico-header`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-header.md#std-dtcompatible-raspberrypi-pico-header) |
| I2C | on-chip | Raspberry Pi Pico I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L319)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L331) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi,pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_plus/rp2040_plus.dts?plain=1#L80) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_plus/rp2040_plus.dts?plain=1#L63) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_plus/rp2040_plus.dts?plain=1#L71) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L409) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi,pico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L204) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_plus/rp2040_plus.dts?plain=1#L91) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Raspberry Pi Pico Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L436) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L361) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi,pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Regulator | on-chip | Raspberry Pi Pico core supply regurator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L401) | [`raspberrypi,core-supply-regulator`](../../../../build/dts/api/bindings/regulator/raspberrypi,core-supply-regulator.md#std-dtcompatible-raspberrypi-core-supply-regulator) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L211) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi,pico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| RTC | on-chip | Raspberry Pi Pico RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L425) | [`raspberrypi,pico-rtc`](../../../../build/dts/api/bindings/rtc/raspberrypi,pico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc) |
| Sensors | on-chip | Raspberry Pi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L440) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrypi,pico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L264)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L274) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi,pico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L284)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L296) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi,pico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Raspberry Pi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L350) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi,pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L343) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi,pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

![Waveshare RP2040-Plus pinout overview](https://docs.zephyrproject.org/4.2.0/_images/rp2040_plus-details.webp)

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P6
- I2C1\_SCL : P7
- SPI0\_RX : P16
- SPI0\_CSN : P17
- SPI0\_SCK : P18
- SPI0\_TX : P19
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28

## Programming and Debugging

The `rp2040_plus` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **[uf2](../../../../develop/flash_debug/host-tools.md#runner-uf2)** | ✅ (default) |  |

### Flashing

#### Using UF2

Here is an example of building the sample for driving the built-in led.

```shell
west build -b rp2040_plus samples/basic/blinky
```

You must flash the RP2040-Plus with an UF2 file. One option is to use West (Zephyr’s meta-tool). To enter the UF2 flashing mode just keep the `BOOT` button pressed while you connect the USB port, it will appear on the host as a mass storage device. In alternative with the board already connected via USB you can keep the `RESET` button pressed, press and release `BOOT`, release `RESET`. At this point you can flash the image file by running:

```shell
west flash
```

Alternatively, you can locate the generated `build/zephyr/zephyr.uf2` file and simply drag-and-drop to the device after entering the UF2 flashing mode.

## References

- [Official Documentation](https://www.waveshare.com/wiki/RP2040-Plus)
