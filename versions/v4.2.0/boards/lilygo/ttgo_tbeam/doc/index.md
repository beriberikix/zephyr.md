---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/lilygo/ttgo_tbeam/doc/index.html
original_path: boards/lilygo/ttgo_tbeam/doc/index.html
---

# TTGO TBeam

Board Overview

[![../../../../_images/ttgo_tbeam.webp](../../../../_images/ttgo_tbeam.webp)
](../../../../_images/ttgo_tbeam.webp)

TTGO TBeam

Name:
:   `ttgo_tbeam`

Vendor:
:   Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lilygo/ttgo_tbeam/doc/index.rst/../..)

## Overview

The Lilygo TTGO TBeam, is an ESP32-based development board for LoRa applications.

It’s available in two versions supporting two different frequency ranges and features the following integrated components:

- ESP32-PICO-D4 chip (240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi)
- SSD1306, 128x64 px, 0.96” screen (optional)
- SX1278 (433MHz) or SX1276 (868/915/923MHz) LoRa radio frontend (optional, with SMA or IPEX connector)
- NEO-6M or NEO-M8N GNSS module
- X-Powers AXP2101 PMIC
- JST GH 2-pin battery connector
- 18650 Li-Ion battery clip

Some of the ESP32 I/O pins are accessible on the board’s pin headers.

## Hardware

### Supported Features

The `ttgo_tbeam` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Start Application Development

Before powering up your Lilygo TTGO TBeam, please make sure that the board is in good
condition with no obvious signs of damage.

## System requirements

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order to work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Building & Flashing

The `ttgo_tbeam` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Simple boot

The board could be loaded using a single binary image, without 2nd stage bootloader.
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

The sysbuild makes it possible to build and flash all necessary images needed to
bootstrap the board with the ESP32-PICO-D4 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b ttgo_tbeam/esp32/procpu --sysbuild samples/hello_world
```

By default, the ESP32-PICO-D4 sysbuild creates bootloader (MCUboot) and application
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
west build -b ttgo_tbeam/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `ttgo_tbeam` board target.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b ttgo_tbeam/esp32/procpu samples/hello_world
west flash
```

The default baud rate for the Lilygo TTGO TBeam is set to 1500000bps. If experiencing issues when flashing,
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
Hello World! ttgo_tbeam/esp32/procpu
```

### Code samples

The following sample applications will work out of the box with this board:

- [LoRa send](../../../../samples/drivers/lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")
- [LoRa receive](../../../../samples/drivers/lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")
- [GNSS](../../../../samples/drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")
- [Wi-Fi shell](../../../../samples/net/wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")
- [Character frame buffer](../../../../samples/subsys/display/cfb/README.md#character-frame-buffer "Display character strings using the Character Frame Buffer (CFB).")
- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")

## Debugging

Lilygo TTGO TBeam debugging is not supported due to pinout limitations.

## Related Documents

- [Lilygo TTGO TBeam schematic](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/schematic/LilyGo_TBeam_V1.2.pdf) (PDF)
- [Lilygo TTGO TBeam documentation](https://www.lilygo.cc/products/t-beam-v1-1-esp32-lora-module)
- [Lilygo github repo](https://github.com/Xinyuan-LilyGo)
- [ESP32-PICO-D4 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf) (PDF)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) (PDF)
- [ESP32 Hardware Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html)
- [SX127x Datasheet](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276#documentation)
- [SSD1306 Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf) (PDF)
- [NEO-6M Datasheet](https://content.u-blox.com/sites/default/files/products/documents/NEO-6_DataSheet_%28GPS.G6-HW-09005%29.pdf) (PDF)
- [NEO-N8M Datasheet](https://content.u-blox.com/sites/default/files/NEO-M8-FW3_DataSheet_UBX-15031086.pdf) (PDF)
