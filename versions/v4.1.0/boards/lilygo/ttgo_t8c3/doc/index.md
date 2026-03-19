---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/lilygo/ttgo_t8c3/doc/index.html
original_path: boards/lilygo/ttgo_t8c3/doc/index.html
---

# TTGO T8-C3

Board Overview

[![../../../../_images/ttgo_t8c3.webp](../../../../_images/ttgo_t8c3.webp)
](../../../../_images/ttgo_t8c3.webp)

TTGO T8-C3

Name:
:   `ttgo_t8c3`

Vendor:
:   Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

Architecture:
:   riscv

SoC:
:   esp32c3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lilygo/ttgo_t8c3/doc/index.rst/../..)

## Overview

Lilygo TTGO T8-C3 is an IoT mini development board based on the
Espressif ESP32-C3 WiFi/Bluetooth dual-mode chip.

It features the following integrated components:

- ESP32-C3 chip (160MHz single core, 400KB SRAM, Wi-Fi)
- on board antenna and IPEX connector
- USB-C connector for power and communication
- JST GH 2-pin battery connector
- LED

## Functional Description

This board is based on the ESP32-C3 with 4MB of flash, WiFi and BLE support. It
has an USB-C port for programming and debugging, integrated battery charging
and an on-board antenna. The fitted U.FL external antenna connector can be
enabled by moving a 0-ohm resistor.

### Connections and IOs

The `ttgo_t8c3` board target supports the following hardware features:

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

## Start Application Development

Before powering up your Lilygo TTGO T8-C3, please make sure that the board is in good
condition with no obvious signs of damage.

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

### Simple boot

The board could be loaded using the single binary image, without 2nd stage bootloader.
It is the default option when building the application without additional configuration.

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
bootstrap the board with the ESP32-C3 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b ttgo_t8c3 --sysbuild samples/hello_world
```

By default, the ESP32-C3 sysbuild creates bootloader (MCUboot) and application
images. But it can be configured to create other kind of images.

Build directory structure created by sysbuild is different from traditional
Zephyr build. Output is structured by the domain subdirectories:

```text
build/
├── hello_world
│   └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
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

```shell
# From the root of the zephyr repository
west build -b ttgo_t8c3 samples/hello_world
```

The usual `flash` target will work with the `ttgo_t8c3` board target.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b ttgo_t8c3 samples/hello_world
west flash
```

The default baud rate for the Lilygo TTGO T8-C3 is set to 1500000bps. If experiencing issues when flashing,
try using different values by using `--esp-baud-rate <BAUD>` option during
`west flash` (e.g. `west flash --esp-baud-rate 115200`).

You can also open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! ttgo_t8c3
```

### Sample applications

The following samples will run out of the box on the TTGO T8-C3 board.

To build the blinky sample:

```shell
# From the root of the zephyr repository
west build -b ttgo_t8c3 samples/basic/blinky
```

To build the bluetooth beacon sample:

```shell
# From the root of the zephyr repository
west build -b ttgo_t8c3 samples/bluetooth/beacon
```

## Related Documents
