---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/m5stack/m5stack_cores3/doc/index.html
original_path: boards/m5stack/m5stack_cores3/doc/index.html
---

# CoreS3

Board Overview

[![../../../../_images/m5stack_cores3.webp](../../../../_images/m5stack_cores3.webp)
](../../../../_images/m5stack_cores3.webp)

CoreS3

Name:
:   `m5stack_cores3`

Vendor:
:   M5Stack

Architecture:
:   xtensa

SoC:
:   esp32s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/m5stack/m5stack_cores3/doc/index.rst/../..)

## Overview

M5Stack CoreS3 is an ESP32-based development board from M5Stack. It is the third generation of the M5Stack Core series.
M5Stack CoreS3 SE is the compact version of CoreS3. It has the same form factor as the original M5Stack,
and some features were reduced from CoreS3.

M5Stack CoreS3/CoreS3 SE features consist of:

- ESP32-S3 chip (dual-core Xtensa LX7 processor @240MHz, WIFI, OTG and CDC functions)
- PSRAM 8MB
- Flash 16MB
- LCD ISP 2”, 320x240 pixel ILI9342C
- Capacitive multi touch FT6336U
- Speaker 1W AW88298
- Dual Microphones ES7210 Audio decoder
- RTC BM8563
- USB-C
- SD-Card slot
- PMIC AXP2101
- Battery 500mAh 3.7 V (Not available for CoreS3 SE)
- Camera 30W pixel GC0308 (Not available for CoreS3 SE)
- Geomagnetic sensor BMM150 (Not available for CoreS3 SE)
- Proximity sensor LTR-553ALS-WA (Not available for CoreS3 SE)
- 6-Axis IMU BMI270 (Not available for CoreS3 SE)

## Start Application Development

Before powering up your M5Stack CoreS3, please make sure that the board is in good
condition with no obvious signs of damage.

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

M5Stack CoreS3M5Stack CoreS3 SE

```shell
west build -b m5stack_cores3/esp32s3/procpu --sysbuild samples/hello_world
```

```shell
west build -b m5stack_cores3/esp32s3/procpu/se --sysbuild samples/hello_world
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

M5Stack CoreS3M5Stack CoreS3 SE

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu samples/hello_world
```

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu/se samples/hello_world
```

The usual `flash` target will work with the `m5stack_cores3/esp32s3/procpu` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

M5Stack CoreS3M5Stack CoreS3 SE

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu samples/hello_world
west flash
```

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu/se samples/hello_world
west flash
```

The baud rate of 921600bps is set by default. If experiencing issues when flashing,
try using different values by using `--esp-baud-rate <BAUD>` option during
`west flash` (e.g. `west flash --esp-baud-rate 115200`).

You can also open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
*** Booting Zephyr OS build vx.x.x-xxx-gxxxxxxxxxxxx ***
Hello World! m5stack_cores3/esp32s3/procpu
```

## Debugging

ESP32-S3 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[1]](#id2).

ESP32-S3 has a built-in JTAG circuitry and can be debugged without any additional chip. Only an USB cable connected to the D+/D- pins is necessary.

Further documentation can be obtained from the SoC vendor in [JTAG debugging for ESP32-S3](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/) [[2]](#id4).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

M5Stack CoreS3M5Stack CoreS3 SE

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu samples/hello_world
west debug
```

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu/se samples/hello_world
west debug
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

M5Stack CoreS3M5Stack CoreS3 SE

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu samples/hello_world
west debug
```

```shell
# From the root of the zephyr repository
west build -b m5stack_cores3/esp32s3/procpu/se samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)

[[2](#id5)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/jtag-debugging/)
