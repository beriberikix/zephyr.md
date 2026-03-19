---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/vcc-gnd/yd_esp32/doc/index.html
original_path: boards/vcc-gnd/yd_esp32/doc/index.html
---

# YD-ESP32

Board Overview

[![../../../../_images/yd_esp32.png](../../../../_images/yd_esp32.png)
](../../../../_images/yd_esp32.png)

YD-ESP32

Name:
:   `yd_esp32`

Vendor:
:   VCC-GND Studio

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/vcc-gnd/yd_esp32/doc/index.rst/../..)

## Overview

The YD-ESP32 development board is one of VCC-GND® Studio’s official boards.
This board is based on the ESP32-WROOM-32E module, with the ESP32 as the core.

### ESP32

ESP32 is a series of low cost, low power system on a chip microcontrollers
with integrated Wi-Fi & dual-mode Bluetooth. The ESP32 series employs a
Tensilica Xtensa LX6 microprocessor in both dual-core and single-core
variations. ESP32 is created and developed by Espressif Systems, a
Shanghai-based Chinese company, and is manufactured by TSMC using their 40nm
process.

The features include the following:

- Dual core Xtensa microprocessor (LX6), running at 160 or 240MHz
- 520KB of SRAM
- 802.11b/g/n/e/i
- Bluetooth v4.2 BR/EDR and BLE
- Various peripherals:

  - 12-bit ADC with up to 18 channels
  - 2x 8-bit DACs
  - 10x touch sensors
  - Temperature sensor
  - 4x SPI
  - 2x I2S
  - 2x I2C
  - 3x UART
  - SD/SDIO/MMC host
  - Slave (SDIO/SPI)
  - Ethernet MAC
  - CAN bus 2.0
  - IR (RX/TX)
  - Motor PWM
  - LED PWM with up to 16 channels
  - Hall effect sensor
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)
- 5uA deep sleep current

For more information, check the datasheet at [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf) [[3]](#id6).

### Supported Features

The `yd_esp32` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

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
west build -b yd_esp32 --sysbuild samples/hello_world
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
west build -b yd_esp32/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `yd_esp32` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
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
Hello World! yd_esp32
```

### RGB LED

The board contains an addressable RGB LED ([XL-5050RGBC-WS2812B](http://www.xinglight.cn/index.php?c=show&id=947) [[1]](#id2)), driven by GPIO16.
Here is an example of how to test it using the [LED strip](../../../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/drivers/led/led_strip
west flash
```

## Debugging

ESP32 support on OpenOCD is available at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[5]](#id10).

On the YD-ESP32 board, the JTAG pins are not run to a
standard connector (e.g. ARM 20-pin) and need to be manually connected
to the external programmer (e.g. a Flyswatter2):

| ESP32 pin | JTAG pin |
| --- | --- |
| 3V3 | VTRef |
| EN | nTRST |
| IO14 | TMS |
| IO12 | TDI |
| GND | GND |
| IO13 | TCK |
| IO15 | TDO |

Further documentation can be obtained from the SoC vendor in [JTAG debugging for ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html) [[4]](#id8).

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b yd_esp32/esp32/procpu samples/hello_world
west debug
```

### Note on Debugging with GDB Stub

GDB stub is enabled on ESP32.

- When adding breakpoints, please use hardware breakpoints with command
  `hbreak`. Command `break` uses software breakpoints which requires
  modifying memory content to insert break/trap instructions.
  This does not work as the code is on flash which cannot be randomly
  accessed for modification.

## References

[[1](#id3)]

[http://www.xinglight.cn/index.php?c=show&id=947](http://www.xinglight.cn/index.php?c=show&id=947)

[[2](#id5)]

[https://www.espressif.com/sites/default/files/documentation/esp32\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)

[[3](#id7)]

[https://espressif.com/sites/default/files/documentation/esp32\_technical\_reference\_manual\_en.pdf](https://espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)

[[4](#id9)]

[https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html)

[[5](#id11)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
