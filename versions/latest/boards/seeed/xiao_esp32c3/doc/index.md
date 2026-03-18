---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/seeed/xiao_esp32c3/doc/index.html
original_path: boards/seeed/xiao_esp32c3/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# XIAO ESP32C3

## Overview

Seeed Studio XIAO ESP32C3 is an IoT mini development board based on the
Espressif ESP32-C3 WiFi/Bluetooth dual-mode chip.

For more details see the [Seeed Studio XIAO ESP32C3](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started) [[1]](#id4) wiki page.

![XIAO ESP32C3](../../../../_images/xiao_esp32c.jpg)

XIAO ESP32C3

## Hardware

This board is based on the ESP32-C3 with 4MB of flash, WiFi and BLE support. It
has an USB-C port for programming and debugging, integrated battery charging
and an U.FL external antenna connector. It is based on a standard XIAO 14 pin
pinout.

### Supported Features

The XIAO ESP32C3 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| PMP | on-chip | arch/riscv |
| INTMTRX | on-chip | intc\_esp32c3 |
| PINMUX | on-chip | pinctrl\_esp32 |
| USB UART | on-chip | serial\_esp32\_usb |
| GPIO | on-chip | gpio\_esp32 |
| UART | on-chip | uart\_esp32 |
| I2C | on-chip | i2c\_esp32 |
| SPI | on-chip | spi\_esp32\_spim |
| TWAI | on-chip | can\_esp32\_twai |

### Connections and IOs

The board uses a standard XIAO pinout, the default pin mapping is the following:

![XIAO ESP32C3 Pinout](../../../../_images/xiao_esp32c3_pinout.jpg)

XIAO ESP32C3 Pinout

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

### Simple boot

The board could be loaded using the single binary image, without 2nd stage bootloader.
It is the default option when building the application without additional configuration.

Note

Simple boot does not provide any security features nor OTA updates.

### MCUboot bootloader

User may choose to use MCUboot bootloader instead. In that case the bootloader
must be build (and flash) at least once.

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
west build -b xiao_esp32c3 --sysbuild samples/hello_world
```

By default, the ESP32 sysbuild creates bootloader (MCUboot) and application
images. But it can be configured to create other kind of images.

Build directory structure created by Sysbuild is different from traditional
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
For that reason, images can be build one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

For the `Hello, world!` application, follow the instructions below.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c3 samples/hello_world
west flash
```

Since the Zephyr console is by default on the usb\_serial device, we use
the espressif monitor to view.

```shell
$ west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! xiao_esp32c3
```

## Debugging

As with much custom hardware, the ESP32 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[2]](#id6)

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c3 samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c3 samples/hello_world
west debug
```

## References

[[1](#id5)]

[https://wiki.seeedstudio.com/XIAO\_ESP32C3\_Getting\_Started](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started)

[[2](#id7)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
