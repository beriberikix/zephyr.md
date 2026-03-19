---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/adafruit/trinket_m0/doc/index.html
original_path: boards/adafruit/trinket_m0/doc/index.html
---

# Trinket M0

Board Overview

[![../../../../_images/adafruit_trinket_m0.jpg](../../../../_images/adafruit_trinket_m0.jpg)
](../../../../_images/adafruit_trinket_m0.jpg)

Trinket M0

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   samd21e18a

## Overview

The Adafruit Trinket M0 is a tiny (27 mm x 15 mm) ARM development
board with an onboard RGB LED, USB port, and range of I/O broken out
onto 5 pins.

## Hardware

- ATSAMD21E18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Internal trimmed 8 MHz oscillator
- A user LED
- An RGB DotStar LED
- Native USB port
- One reset button

### Supported Features

The adafruit\_trinket\_m0 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| Flash | on-chip | Can be used with LittleFS to store files |
| SYSTICK | on-chip | systick |
| WDT | on-chip | Watchdog |
| GPIO | on-chip | I/O ports |
| PWM | on-chip | Pulse Width Modulation |
| USART | on-chip | Serial ports |
| SPI | on-chip | Serial Peripheral Interface ports |
| USB | on-chip | USB device |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig file
[boards/adafruit/trinket\_m0/adafruit\_trinket\_m0\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/trinket_m0/adafruit_trinket_m0_defconfig).

### Connections and IOs

The [Adafruit Trinket M0 Learn site](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino) [[1]](#id2) has detailed information about
the board including [pinouts](https://learn.adafruit.com/assets/49778) [[2]](#id4) and the [schematic](https://learn.adafruit.com/assets/45723) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 8 MHz internal oscillator
with the on-chip PLL generating the 48 MHz system clock. The internal
APB and GCLK unit are set up in the same way as the upstream Arduino
libraries.

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the Trinket, SERCOM0 is
the Zephyr console and is available on pins 3 (RX) and 4 (TX).
SERCOM2 is available on pins 2 (RX) and 0 (TX).

### PWM

The SAMD21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the Trinket, SERCOM1 is
used to drive the DotStar RGB LED. SERCOM0 can be put into SPI mode
and used to connect to devices over pin 2 (MISO), pin 4 (MOSI), and
pin 3 (SCK).

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

## Programming and Debugging

The Trinket M0 ships the BOSSA compatible UF2 bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

Additionally, if `CONFIG_USB_CDC_ACM` is enabled then the bootloader
will be entered automatically when you run `west flash`.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b adafruit_trinket_m0 samples/hello_world
   ```
2. Connect the Trinket M0 to your host computer using USB
3. Connect a 3.3 V USB to serial adapter to the board and to the
   host. See the [Serial Port](#serial-port) section above for the board’s pin
   connections.
4. Run your favorite terminal program to listen for output. Under Linux the
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
5. Tap the reset button twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b adafruit_trinket_m0 samples/hello_world
   west flash
   ```

   You should see “Hello World! adafruit\_trinket\_m0” in your terminal.

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino)

[[2](#id5)]

[https://learn.adafruit.com/assets/49778](https://learn.adafruit.com/assets/49778)

[[3](#id7)]

[https://learn.adafruit.com/assets/45723](https://learn.adafruit.com/assets/45723)
