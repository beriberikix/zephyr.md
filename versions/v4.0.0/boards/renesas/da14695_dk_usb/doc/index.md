---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/renesas/da14695_dk_usb/doc/index.html
original_path: boards/renesas/da14695_dk_usb/doc/index.html
---

# DA14695 Development Kit USB

## Overview

The DA14695 Development Kit USB is a low cost development board for DA14695.
The development kit comes with an integrated debugger and an USB hub
to have both the on-chip USB and the J-Link connected via a single port.

[![DA14695 Development Kit USB](../../../../_images/da14695-00hqdevkt-u-usb-board.jpg)
](../../../../_images/da14695-00hqdevkt-u-usb-board.jpg)

DA14695 Development Kit USB (Credit: Renesas Electronics Corporation)

## Hardware

DA14695 Development Kit USB has two external oscillators. The frequency of
the sleep clock is 32768 Hz. The frequency of the system clock is 32 MHz.

### Supported Features

The \_da14695\_dk\_usb board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| RTT | Segger | console |
| UART | on-chip | serial |
| SPI | on-chip | spi |

Other hardware features, including the Configurable MAC (CMAC) controller,
are currently not supported by the port.

For more information about the DA14695 Development Kit see:

- [DA14695 DK USB website](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit) [[1]](#id2)

### System Clock

The DA14695 Development Kit USB is configured to use the 32 MHz external oscillator
on the board.

### Connections and IOs

The DA14695 Development Kit USB has one LED and one push button which can be used
by applications. The UART is connected to on-board serial converter and accessible
via USB1 port on motherboard.

The pin connections are as follows:

- LED (red), = P1.01
- BUTTON, labeled k1 = P0.06
- UART RX, connected to J-Link serial = P0.08
- UART TX, connected to J-Link serial = P0.09

## Programming and Debugging

Applications for the `da14695_dk_usb` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

The DA14695 boots from an external flash connected to QSPI interface. The image
written to flash has to have proper header prepended. The process is simplified
by using dedicated [eZFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[3]](#id6) tool that takes care of writing header and can
handle different types of flash chips connected to DA1469x MCU. Follow instructions
on [ezFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[3]](#id6) to install the tool. Once installed, flashing can be done in the
usual way.

```shell
# From the root of the zephyr repository
west build -b da14695_dk_usb samples/basic/blinky
west flash
```

### Debugging

The DA14695 Development Kit USB includes a [J-Link](https://www.segger.com/jlink-debug-probes.html) [[2]](#id4) adaptor built-in
which provides both debugging interface and serial port.
Application can be debugged in the usual way once DA14695 Development Kit USB
is connected to PC via USB.

## References

[[1](#id3)]

[https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit)

[[2](#id5)]

[https://www.segger.com/jlink-debug-probes.html](https://www.segger.com/jlink-debug-probes.html)

[3]
([1](#id7),[2](#id8))

[https://github.com/ezflash/ezFlashCLI/](https://github.com/ezflash/ezFlashCLI/)
