---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/arduino/uno_r4/doc/index.html
original_path: boards/arduino/uno_r4/doc/index.html
---

# Arduino UNO R4

## Overview

The Arduino UNO R4 Minima/WiFi is a development board featuring the Renesas RA4M1 SoC
in the Arduino form factor and is compatible with traditional Arduino.

## Hardware

- Renesas RA4MA1 Processor (ARM Cortex-M4 at 48 MHz)
- 256 KiB flash memory and 32 KiB of RAM
- One user LEDs
- One reset button
- One WiFi Transceiver (Arduino UNO R4 WiFi only)
- One 12x8 LED Matrix (Arduino UNO R4 WiFi only)
- Built-in CMSIS-DAP debug adapter (Arduino UNO R4 WiFi only)

### Supported Features

The Arduino UNO R4 Minima/Wifi board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GPIO | on-chip | I/O ports |
| UART | on-chip | Serial ports |

## Programming and debugging

### Debug adapter

A debug adapter is required to flash and debug programs.
Arduino UNO R4 WiFi has a built-in debug adapter that
you can use for flashing and debugging.

In the Arduino UNO R4 Minima case, You need to prepare
debug adapter separately. A 5V-compatible CMSIS-DAP adapter
adapts to this board.

### Building & Flashing

You can build and flash with `west flash` command (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_minima samples/basic/blinky
west flash
```

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_wifi samples/basic/blinky
west flash
```

### Debugging

Debugging can be done with `west debug` command.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_minima samples/basic/blinky
west debug
```

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_wifi samples/basic/blinky
west debug
```

#### Using pyOCD

Various debug adapters, including cmsis-dap probes, can debug the Arduino UNO R4 with pyOCD.
The default configuration uses the pyOCD for debugging.
You must install CMSIS-Pack when flashing or debugging Arduino UNO R4 Minima with pyOCD.
If not installed yet, execute the following command to install CMSIS-Pack for Arduino UNO R4.

```shell
pyocd pack install r7fa4m1ab
```

### Restoring Arduino Bootloader

If you corrupt the Arduino bootloader, you can restore it with the following command.

```shell
wget https://raw.githubusercontent.com/arduino/ArduinoCore-renesas/main/bootloaders/UNO_R4/dfu_minima.hex
pyocd flash -e sector -a 0x0 -t r7fa4m1ab dfu_minima.hex
```

```shell
wget https://raw.githubusercontent.com/arduino/ArduinoCore-renesas/main/bootloaders/UNO_R4/dfu_wifi.hex
pyocd flash -e sector -a 0x0 -t r7fa4m1ab dfu_wifi.hex
```
