---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seeed/xiao_esp32c6/doc/index.html
original_path: boards/seeed/xiao_esp32c6/doc/index.html
---

# XIAO ESP32C6

Board Overview

[![../../../../_images/xiao_esp32c6.webp](../../../../_images/xiao_esp32c6.webp)
](../../../../_images/xiao_esp32c6.webp)

XIAO ESP32C6

Name:
:   `xiao_esp32c6`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   riscv

SoC:
:   esp32c6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/xiao_esp32c6/doc/index.rst/../..)

## Overview

Seeed Studio XIAO ESP32C6 is powered by the highly-integrated ESP32-C6 SoC.
It consists of a high-performance (HP) 32-bit RISC-V processor, which can be clocked up to 160 MHz,
and a low-power (LP) 32-bit RISC-V processor, which can be clocked up to 20 MHz.
It has a 320KB ROM, a 512KB SRAM, and works with external flash.
This board integrates complete Wi-Fi, Bluetooth LE, Zigbee, and Thread functions.
For more information, check [Seeed Studio XIAO ESP32C6](https://wiki.seeedstudio.com/xiao_esp32c6_getting_started/) [[1]](#id3) .

## Hardware

This board is based on the ESP32-C6 with 4MB of flash, integrating 2.4 GHz Wi-Fi 6,
Bluetooth 5.3 (LE) and the 802.15.4 protocol. It has an USB-C port for programming
and debugging, integrated battery charging and an U.FL external antenna connector.
It is based on a standard XIAO 14 pin pinout.

### Supported Features

The `xiao_esp32c6` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xiao_esp32c6/esp32c6` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L28) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif%2Criscv.md#std-dtcompatible-espressif-riscv) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L192) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Clock control | on-chip | ESP32 RTC (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L123) | [`espressif,esp32-rtc`](../../../../build/dts/api/bindings/clock/espressif%2Cesp32-rtc.md#std-dtcompatible-espressif-esp32-rtc) |
| Counter | on-chip | ESP32 general-purpose timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L101) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 Counter Driver based on RTC Main Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L132) | [`espressif,esp32-rtc-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L202) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif%2Cesp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L177) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif%2Cesp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L220) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif%2Cesp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| on-board | GPIO pins exposed on Seeeduino Xiao (and compatible devices) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_esp32c6/seeed_xiao_connector.dtsi?plain=1#L8) | [`seeed,xiao-gpio`](../../../../build/dts/api/bindings/gpio/seeed-xiao-header.md#std-dtcompatible-seeed-xiao-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L230) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L84) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_esp32c6/xiao_esp32c6.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L184) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/espressif/partitions_0x0_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L56) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L269) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L278) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L141) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif%2Cesp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L241)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L250) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L260) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L148) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Timer | on-chip | ESP32 System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L93) | [`espressif,esp32-systimer`](../../../../build/dts/api/bindings/timer/espressif%2Cesp32-systimer.md#std-dtcompatible-espressif-esp32-systimer) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L159)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L168) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L61) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

The board uses a standard XIAO pinout, the default pin mapping is the following:

![XIAO ESP32C6 Pinout](../../../../_images/xiao_esp32c6_pinout.webp)

XIAO ESP32C6 Pinout

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
bootstrap the board with the EPS32 SoC.

To build the sample application using sysbuild use the command:

```shell
west build -b xiao_esp32c6 --sysbuild samples/hello_world
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
For that reason, images can be built one at a time using traditional build.

The instructions following are relevant for both manual build and sysbuild.
The only difference is the structure of the build directory.

Note

Remember that bootloader (MCUboot) needs to be flash at least once.

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c6 samples/hello_world
```

The usual `flash` target will work with the `xiao_esp32c6` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c6 samples/hello_world
west flash
```

Since the Zephyr console is by default on the `usb_serial` device, we use
the espressif monitor to view.

```shell
$ west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! xiao_esp32c6/esp32c6
```

## Debugging

As with much custom hardware, the ESP32-C6 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[2]](#id5).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c6 samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xiao_esp32c6 samples/hello_world
west debug
```

## References

[[1](#id4)]

[https://wiki.seeedstudio.com/xiao\_esp32c6\_getting\_started/](https://wiki.seeedstudio.com/xiao_esp32c6_getting_started/)

[[2](#id6)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
