---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/espressif/esp32c6_devkitc/doc/index.html
original_path: boards/espressif/esp32c6_devkitc/doc/index.html
---

# ESP32-C6-DevKitC

Board Overview

[![../../../../_images/esp32c6_devkitc.webp](https://docs.zephyrproject.org/4.2.0/_images/esp32c6_devkitc.webp)
](https://docs.zephyrproject.org/4.2.0/_images/esp32c6_devkitc.webp)

ESP32-C6-DevKitC

Name:
:   `esp32c6_devkitc`

Vendor:
:   Espressif Systems

Architecture:
:   riscv

SoC:
:   esp32c6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/espressif/esp32c6_devkitc/doc/index.rst/../..)

## Overview

ESP32-C6-DevKitC is an entry-level development board based on ESP32-C6-WROOM-1(U),
a general-purpose module with a 8 MB SPI flash. This board integrates complete Wi-Fi,
Bluetooth LE, Zigbee, and Thread functions. For more information, check [ESP32-C6-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide.html) [[1]](#id2).

## Hardware

ESP32-C6 is Espressif’s first Wi-Fi 6 SoC integrating 2.4 GHz Wi-Fi 6, Bluetooth 5.3 (LE) and the
802.15.4 protocol. ESP32-C6 achieves an industry-leading RF performance, with reliable security
features and multiple memory resources for IoT products.
It consists of a high-performance (HP) 32-bit RISC-V processor, which can be clocked up to 160 MHz,
and a low-power (LP) 32-bit RISC-V processor, which can be clocked up to 20 MHz.
It has a 320KB ROM, a 512KB SRAM, and works with external flash.

ESP32-C6-DevKitC is an entry-level development board based on ESP32-C6-WROOM-1(U),
a general-purpose module with a 8 MB SPI flash.

Most of the I/O pins are broken out to the pin headers on both sides for easy interfacing.
Developers can either connect peripherals with jumper wires or mount ESP32-C6-DevKitC on
a breadboard.

ESP32-C6 includes the following features:

- 32-bit core RISC-V microcontroller with a clock speed of up to 160 MHz
- 400 KB of internal RAM
- WiFi 802.11 ax 2.4GHz
- Fully compatible with IEEE 802.11b/g/n protocol
- Bluetooth LE: Bluetooth 5.3 certified
- Internal co-existence mechanism between Wi-Fi and Bluetooth to share the same antenna
- IEEE 802.15.4 (Zigbee and Thread)

Digital interfaces:

- 30x GPIOs (QFN40), or 22x GPIOs (QFN32)
- 2x UART
- 1x Low-power (LP) UART
- 1x General purpose SPI
- 1x I2C
- 1x Low-power (LP) I2C
- 1x I2S
- 1x Pulse counter
- 1x USB Serial/JTAG controller
- 1x TWAI® controller, compatible with ISO 11898-1 (CAN Specification 2.0)
- 1x SDIO 2.0 slave controller
- LED PWM controller, up to 6 channels
- 1x Motor control PWM (MCPWM)
- 1x Remote control peripehral
- 1x Parallel IO interface (PARLIO)
- General DMA controller (GDMA), with 3 transmit channels and 3 receive channels
- Event task matrix (ETM)

Analog interfaces:

- 1x 12-bit SAR ADCs, up to 7 channels
- 1x temperature sensor

Timers:

- 1x 52-bit system timer
- 1x 54-bit general-purpose timers
- 3x Watchdog timers
- 1x Analog watchdog timer

Low Power:

- Four power modes designed for typical scenarios: Active, Modem-sleep, Light-sleep, Deep-sleep

Security:

- Secure boot
- Flash encryption
- 4-Kbit OTP, up to 1792 bits for users
- Cryptographic hardware acceleration: (AES-128/256, ECC, HMAC, RSA, SHA, Digital signature, Hash)
- Random number generator (RNG)

For more information, check the datasheet at [ESP32-C6 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32-C6 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf) [[3]](#id7).

### Supported Features

The `esp32c6_devkitc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `esp32c6_devkitc/esp32c6/hpcore` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L34) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif,riscv.md#std-dtcompatible-espressif-riscv) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L248) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif,esp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L67) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif,esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L179) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif,esp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L72) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif,esp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 general-purpose timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L131) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif,esp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L141) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif,esp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L258) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif,esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L226) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L276) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L286) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif,esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L297) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif,esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| IEEE 802.15.4 | on-chip | Espressif ESP32 IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L85) | [`espressif,esp32-ieee802154`](../../../../build/dts/api/bindings/ieee802154/espressif,esp32-ieee802154.md#std-dtcompatible-espressif-esp32-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/esp32c6_devkitc/esp32c6_devkitc_hpcore.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L114) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif,esp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L233) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x0_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L62) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L344) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif,esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| on-chip | ESP32 Motor Control Pulse Width Modulator (MCPWM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L353) | [`espressif,esp32-mcpwm`](../../../../build/dts/api/bindings/pwm/espressif,esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L172) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif,esp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L241) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif,esp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| on-chip | ESP32 Pulse Counter (PCNT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L363) | [`espressif,esp32-pcnt`](../../../../build/dts/api/bindings/sensor/espressif,esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt) |
| Serial controller | on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L309)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L318) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif,esp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 Low Power UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L328) | [`espressif,esp32-lpuart`](../../../../build/dts/api/bindings/serial/espressif,esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L335) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif,esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L197) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif,esp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Timer | on-chip | ESP32 System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L123) | [`espressif,esp32-systimer`](../../../../build/dts/api/bindings/timer/espressif,esp32-systimer.md#std-dtcompatible-espressif-esp32-systimer) |
| Watchdog | on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L208)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L217) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif,esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L80) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif,esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

#### `esp32c6_devkitc/esp32c6/lpcore` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L21) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif,riscv.md#std-dtcompatible-espressif-riscv) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L49) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif,esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L69) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif,esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L55) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x0_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Serial controller | on-chip | ESP32 Low Power UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L63) | [`espressif,esp32-lpuart`](../../../../build/dts/api/bindings/serial/espressif,esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |

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

The `esp32c6_devkitc` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **esp32** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

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
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/hello_world
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
west build -b esp32c6_devkitc/esp32c6/hpcore samples/hello_world
```

The usual `flash` target will work with the `esp32c6_devkitc` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32c6_devkitc/esp32c6/hpcore samples/hello_world
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
Hello World! esp32c6_devkitc/esp32c6/hpcore
```

## Debugging

As with much custom hardware, the ESP32-C6 modules require patches to
OpenOCD that are not upstreamed yet. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained at [OpenOCD ESP32](https://github.com/espressif/openocd-esp32/releases) [[4]](#id10).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp32c6_devkitc/esp32c6/hpcore samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b esp32c6_devkitc/esp32c6/hpcore samples/hello_world
west debug
```

## Low-Power CPU (LP CORE)

The ESP32-C6 SoC has two RISC-V cores: the High-Performance Core (HP CORE) and the Low-Power Core (LP CORE).
The LP Core features ultra low power consumption, an interrupt controller, a debug module and a system bus
interface for memory and peripheral access.

The LP Core is in sleep mode by default. It has two application scenarios:

- Power insensitive scenario: When the High-Performance CPU (HP Core) is active, the LP Core can assist the HP CPU with some speed and efficiency-insensitive controls and computations.
- Power sensitive scenario: When the HP CPU is in the power-down state to save power, the LP Core can be woken up to handle some external wake-up events.

For more information, check the datasheet at [ESP32-C6 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf) [[2]](#id4) or the technical reference
manual at [ESP32-C6 Technical Reference Manual](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf) [[3]](#id7).

The LP Core support is fully integrated with [Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild). The user can enable the LP Core by adding
the following configuration to the project:

```cfg
CONFIG_ULP_COPROC_ENABLED=y
```

See [Low-Power CPU (LP CORE)](../../../../samples/boards/espressif/ulp/lp_core/index.md#lp-core) folder as code reference.

## References

[[1](#id3)]

[https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user\_guide.html](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide.html)

[2]
([1](#id5),[2](#id6))

[https://www.espressif.com/sites/default/files/documentation/esp32-c6\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)

[3]
([1](#id8),[2](#id9))

[https://espressif.com/sites/default/files/documentation/esp32-c6\_technical\_reference\_manual\_en.pdf](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf)

[[4](#id11)]

[https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)
