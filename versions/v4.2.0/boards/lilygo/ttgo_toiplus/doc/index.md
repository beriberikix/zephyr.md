---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/lilygo/ttgo_toiplus/doc/index.html
original_path: boards/lilygo/ttgo_toiplus/doc/index.html
---

# TTGO T-OI-PLUS

Board Overview

[![../../../../_images/ttgo_toiplus.webp](../../../../_images/ttgo_toiplus.webp)
](../../../../_images/ttgo_toiplus.webp)

TTGO T-OI-PLUS

Name:
:   `ttgo_toiplus`

Vendor:
:   Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

Architecture:
:   riscv

SoC:
:   esp32c3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lilygo/ttgo_toiplus/doc/index.rst/../..)

## Overview

Lilygo TTGO T-OI-PLUS is an mini IoT development board based on
Espressif’s ESP32-C3 WiFi/Bluetooth dual-mode chip.

It features the following integrated components:

- ESP32-C3 SoC (RISC-V 160MHz single core, 400KB SRAM, Wi-Fi, Bluetooth)
- on board Grove connector
- USB-C connector for power and communication (on board serial)
- optional 18340 Li-ion battery holder
- LED

## Functional Description

This board is based on the ESP32-C3 with 4MB of flash, WiFi and BLE support. It
has an USB-C port for programming and debugging, integrated battery charging
and an Grove connector.

### Connections and IOs

The `ttgo_toiplus` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

(Note: the above UART interface also supports connecting through USB.)

## Start Application Development

Before powering up your Lilygo TTGO T-OI-PLUS, please make sure that the board is in good
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
west build -b ttgo_toiplus --sysbuild samples/hello_world
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
west build -b ttgo_toiplus samples/hello_world
```

The usual `flash` target will work with the `ttgo_toiplus` board target.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b ttgo_toiplus samples/hello_world
west flash
```

You can also open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! ttgo_toiplus
```

### Sample applications

The following samples will run out of the box on the TTGO T-OI-PLUS board.

To build the blinky sample:

```shell
# From the root of the zephyr repository
west build -b ttgo_toiplus samples/basic/blinky
```

To build the bluetooth beacon sample:

```shell
# From the root of the zephyr repository
west build -b ttgo_toiplus samples/bluetooth/beacon
```

## Related Documents
