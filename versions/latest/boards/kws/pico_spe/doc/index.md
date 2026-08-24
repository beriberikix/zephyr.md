---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/kws/pico_spe/doc/index.html
original_path: boards/kws/pico_spe/doc/index.html
---

# Pico-SPE

Board Overview

[![../../../../_images/pico_spe.webp](https://docs.zephyrproject.org/4.2.0/_images/pico_spe.webp)
](https://docs.zephyrproject.org/4.2.0/_images/pico_spe.webp)

Pico-SPE

Name:
:   `pico_spe`

Vendor:
:   KWS Computersysteme Gmbh

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/kws/pico_spe/doc/index.rst/../..)

## Overview

The Pico-SPE is a small, low-cost, versatile boards from
KWS Computersysteme Gmbh. They are equipped with an RP2040 SoC, an on-board LED,
a USB connector, an SWD interface. The Pico-SPE additionally contains an
Microchip LAN8651 10Base-T1S module. The USB bootloader allows the
ability to flash without any adapter, in a drag-and-drop manner.
It is also possible to flash and debug the boards with their SWD interface,
using an external adapter.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
- 16 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- Microchip LAN8651 10Base-T1S

### Supported Features

The `pico_spe` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `pico_spe/rp2040` target

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
| Ethernet | on-board | LAN865x standalone 10BASE-T1L Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L146) | [`microchip,lan865x`](../../../../build/dts/api/bindings/ethernet/microchip,lan865x.md#std-dtcompatible-microchip-lan865x) |
| on-board | Microchip’s 10BASE-T1S PHYs support[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L160) | [`microchip,t1s-phy`](../../../../build/dts/api/bindings/ethernet/phy/microchip,t1s-phy.md#std-dtcompatible-microchip-t1s-phy) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi,pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L241) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| on-chip | Raspberry Pi Pico GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L254) | [`raspberrypi,pico-gpio-port`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port) |
| on-board | GPIO pins exposed on Raspberry Pi Pico headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L53) | [`raspberrypi,pico-header`](../../../../build/dts/api/bindings/gpio/raspberrypi,pico-header.md#std-dtcompatible-raspberrypi-pico-header) |
| I2C | on-chip | Raspberry Pi Pico I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L319)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L331) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi,pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L36) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L409) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi,pico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L204) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/kws/pico_spe/pico_spe.dts?plain=1#L90) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Raspberry Pi Pico Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L436) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L361) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi,pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Regulator | on-chip | Raspberry Pi Pico core supply regurator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L401) | [`raspberrypi,core-supply-regulator`](../../../../build/dts/api/bindings/regulator/raspberrypi,core-supply-regulator.md#std-dtcompatible-raspberrypi-core-supply-regulator) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L211) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi,pico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| RTC | on-chip | Raspberry Pi Pico RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L425) | [`raspberrypi,pico-rtc`](../../../../build/dts/api/bindings/rtc/raspberrypi,pico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc) |
| Sensors | on-chip | Raspberry Pi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L440) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrypi,pico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L264)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L274) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi,pico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L296)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L284) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi,pico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Raspberry Pi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L350) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi,pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L343) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi,pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

External pin mapping on the Pico-SPE is identical to the Pico, but note that internal
RP2040 GPIO lines 10, 11, 12, 13, 20, 21 are routed to the Microchip LAN8651 on the
Pico-SPE.

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

## Programmable I/O (PIO)

The RP2040 SoC comes with two PIO periherals. These are two simple
co-processors that are designed for I/O operations. The PIOs run
a custom instruction set, generated from a custom assembly language.
PIO programs are assembled using **pioasm**, a tool provided by Raspberry Pi.

Zephyr does not (currently) assemble PIO programs. Rather, they should be
manually assembled and embedded in source code. An example of how this is done
can be found at [drivers/serial/uart\_rpi\_pico\_pio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_rpi_pico_pio.c).

### Sample: SPI via PIO

The [BME280 humidity and pressure sensor](../../../../samples/sensor/bme280/README.md#bme280 "Get temperature, pressure, and humidity data from a BME280 sensor.") sample includes a
demonstration of using the PIO SPI driver to communicate with an
environmental sensor. The PIO SPI driver supports using any
combination of GPIO pins for an SPI bus, as well as allowing up to
four independent SPI buses on a single board (using the two SPI
devices as well as both PIO devices).

## Programming and Debugging

The `pico_spe` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[blackmagicprobe](../../../../develop/flash_debug/host-tools.md#runner-blackmagicprobe)** | ✅ | ✅ | ✅ |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[uf2](../../../../develop/flash_debug/host-tools.md#runner-uf2)** | ✅ |  |  |  |  |

The SWD interface can be used to program and debug the device,
e.g. using OpenOCD with the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) .

The overall explanation regarding flashing and debugging is the same as for [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
Refer to [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) for more information. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b pico_spe samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```
