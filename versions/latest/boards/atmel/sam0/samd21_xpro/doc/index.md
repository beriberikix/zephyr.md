---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/atmel/sam0/samd21_xpro/doc/index.html
original_path: boards/atmel/sam0/samd21_xpro/doc/index.html
---

# SAM D21 Xplained Pro Evaluation Kit

Board Overview

[![../../../../../_images/atsamd21_xpro.jpg](../../../../../_images/atsamd21_xpro.jpg)
](../../../../../_images/atsamd21_xpro.jpg)

SAM D21 Xplained Pro Evaluation Kit

Name:
:   `samd21_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   samd21j18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam0/samd21_xpro/doc/index.rst/../..)

## Overview

The SAM D21 Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM D21 Cortex®-M0+ processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

## Hardware

- SAMD21J18 ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory and 32 KiB of RAM
- One yellow user LED
- One mechanical user push button
- One reset button
- On-board USB based EDBG unit with serial console

### Supported Features

The `samd21_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `samd21_xpro/samd21j18a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L44) | [`arm,cortex-m0+`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L202) | [`atmel,sam0-adc`](../../../../../build/dts/api/bindings/adc/atmel%2Csam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L144) | [`atmel,sam0-sercom`](../../../../../build/dts/api/bindings/arm/atmel%2Csam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L56) | [`atmel,sam0-id`](../../../../../build/dts/api/bindings/arm/atmel%2Csam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L82) | [`atmel,sam0-mclk`](../../../../../build/dts/api/bindings/clock/atmel%2Csam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L90) | [`atmel,sam0-gclk`](../../../../../build/dts/api/bindings/clock/atmel%2Csam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L156) | [`atmel,sam0-tc32`](../../../../../build/dts/api/bindings/counter/atmel%2Csam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DAC | on-chip | Atmel SAM0 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L212) | [`atmel,sam0-dac`](../../../../../build/dts/api/bindings/dac/atmel%2Csam0-dac.md#std-dtcompatible-atmel-sam0-dac) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L29) | [`atmel,sam0-dmac`](../../../../../build/dts/api/bindings/dma/atmel%2Csam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L65) | [`atmel,sam0-nvmctrl`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L169) | [`atmel,sam0-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L132) | [`atmel,sam0-i2c`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samd21_xpro/samd21_xpro.dts?plain=1#L49) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L98) | [`atmel,sam0-eic`](../../../../../build/dts/api/bindings/interrupt-controller/atmel%2Csam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samd21_xpro/samd21_xpro.dts?plain=1#L34) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samd21_xpro/samd21_xpro.dts?plain=1#L42) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Atmel SAM0 PINMUX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L104) | [`atmel,sam0-pinmux`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L162) | [`atmel,sam0-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L49) | [`atmel,sam0-tcc-pwm`](../../../../../build/dts/api/bindings/pwm/atmel%2Csam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L190) | [`atmel,sam0-rtc`](../../../../../build/dts/api/bindings/rtc/atmel%2Csam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L120) | [`atmel,sam0-uart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L150) | [`atmel,sam0-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L52) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L20) | [`atmel,sam0-usb`](../../../../../build/dts/api/bindings/usb/atmel%2Csam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L114) | [`atmel,sam0-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Pin Mapping

The SAM D21 Xplained Pro evaluation kit has 3 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM D21 Family Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM-D21-Family-Datasheet-DS40001882C.pdf) [[1]](#id2) and the [SAM D21
Xplained Pro Schematic](http://ww1.microchip.com/downloads/en/DeviceDoc/SAMD21-Xplained-Pro_Design-Documentation.zip) [[2]](#id4).

![SAMD21-XPRO-pinout](../../../../../_images/ATSAMD21-XPRO-pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- SERCOM0 USART TX : PA10
- SERCOM0 USART RX : PA11
- SERCOM1 USART TX : PA16
- SERCOM1 USART RX : PA19
- SERCOM2 I2C SDA : PA08
- SERCOM2 I2C SCL : PA09
- SERCOM3 USART TX : PA22
- SERCOM3 USART RX : PA23
- SERCOM5 SPI MISO : PB16
- SERCOM5 SPI MOSI : PB22
- SERCOM5 SPI SCK : PB23
- USB DP : PA25
- USB DM : PA24
- GPIO SPI CS : PB17
- GPIO/PWM LED0 : PB30

### System Clock

The SAMD21 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAMD21 MCU has six SERCOM based USARTs with three configured as USARTs in
this BSP. SERCOM3 is the default Zephyr console.

- SERCOM0 9600 8n1
- SERCOM1 115200 8n1
- SERCOM3 115200 8n1 connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAMD21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the SAM D21 Xplained Pro,
SERCOM5 is connected to an 8 megabit SPI flash.

## Programming and Debugging

The `samd21_xpro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The SAM D21 Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAMD21 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b samd21_xpro samples/hello_world
   ```
2. Connect the SAM D21 Xplained Pro to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b samd21_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! samd21\_xpro” in your terminal.

## References

[[1](#id3)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAM-D21-Family-Datasheet-DS40001882C.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM-D21-Family-Datasheet-DS40001882C.pdf)

[[2](#id5)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAMD21-Xplained-Pro\_Design-Documentation.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAMD21-Xplained-Pro_Design-Documentation.zip)
