---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/espressif/esp32s2_devkitc/doc/index.html
original_path: boards/espressif/esp32s2_devkitc/doc/index.html
---

# ESP32-S2-DevKitC

Board Overview

[![../../../../_images/esp32s2_devkitc.webp](../../../../_images/esp32s2_devkitc.webp)
](../../../../_images/esp32s2_devkitc.webp)

ESP32-S2-DevKitC

Vendor:
:   Espressif Systems

Architecture:
:   xtensa

SoC:
:   esp32s2

## Overview

ESP32-S2-DevKitC is an entry-level development board. This board integrates complete Wi-Fi functions.
Most of the I/O pins are broken out to the pin headers on both sides for easy interfacing.
Developers can either connect peripherals with jumper wires or mount ESP32-S2-DevKitC on a breadboard.
For more information, check [ESP32-S2-DevKitC](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-saola-1-v1.2.html) [[1]](#id2).

## Hardware

ESP32-S2 is a highly integrated, low-power, single-core Wi-Fi Microcontroller SoC, designed to be secure and
cost-effective, with a high performance and a rich set of IO capabilities.

The features include the following:

- RSA-3072-based secure boot
- AES-XTS-256-based flash encryption
- Protected private key and device secrets from software access
- Cryptographic accelerators for enhanced performance
- Protection against physical fault injection attacks
- Various peripherals:

  - 43x programmable GPIOs
  - 14x configurable capacitive touch GPIOs
  - USB OTG
  - LCD interface
  - camera interface
  - SPI
  - I2S
  - UART
  - ADC
  - DAC
  - LED PWM with up to 8 channels

For more information, check the datasheet at [ESP32-S2 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32-S2 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32-s2_technical_reference_manual_en.pdf) [[3]](#id6).

### Supported Features

Current Zephyr’s ESP32-S2-devkitc board supports the following features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| PINMUX | on-chip | pinmux |
| USB-JTAG | on-chip | hardware interface |
| SPI Master | on-chip | spi |
| Timers | on-chip | counter |
| Watchdog | on-chip | watchdog |
| TRNG | on-chip | entropy |
| LEDC | on-chip | pwm |
| PCNT | on-chip | qdec |
| SPI DMA | on-chip | spi |
| ADC | on-chip | adc |
| DAC | on-chip | dac |
| Wi-Fi | on-chip |  |

### System requirements

#### Prerequisites

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
west build -b esp32s2_devkitc --sysbuild samples/hello_world
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
west build -b esp32s2_devkitc samples/hello_world
```

The usual `flash` target will work with the `esp32s2_devkitc` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32s2_devkitc samples/hello_world
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
Hello World! esp32s2_devkitc
```

## Debugging

ESP32-S2 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[5]](#id10).

The following table shows the pin mapping between ESP32-S2 board and JTAG interface.

| ESP32 pin | JTAG pin |
| --- | --- |
| MTDO / GPIO40 | TDO |
| MTDI / GPIO41 | TDI |
| MTCK / GPIO39 | TCK |
| MTMS / GPIO42 | TMS |

Further documentation can be obtained from the SoC vendor in [JTAG debugging for ESP32-S2](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/index.html) [[4]](#id8).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp32s2_devkitc samples/hello_world
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp32s2_devkitc samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-saola-1-v1.2.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-saola-1-v1.2.html)

[[2](#id5)]

[https://www.espressif.com/sites/default/files/documentation/esp32-s2\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf)

[[3](#id7)]

[https://espressif.com/sites/default/files/documentation/esp32-s2\_technical\_reference\_manual\_en.pdf](https://espressif.com/sites/default/files/documentation/esp32-s2_technical_reference_manual_en.pdf)

[[4](#id9)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/index.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/index.html)

[[5](#id11)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
