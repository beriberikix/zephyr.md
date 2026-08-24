---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/espressif/esp8684_devkitm/doc/index.html
original_path: boards/espressif/esp8684_devkitm/doc/index.html
---

# ESP8684-DevKitM

Board Overview

[![../../../../_images/esp8684_devkitm.webp](https://docs.zephyrproject.org/4.1.0/_images/esp8684_devkitm.webp)
](https://docs.zephyrproject.org/4.1.0/_images/esp8684_devkitm.webp)

ESP8684-DevKitM

Name:
:   `esp8684_devkitm`

Vendor:
:   Espressif Systems

Architecture:
:   riscv

SoC:
:   esp32c2

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/espressif/esp8684_devkitm/doc/index.rst/../..)

## Overview

The ESP8684-DevKitM is an entry-level development board based on ESP8684-MINI-1, a general-purpose
module with 1 MB/2 MB/4 MB SPI flash. This board integrates complete Wi-Fi and Bluetooth LE functions.
For more information, check [ESP8684-DevKitM User Guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp8684/esp8684-devkitm-1/user_guide.html) [[1]](#id2)

## Hardware

ESP32-C2 (ESP8684 core) is a low-cost, Wi-Fi 4 & Bluetooth 5 (LE) chip. Its unique design
makes the chip smaller and yet more powerful than ESP8266. ESP32-C2 is built around a RISC-V
32-bit, single-core processor, with 272 KB of SRAM (16 KB dedicated to cache) and 576 KB of ROM.
ESP32-C2 has been designed to target simple, high-volume, and low-data-rate IoT applications,
such as smart plugs and smart light bulbs. ESP32-C2 offers easy and robust wireless connectivity,
which makes it the go-to solution for developing simple, user-friendly and reliable
smart-home devices. For more information, check [ESP8684 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp8684_datasheet_en.pdf) [[2]](#id5).

Features include the following:

- 32-bit core RISC-V microcontroller with a maximum clock speed of 120 MHz
- 2 MB or 4 MB in chip (ESP8684) or in package (ESP32-C2) flash
- 272 KB of internal RAM
- 802.11b/g/n
- A Bluetooth LE subsystem that supports features of Bluetooth 5 and Bluetooth Mesh
- Various peripherals:

  - 14 programmable GPIOs
  - 3 SPI
  - 2 UART
  - 1 I2C Master
  - LED PWM controller, with up to 6 channels
  - General DMA controller (GDMA)
  - 1 12-bit SAR ADC, up to 5 channels
  - 1 temperature sensor
  - 1 54-bit general-purpose timer
  - 2 watchdog timers
  - 1 52-bit system timer
- Cryptographic hardware acceleration (RNG, ECC, RSA, SHA-2, AES)

For detailed information check [ESP8684 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp8684_technical_reference_manual_en.pdf) [[3]](#id7).

### Supported Features

The `esp8684_devkitm` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `esp8684_devkitm/esp32c2` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L32) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif,riscv.md#std-dtcompatible-espressif-riscv) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L219) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L88) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif,esp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L97) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| on-chip | ESP32 general-purpose timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L175) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L106) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L121) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L136) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp8684_devkitm/esp8684_devkitm.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L71) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L113) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x0_default_2M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L43) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L166) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L186) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L212) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L147)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L156) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L192) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Timer | on-chip | ESP32 System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L80) | [`espressif,esp32-systimer`](../../../../build/dts/api/bindings/timer/espressif,esp32-systimer.md#std-dtcompatible-espressif-esp32-systimer) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L203) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c2/esp32c2_common.dtsi?plain=1#L48) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

For a getting started user guide, please check [ESP8684-DevKitM User Guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp8684/esp8684-devkitm-1/user_guide.html) [[1]](#id2).

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
west build -b esp8684_devkitm --sysbuild samples/hello_world
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
west build -b esp8684_devkitm samples/hello_world
```

The usual `flash` target will work with the `esp8684_devkitm` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp8684_devkitm samples/hello_world
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
Hello World! esp8684_devkitm
```

## Debugging

As with much custom hardware, the ESP8684 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[4]](#id9).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp8684_devkitm samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp8684_devkitm samples/hello_world
west debug
```

## References

[1]
([1](#id3),[2](#id4))

[https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp8684/esp8684-devkitm-1/user\_guide.html](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp8684/esp8684-devkitm-1/user_guide.html)

[[2](#id6)]

[https://www.espressif.com/sites/default/files/documentation/esp8684\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp8684_datasheet_en.pdf)

[[3](#id8)]

[https://www.espressif.com/sites/default/files/documentation/esp8684\_technical\_reference\_manual\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp8684_technical_reference_manual_en.pdf)

[[4](#id10)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
