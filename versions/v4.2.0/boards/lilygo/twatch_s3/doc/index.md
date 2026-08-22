---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/lilygo/twatch_s3/doc/index.html
original_path: boards/lilygo/twatch_s3/doc/index.html
---

# T-Watch S3

Board Overview

[![../../../../_images/twatch_s3.webp](../../../../_images/twatch_s3.webp)
](../../../../_images/twatch_s3.webp)

T-Watch S3

Name:
:   `twatch_s3`

Vendor:
:   Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lilygo/twatch_s3/doc/index.rst/../..)

## Overview

LILYGO T-Watch S3 is an ESP32-S3 based smartwatch with the following features:

- ESP32-S3-R8 chip

  > - Dual core Xtensa LX-7 up to 240MHz
  > - 8 MB of integrated PSRAM
  > - Bluetooth LE v5.0
  > - Wi-Fi 802.11 b/g/n
- 16 MB external QSPI flash (Winbond W25Q128JWPIQ)
- Power Management Unit (X-Powers AXP2101) which provides

  > - Regulators (DC-DCs and LDOs)
  > - Battery charging
  > - Fuel gauge
- 470 mAh battery
- RTC (NXP PCF8563)
- Haptic (Texas Instruments DRV2605)
- Accelerometer (Bosch BMA423)
- 240x240 pixels LCD with touchscreen

  > - ST7789V LCD Controller
  > - Focaltech FT5336 touch sensor
- Microphone (Knowles SPM1423HM4H-B)
- LoRA radio (Semtech SX1262)
- Audio amplifier (Maxim MAX98357A)

The board features a single micro USB connector which can be used for serial
flashing, debugging and console thanks to the integrated JTAG support in the
chip.

It does not have any GPIO that can easily be connected to something external.
There is only 1 physical button which is connected to the PMU and it’s used
to turn on/off the device.

### Supported Features

The `twatch_s3` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Building & Flashing

The `twatch_s3` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order to work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

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

#### Sysbuild

The sysbuild makes it possible to build and flash all necessary images needed to
bootstrap the board with the ESP32 SoC.

To build the sample application using sysbuild, use the command:

```shell
west build -b twatch_s3/esp32s3/procpu --sysbuild samples/hello_world
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

With `--sysbuild` option the bootloader will be re-built and re-flashed
every time the pristine build is used.

For more information about the system build please read the [Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild) documentation.

#### Manual build

During the development cycle, it is intended to build & flash as quickly as possible.
For that reason, images can be built one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flashed at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b twatch_s3/esp32s3/procpu samples/hello_world
```

The usual `flash` target will work with the `twatch_s3` board target
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b twatch_s3/esp32s3/procpu samples/hello_world
west flash
```

The default baud rate is set to 1500000bps. If experiencing issues when flashing,
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
Hello World! twatch_s3/esp32s3/procpu
```

## References
