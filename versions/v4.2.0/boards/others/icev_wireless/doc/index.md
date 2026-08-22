---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/others/icev_wireless/doc/index.html
original_path: boards/others/icev_wireless/doc/index.html
---

# ICE-V Wireless

Board Overview

[![../../../../_images/icev_wireless.jpg](../../../../_images/icev_wireless.jpg)
](../../../../_images/icev_wireless.jpg)

ICE-V Wireless

Name:
:   `icev_wireless`

Vendor:
:   Other/Unknown

Architecture:
:   riscv

SoC:
:   esp32c3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/icev_wireless/doc/index.rst/../..)

## Overview

The ICE-V Wireless is a combined ESP32C3 and iCE40 FPGA board.

See the [ICE-V Wireless Github Project](https://github.com/ICE-V-Wireless/ICE-V-Wireless) [[1]](#id3) for details.

## Hardware

This board combines an Espressif ESP32-C3-MINI-1 (which includes 4MB of flash in the module) with a
Lattice iCE40UP5k-SG48 FPGA to allow WiFi and Bluetooth control of the FPGA. ESP32 and FPGA I/O is
mostly uncommitted except for the pins used for SPI communication between ESP32 and FPGA. Several
of the ESP32C3 GPIO pins are available for additonal interfaces such as serial, ADC, I2C, etc.

For details on ESP32-C3 hardware please refer to the following resources:

- [ESP32-C3-MINI-1 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf) [[2]](#id5)
- [ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf) [[3]](#id7)
- [ESP32-C3 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf) [[4]](#id9)

For details on iCE40 hardware please refer to the following resources:

- [iCE40 UltraPlus Family Datasheet](https://www.latticesemi.com/-/media/LatticeSemi/Documents/DataSheets/iCE/iCE40-UltraPlus-Family-Data-Sheet.ashx) [[5]](#id11)

### Supported Features

The `icev_wireless` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `icev_wireless/esp32c3` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Espressif RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L34) | [`espressif,riscv`](../../../../build/dts/api/bindings/cpu/espressif%2Criscv.md#std-dtcompatible-espressif-riscv) |
| ADC | on-chip | ESP32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L313) | [`espressif,esp32-adc`](../../../../build/dts/api/bindings/adc/espressif%2Cesp32-adc.md#std-dtcompatible-espressif-esp32-adc) |
| Bluetooth | on-chip | Bluetooth HCI for Espressif ESP32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L72) | [`espressif,esp32-bt-hci`](../../../../build/dts/api/bindings/bluetooth/espressif%2Cesp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci) |
| CAN | on-chip | ESP32 Two-Wire Automotive Interface (TWAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L268) | [`espressif,esp32-twai`](../../../../build/dts/api/bindings/can/espressif%2Cesp32-twai.md#std-dtcompatible-espressif-esp32-twai) |
| Clock control | on-chip | ESP32 Clock (Power & Clock Controller Module) Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L77) | [`espressif,esp32-clock`](../../../../build/dts/api/bindings/clock/espressif%2Cesp32-clock.md#std-dtcompatible-espressif-esp32-clock) |
| Counter | on-chip | ESP32 general-purpose timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L230) | [`espressif,esp32-timer`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-timer.md#std-dtcompatible-espressif-esp32-timer) |
| on-chip | ESP32 counters[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L240) | [`espressif,esp32-counter`](../../../../build/dts/api/bindings/counter/espressif%2Cesp32-counter.md#std-dtcompatible-espressif-esp32-counter) |
| DMA | on-chip | ESP32 GDMA (General Direct Memory Access)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L323) | [`espressif,esp32-gdma`](../../../../build/dts/api/bindings/dma/espressif%2Cesp32-gdma.md#std-dtcompatible-espressif-esp32-gdma) |
| Flash controller | on-chip | ESP32 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L138) | [`espressif,esp32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/espressif%2Cesp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller) |
| GPIO & Headers | on-chip | ESP32 GPIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L153) | [`espressif,esp32-gpio`](../../../../build/dts/api/bindings/gpio/espressif%2Cesp32-gpio.md#std-dtcompatible-espressif-esp32-gpio) |
| I2C | on-chip | ESP32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L168) | [`espressif,esp32-i2c`](../../../../build/dts/api/bindings/i2c/espressif%2Cesp32-i2c.md#std-dtcompatible-espressif-esp32-i2c) |
| I2S | on-chip | ESP32 I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L179) | [`espressif,esp32-i2s`](../../../../build/dts/api/bindings/i2s/espressif%2Cesp32-i2s.md#std-dtcompatible-espressif-esp32-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/icev_wireless/icev_wireless.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ESP32 Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L103) | [`espressif,esp32-intc`](../../../../build/dts/api/bindings/interrupt-controller/espressif%2Cesp32-intc.md#std-dtcompatible-espressif-esp32-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/icev_wireless/icev_wireless.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L145) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/espressif/partitions_0x0_default_4M.dtsi?plain=1#L8) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | ESP32 pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L62) | [`espressif,esp32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl) |
| PWM | on-chip | ESP32 LED Control (LEDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L212) | [`espressif,esp32-ledc`](../../../../build/dts/api/bindings/pwm/espressif%2Cesp32-ledc.md#std-dtcompatible-espressif-esp32-ledc) |
| RNG | on-chip | ESP32 TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L262) | [`espressif,esp32-trng`](../../../../build/dts/api/bindings/rng/espressif%2Cesp32-trng.md#std-dtcompatible-espressif-esp32-trng) |
| Sensors | on-chip | ESP32 temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L306) | [`espressif,esp32-temp`](../../../../build/dts/api/bindings/sensor/espressif%2Cesp32-temp.md#std-dtcompatible-espressif-esp32-temp) |
| Serial controller | on-chip | ESP32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L193) | [`espressif,esp32-uart`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-uart.md#std-dtcompatible-espressif-esp32-uart) |
| on-chip | ESP32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L221) | [`espressif,esp32-usb-serial`](../../../../build/dts/api/bindings/serial/espressif%2Cesp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial) |
| SPI | on-chip | ESP32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L277) | [`espressif,esp32-spi`](../../../../build/dts/api/bindings/spi/espressif%2Cesp32-spi.md#std-dtcompatible-espressif-esp32-spi) |
| Timer | on-chip | ESP32 System Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L112) | [`espressif,esp32-systimer`](../../../../build/dts/api/bindings/timer/espressif%2Cesp32-systimer.md#std-dtcompatible-espressif-esp32-systimer) |
| Watchdog | on-chip | ESP32 XT Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L120) | [`espressif,esp32-xt-wdt`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-xt-wdt.md#std-dtcompatible-espressif-esp32-xt-wdt) |
| on-chip | ESP32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L288)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L297) | [`espressif,esp32-watchdog`](../../../../build/dts/api/bindings/watchdog/espressif%2Cesp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog) |
| Wi-Fi | on-chip | ESP32 SoC Wi-Fi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c3/esp32c3_common.dtsi?plain=1#L67) | [`espressif,esp32-wifi`](../../../../build/dts/api/bindings/wifi/espressif%2Cesp32-wifi.md#std-dtcompatible-espressif-esp32-wifi) |

### Connections and IOs

The ICE-V Wireless provides 1 row of reference, ESP32-C3, and iCE40 signals
brought out to J3, as well as 3 PMOD connectors for interfacing directly to
the iCE40 FPGA. Note that several of the iCE40 pins brought out to the PMOD
connectors are capable of operating as differential pairs.

![ICE-V Wireless (Back)](../../../../_images/icev_wireless_back.jpg)

ICE-V Wireless (Back)

The J3 pins are 4V, 3.3V, NRST, GPIO2, GPIO3, GPIO8, GPIO9, GPIO10, GPIO20,
GPIO21, FPGA\_P34, and GND. Note that GPIO2 and GPIO3 may be configured for
ADC operation.

For PMOD details, please refer to the [PMOD Specification](https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf) [[6]](#id13) and the image
below.

![ICE-V Wireless Pinout](../../../../_images/icev_wireless_pinout.jpg)

## Programming and Debugging

The `icev_wireless` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **esp32** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

Programming and debugging for the ICE-V Wireless ESP32-C3 target is
incredibly easy 🎉 following the steps below.

## Building and Flashing

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
west build -b icev_wireless --sysbuild samples/hello_world
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

For the `Hello, world!` application, follow the instructions below.

```shell
# From the root of the zephyr repository
west build -b icev_wireless samples/hello_world
west flash
```

Open the serial monitor using the following command:

```shell
$ west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! icev_wireless
```

## Debugging

As with much custom hardware, the ESP32C3 modules require patches to
OpenOCD that are not upstreamed. Espressif maintains their own fork of
the project. The custom OpenOCD can be obtained by running the following extension:

```shell
west espressif install
```

Note

By default, the OpenOCD will be downloaded and installed under $HOME/.espressif/tools/zephyr directory
(%USERPROFILE%/.espressif/tools/zephyr on Windows).

The Zephyr SDK uses a bundled version of OpenOCD by default. You can overwrite that behavior by adding the
`-DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>`
parameter when building.

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b icev_wireless samples/hello_world -- -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west flash
```

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b icev_wireless samples/hello_world
west debug
```

## References

[[1](#id4)]

[https://github.com/ICE-V-Wireless/ICE-V-Wireless](https://github.com/ICE-V-Wireless/ICE-V-Wireless)

[[2](#id6)]

[https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf)

[[3](#id8)]

[https://www.espressif.com/sites/default/files/documentation/esp32-c3\_datasheet\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)

[[4](#id10)]

[https://www.espressif.com/sites/default/files/documentation/esp32-c3\_technical\_reference\_manual\_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)

[[5](#id12)]

[https://www.latticesemi.com/-/media/LatticeSemi/Documents/DataSheets/iCE/iCE40-UltraPlus-Family-Data-Sheet.ashx](https://www.latticesemi.com/-/media/LatticeSemi/Documents/DataSheets/iCE/iCE40-UltraPlus-Family-Data-Sheet.ashx)

[[6](#id14)]

[https://digilent.com/reference/\_media/reference/pmod/pmod-interface-specification-1\_2\_0.pdf](https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf)
