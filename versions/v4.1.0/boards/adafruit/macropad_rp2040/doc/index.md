---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/macropad_rp2040/doc/index.html
original_path: boards/adafruit/macropad_rp2040/doc/index.html
---

# Adafruit MacroPad RP2040

Board Overview

[![../../../../_images/adafruit_macropad_rp2040.webp](../../../../_images/adafruit_macropad_rp2040.webp)
](../../../../_images/adafruit_macropad_rp2040.webp)

Adafruit MacroPad RP2040

Name:
:   `adafruit_macropad_rp2040`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/macropad_rp2040/doc/index.rst/../..)

## Adafruit MacroPad RP2040

### Overview

The Adafruit MacroPad RP2040 is a 3x4 mechanical keyboard development board featuring
the Raspberry Pi RP2040 microcontroller. It includes 12 mechanical key switches with
individual RGB NeoPixels, a rotary encoder with push button, a 128x64 OLED display,
and a small speaker for audio feedback.

### Hardware

- Dual core Cortex-M0+ at up to 133MHz
- 264KB of SRAM
- 8MB of QSPI flash memory
- 12 mechanical key switches (Cherry MX compatible)
- 12 RGB NeoPixel LEDs (one per key)
- 128x64 monochrome OLED display (SH1106)
- Rotary encoder with push button
- Small speaker with Class D amplifier
- STEMMA QT / Qwiic I2C connector
- USB Type-C connector
- Reset button
- 4x M3 mounting holes

### Supported Features

