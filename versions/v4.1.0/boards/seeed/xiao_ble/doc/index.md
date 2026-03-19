---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seeed/xiao_ble/doc/index.html
original_path: boards/seeed/xiao_ble/doc/index.html
---

# XIAO BLE (Sense)

Board Overview

[![../../../../_images/xiao_ble.jpg](../../../../_images/xiao_ble.jpg)
](../../../../_images/xiao_ble.jpg)

XIAO BLE (Sense)

Name:
:   `xiao_ble`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/xiao_ble/doc/index.rst/../..)

## Overview

The Seeed XIAO BLE (Sense) is a tiny (21 mm x 17.5 mm) Nordic Semiconductor
nRF52840 ARM Cortex-M4F development board with onboard LEDs, USB port, QSPI
flash, battery charger, and range of I/O broken out into 14 pins.

## Hardware

- Nordic nRF52840 Cortex-M4F processor at 64MHz
- 2MB QSPI Flash
- RGB LED
- USB Type-C Connector, nRF52840 acting as USB device
- Battery charger BQ25101
- Reset button
- Bluetooth antenna
- LSM6DS3TR-C 6D IMU (3D accelerometer and 3D gyroscope) (XIAO BLE Sense only)
- PDM microphone (XIAO BLE Sense only)

### Supported Features

The `xiao_ble` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [XIAO BLE wiki](https://wiki.seeedstudio.com/XIAO_BLE/) [[1]](#id2) has detailed information about the board including
[pinouts](https://wiki.seeedstudio.com/XIAO_BLE/#hardware-overview) [[2]](#id4) and the [schematic](https://wiki.seeedstudio.com/XIAO_BLE/#resources) [[3]](#id6).

#### LED

- LED1 (red) = P0.26
- LED2 (green) = P0.30
- LED3 (blue) = P0.06

## Programming and Debugging

The XIAO BLE ships with the [Adafruit nRF52 Bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader) [[5]](#id10) which supports flashing
using [UF2](https://github.com/microsoft/uf2) [[6]](#id12). Doing so allows easy flashing of new images, but does not support
debugging the device. For debugging please use [External Debugger](#external-debugger).

### UF2 Flashing

To enter the bootloader, connect the USB port of the XIAO BLE to your host, and
double tap the reset botton to the left of the USB connector. A mass storage
device named `XIAO BLE` should appear on the host. Using the command line, or
your file manager copy the `zephyr/zephyr.uf2` file from your build to the base
of the `XIAO BLE` mass storage device. The XIAO BLE will automatically reset
and launch the newly flashed application.

### External Debugger

In order to support debugging the device, instead of using the bootloader, you
can use an [External Debug Probe](../../../../develop/flash_debug/probes.md#debug-probes). To flash and debug Zephyr
applications you need to use [Seeeduino XIAO Expansion Board](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/) [[4]](#id8) or solder an SWD
header onto the back side of the board.

For Segger J-Link debug probes, follow the instructions in the
[J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) page to install and configure all the
necessary software.

#### Flashing

Setup and connect a supported debug probe (JLink, instructions at [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) or
BlackMagic Probe). Then build and flash applications as
usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board XIAO BLE
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way. Just add
`CONFIG_BOOT_DELAY=5000` to the configuration, so that USB CDC ACM is
initialized before any text is printed, as below:

XIAO BLEXIAO BLE Sense

```shell
# From the root of the zephyr repository
west build -b xiao_ble samples/hello_world -- -DCONFIG_BOOT_DELAY=5000
west flash
```

```shell
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840/sense samples/hello_world -- -DCONFIG_BOOT_DELAY=5000
west flash
```

#### Debugging

Refer to the [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) page to learn about debugging
boards with a Segger IC.

Debugging using a BlackMagic Probe is also supported.

## Testing the LEDs in the XIAO BLE (Sense)

There is a sample that allows to test that LEDs on the board are working
properly with Zephyr:

XIAO BLEXIAO BLE Sense

```shell
# From the root of the zephyr repository
west build -b xiao_ble samples/basic/blinky
west flash
```

```shell
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840/sense samples/basic/blinky
west flash
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The LED definitions can be found in
[boards/seeed/xiao\_ble/xiao\_ble\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_ble/xiao_ble_common.dtsi).

## Testing shell over USB in the XIAO BLE (Sense)

There is a sample that allows to test shell interface over USB CDC ACM interface
with Zephyr:

XIAO BLEXIAO BLE Sense

```shell
# From the root of the zephyr repository
west build -b xiao_ble samples/subsys/shell/shell_module
west flash
```

```shell
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840/sense samples/subsys/shell/shell_module
west flash
```

## References

[[1](#id3)]

[https://wiki.seeedstudio.com/XIAO\_BLE/](https://wiki.seeedstudio.com/XIAO_BLE/)

[[2](#id5)]

[https://wiki.seeedstudio.com/XIAO\_BLE/#hardware-overview](https://wiki.seeedstudio.com/XIAO_BLE/#hardware-overview)

[[3](#id7)]

[https://wiki.seeedstudio.com/XIAO\_BLE/#resources](https://wiki.seeedstudio.com/XIAO_BLE/#resources)

[[4](#id9)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/)

[[5](#id11)]

[https://github.com/adafruit/Adafruit\_nRF52\_Bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader)

[[6](#id13)]

[https://github.com/microsoft/uf2](https://github.com/microsoft/uf2)
