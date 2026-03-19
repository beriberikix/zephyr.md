---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/qt_py_esp32s3/doc/index.html
original_path: boards/adafruit/qt_py_esp32s3/doc/index.html
---

# QT Py ESP32-S3

Board Overview

[![../../../../_images/adafruit_qt_py_esp32s3.webp](../../../../_images/adafruit_qt_py_esp32s3.webp)
](../../../../_images/adafruit_qt_py_esp32s3.webp)

QT Py ESP32-S3

Name:
:   `adafruit_qt_py_esp32s3`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/qt_py_esp32s3/doc/index.rst/../..)

## Overview

An Adafruit based Xiao compatible board based on the ESP32-S3, which is great
for IoT projects and prototyping with new sensors.

For more details see the [Adafruit QT Py ESP32S3](https://www.adafruit.com/product/5426) [[1]](#id2) product page.

## Hardware

This board comes in 2 variants, both based on the ESP32-S3 with WiFi and BLE
support. The default variant supporting 8MB of flash with no PSRAM, while the
`psram` variant supporting 4MB of flash with 2MB of PSRAM. Both boards have a
USB-C port for programming and debugging and is based on a standard XIAO 14
pin pinout.

In addition to the Xiao compatible pinout, it also has a RGB NeoPixel for
status and debugging, a reset button, and a button for entering the ROM
bootloader or user input. Like many other Adafruit boards, it has a
[SparkFun Qwiic](https://www.sparkfun.com/qwiic) [[4]](#id8)-compatible [STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt) [[5]](#id10) connector for the I2C bus so you
don’t even need to solder.

ESP32-S3 is a low-power MCU-based system on a chip (SoC) with integrated
2.4 GHz Wi-Fi and Bluetooth® Low Energy (Bluetooth LE). It consists of
high-performance dual-core microprocessor (Xtensa® 32-bit LX7), a low power
coprocessor, a Wi-Fi baseband, a Bluetooth LE baseband, RF module, and
numerous peripherals.

### Supported Features

The `adafruit_qt_py_esp32s3` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the
command below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

### Simple boot

The board could be loaded using the single binary image, without 2nd stage
bootloader. It is the default option when building the application without
additional configuration.

Note

Simple boot does not provide any security features nor OTA updates.

### MCUboot bootloader

User may choose to use MCUboot bootloader instead. In that case the bootloader
must be built (and flashed) at least once.

There are two options to be used when building an application:

1. Sysbuild
2. Manual build

Note

User can select the MCUboot bootloader by adding the following line
to the board default configuration file.

```cfg
CONFIG_BOOTLOADER_MCUBOOT=y
```

### Sysbuild

The sysbuild makes possible to build and flash all necessary images needed to
bootstrap the board with the ESP32 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b adafruit_qt_py_esp32s3 --sysbuild samples/hello_world
```

By default, the ESP32 sysbuild creates bootloader (MCUboot) and application
images. But it can be configured to create other kind of images.

Build directory structure created by sysbuild is different from traditional
Zephyr build. Output is structured by the domain subdirectories:

```text
build/
├── hello_world
│   └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
├── mcuboot
│    └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
└── domains.yaml
```

Note

With `--sysbuild` option the bootloader will be re-build and re-flash
every time the pristine build is used.

For more information about the system build please read the [Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild) documentation.

### Manual build

During the development cycle, it is intended to build & flash as quickly possible.
For that reason, images can be built one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

QT Py ESP32S3QT Py ESP32S3 with PSRAM

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3/esp32s3/procpu samples/hello_world
```

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3@psram/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `adafruit_qt_py_esp32s3` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

QT Py ESP32S3QT Py ESP32S3 with PSRAM

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3/esp32s3/procpu samples/hello_world
west flash
```

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3@psram/esp32s3/procpu samples/hello_world
west flash
```

Open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! adafruit_qt_py_esp32s3/esp32s3/procpu
```

## Debugging

ESP32-S3 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[3]](#id6).

ESP32-S3 has a built-in JTAG circuitry and can be debugged without any
additional chip. Only an USB cable connected to the D+/D- pins is necessary.

Further documentation can be obtained from the SoC vendor
in [JTAG debugging for ESP32-S3](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/) [[2]](#id4).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

QT Py ESP32S3QT Py ESP32S3 with PSRAM

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3/esp32s3/procpu samples/hello_world
west debug
```

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3@psram/esp32s3/procpu samples/hello_world
west debug
```

You can debug an application in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

QT Py ESP32S3QT Py ESP32S3 with PSRAM

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3/esp32s3/procpu samples/hello_world
west debug
```

```shell
# From the root of the zephyr repository
west build -b adafruit_qt_py_esp32s3@psram/esp32s3/procpu samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.adafruit.com/product/5426](https://www.adafruit.com/product/5426)

[[2](#id5)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/)

[[3](#id7)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)

[[4](#id9)]

[https://www.sparkfun.com/qwiic](https://www.sparkfun.com/qwiic)

[[5](#id11)]

[https://learn.adafruit.com/introducing-adafruit-stemma-qt](https://learn.adafruit.com/introducing-adafruit-stemma-qt)
