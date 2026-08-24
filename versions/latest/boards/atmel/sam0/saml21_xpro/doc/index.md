---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/atmel/sam0/saml21_xpro/doc/index.html
original_path: boards/atmel/sam0/saml21_xpro/doc/index.html
---

# SAM L21 Xplained Pro Evaluation Kit

Board Overview

[![../../../../../_images/atsaml21-xpro.jpg](https://docs.zephyrproject.org/4.2.0/_images/atsaml21-xpro.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/atsaml21-xpro.jpg)

SAM L21 Xplained Pro Evaluation Kit

Name:
:   `saml21_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   saml21j18b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam0/saml21_xpro/doc/index.rst/../..)

## Overview

The SAM L21 Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM L21 Cortex®-M0+ processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

## Hardware

- SAML21J18 ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory, 32 KiB of SRAM, 8KB Low Power SRAM
- One yellow user LED
- One mechanical user push button
- One reset button
- On-board USB based EDBG unit with serial console

### Supported Features

The `saml21_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `saml21_xpro/saml21j18b` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L45) | [`arm,cortex-m0+`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L213) | [`atmel,sam0-adc`](../../../../../build/dts/api/bindings/adc/atmel,sam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L58) | [`atmel,sam0-id`](../../../../../build/dts/api/bindings/arm/atmel,sam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L85) | [`atmel,sam0-mclk`](../../../../../build/dts/api/bindings/clock/atmel,sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAM0 32kHz Oscillator Controller (OSC32KCTRL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L92) | [`atmel,sam0-osc32kctrl`](../../../../../build/dts/api/bindings/clock/atmel,sam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L100) | [`atmel,sam0-gclk`](../../../../../build/dts/api/bindings/clock/atmel,sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L165) | [`atmel,sam0-tc32`](../../../../../build/dts/api/bindings/counter/atmel,sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DAC | on-chip | Atmel SAM0 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L223) | [`atmel,sam0-dac`](../../../../../build/dts/api/bindings/dac/atmel,sam0-dac.md#std-dtcompatible-atmel-sam0-dac) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L108) | [`atmel,sam0-dmac`](../../../../../build/dts/api/bindings/dma/atmel,sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L67) | [`atmel,sam0-nvmctrl`](../../../../../build/dts/api/bindings/flash_controller/atmel,sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L178) | [`atmel,sam0-gpio`](../../../../../build/dts/api/bindings/gpio/atmel,sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L141) | [`atmel,sam0-i2c`](../../../../../build/dts/api/bindings/i2c/atmel,sam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/saml21_xpro/saml21_xpro.dts?plain=1#L46) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L117) | [`atmel,sam0-eic`](../../../../../build/dts/api/bindings/interrupt-controller/atmel,sam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/saml21_xpro/saml21_xpro.dts?plain=1#L31) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/saml21_xpro/saml21_xpro.dts?plain=1#L39) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L77) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L171) | [`atmel,sam0-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml21.dtsi?plain=1#L18) | [`atmel,sam0-tcc-pwm`](../../../../../build/dts/api/bindings/pwm/atmel,sam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L231) | [`atmel,sam-trng`](../../../../../build/dts/api/bindings/rng/atmel,sam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L199) | [`atmel,sam0-rtc`](../../../../../build/dts/api/bindings/rtc/atmel,sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L135) | [`atmel,sam0-uart`](../../../../../build/dts/api/bindings/serial/atmel,sam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L129) | [`atmel,sam0-spi`](../../../../../build/dts/api/bindings/spi/atmel,sam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L53) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L237) | [`atmel,sam0-usb`](../../../../../build/dts/api/bindings/usb/atmel,sam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/saml2x.dtsi?plain=1#L123) | [`atmel,sam0-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel,sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Pin Mapping

The SAM L21 Xplained Pro evaluation kit has 2 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM L21 Family Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/SAM_L21_Family_DataSheet_DS60001477C.pdf) [[1]](#id2) and the [SAM L21
Xplained Pro Schematic](https://ww1.microchip.com/downloads/en/DeviceDoc/SAML21-Xplained-Pro_Design-Documentation.zip) [[2]](#id4).

![SAML21-XPRO-pinout](https://docs.zephyrproject.org/4.2.0/_images/atsaml21-xpro-pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- SERCOM0 SPI MISO : PA04
- SERCOM0 SPI MOSI : PA06
- SERCOM0 SPI SCK : PA07
- SERCOM1 USART TX : PA18
- SERCOM1 USART RX : PA19
- SERCOM2 I2C SDA : PA08
- SERCOM2 I2C SCL : PA09
- SERCOM3 USART TX : PA22
- SERCOM3 USART RX : PA23
- SERCOM4 USART TX : PB08
- SERCOM4 USART RX : PB09
- SERCOM5 SPI MISO : PB16
- SERCOM5 SPI MOSI : PB22
- SERCOM5 SPI SCK : PB23
- USB DP : PA25
- USB DM : PA24
- GPIO SPI CS : PB17
- GPIO/PWM LED0 : PB10

### System Clock

The SAML21 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAML21 MCU has six SERCOM based USARTs with two configured as USARTs in
this BSP. SERCOM3 is the default Zephyr console.

- SERCOM1 115200 8n1 - connected to EXT2 and EXT3
- SERCOM3 115200 8n1 - connected to the onboard Atmel Embedded Debugger (EDBG)
- SERCOM4 115200 8n1 - connected to EXT1

### PWM

The SAML21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAML21 MCU has 6 SERCOM based SPIs, with two configured as SPI in this BSP.

- SERCOM0 - connected to EXT1
- SERCOM5 - connected to EXT2 and EXT3

## Programming and Debugging

The `saml21_xpro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The SAM L21 Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAML21 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b saml21_xpro samples/hello_world
   ```
2. Connect the SAM L21 Xplained Pro to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ picocom -b 115200 /dev/ttyACM0
   ```

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b saml21_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! saml21\_xpro” in your terminal.

## References

[[1](#id3)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/SAM\_L21\_Family\_DataSheet\_DS60001477C.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/SAM_L21_Family_DataSheet_DS60001477C.pdf)

[[2](#id5)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/SAML21-Xplained-Pro\_Design-Documentation.zip](https://ww1.microchip.com/downloads/en/DeviceDoc/SAML21-Xplained-Pro_Design-Documentation.zip)
