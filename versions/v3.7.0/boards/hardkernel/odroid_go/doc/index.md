---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/hardkernel/odroid_go/doc/index.html
original_path: boards/hardkernel/odroid_go/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ODROID-GO

## Overview

ODROID-GO Game Kit is a “Do it yourself” (“DIY”) portable game console by
HardKernel. It features a custom ESP32-WROVER with 16 MB flash and it operates
from 80 MHz - 240 MHz [[1]](#id3).

The features include the following:

- Dual core Xtensa microprocessor (LX6), running at 80 - 240MHz
- 4 MB of PSRAM
- 802.11b/g/n/e/i
- Bluetooth v4.2 BR/EDR and BLE
- 2.4 inch 320x240 TFT LCD
- Speaker
- Micro SD card slot
- Micro USB port (battery charging and USB\_UART data communication
- Input Buttons (Menu, Volume, Select, Start, A, B, Direction Pad)
- Expansion port (I2C, GPIO, SPI)
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)

![ODROID-GO](../../../../_images/odroid_go.jpg)

ODROID-Go Game Kit

### External Connector

| PIN # | Signal Name | ESP32-WROVER Functions |
| --- | --- | --- |
| 1 | GND | GND |
| 2 | VSPI.SCK (IO18) | GPIO18, VSPICLK |
| 3 | IO12 | GPIO12 |
| 4 | IO15 | GPIO15, ADC2\_CH3 |
| 5 | IO4 | GPIO4, ADC2\_CH0 |
| 6 | P3V3 | 3.3 V |
| 7 | VSPI.MISO (IO19) | GPIO19, VSPIQ |
| 8 | VSPI.MOSI (IO23) | GPIO23, VSPID |
| 9 | N.C | N/A |
| 10 | VBUS | USB VBUS (5V) |

### Supported Features

The Zephyr odroid\_go board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| PINMUX | on-chip | pinmux |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |

## System requirements

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

### ESP-IDF bootloader

The board is using the ESP-IDF bootloader as the default 2nd stage bootloader.
It is build as a subproject at each application build. No further attention
is expected from the user.

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
west build -b odroid_go --sysbuild samples/hello_world
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
For that reason, images can be build one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `odroid_go` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world)
application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world
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
Hello World! odroid_go
```

## Debugging

As with much custom hardware, the ESP32 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[2]](#id5)

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b odroid_go/esp32/procpu samples/hello_world
west debug
```

## References

[[2](#id6)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)

[[1](#id2)]

[https://wiki.odroid.com/odroid\_go/odroid\_go](https://wiki.odroid.com/odroid_go/odroid_go)
