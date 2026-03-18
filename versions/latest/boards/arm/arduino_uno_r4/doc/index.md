---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/arduino_uno_r4/doc/index.html
original_path: boards/arm/arduino_uno_r4/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Arduino UNO R4 Minima

## Overview

The Arduino UNO R4 Minima is a development board featuring the Renesas RA4M1 SoC
in the Arduino form factor and is compatible with traditional Arduino.

## Programming and debugging

### Building & Flashing

You can build and flash an application in the usual way (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_minima samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4_minima samples/basic/blinky
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
