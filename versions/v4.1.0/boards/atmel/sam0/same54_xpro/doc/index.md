---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/atmel/sam0/same54_xpro/doc/index.html
original_path: boards/atmel/sam0/same54_xpro/doc/index.html
---

# SAM E54 Xplained Pro Evaluation Kit

Board Overview

[![../../../../../_images/atsame54_xpro.jpg](../../../../../_images/atsame54_xpro.jpg)
](../../../../../_images/atsame54_xpro.jpg)

SAM E54 Xplained Pro Evaluation Kit

Name:
:   `same54_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   same54p20a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam0/same54_xpro/doc/index.rst/../..)

## Overview

The SAM E54 Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM E54 Cortex®-M4F processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

## Hardware

- SAME54P20A ARM Cortex-M4F processor at 120 MHz
- 32.768 kHz crystal oscillator
- 12 MHz crystal oscillator
- 1024 KiB flash memory and 256 KiB of RAM
- One yellow user LED
- One mechanical user push button
- One reset button
- On-board USB based EDBG unit with serial console
- One QTouch® PTC button
- 32 MiB QSPI Flash
- ATECC508 CryptoAuthentication™ device
- AT24MAC402 serial EEPROM with EUI-48™ MAC address
- Ethernet

  > - RJ45 connector with built-in magnetics
  > - KSZ8091RNA PHY
  > - 10Base-T/100Base-TX IEE 802.3 compliant Ethernet transceiver
- USB interface, host, and device
- SD/SDIO card connector

### Supported Features

The `same54_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The SAM E54 Xplained Pro evaluation kit has 4 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM D5x/E5x Family Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/60001507C.pdf) [[1]](#id2) and the [SAM E54
Xplained Pro Schematic](http://ww1.microchip.com/downloads/en/DeviceDoc/SAME54-Xplained-Pro_Design-Documentation.zip) [[2]](#id4).

![SAME54-XPRO-pinout](../../../../../_images/ATSAME54-XPRO-pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- SERCOM2 USART TX : PB24
- SERCOM2 USART RX : PB25
- GPIO/PWM LED0 : PC18
- GPIO SW0 : PB31
- GMAC RMII REFCK : PA14
- GMAC RMII TXEN : PA17
- GMAC RMII TXD0 : PA18
- GMAC RMII TXD1 : PA19
- GMAC RMII CRSDV : PC20
- GMAC RMII RXD0 : PA13
- GMAC RMII RXD1 : PA12
- GMAC RMII RXER : PA15
- GMAC MDIO MDC : PC11
- GMAC MDIO MDIO : PC12
- SERCOM4 SPI SCK : PB26
- SERCOM4 SPI MOSI : PB27
- SERCOM4 SPI MISO : PB29
- SERCOM7 I2C SDA : PD08
- SERCOM7 I2C SCL : PD09
- USB DP : PA25
- USB DM : PA24

### System Clock

The SAME54 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAME54 MCU has 8 SERCOM based USARTs with one configured as USARTs in
this BSP. SERCOM2 is the default Zephyr console.

- SERCOM2 115200 8n1 connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAME54 MCU has 5 TCC based PWM units with up to 6 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAME54 MCU has 8 SERCOM based SPIs.

### I2C Port

The SAME54 MCU has 8 SERCOM based I2Cs. On the SAM E54 Xplained Pro,
SERCOM7 is connected to a AT24MAC402 EEPROM and a ATECC508A Crypto
Authentication device.

## Programming and Debugging

The SAM E54 Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAME54 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b same54_xpro samples/hello_world
   ```
2. Connect the SAM E54 Xplained Pro to your host computer using the USB debug
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
   west build -b same54_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! same54\_xpro” in your terminal.

## References

[[1](#id3)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/60001507C.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/60001507C.pdf)

[[2](#id5)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAME54-Xplained-Pro\_Design-Documentation.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAME54-Xplained-Pro_Design-Documentation.zip)
