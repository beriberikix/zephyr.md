---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/pimoroni/pico_plus2/doc/index.html
original_path: boards/pimoroni/pico_plus2/doc/index.html
---

# Pimoroni Pico Plus2

Board Overview

[![../../../../_images/pico_plus2.webp](https://docs.zephyrproject.org/4.2.0/_images/pico_plus2.webp)
](https://docs.zephyrproject.org/4.2.0/_images/pico_plus2.webp)

Pimoroni Pico Plus2

Name:
:   `pico_plus2`

Vendor:
:   Pimoroni Ltd.

Architecture:
:   arm

SoC:
:   rp2350b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/pimoroni/pico_plus2/doc/index.rst/../..)

## Overview

The [Pimoroni Pico Plus 2](https://shop.pimoroni.com/products/pimoroni-pico-plus-2) [[1]](#id2) is a compact and versatile board featuring the Raspberry Pi RP2350B SoC.
It includes USB Type-C, Qwiic/STEMMA QT connectors, SP/CE connectors, a debug connector,
a reset button, and a BOOT button.

## Hardware

- Dual Cortex-M33 or Hazard3 processors at up to 150MHz
- 520KB of SRAM, and 4MB of on-board flash memory
- 16MB of on-board QSPI flash (supports XiP)
- 8MB of PSRAM
- USB 1.1 with device and host support
- Low-power sleep and dormant modes
- Drag-and-drop programming using mass storage over USB
- 48 multi-function GPIO pins including 8 that can be used for ADC
- 2 SPI, 2 I2C, 2 UART, 3 12-bit 500ksps Analogue to Digital - Converter (ADC), 24 controllable PWM channels
- 2 Timer with 4 alarms, 1 AON Timer
- Temperature sensor
- 3 Programmable IO (PIO) blocks, 12 state machines total for custom peripheral support
- USB-C connector for power, programming, and data transfer
- Qwiic/STEMMA QT(Qw/ST) connector
- SP/CE connector
- 3-pin debug connector, this can use with [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) [[2]](#id4).
- Reset button and BOOT button (BOOT button also usable as a user switch)

### Supported Features

The `pico_plus2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `pico_plus2/rp2350b/m33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L33) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Raspberry Pi Pico ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L338) | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi,pico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| Clock control | on-chip | The representation of Raspberry Pi Pico’s clock[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L43)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L170) | [`raspberrypi,pico-clock`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock.md#std-dtcompatible-raspberrypi-pico-clock) |
| on-chip | The representation of Raspberry Pi Pico’s PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L124) | [`raspberrypi,pico-pll`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-pll.md#std-dtcompatible-raspberrypi-pico-pll) |
| on-chip | The representation of Raspberry Pi Pico ring oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L146) | [`raspberrypi,pico-rosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc) |
| on-chip | The representation of Raspberry Pi Pico external oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L164) | [`raspberrypi,pico-xosc`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc) |
| on-chip | Raspberry Pi Pico clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L216) | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi,pico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| Counter | on-chip | Raspberry Pi Pico timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L362)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L378) | [`raspberrypi,pico-timer`](../../../../build/dts/api/bindings/counter/raspberrypi,pico-timer.md#std-dtcompatible-raspberrypi-pico-timer) |
| DMA | on-chip | Raspberry Pi Pico DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L401) | [`raspberrypi,pico-dma`](../../../../build/dts/api/bindings/dma/raspberrypi,pico-dma.md#std-dtcompatible-raspberrypi-pico-dma) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L193) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi,pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L238) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| on-chip | Raspberry Pi Pico GPIO Port[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L251) | [`raspberrypi,pico-gpio-port`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port) |
| on-board | GPIO pins exposed on Raspberry Pi Pico headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pimoroni/pico_plus2/pico_plus2.dtsi?plain=1#L59) | [`raspberrypi,pico-header`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-header.md#std-dtcompatible-raspberrypi-pico-header) |
| I2C | on-chip | Raspberry Pi Pico I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L314)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L326) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi,pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pimoroni/pico_plus2/pico_plus2.dtsi?plain=1#L50) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pimoroni/pico_plus2/pico_plus2.dtsi?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pimoroni/pico_plus2/pico_plus2.dtsi?plain=1#L40) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L427) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi,pico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L200) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pimoroni/pico_plus2/pico_plus2.dtsi?plain=1#L96) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Raspberry Pi Pico Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L452) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L349) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi,pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L208) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi,pico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| Sensors | on-chip | Raspberry Pi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L457) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrypi,pico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L270)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L280) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi,pico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L290)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L302) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi,pico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L188) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Raspberry Pi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L416) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi,pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L394) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi,pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

You can use peripherals that are made by using the PIO.
See [PIO Based Features](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-pio-based-features)

## Programming and Debugging

The `pico_plus2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[uf2](../../../../develop/flash_debug/host-tools.md#runner-uf2)** | ✅ |  |  |  |  |

The overall explanation regarding flashing and debugging is the same as or [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
See [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) in [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico) documentation. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b pico_plus2/rp2350b/m33 samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```

[[1](#id3)]

[https://shop.pimoroni.com/products/pimoroni-pico-plus-2](https://shop.pimoroni.com/products/pimoroni-pico-plus-2)

[[2](#id5)]

[https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html)
