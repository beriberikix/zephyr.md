---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/lilygo/ttgo_lora32/doc/index.html
original_path: boards/lilygo/ttgo_lora32/doc/index.html
---

# TTGO LoRa32

Board Overview

[![../../../../_images/ttgo_lora32.webp](../../../../_images/ttgo_lora32.webp)
](../../../../_images/ttgo_lora32.webp)

TTGO LoRa32

Name:
:   `ttgo_lora32`

Vendor:
:   Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lilygo/ttgo_lora32/doc/index.rst/../..)

## Overview

The Lilygo TTGO LoRa32 is a development board for LoRa applications based on the ESP32-PICO-D4.

It’s available in two versions supporting two different frequency ranges and features the following integrated components:

- ESP32-PICO-D4 chip (240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi)
- SSD1306, 128x64 px, 0.96” screen
- SX1278 (433MHz) or SX1276 (868/915/923MHz) LoRa radio frontend
- JST GH 2-pin battery connector
- TF card slot

Some of the ESP32 I/O pins are accessible on the board’s pin headers.

## Functional Description

The following table below describes the key components, interfaces, and controls
of the Lilygo TTGO LoRa32 board.

| Key Component | Description |
| --- | --- |
| ESP32-PICO-D4 | This [ESP32-PICO-D4](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf) module provides complete Wi-Fi and Bluetooth functionalities and integrates a 4-MB SPI flash. |
| Diagnostic LED | One user LED connected to the GPIO pin. |
| USB Port | USB interface. Power supply for the board as well as the serial communication interface between a computer and the board. Micro-USB type connector. |
| Power Switch | Sliding power switch. |
| OLED display | Built-in OLED display ([SSD1306](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf), 0.96”, 128x64 px) controlled by I2C interface |
| SX1276/SX1278 | LoRa radio frontend chip, connected via SPI. Use SX1276 for 433MHz and SX1276 for 868/915/923MHz. |
| TF card slot | TF card slot wired to the SDHC interface of the MCU. |

## Start Application Development

Before powering up your Lilygo TTGO LoRa32, please make sure that the board is in good
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
bootstrap the board with the ESP32-PICO-D4 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b ttgo_lora32/esp32/procpu --sysbuild samples/hello_world
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
west build -b ttgo_lora32/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `ttgo_lora32` board target.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b ttgo_lora32/esp32/procpu samples/hello_world
west flash
```

The default baud rate for the Lilygo TTGO LoRa32 is set to 1500000bps. If experiencing issues when flashing,
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
Hello World! ttgo_lora32
```

### Code samples

The following sample applications will work out of the box with this board:

- [LoRa send](../../../../samples/drivers/lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")
- [LoRa receive](../../../../samples/drivers/lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")
- [File system manipulation](../../../../samples/subsys/fs/fs_sample/README.md#fs "Use file system API with various filesystems and storage devices.")
- [Character frame buffer](../../../../samples/subsys/display/cfb/README.md#character-frame-buffer "Display character strings using the Character Frame Buffer (CFB).")

## Debugging

Lilygo TTGO LoRa32 debugging is not supported due to pinout limitations.

## Related Documents

- [Lilygo TTGO LoRa32 schematic](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/schematic/T3_V1.6.1.pdf) (PDF)
- [Lilygo TTGO LoRa32 documentation](https://www.lilygo.cc/products/lora3)
- [Lilygo github repo](https://github.com/Xinyuan-LilyGo)
- [ESP32-PICO-D4 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf) (PDF)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) (PDF)
- [ESP32 Hardware Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html)
