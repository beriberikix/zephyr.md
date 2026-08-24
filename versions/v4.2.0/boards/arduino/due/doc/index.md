---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/due/doc/index.html
original_path: boards/arduino/due/doc/index.html
---

# Arduino Due

Board Overview

[![../../../../_images/arduino_due.jpg](https://docs.zephyrproject.org/4.2.0/_images/arduino_due.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/arduino_due.jpg)

Arduino Due

Name:
:   `arduino_due`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   sam3x8e

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/due/doc/index.rst/../..)

## Overview

The arduino\_due board configuration is used by Zephyr applications
that run on the Arduino Due board. It provides support for the Atmel
SAM3X8E ARM Cortex-M3 CPU and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Serial Port over USB (ATMEL\_SAM3)

More information about the board can be found at the [Arduino Due website](https://www.arduino.cc/en/Main/ArduinoBoardDue) [[1]](#id3).
The [Atmel SAM3X8E Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf) [[2]](#id6) has the information and the datasheet about
the processor.

Note

This configuration is not supported by Arduino.

## Hardware

### Supported Features

The `arduino_due` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `arduino_due/sam3x8e` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L26) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm,cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | Atmel SAM family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L262) | [`atmel,sam-adc`](../../../../build/dts/api/bindings/adc/atmel,sam-adc.md#std-dtcompatible-atmel-sam-adc) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L34) | [`atmel,sam-pmc`](../../../../build/dts/api/bindings/clock/atmel,sam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L226) | [`atmel,sam-tc`](../../../../build/dts/api/bindings/counter/atmel,sam-tc.md#std-dtcompatible-atmel-sam-tc) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L75) | [`atmel,sam-flash-controller`](../../../../build/dts/api/bindings/flash_controller/atmel,sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L175) | [`atmel,sam-gpio`](../../../../build/dts/api/bindings/gpio/atmel,sam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/due/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L284) | [`atmel,sam-rstc`](../../../../build/dts/api/bindings/hwinfo/atmel,sam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWI)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L107) | [`atmel,sam-i2c-twi`](../../../../build/dts/api/bindings/i2c/atmel,sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/due/arduino_due.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L84) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Atmel SAM Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L169) | [`atmel,sam-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel,sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L42) | [`atmel,sam-supc`](../../../../build/dts/api/bindings/power/atmel,sam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L273) | [`atmel,sam-pwm`](../../../../build/dts/api/bindings/pwm/atmel,sam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L291) | [`atmel,sam-rtc`](../../../../build/dts/api/bindings/rtc/atmel,sam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| Serial controller | on-chip | SAM family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L129) | [`atmel,sam-uart`](../../../../build/dts/api/bindings/serial/atmel,sam-uart.md#std-dtcompatible-atmel-sam-uart) |
| on-chip | Atmel SAM family USART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L137) | [`atmel,sam-usart`](../../../../build/dts/api/bindings/serial/atmel,sam-usart.md#std-dtcompatible-atmel-sam-usart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L54)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L64) | [`atmel,sam-spi`](../../../../build/dts/api/bindings/spi/atmel,sam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L49) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L99) | [`atmel,sam-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel,sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

See [Arduino Due website](https://www.arduino.cc/en/Main/ArduinoBoardDue) [[1]](#id3) and [Atmel SAM3X8E Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf) [[2]](#id6) for a complete
list of Arduino Due board hardware features.

Note

For I2C, pull-up resistors are required for using SCL1 and SDA1 (near IO13).

### Interrupt Controller

There are 15 fixed exceptions including exceptions 12 (debug monitor) and 15
(SYSTICK) that behave more as interrupts than exceptions. In addition, there can
be a variable number of IRQs. Exceptions 7-10 and 13 are reserved. They don’t
need handlers.

A Cortex-M3/4-based board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Handlers are provided for exceptions 1-6, 11-12, and 14-15. The table here
identifies the handlers used for each exception.

| Exc# | Name | Remarks | Used by Zephyr Kernel |
| --- | --- | --- | --- |
| 1 | Reset |  | system initialization |
| 2 | NMI |  | system fatal error |
| 3 | Hard fault |  | system fatal error |
| 4 | MemManage | MPU fault | system fatal error |
| 5 | Bus |  | system fatal error |
| 6 | Usage fault | undefined instruction, or switch attempt to ARM mode | system fatal error |
| 11 | SVC |  | system calls, kernel run-time exceptions, and IRQ offloading |
| 12 | Debug monitor |  | system fatal error |
| 14 | PendSV |  | context switch |
| 15 | SYSTICK |  | system clock |

Note

After a reset, all exceptions have a priority of 0. Interrupts cannot run
at priority 0 for the interrupt locking mechanism and exception handling
to function properly.

### System Clock

Arduino Due has two external oscillators/resonators. The slow clock is
32.768 kHz, and the main clock is 12 MHz. The processor can set up PLL to drive
the master clock, which can be set as high as 84 MHz.

### Serial Port

The Atmel SAM3X8E processor has a single UART that is used by the SAM-BA
bootloader. This UART has only two wires for RX/TX and does not have flow
control (CTS/RTS) or FIFO. The RX/TX pins are connected to the ATmega16U2,
which provides USB-to-TTL serial function. The Zephyr console output, by
default, is utilizing this controller.

## Programming and Debugging

The `arduino_due` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[bossac](../../../../develop/flash_debug/host-tools.md#runner-bossac)** | ✅ (default) |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

#### BOSSA Tool

Flashing the Zephyr kernel onto Arduino Due requires the [bossa tool](https://github.com/shumatech/BOSSA) [[3]](#id9).

There are GUI and command line versions of the bossa tool. The following
section provides the steps to build the command line version. Please
refer to the bossa tool’s README file on how to build the GUI version.

To build the bossa tool, follow these steps:

1. Checkout the bossa tool’s code from the repository.

   ```shell
   $ git clone https://github.com/shumatech/BOSSA.git
   $ cd BOSSA
   ```
2. Checkout the arduino branch. The code on the master branch does not
   work with Arduino Due.

   ```shell
   $ git checkout arduino
   ```
3. Build the command line version of the bossa tool.

   ```shell
   $ make bin/bossac
   ```
4. The resulting binary is available at `bin/bossac`.

#### Flashing an Application to Arduino Due

Applications for the `arduino_due` board configuration can be built
and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. After
building the application, press the Reset button before running the
flash command, so the board will boot into the SAM-BA bootloader and
be prepared to receive the new program.

```shell
# From the root of the zephyr repository
west build -b arduino_due samples/hello_world
west flash
```

After flashing the application, run your favorite terminal program to
listen for output. For example, under Linux, the terminal should be
`/dev/ttyACM0`. For example:

```shell
$ sudo minicom -D /dev/ttyACM0 -o
```

The -o option tells minicom not to send the modem initialization
string.

Now press the Reset button and you should see “Hello World! arduino\_due” in your terminal.

Note

Make sure your terminal program is closed before flashing the binary image,
or it will interfere with the flashing process.

## References

[1]
([1](#id4),[2](#id5))

[https://www.arduino.cc/en/Main/ArduinoBoardDue](https://www.arduino.cc/en/Main/ArduinoBoardDue)

[2]
([1](#id7),[2](#id8))

[http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A\_Datasheet.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf)

[[3](#id10)]

[https://github.com/shumatech/BOSSA](https://github.com/shumatech/BOSSA)
