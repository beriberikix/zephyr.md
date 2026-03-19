---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/olimex/olimex_esp32_evb/doc/index.html
original_path: boards/olimex/olimex_esp32_evb/doc/index.html
---

# ESP32-EVB

Board Overview

[![../../../../_images/ESP32-EVB.jpg](../../../../_images/ESP32-EVB.jpg)
](../../../../_images/ESP32-EVB.jpg)

ESP32-EVB

Name:
:   `olimex_esp32_evb`

Vendor:
:   OLIMEX Ltd.

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/olimex/olimex_esp32_evb/doc/index.rst/../..)

## Overview

The Olimex ESP32-EVB is an OSHW certified, open-source IoT board based on the
Espressif ESP32-WROOM-32E/UE module. It has a wired 100Mbit/s Ethernet Interface,
Bluetooth LE, WiFi, infrared remote control, and CAN connectivity. Two relays
allows switching power appliances on and off.

The board can operate from a single LiPo backup battery as it has an internal
LiPo battery charger. There is no step-up converter, so relays, CAN, and USB
power does not work when running off battery.

## Hardware

- ESP32-WROOM-32E/UE module with 4MB flash.
- On-board programmer, CH340T USB-to-UART
- WiFi, Bluetooth LE connectivity.
- 100Mbit/s Ethernet interface, Microchip LAN8710A PHY.
- MicroSD card slot.
- 2 x 10A/250VAC (15A/120VAC 15A/24VDC) relays with connectors and status LEDs.
- CAN interface, Microchip MCP2562-E high-speed CAN transceiver.
- IR receiver and transmitter, up to 5 meters distance.
- BL4054B LiPo battery charger with status LEDs for stand-alone operation during
  power outages.
- Power jack for external 5VDC power supply.
- Univeral EXTension (UEXT) connector for connecting UEXT modules.
- User push button.
- 40 pin GPIO connector with all ESP32 pins.

For more information about the ESP32-EVB and the ESP32-WROOM-32E/UE module, see
these reference documents:

- [ESP32-EVB Website](https://www.olimex.com/Products/IoT/ESP32/ESP32-EVB/open-source-hardware) [[1]](#id2)
- [ESP32-EVB Schematic](https://github.com/OLIMEX/ESP32-EVB/raw/master/HARDWARE/REV-I/ESP32-EVB_Rev_I.pdf) [[2]](#id4)
- [ESP32-EVB GitHub Repository](https://github.com/OLIMEX/ESP32-EVB) [[3]](#id6)
- [ESP32-WROOM32-E/UE Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf) [[4]](#id8)

## Supported Features

The `olimex_esp32_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

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
bootstrap the board with the ESP32 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b olimex_esp32_evb --sysbuild samples/hello_world
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

```shell
# From the root of the zephyr repository
west build -b olimex_esp32_evb/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `olimex_esp32_evb` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b olimex_esp32_evb/esp32/procpu samples/hello_world
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
Hello World! olimex_esp32_evb
```

## Debugging

As with much custom hardware, the ESP32 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[5]](#id10).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_esp32_evb/esp32/procpu samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_esp32_evb/esp32/procpu samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.olimex.com/Products/IoT/ESP32/ESP32-EVB/open-source-hardware](https://www.olimex.com/Products/IoT/ESP32/ESP32-EVB/open-source-hardware)

[[2](#id5)]

[https://github.com/OLIMEX/ESP32-EVB/raw/master/HARDWARE/REV-I/ESP32-EVB\_Rev\_I.pdf](https://github.com/OLIMEX/ESP32-EVB/raw/master/HARDWARE/REV-I/ESP32-EVB_Rev_I.pdf)

[[3](#id7)]

[https://github.com/OLIMEX/ESP32-EVB](https://github.com/OLIMEX/ESP32-EVB)

[[4](#id9)]

[https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e\_esp32-wroom-32ue\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)

[[5](#id11)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
