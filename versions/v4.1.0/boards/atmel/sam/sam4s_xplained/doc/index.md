---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/atmel/sam/sam4s_xplained/doc/index.html
original_path: boards/atmel/sam/sam4s_xplained/doc/index.html
---

# SAM4S Xplained

Board Overview

[![../../../../../_images/sam4s_xplained.jpg](https://docs.zephyrproject.org/4.1.0/_images/sam4s_xplained.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/sam4s_xplained.jpg)

SAM4S Xplained

Name:
:   `sam4s_xplained`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   sam4s16c

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4s_xplained/doc/index.rst/../..)

## Overview

The SAM4S Xplained evaluation kit is a development platform to evaluate the
Atmel SAM4S series microcontrollers.

## Hardware

- ATSAM4S16C ARM Cortex-M4 Processor
- 12 MHz crystal oscillator
- internal 32.768 kHz crystal oscillator
- IS66WV51216DALL 8 Mb SRAM
- Micro-AB USB device
- Micro-AB USB debug interface supporting SEGGER OB and Virtual COM Port and
  Data
- One reset and one user pushbutton
- 2 yellow user LEDs
- IC pads for external flash chip

### Supported Features

The `sam4s_xplained` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sam4s_xplained/sam4s16c` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L28) | [`arm,cortex-m4`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | Atmel SAM family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L224) | [`atmel,sam-adc`](../../../../../build/dts/api/bindings/adc/atmel,sam-adc.md#std-dtcompatible-atmel-sam-adc) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L43) | [`atmel,sam-pmc`](../../../../../build/dts/api/bindings/clock/atmel,sam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L200) | [`atmel,sam-tc`](../../../../../build/dts/api/bindings/counter/atmel,sam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DAC | on-chip | Atmel SAM family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L235) | [`atmel,sam-dac`](../../../../../build/dts/api/bindings/dac/atmel,sam-dac.md#std-dtcompatible-atmel-sam-dac) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L62) | [`atmel,sam-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/atmel,sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO PORT node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L169) | [`atmel,sam-gpio`](../../../../../build/dts/api/bindings/gpio/atmel,sam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| on-board | GPIO pins exposed on Atmel Xplained headers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L68) | [`atmel-xplained-header`](../../../../../build/dts/api/bindings/gpio/atmel-xplained-header.md#std-dtcompatible-atmel-xplained-header) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L244) | [`atmel,sam-rstc`](../../../../../build/dts/api/bindings/hwinfo/atmel,sam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L87)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L98) | [`atmel,sam-i2c-twi`](../../../../../build/dts/api/bindings/i2c/atmel,sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L59) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L47) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Atmel Static Memory Controller (SMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L251) | [`atmel,sam-smc`](../../../../../build/dts/api/bindings/memory-controllers/atmel,sam-smc.md#std-dtcompatible-atmel-sam-smc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L35) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L72) | [`atmel,sam-flash`](../../../../../build/dts/api/bindings/mtd/atmel,sam-flash.md#std-dtcompatible-atmel-sam-flash) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L162) | [`atmel,sam-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel,sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L51) | [`atmel,sam-supc`](../../../../../build/dts/api/bindings/power/atmel,sam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L135) | [`atmel,sam-pwm`](../../../../../build/dts/api/bindings/pwm/atmel,sam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L260) | [`atmel,sam-rtc`](../../../../../build/dts/api/bindings/rtc/atmel,sam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| Serial controller | on-chip | SAM family UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L119) | [`atmel,sam-uart`](../../../../../build/dts/api/bindings/serial/atmel,sam-uart.md#std-dtcompatible-atmel-sam-uart) |
| on-chip | Atmel SAM family USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L146) | [`atmel,sam-usart`](../../../../../build/dts/api/bindings/serial/atmel,sam-usart.md#std-dtcompatible-atmel-sam-usart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L109) | [`atmel,sam-spi`](../../../../../build/dts/api/bindings/spi/atmel,sam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L58) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L79) | [`atmel,sam-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel,sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

### Connections and IOs

Download the [SAM4S Xplained Design Files](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip) [[2]](#id4) for more information. It has
full schematic and gerbers files.

### System Clock

The SAM4S MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 84 MHz system clock.

### Serial Port

The ATSAM4S16C MCU has 2 UARTs and 2 USARTs. One of the UARTs (UART0) is
connected to the Segger J-Link OB chip (the AT91SAM3U4 is programmed to be
Segger J-Link OB). Segger J-Link OB brings the UART out as a virtual COM port.
The section flashing uses the UART from the Segger USB debug connection.

## Programming and Debugging

The SAM4S Xplained board comes with Segger
[J-Link OB](https://www.segger.com/jlink-ob.html). This provides a debug
interface to the SAM4S16C chip. You can use Ozone or JLink to communicate with
the SAM4S16C.

### Flashing

For flash the board Zephyr provides two paths. One uses the default JLink
tool and the second one uses [SAM Boot Assistant (SAM-BA)](../../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).

#### Using JLink

1. Download JLink from the Segger [JLink Downloads Page](https://www.segger.com/downloads/jlink) [[1]](#id2). Go to the section
   “J-Link Software and Documentation Pack” and install the “J-Link Software
   and Documentation pack for Linux”. The application JLinkExe needs to be
   accessible from your path.
2. Connect the SAM4S Xplained board to your host computer using the USB debug
   port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4s_xplained samples/hello_world
   west flash
   ```

#### Using SAM-BA bootloader

1. Close the `J25` jumper on the SAM4S Xplained board. Power on the board
   for 10s.
2. Open the `J25` jumper.
3. Connect the SAM4S Xplained board to your host computer using the SoC USB
   port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4s_xplained samples/hello_world
   ```

   ```shell
   $ west flash -r bossac
   ```

#### Visualizing the message

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization string.
   Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Press reset button

   You should see “Hello World! sam4s\_xplained” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam4s_xplained samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)

[[2](#id5)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD\_\_KitsFiles.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip)