The `adafruit_macropad_rp2040` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `adafruit_macropad_rp2040/rp2040` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L35) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | RaspberryPi Pico ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L295) | [`raspberrypi,pico-adc`](../../../../build/dts/api/bindings/adc/raspberrypi%2Cpico-adc.md#std-dtcompatible-raspberrypi-pico-adc) |
| Clock control | on-chip | Raspberry Pi Pico clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L219) | [`raspberrypi,pico-clock-controller`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller) |
| on-chip | The representation of Raspberry Pi Pico’s clock[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L47)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L174) | [`raspberrypi,pico-clock`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-clock.md#std-dtcompatible-raspberrypi-pico-clock) |
| on-chip | The representation of Raspberry Pi Pico’s PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L128) | [`raspberrypi,pico-pll`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-pll.md#std-dtcompatible-raspberrypi-pico-pll) |
| on-chip | The representation of Raspberry Pi Pico ring oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L150) | [`raspberrypi,pico-rosc`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc) |
| on-chip | The representation of Raspberry Pi Pico external oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L168) | [`raspberrypi,pico-xosc`](../../../../build/dts/api/bindings/clock/raspberrypi%2Cpico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc) |
| Counter | on-chip | RaspberryPi Pico timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L359) | [`raspberrypi,pico-timer`](../../../../build/dts/api/bindings/counter/raspberrypi%2Cpico-timer.md#std-dtcompatible-raspberrypi-pico-timer) |
| Display | on-board | SH1106 128x64 dot-matrix display controller on SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L180) | [`sinowealth,sh1106`](../../../../build/dts/api/compatibles/sinowealth%2Csh1106.md#std-dtcompatible-sinowealth-sh1106) |
| DMA | on-chip | Raspberry Pi Pico DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L375) | [`raspberrypi,pico-dma`](../../../../build/dts/api/bindings/dma/raspberrypi%2Cpico-dma.md#std-dtcompatible-raspberrypi-pico-dma) |
| Flash controller | on-chip | Raspberry Pi Pico flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197) | [`raspberrypi,pico-flash-controller`](../../../../build/dts/api/bindings/flash_controller/raspberrypi%2Cpico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller) |
| GPIO & Headers | on-chip | Raspberry Pi Pico GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L241) | [`raspberrypi,pico-gpio`](../../../../build/dts/api/bindings/gpio/raspberrypi%2Cpico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio) |
| on-board | STEMMA QT is a 4-pin JST-SH connector for I2C devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L123) | [`stemma-qt-connector`](../../../../build/dts/api/bindings/gpio/stemma-qt-connector.md#std-dtcompatible-stemma-qt-connector) |
| I2C | on-chip | Raspberry Pi Pico I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L306) | [`raspberrypi,pico-i2c`](../../../../build/dts/api/bindings/i2c/raspberrypi%2Cpico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| on-board | GPIO based QDEC input device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L113) | [`gpio-qdec`](../../../../build/dts/api/bindings/input/gpio-qdec.md#std-dtcompatible-gpio-qdec) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L105) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LED strip | on-board | The pio node configured for ws2812[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L221) | [`worldsemi,ws2812-rpi_pico-pio`](../../../../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio) |
| Miscellaneous | on-chip | Raspberry Pi Pico PIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L404)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L396) | [`raspberrypi,pico-pio`](../../../../build/dts/api/bindings/misc/raspberrypi%2Cpico-pio.md#std-dtcompatible-raspberrypi-pico-pio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L204) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L136) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The RPi Pico pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART0 Rx to pin 1 and enabling the pullup resistor on that pin[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L423) | [`raspberrypi,pico-pinctrl`](../../../../build/dts/api/bindings/pinctrl/raspberrypi%2Cpico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl) |
| PWM | on-chip | Raspberry Pi Pico PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L348) | [`raspberrypi,pico-pwm`](../../../../build/dts/api/bindings/pwm/raspberrypi%2Cpico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm) |
| Regulator | on-chip | RaspberryPi Pico core supply regurator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L388) | [`raspberrypi,core-supply-regulator`](../../../../build/dts/api/bindings/regulator/raspberrypi%2Ccore-supply-regulator.md#std-dtcompatible-raspberrypi-core-supply-regulator) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/macropad_rp2040/adafruit_macropad_rp2040.dts?plain=1#L30) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | Raspberry Pi Pico Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L211) | [`raspberrypi,pico-reset`](../../../../build/dts/api/bindings/reset/raspberrypi%2Cpico-reset.md#std-dtcompatible-raspberrypi-pico-reset) |
| RTC | on-chip | RaspberryPi Pico RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L412) | [`raspberrypi,pico-rtc`](../../../../build/dts/api/bindings/rtc/raspberrypi%2Cpico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc) |
| Sensors | on-chip | RaspberryPi Pico family temperature sensor node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L427) | [`raspberrypi,pico-temp`](../../../../build/dts/api/bindings/sensor/raspberrrypi%2Cpico-temp.md#std-dtcompatible-raspberrypi-pico-temp) |
| Serial controller | on-chip | Raspberry Pi Pico UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L261)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L251) | [`raspberrypi,pico-uart`](../../../../build/dts/api/bindings/serial/raspberrypi%2Cpico-uart.md#std-dtcompatible-raspberrypi-pico-uart) |
| SPI | on-chip | Raspberry Pi Pico SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L283)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L271) | [`raspberrypi,pico-spi`](../../../../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi.md#std-dtcompatible-raspberrypi-pico-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | RaspberryPi Pico USB Device Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L337) | [`raspberrypi,pico-usbd`](../../../../build/dts/api/bindings/usb/raspberrypi%2Cpico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd) |
| Watchdog | on-chip | Raspberry Pi Pico Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L330) | [`raspberrypi,pico-watchdog`](../../../../build/dts/api/bindings/watchdog/raspberrypi%2Cpico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog) |

### Programming and Debugging

Applications for the `adafruit_macropad_rp2040` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Building and Flashing

The MacroPad RP2040 has a built-in UF2 bootloader which can be entered by holding down the rotary
encoder button (BOOT) and, while continuing to hold it, pressing and releasing the reset button.
A “RPI-RP2” drive should appear on your host machine.

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application
using UF2.

```shell
# From the root of the zephyr repository
west build -b adafruit_macropad_rp2040 samples/basic/blinky
west flash --runner uf2
```

### References

- [Adafruit MacroPad RP2040 Product Page](https://www.adafruit.com/product/5128)
- [Adafruit MacroPad RP2040 Learn Guide](https://learn.adafruit.com/adafruit-macropad-rp2040)
