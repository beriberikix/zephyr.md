---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/others/serpente/doc/index.html
original_path: boards/others/serpente/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Arturo182 Serpente

## Overview

The Serpente is a very small low-cost development and prototyping
board equipped with 4MiB flash storage, a PWM enabled RGB led and 6 I/O pins.
The board comes with 3 different USB connector options: USB Type-C plug,
USB Type-C socket and USB Type-A plug.

![Serpente Boards](../../../../_images/serpente.jpg)

## Hardware

- ATSAMD21E18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Extra 4MiB SPI flash memory
- RGB User LED
- Reset button
- Native USB port

### Supported Features

The Serpente board configuration supports the
following hardware features:

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
[boards/others/serpente/serpente\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/serpente/serpente_defconfig).

### Connections and IOs

The [Serpente documentation](https://www.solder.party/docs/serpente/r2/) [[1]](#id1) has detailed information about the board
including [pinouts](https://www.solder.party/docs/serpente/r2/pinout/) [[2]](#id3) and the [schematic](https://www.solder.party/docs/serpente/r2/downloads/) [[3]](#id5).

### System Clock

The SAMD21 MCU is configured to use the 8MHz internal oscillator
with the on-chip PLL generating the 48 MHz system clock.

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support samples](../../../../samples/subsys/usb/usb.md#usb-samples) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which prints “Hello World!”
to the host PC.

### Programming and Debugging

The Serpente ships the BOSSA compatible UF2 bootloader. The bootloader
can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application:

   ```shell
   west build -b serpente samples/basic/blinky
   ```
2. Connect the Serpente to your host computer using USB
3. Tap the reset button twice quickly to enter bootloader mode
4. Flash the image:

   ```shell
   west build -b serpente samples/basic/blinky
   west flash
   ```

   You should see the User LED blink.

## References

[[1](#id2)]

[https://www.solder.party/docs/serpente/r2/](https://www.solder.party/docs/serpente/r2/)

[[2](#id4)]

[https://www.solder.party/docs/serpente/r2/pinout/](https://www.solder.party/docs/serpente/r2/pinout/)

[[3](#id6)]

[https://www.solder.party/docs/serpente/r2/downloads/](https://www.solder.party/docs/serpente/r2/downloads/)
