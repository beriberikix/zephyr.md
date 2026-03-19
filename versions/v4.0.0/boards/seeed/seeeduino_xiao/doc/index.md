---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/seeed/seeeduino_xiao/doc/index.html
original_path: boards/seeed/seeeduino_xiao/doc/index.html
---

# Seeeduino XIAO

Board Overview

[![../../../../_images/seeeduino_xiao.jpg](../../../../_images/seeeduino_xiao.jpg)
](../../../../_images/seeeduino_xiao.jpg)

Seeeduino XIAO

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   samd21g18a

## Overview

The Seeeduino XIAO is a tiny (20 mm x 17.5 mm) ARM development
board with onboard LEDs, USB port, and range of I/O broken out
onto 14 pins.

## Hardware

- ATSAMD21G18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Three user LEDs
- Native USB port

### Supported Features

The seeeduino\_xiao board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| DMA | on-chip | Direct memory access |
| DAC | on-chip | Digital to analogue converter |
| Flash | on-chip | Can be used with LittleFS to store files |
| GPIO | on-chip | I/O ports |
| HWINFO | on-chip | Hardware info |
| I2C | on-chip | Inter-Integrated Circuit |
| NVIC | on-chip | nested vector interrupt controller |
| SPI | on-chip | Serial Peripheral Interface ports |
| SYSTICK | on-chip | systick |
| USART | on-chip | Serial ports |
| USB | on-chip | USB device |
| WDT | on-chip | Watchdog |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig file
[boards/seeed/seeeduino\_xiao/seeeduino\_xiao\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/seeeduino_xiao/seeeduino_xiao_defconfig).

### Connections and IOs

The [Seeeduino XIAO wiki](https://wiki.seeedstudio.com/Seeeduino-XIAO/) [[1]](#id2) has detailed information about
the board including [pinouts](https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview) [[2]](#id4) and the [schematic](https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 32 kHz external crystal
with the on-chip PLL generating the 48 MHz system clock. The internal
APB and GCLK unit are set up in the same way as the upstream Arduino
libraries.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the XIAO, SERCOM0 can be put
into SPI mode and used to connect to devices over pin 9 (MISO), pin 10
(MOSI), and pin 8 (SCK).

### I2C Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the XIAO, SERCOM2 is available on
pin 4 (SDA) and pin 5 (SCL).

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the XIAO, SERCOM4 is
the Zephyr console and is available on pins 7 (RX) and 6 (TX).

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

### DAC

The SAMD21 MCU has a single channel DAC with 10 bits of resolution. On
the XIAO, the DAC is available on pin 0.

## Programming and Debugging

The XIAO ships the BOSSA compatible UF2 bootloader. The bootloader can be
entered by shorting the RST and GND pads twice.

Additionally, if `CONFIG_USB_CDC_ACM` is enabled then the bootloader
will be entered automatically when you run `west flash`.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b seeeduino_xiao samples/hello_world
   ```
2. Connect the XIAO to your host computer using USB
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
5. Short the RST and GND pads twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b seeeduino_xiao samples/hello_world
   west flash
   ```

   You should see “Hello World! seeeduino\_xiao” in your terminal.

## References

[[1](#id3)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/](https://wiki.seeedstudio.com/Seeeduino-XIAO/)

[[2](#id5)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview](https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview)

[[3](#id7)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses](https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses)
