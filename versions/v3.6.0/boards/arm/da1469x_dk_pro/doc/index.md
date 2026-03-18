---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/da1469x_dk_pro/doc/index.html
original_path: boards/arm/da1469x_dk_pro/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DA1469x Development Kit Pro

## Overview

The DA1469x Development Kit Pro hardware provides support for the Renesas
DA1469x ARM Cortex-M33 MCU family. The development kit consist of a motherboard
with connectors and integrated debugger and an interchangeable daughterboard
with an actual MCU (e.g. DA14695 or DA14699).

[![DA14695 Development Kit Pro](../../../../_images/da14695-00hqdevkt-board.jpg)](../../../../_images/da14695-00hqdevkt-board.jpg)

DA14695 Development Kit Pro (Credit: Renesas Electronics Corporation)

## Hardware

DA1469x Development Kit Pro has two external oscillators. The frequency of
the sleep clock is 32768 Hz. The frequency of the system clock is 32 MHz.

### Supported Features

The \_da1469x\_dk\_pro board configuration supports the following
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

- [DA14695 DK website](https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro) [[1]](#id2)
- [DA14699 daughterboard website](https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard) [[2]](#id4)

### System Clock

The DA1469x Development Kit Pro is configured to use the 32 MHz external oscillator
on the board.

### Connections and IOs

The DA1469x Development Kit Pro has one LED and one push button which can be used
by applications. The UART is connected to on-board serial converter and accessible
via USB1 port on motherboard.

The pin connections are as follows:

- LED (red), located on daughterboard = P1.01
- BUTTON, located on motherboard = P0.06
- UART RX, via USB1 on motherboard = P0.08
- UART TX, via USB1 on motherboard = P0.09

## Programming and Debugging

Applications for the `da1469x_dk_pro` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

The DA1469x boots from an external flash connected to QSPI interface. The image
written to flash has to have proper header prepended. The process is simplified
by using dedicated [eZFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[4]](#id8) tool that takes care of writing header and can
handle different types of flash chips connected to DA1469x MCU. Follow instructions
on [ezFlashCLI](https://github.com/ezflash/ezFlashCLI/) [[4]](#id8) to install the tool. Once installed, flashing can be done in the
usual way.

```shell
# From the root of the zephyr repository
west build -b da1469x_dk_pro samples/basic/blinky
west flash
```

### Debugging

The DA1469x Development Kit Pro includes a [J-Link](https://www.segger.com/jlink-debug-probes.html) [[3]](#id6) adaptor built-in on
motherboard which provides both debugging interface and serial port.
Application can be debugged in the usual way once DA1469x Development Kit Pro
is connected to PC via USB port on motherboard.

## References

[[1](#id3)]

[https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro](https://www.renesas.com/eu/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14695-00hqdevkt-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro)

[[2](#id5)]

[https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard](https://www.renesas.com/br/en/products/interface-connectivity/wireless-communications/bluetooth-low-energy/da14699-00hrdb-p-smartbond-da14695-bluetooth-low-energy-52-development-kit-pro-vfbga100-daughterboard)

[[3](#id7)]

[https://www.segger.com/jlink-debug-probes.html](https://www.segger.com/jlink-debug-probes.html)

[4]
([1](#id9),[2](#id10))

[https://github.com/ezflash/ezFlashCLI/](https://github.com/ezflash/ezFlashCLI/)
