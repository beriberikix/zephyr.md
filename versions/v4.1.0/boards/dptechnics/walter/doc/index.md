---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/dptechnics/walter/doc/index.html
original_path: boards/dptechnics/walter/doc/index.html
---

# Walter

Board Overview

[![../../../../_images/walter.webp](../../../../_images/walter.webp)
](../../../../_images/walter.webp)

Walter

Name:
:   `walter`

Vendor:
:   DPTechnics

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/dptechnics/walter/doc/index.rst/../..)

## Overview

Walter is a compact IoT development board that combines an Espressif ESP32-S3 SoC
with a Sequans Monarch 2 GM02SP LTE-M/NB-IoT/GNSS modem.
More information about Walter can be found on the [QuickSpot Website](https://www.quickspot.io/) [[1]](#id2) and on the
[QuickSpot GitHub page](https://github.com/QuickSpot) [[2]](#id4).

## Hardware

ESP32-S3-WROOM-1-N16R2 microcontroller:

- Xtensa dual-core 32-bit LX7 CPU
- 16 MiB quad SPI flash memory
- 2 MiB quad SPI PSRAM
- 150 Mbps 802.11 b/g/n Wi-Fi 4 with on-board PCB antenna
- 2 Mbps Bluetooth 5 Low Energy with on-board PCB antenna

Sequans Monarch 2 GM02SP modem:

- Dual-mode LTE-M / NB-IoT (NB1, NB2)
- 3GPP LTE release 14 (Upgradable up to release 17)
- Ultra-low, deep-sleep mode in eDRX and PSM
- Adaptive +23 dBm, +20 dBm and +14 dBm output power
- Integrated LNA and SAW filter for GNSS reception
- Assisted and non-assisted GNSS with GPS and Galileo constellations
- Integrated SIM card
- Nano-SIM card slot
- u.FL RF connectors for GNSS and 5G antennas

Inputs & outputs:

- 24 GPIO pins for application use
- UART, SPI, I²C, CAN, I²S, and SD available on any of the GPIO pins
- ADC, DAC, and PWM integrated in ESP32-S3
- 3.3 V software-controllable output
- USB Type-C connector for flashing and debugging
- 22 test points for production programming and testing
- On-board reset button

Power supply

- 5.0 V via USB Type-C
- 3.0 - 5.5 V via Vin pin
- Not allowed to use both power inputs simultaneously
- Designed for extremely low quiescent current

Form factor

- Easy to integrate via 2.54 mm headers
- 55 mm x 24.8 mm board dimensions
- Pin and footprint compatible with EOL Pycom GPy
- Breadboard friendly

### Supported Features

The `walter` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

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
bootstrap the board with the ESP32-S3 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b walter/esp32s3/procpu --sysbuild samples/hello_world
```

By default, the ESP32 sysbuild creates bootloader (MCUboot) and application
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
For that reason, images can be build one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b walter/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `walter` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b walter/esp32s3/procpu samples/hello_world
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
Hello World! walter/esp32s3/procpu
```

## Debugging

ESP32-S3 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/openocd-org/openocd) [[4]](#id8).

ESP32-S3 has a built-in JTAG circuitry and can be debugged without any additional chip. Only an USB cable connected to the D+/D- pins is necessary.

Further documentation can be obtained from the SoC vendor in [JTAG debugging for ESP32-S3](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/) [[3]](#id6).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b walter/esp32s3/procpu samples/hello_world
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b walter/esp32s3/procpu samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.quickspot.io/](https://www.quickspot.io/)

[[2](#id5)]

[https://github.com/QuickSpot](https://github.com/QuickSpot)

[[3](#id7)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/)

[[4](#id9)]

[https://github.com/openocd-org/openocd](https://github.com/openocd-org/openocd)
