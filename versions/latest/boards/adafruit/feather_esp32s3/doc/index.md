---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adafruit/feather_esp32s3/doc/index.html
original_path: boards/adafruit/feather_esp32s3/doc/index.html
---

# Adafruit Feather ESP32S3

Board Overview

[![../../../../_images/adafruit_feather_esp32s3.webp](https://docs.zephyrproject.org/4.2.0/_images/adafruit_feather_esp32s3.webp)
](https://docs.zephyrproject.org/4.2.0/_images/adafruit_feather_esp32s3.webp)

Adafruit Feather ESP32S3

Name:
:   `adafruit_feather_esp32s3`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_esp32s3/doc/index.rst/../..)

## Overview

The Adafruit Feather ESP32-S3 is an ESP32-S3 development board in the Feather
standard layout, sharing peripheral placement with other devices labeled as
Feathers or FeatherWings. The board is equipped with an ESP32-S3 mini module, a
LiPo battery charger, a fuel gauge, a USB-C and Qwiic/STEMMA-QT connector. For
more information, check [Adafruit Feather ESP32-S3](https://www.adafruit.com/product/5323) [[1]](#id2).

## Hardware

- ESP32-S3 mini module, featuring the dual core 32-bit Xtensa Microprocessor
  (Tensilica LX7), running at up to 240MHz
- 512KB SRAM and either 8MB flash or 4MB flash + 2MB PSRAM, depending on the
  module variant
- USB-C directly connected to the ESP32-S3 for USB/UART and JTAG debugging
- LiPo connector and built-in battery charging when powered via USB-C
- MAX17048 fuel gauge for battery voltage and state-of-charge reporting
- Charging indicator LED, user LED, reset and boot buttons
- Built-in NeoPixel indicator RGB LED
- STEMMA QT connector for I2C devices, with switchable power for low-power mode

### Asymmetric Multiprocessing (AMP)

The ESP32-S3 SoC allows 2 different applications to be executed in asymmetric
multiprocessing. Due to its dual-core architecture, each core can be enabled to
execute customized tasks in stand-alone mode and/or exchanging data over OpenAMP
framework. See [Inter-Processor Communication (IPC)](../../../../samples/subsys/ipc/ipc.md#ipc) folder as code reference.

For more information, check the datasheet at [ESP32-S3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) [[7]](#id14).

### Supported Features

The current `adafruit_feather_esp32s3` board supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| PINMUX | on-chip | pinmux |
| USB-JTAG | on-chip | hardware interface |
| SPI Master | on-chip | spi |
| TWAI/CAN | on-chip | can |
| ADC | on-chip | adc |
| Timers | on-chip | counter |
| Watchdog | on-chip | watchdog |
| TRNG | on-chip | entropy |
| LEDC | on-chip | pwm |
| MCPWM | on-chip | pwm |
| PCNT | on-chip | qdec |
| GDMA | on-chip | dma |
| USB-CDC | on-chip | serial |
| Wi-Fi | on-chip |  |
| Bluetooth | on-chip |  |

### Connections and IOs

The [Adafruit Feather ESP32-S3 User Guide](https://learn.adafruit.com/adafruit-esp32-s3-feather) [[4]](#id8) has detailed information about the
board including [pinouts](https://learn.adafruit.com/adafruit-esp32-s3-feather/pinouts) [[5]](#id10) and the [schematic](https://learn.adafruit.com/adafruit-esp32-s3-feather/downloads) [[6]](#id12).

## Programming and Debugging

The `adafruit_feather_esp32s3` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **esp32** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the
command below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

### Building & Flashing

#### Simple boot

The board could be loaded using the single binary image, without 2nd stage
bootloader. It is the default option when building the application without
additional configuration.

Note

Simple boot does not provide any security features nor OTA updates.

#### MCUboot bootloader

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

#### Sysbuild

The sysbuild makes possible to build and flash all necessary images needed to
bootstrap the board with the ESP32-S3 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b adafruit_feather_esp32s3/esp32s3/procpu --sysbuild samples/hello_world
```

By default, the ESP32-S3 sysbuild creates bootloader (MCUboot) and application
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

For more information about the system build please read the [Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild)
documentation.

#### Manual build

During the development cycle, it is intended to build & flash as quickly
possible. For that reason, images can be build one at a time using traditional
build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s3/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `adafruit_feather_esp32s3` board
. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s3/esp32s3/procpu samples/hello_world
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
Hello World! adafruit_feather_esp32s3
```

### Debugging

ESP32-S3 support on OpenOCD is available upstream as of version 0.12.0. Download
and install OpenOCD from [OpenOCD](https://github.com/openocd-org/openocd) [[2]](#id4).

ESP32-S3 has a built-in JTAG circuitry and can be debugged without any
additional chip. Only an USB cable connected to the D+/D- pins is necessary.

Further documentation can be obtained from the SoC vendor in [JTAG debugging
for ESP32-S3](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/) [[3]](#id6).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s3/esp32s3/procpu samples/hello_world
west flash
```

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s3/esp32s3/procpu samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.adafruit.com/product/5323](https://www.adafruit.com/product/5323)

[[2](#id5)]

[https://github.com/openocd-org/openocd](https://github.com/openocd-org/openocd)

[[3](#id7)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/)

[[4](#id9)]

[https://learn.adafruit.com/adafruit-esp32-s3-feather](https://learn.adafruit.com/adafruit-esp32-s3-feather)

[[5](#id11)]

[https://learn.adafruit.com/adafruit-esp32-s3-feather/pinouts](https://learn.adafruit.com/adafruit-esp32-s3-feather/pinouts)

[[6](#id13)]

[https://learn.adafruit.com/adafruit-esp32-s3-feather/downloads](https://learn.adafruit.com/adafruit-esp32-s3-feather/downloads)

[[7](#id15)]

[https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1\_wroom-1u\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)
