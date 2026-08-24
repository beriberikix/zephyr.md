---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/atmel/sam/sam4l_ek/doc/index.html
original_path: boards/atmel/sam/sam4l_ek/doc/index.html
---

# SAM4L-EK

Board Overview

[![../../../../../_images/atmel-sam4l-ek-callouts.jpg](https://docs.zephyrproject.org/4.1.0/_images/atmel-sam4l-ek-callouts.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/atmel-sam4l-ek-callouts.jpg)

SAM4L-EK

Name:
:   `sam4l_ek`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   sam4lc4c

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4l_ek/doc/index.rst/../..)

## Overview

The SAM4L series embeds picoPower technology for ultra-low power consumption.
Combined power control techniques are used to bring active current consumption
down to 90μA/MHz. The device allows a wide range of configurations giving the
user the ability to balance between the lowest possible power consumption and
the feature set selected for the application. The WAIT and RETENTION modes
provide full logic and RAM retention, associated with fast wake-up capability
(<1.5μs) and a very low consumption of, respectively, 3 μA and 1.5 μA. In
addition, WAIT mode supports SleepWalking features. In BACKUP mode, CPU,
peripherals and RAM are powered off consuming less than 0.9μA with external
interrupt wake-up support.

The SAM4L-EK is a full featured design to develop for Atmel SAM4L SoC series.
The kit is equipped with a rich set of peripherals that make the ATSAM4L-EK a
perfect evaluation platform. Download the [SAM4L-EK Online User Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide_ApplicationNote_AVR32850.pdf) [[1]](#id2) for
more details.

## Hardware

- ATSAM4LC4C ARM Cortex-M4 Processor
- 12 MHz crystal oscillator
- 32.768 kHz crystal oscillator
- 1 Micro-AB USB OTG host/device
- 1 AT86RF2xx IEEE 802.15.4 transceiver connector
- 1 RS-485 full duplex interface
- 1 Sensor Xplained board connector
- 1 Audio Jack connector 3.5mm
- 1 Dedicated Board Monitor MCU

  - Power measurement (VDDIN, VDDIO, VDDANA)
  - 1 OLED Display (128x64)
  - 5 LEDs
  - 1 Joystick
  - 1 USART
  - 1 TWI
- 1 40x4 LCD Segment Display
- 1 user touch button and One user pushbutton
- 1 user LED
- 1 QTouch Slider
- 1 QTouch Button
- 1 TEMT6000 Light Sensor
- 1 AT25DF641A Serial NOR Flash

### Supported Features

The `sam4l_ek` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sam4l_ek/sam4lc4c` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L26) | [`arm,cortex-m4`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L57) | [`atmel,sam-pmc`](../../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L211)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L221) | [`atmel,sam-tc`](../../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| Flash controller | on-chip | Atmel SAM4L Flash Controller Double Word (FLASHCALW)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L65) | [`atmel,sam4l-flashcalw-controller`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam4l-flashcalw-controller.md#std-dtcompatible-atmel-sam4l-flashcalw-controller) |
| GPIO & Headers | on-chip | SAM4L GPIO PORT node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L182) | [`atmel,sam4l-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam4l-gpio.md#std-dtcompatible-atmel-sam4l-gpio) |
| Hardware information | on-chip | ATMEL SAM4L Unique 120-bit Serial Number[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L239) | [`atmel,sam4l-uid`](../../../../../build/dts/api/bindings/hwinfo/atmel%2Csam4l-uid.md#std-dtcompatible-atmel-sam4l-uid) |
| I2C | on-chip | Atmel SAM4L Family I2C (TWIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L85)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L95) | [`atmel,sam-i2c-twim`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twim.md#std-dtcompatible-atmel-sam-i2c-twim) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4l_ek/sam4l_ek.dts?plain=1#L37) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4l_ek/sam4l_ek.dts?plain=1#L29) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L33) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L72) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L176) | [`atmel,sam-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L231) | [`atmel,sam-trng`](../../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| Serial controller | on-chip | Atmel SAM family USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L150)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L136) | [`atmel,sam-usart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L126) | [`atmel,sam-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L40) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBC) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L165) | [`atmel,sam-usbc`](../../../../../build/dts/api/bindings/usb/atmel%2Csam-usbc.md#std-dtcompatible-atmel-sam-usbc) |
| Watchdog | on-chip | ATMEL SAM4L watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L245) | [`atmel,sam4l-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam4l-watchdog.md#std-dtcompatible-atmel-sam4l-watchdog) |

### Connections and IOs

The [SAM4L-EK Design Documentation](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF) [[2]](#id4) has detailed information about board
connections. Download the [SAM4L-EK Design Documentation](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF) [[2]](#id4) for more details.

### System Clock

The SAM4L MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 48 MHz system clock.

### Serial Port

The ATSAM4LC4C MCU has 4 USARTs. One of the USARTs (USART2) is connected on
the embedded debug unit and can works as a console. The USART0 is shared
between all others headers and RS-485 port.

## Programming and Debugging

The SAM4L-EK board have a Segger Embedded Debugger Unit
[J-Link OB](https://www.segger.com/jlink-ob.html). This provides a debug
interface to the SAM4LC4C chip. You can use Ozone or JLink to communicate with
the SAM4LC4C.

### Flashing

1. Download JLink from the Segger [JLink Downloads Page](https://www.segger.com/downloads/jlink) [[3]](#id7). Go to the section
   “J-Link Software and Documentation Pack” and install the “J-Link Software
   and Documentation pack for Linux”. The application JLinkExe needs to be
   accessible from your path.
2. Run your favorite terminal program to listen for output. Under Linux the
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
3. Connect the SAM4L-EK board to your host computer using the USB debug port.
   Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4l_ek samples/hello_world
   west flash
   ```

   You should see “Hello World! sam4l\_ek” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam4l_ek samples/hello_world
west debug
```

## References

[[1](#id3)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide\_ApplicationNote\_AVR32850.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide_ApplicationNote_AVR32850.pdf)

[2]
([1](#id5),[2](#id6))

[http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027\_SAM4L-EK\_Design\_Documentation.PDF](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF)

[[3](#id8)]

[https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)
