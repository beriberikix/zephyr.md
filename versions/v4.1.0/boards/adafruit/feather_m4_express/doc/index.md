---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/feather_m4_express/doc/index.html
original_path: boards/adafruit/feather_m4_express/doc/index.html
---

# Feather M4 Express

Board Overview

[![../../../../_images/adafruit_feather_m4_express.webp](../../../../_images/adafruit_feather_m4_express.webp)
](../../../../_images/adafruit_feather_m4_express.webp)

Feather M4 Express

Name:
:   `adafruit_feather_m4_express`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   samd51j19a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_m4_express/doc/index.rst/../..)

## Overview

The Adafruit Feather M4 Express is a compact, lightweight
ARM development board with an onboard mini NeoPixel, 2 MiB
of SPI flash, charging status indicator and user LEDs, USB
connector, 21 GPIO pins and a small prototyping area.

## Hardware

- ATSAMD51J19A ARM Cortex-M4 processor at 120 MHz
- 512 KiB of flash memory and 192 KiB of RAM
- 2 MiB of SPI flash
- Internal trimmed 8 MHz oscillator
- A user LED
- An RGB NeoPixel LED
- Native USB port
- One reset button

### Supported Features

The `adafruit_feather_m4_express` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Zephyr can use the default Cortex-M SYSTICK timer or the SAM0 specific RTC.
To use the RTC, set `CONFIG_CORTEX_M_SYSTICK=n` and set
`CONFIG_SYS_CLOCK_TICKS_PER_SEC` to no more than 32 kHZ divided by 7,
i.e. no more than 4500.

### Connections and IOs

The [Adafruit Learning System](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51) [[1]](#id2) has detailed information about
the board including [pinouts](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads) [[3]](#id6).

### System Clock

The SAMD51 MCU is configured to use the 32 kHz internal oscillator
with the on-chip PLL generating the 120 MHz system clock.

### Serial Port

The SAMD51 MCU has 6 SERCOM based USARTs. On the Feather, SERCOM5 is
the Zephyr console and is available on pins 0 (RX) and 1 (TX).

### SPI Port

The SAMD51 MCU has 6 SERCOM based SPIs. On the Feather, SERCOM1 can be put
into SPI mode and used to connect to devices over the SCK (SCLK), MO (MOSI), and
MI (MISO) pins.

### PWM

The SAMD51 has three PWM generators with up to six channels each. `TCC_0`
has a resolution of 24 bits and all other generators are 16 bit. `TCC_1`
pin 2 is mapped to PA18 (D7) and pin 3 is mapped to PA19 (D9).

### USB Device Port

The SAMD51 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB](../../../../connectivity/usb/index.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

## Programming and Debugging

The Feather ships with a the BOSSA compatible UF2 bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

Additionally, if [`CONFIG_USB_CDC_ACM`](../../../../kconfig.md#CONFIG_USB_CDC_ACM "CONFIG_USB_CDC_ACM") is enabled then the
bootloader will be entered automatically when you run `west flash`.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b adafruit_feather_m4_express samples/hello_world
   ```
2. Connect the feather to your host computer using USB
3. Connect a 3.3 V USB to serial adapter to the board and to the
   host. See the [Serial Port](#serial-port) section above for the board’s pin
   connections.
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
5. Tap the reset button twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b adafruit_feather_m4_express samples/hello_world
   west flash
   ```

   You should see “Hello World! adafruit\_feather\_m4\_express” in your terminal.

### Debugging

In addition to the built-in bootloader, the Feather can be flashed and
debugged using a SWD probe such as the Segger J-Link.

1. Connect the board to the probe by connecting the `SWCLK`,
   `SWDIO`, `RESET`, `GND`, and `3V3` pins on the
   Feather to the `SWCLK`, `SWDIO`, `RESET`, `GND`,
   and `VTref` pins on the [J-Link](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/) [[4]](#id8).
2. Flash the image:

   ```shell
   west build -b adafruit_feather_m4_express samples/hello_world
   west flash -r openocd
   ```
3. Start debugging:

   ```shell
   west build -b adafruit_feather_m4_express samples/hello_world
   west debug
   ```

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads)

[[4](#id9)]

[https://www.segger.com/products/debug-probes/j-link/technology/interface-description/](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)
