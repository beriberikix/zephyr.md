---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/atmel/sam0/samd21_xpro/doc/index.html
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
