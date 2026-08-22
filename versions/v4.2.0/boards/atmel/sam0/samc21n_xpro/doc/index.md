---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/atmel/sam0/samc21n_xpro/doc/index.html
original_path: boards/atmel/sam0/samc21n_xpro/doc/index.html
---

# SAM C21N Xplained Pro Evaluation Kit

Board Overview

[![../../../../../_images/atsamc21n_xpro.jpg](../../../../../_images/atsamc21n_xpro.jpg)
](../../../../../_images/atsamc21n_xpro.jpg)

SAM C21N Xplained Pro Evaluation Kit

Name:
:   `samc21n_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   samc21n18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam0/samc21n_xpro/doc/index.rst/../..)

## Overview

The SAM C21N Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM C21N Cortex®-M0+ processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

## Hardware

- SAMC21N18A ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory, 32 KiB of RAM, 8KB RRW flash
- One yellow user LED
- One mechanical user push button
- One reset button
- One QTouch® button
- On-board USB based EDBG unit with serial console
- Two CAN transceivers

### Supported Features

The `samc21n_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `samc21n_xpro/samc21n18a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L45) | [`arm,cortex-m0+`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L130)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc21.dtsi?plain=1#L19) | [`atmel,sam0-adc`](../../../../../build/dts/api/bindings/adc/atmel%2Csam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L179) | [`atmel,sam0-sercom`](../../../../../build/dts/api/bindings/arm/atmel%2Csam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L57) | [`atmel,sam0-id`](../../../../../build/dts/api/bindings/arm/atmel%2Csam0-id.md#std-dtcompatible-atmel-sam0-id) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM0[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc21.dtsi?plain=1#L57)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc21.dtsi?plain=1#L72) | [`atmel,sam0-can`](../../../../../build/dts/api/bindings/can/atmel%2Csam0-can.md#std-dtcompatible-atmel-sam0-can) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L82) | [`atmel,sam0-mclk`](../../../../../build/dts/api/bindings/clock/atmel%2Csam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAM0 32kHz Oscillator Controller (OSC32KCTRL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L89) | [`atmel,sam0-osc32kctrl`](../../../../../build/dts/api/bindings/clock/atmel%2Csam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L96) | [`atmel,sam0-gclk`](../../../../../build/dts/api/bindings/clock/atmel%2Csam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L121) | [`atmel,sam0-dmac`](../../../../../build/dts/api/bindings/dma/atmel%2Csam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L66) | [`atmel,sam0-nvmctrl`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L239) | [`atmel,sam0-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L157) | [`atmel,sam0-i2c`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samc21n_xpro/samc21n_xpro.dts?plain=1#L50) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L104) | [`atmel,sam0-eic`](../../../../../build/dts/api/bindings/interrupt-controller/atmel%2Csam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samc21n_xpro/samc21n_xpro.dts?plain=1#L35) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samc21n_xpro/samc21n_xpro.dts?plain=1#L43) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samc21n_xpro/samc21n_xpro.dts?plain=1#L151) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L110) | [`atmel,sam0-pinmux`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L232) | [`atmel,sam0-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L218) | [`atmel,sam0-tcc-pwm`](../../../../../build/dts/api/bindings/pwm/atmel%2Csam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L270) | [`atmel,sam0-rtc`](../../../../../build/dts/api/bindings/rtc/atmel%2Csam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L146) | [`atmel,sam0-uart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc21.dtsi?plain=1#L46) | [`atmel,sam0-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L53) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samc2x.dtsi?plain=1#L115) | [`atmel,sam0-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Pin Mapping

The SAM C21N Xplained Pro evaluation kit has 4 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM C21 Family Datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf) [[1]](#id2) and the [SAM C21N
Xplained Pro Schematic](https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N_Xplained_Pro_Design_Files.zip) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- ADC0 : PB09
- ADC1 : PA08
- CAN0 TX : PA24
- CAN0 RX : PA25
- CAN1 TX : PB14
- CAN1 RX : PB15
- SERCOM0 USART TX : PB24
- SERCOM0 USART RX : PB25
- SERCOM1 I2C SDA : PA16
- SERCOM1 I2C SCL : PA17
- SERCOM2 USART TX : PA12
- SERCOM2 USART RX : PA13
- SERCOM4 USART TX : PB10
- SERCOM4 USART RX : PB11
- SERCOM5 SPI MISO : PB00
- SERCOM5 SPI MOSI : PB02
- SERCOM5 SPI SCK : PB01
- GPIO/PWM LED0 : PC05

### System Clock

The SAMC21 MCU is configured to use the 32.768 kHz internal oscillator
with the on-chip internal oscillator generating the 48 MHz system clock.

### Serial Port

The SAMC21 MCU has eight SERCOM based USARTs with three configured as USARTs in
this BSP. SERCOM4 is the default Zephyr console.

- SERCOM0 9600 8n1
- SERCOM2 115200 8n1
- SERCOM4 115200 8n1 connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAMC21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC2 instead of by GPIO.

## Programming and Debugging

The `samc21n_xpro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The SAM C21N Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAMC21 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b samc21n_xpro samples/hello_world
   ```
2. Connect the SAM C21N Xplained Pro to your host computer using the USB debug
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
   west build -b samc21n_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! samc21n\_xpro” in your terminal.

## References

[[1](#id3)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf)

[[2](#id5)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N\_Xplained\_Pro\_Design\_Files.zip](https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N_Xplained_Pro_Design_Files.zip)
