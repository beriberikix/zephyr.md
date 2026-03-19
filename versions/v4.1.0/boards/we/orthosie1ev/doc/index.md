---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/we/orthosie1ev/doc/index.html
original_path: boards/we/orthosie1ev/doc/index.html
---

# Orthosie-I-EV

Board Overview

[![../../../../_images/we_orthosie1ev.webp](../../../../_images/we_orthosie1ev.webp)
](../../../../_images/we_orthosie1ev.webp)

Orthosie-I-EV

Name:
:   `we_orthosie1ev`

Vendor:
:   Würth Elektronik GmbH.

Architecture:
:   riscv

SoC:
:   esp32c3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/we/orthosie1ev/doc/index.rst/../..)

## Overview

Orthosie-I-EV is an entry-level development board based on Orthosie-I,
a module named for its small size. This board integrates complete Wi-Fi and Bluetooth® Low Energy functions.
For more information, check [Orthosie-I Website](https://www.we-online.com/en/components/products/ORTHOSIE-I) [[1]](#id2).

## Hardware

ESP32-C3 is a single-core Wi-Fi and Bluetooth 5 (LE) microcontroller SoC,
based on the open-source RISC-V architecture. It strikes the right balance of power,
I/O capabilities and security, thus offering the optimal cost-effective
solution for connected devices.
The availability of Wi-Fi and Bluetooth 5 (LE) connectivity not only makes the device configuration easy,
but it also facilitates a variety of use-cases based on dual connectivity.

The features include the following:

- 32-bit core RISC-V microcontroller with a maximum clock speed of 160 MHz
- 400 KB of internal RAM
- 802.11b/g/n/e/i
- A Bluetooth LE subsystem that supports features of Bluetooth 5 and Bluetooth Mesh
- Various peripherals:

  - 12-bit ADC with up to 6 channels
  - TWAI compatible with CAN bus 2.0
  - Temperature sensor
  - 3x SPI
  - 1x I2S
  - 1x I2C
  - 2x UART
  - LED PWM with up to 6 channels
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)

For more information, check the datasheet at [ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32-C3 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf) [[3]](#id6).

### Supported Features

The `we_orthosie1ev` board supports the hardware features listed below.

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
west build -b orthosie1ev --sysbuild samples/hello_world
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
west build -b orthosie1ev samples/hello_world
```

The usual `flash` target will work with the `orthosie1ev` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b orthosie1ev samples/hello_world
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
Hello World! orthosie1ev
```

## Debugging

As with much custom hardware, the ESP32-C3 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[4]](#id8).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b orthosie1ev samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b orthosie1ev samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.we-online.com/en/components/products/ORTHOSIE-I](https://www.we-online.com/en/components/products/ORTHOSIE-I)

[[2](#id5)]

[https://www.espressif.com/sites/default/files/documentation/esp32-c3\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)

[[3](#id7)]

[https://espressif.com/sites/default/files/documentation/esp32-c3\_technical\_reference\_manual\_en.pdf](https://espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)

[[4](#id9)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
