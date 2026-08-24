---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/waveshare/rp2040_zero/doc/index.html
original_path: boards/waveshare/rp2040_zero/doc/index.html
---

# RP2040-Zero

Board Overview

[![../../../../_images/rp2040_zero.png](https://docs.zephyrproject.org/4.1.0/_images/rp2040_zero.png)
](https://docs.zephyrproject.org/4.1.0/_images/rp2040_zero.png)

RP2040-Zero

Name:
:   `rp2040_zero`

Vendor:
:   Waveshare Electronics

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/waveshare/rp2040_zero/doc/index.rst/../..)

## Overview

RP2040-Zero, A Low-Cost, High-Performance Pico-Like MCU Board Based On Raspberry Pi Microcontroller RP2040.

## Hardware

- RP2040 microcontroller chip designed by Raspberry Pi in the United Kingdom.
- Dual-core Arm Cortex M0+ processor, flexible clock running up to 133 MHz.
- 264KB of SRAM, and 2MB of on-board Flash memory.
- USB-C connector, keeps it up to date, easier to use.
- The castellated module allows soldering direct to carrier boards.
- USB 1.1 with device and host support.
- Low-power sleep and dormant modes.
- Drag-and-drop programming using mass storage over USB.
- 29 × multi-function GPIO pins (20× via edge pinout, others via solder points).
- 2 × SPI, 2 × I2C, 2 × UART, 4 × 12-bit ADC, 16 × controllable PWM channels.
- Accurate clock and timer on-chip.
- Temperature sensor.
- Accelerated floating-point libraries on-chip.
- 8 × Programmable I/O (PIO) state machines for custom peripheral support.

### Supported Features

The `rp2040_zero` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rp2040_zero/rp2040` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L35) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | RaspberryPi Pico ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L295) | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi,pico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| Clock control | on-chip | Raspberry Pi Pico clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L219) | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| on-chip | The representation of Raspberry Pi Pico’s clock[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L47)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L174) | [`raspberrypi,pico-clock`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock.md#std-dtcompatible-raspberrypi-pico-clock) |
| on-chip | The representation of Raspberry Pi Pico’s PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L128) | [`raspberrypi,pico-pll`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-pll.md#std-dtcompatible-raspberrypi-pico-pll) |
| on-chip | The representation of Raspberry Pi Pico ring oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L150) | [`raspberrypi,pico-rosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc) |
| on-chip | The representation of Raspberry Pi Pico external oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L168) | [`raspberrypi,pico-xosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc) |
| Counter | on-chip | RaspberryPi Pico timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L359) | [`raspberrypi,pico-timer`](../../../../build/dts/api/bindings/counter/raspberrypi,pico-timer.md#std-dtcompatible-raspberrypi-pico-timer) |
| DMA | on-chip | Raspberry Pi Pico DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L375) | [`raspberrypi,pico-dma`](../../../../build/dts/api/bindings/dma/raspberrypi,pico-dma.md#std-dtcompatible-raspberrypi-pico-dma) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi,pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L241) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| I2C | on-chip | Raspberry Pi Pico I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L306) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi,pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED strip | on-board | The pio node configured for ws2812[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_zero/rp2040_zero.dts?plain=1#L111) | [`worldsemi,ws2812-rpi_pico-pio`](../../../../build/dts/api/bindings/led_strip/worldsemi,ws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L396) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi,pico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L204) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/waveshare/rp2040_zero/rp2040_zero.dts?plain=1#L33) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The RPi Pico pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART0 Rx to pin 1 and enabling the pullup resistor on that pin[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L423) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L348) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi,pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Regulator | on-chip | RaspberryPi Pico core supply regurator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L388) | [`raspberrypi,core-supply-regulator`](../../../../build/dts/api/bindings/regulator/raspberrypi,core-supply-regulator.md#std-dtcompatible-raspberrypi-core-supply-regulator) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L211) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi,pico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| RTC | on-chip | RaspberryPi Pico RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L412) | [`raspberrypi,pico-rtc`](../../../../build/dts/api/bindings/rtc/raspberrypi,pico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc) |
| Sensors | on-chip | RaspberryPi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L427) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrrypi,pico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L251)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L261) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi,pico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L271)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L283) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi,pico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | RaspberryPi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L337) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi,pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L330) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi,pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board. The configuration of these routes can be modified through DTS. Please refer to the datasheet to see the possible routings for each peripheral.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P6
- I2C1\_SCL : P7
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28
- ADC\_CH3 : P29

## Programming and Debugging

### Flashing

#### Using UF2

Here is an example of building the sample for driving the built-in RGB led.

```shell
west build -b rp2040_zero samples/drivers/led/led_strip
```

You must flash the RP2040-Zero with an UF2 file. One option is to use West (Zephyr’s meta-tool). To enter the UF2 flashing mode just keep the `BOOT` button pressed while you connect the USB port, it will appear on the host as a mass storage device. In alternative with the board already connected via USB you can keep the `RESET` button pressed, press and release `BOOT`, release `RESET`. At this point you can flash the image file by running:

```shell
west flash
```

In alternative you can locate the generated file at `build/zephyr/zephyr.uf2 file` and simply drag-and-drop to the device after entreing the UF2 flashing mode.

## References

- [Official Documentation](https://www.waveshare.com/wiki/RP2040-Zero)
- [WS2812 datasheet](https://cdn-shop.adafruit.com/datasheets/WS2812.pdf)
