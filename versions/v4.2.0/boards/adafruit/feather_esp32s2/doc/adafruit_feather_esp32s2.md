---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2.html
original_path: boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2.html
---

# Adafruit Feather ESP32S2

Board Overview

[![../../../../_images/adafruit_feather_esp32s2.webp](../../../../_images/adafruit_feather_esp32s2.webp)
](../../../../_images/adafruit_feather_esp32s2.webp)

Adafruit Feather ESP32S2

Name:
:   `adafruit_feather_esp32s2`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   xtensa

SoC:
:   esp32s2

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_esp32s2/doc/adafruit_feather_esp32s2.rst/../..)

## Overview

The Adafruit Feather ESP32-S2 boards are ESP32-S2 development boards in the
Feather standard layout, sharing peripheral placement with other devices labeled
as Feathers or FeatherWings. The board is equipped with an ESP32-S2 mini module,
a LiPo battery charger, a fuel gauge, a USB-C and [SparkFun Qwiic](https://www.sparkfun.com/qwiic) [[7]](#id17)-compatible
[STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt) [[8]](#id19) connector for the I2C bus.

## Hardware

- ESP32-S2 mini module, featuring the 240MHz Tensilica processor
- 320KB SRAM, 4MB flash + 2MB PSRAM
- USB-C directly connected to the ESP32-S2 for USB
- LiPo connector and built-in battery charging when powered via USB-C
- LC709203F or MAX17048 fuel gauge for battery voltage and state-of-charge reporting
- Built-in NeoPixel indicator RGB LED
- STEMMA QT connector for I2C devices, with switchable power for low-power mode

Note

- The [Adafruit ESP32-S2 Feather with BME280 Sensor](https://www.adafruit.com/product/5303) [[2]](#id6) is the same board as the
  [Adafruit ESP32-S2 Feather](https://www.adafruit.com/product/5000) [[1]](#id2) but with an already equipped BME280 Sensor, but is not
  stated as a separate board, instead the BME280 needs to be added via a devicetree
  overlay. All boards, except the [Adafruit ESP32-S2 Feather with BME280 Sensor](https://www.adafruit.com/product/5303) [[2]](#id6) have a
  space for it, but will not be shipped with.
- As of May 31, 2023 - Adafruit has changed the battery monitor chip from the
  now-discontinued LC709203F to the MAX17048. Check the back silkscreen of your Feather to
  see which chip you have.
- For the MAX17048 and LC709203F a driver in zephyr exists and is supported, but needs to be
  added via a devicetree overlay.
- For the [Adafruit ESP32-S2 Feather](https://www.adafruit.com/product/5000) [[1]](#id2) there are two different Revisions `rev B` and
  `rev C`. The `rev C` board has revised the power circuitry for the NeoPixel and I2C
  QT port. Instead of a transistor the `rev C` has a LDO regulator. To enable the
  NeoPixel and I2C QT port on `rev B` boards `GPIO7` (`i2c_reg`) needs to be set to
  LOW and on `rev C` boards it needs to be set HIGH.

### Supported Features

The `adafruit_feather_esp32s2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

USB-OTG is until now not supported see [ESP32 development overview](https://github.com/zephyrproject-rtos/zephyr/issues/29394#issuecomment-2635037831) [[4]](#id11). To see a serial output
a FTDI-USB-RS232 or similar needs to be connected to the RX/TX pins on the feather connector.

### Connections and IOs

The [Adafruit ESP32-S2 Feather](https://www.adafruit.com/product/5000) [[1]](#id2) User Guide has detailed information about the board including
pinouts and the schematic.

- [Adafruit ESP32-S2 Feather Pinouts](https://learn.adafruit.com/adafruit-esp32-s2-feather/pinouts) [[5]](#id13)
- [Adafruit ESP32-S2 Feather Schematic](https://learn.adafruit.com/adafruit-esp32-s2-feather/downloads) [[6]](#id15)

## Programming and Debugging

The `adafruit_feather_esp32s2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Prerequisites

Espressif HAL requires WiFi binary blobs in order work. Run the command below
to retrieve those files.

```shell
west update
west blobs fetch hal_espressif
```

## Building & Flashing

### Simple boot

The board could be loaded using the single binary image, without 2nd stage
bootloader. It is the default option when building the application without
additional configuration.

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

**Rev B**

```shell
west build -b adafruit_feather_esp32s2@B --sysbuild samples/hello_world
```

**Rev C**

```shell
west build -b adafruit_feather_esp32s2@C --sysbuild samples/hello_world
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

Build and flash applications as usual:

**Rev B**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@B samples/hello_world
```

**Rev C**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@C samples/hello_world
```

The usual `flash` target will work. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

To enter ROM bootloader mode, hold down `boot-button` while clicking reset button.
When in the ROM bootloader, you can upload code and query the chip using `west flash`.

**Rev B**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@B samples/hello_world
> west flash
> ```

**Rev C**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@C samples/hello_world
> west flash
> ```

After the flashing you will receive most likely this Error:

```shell
WARNING: ESP32-S2FNR2 (revision v0.0) chip was placed into download mode using GPIO0.
esptool.py can not exit the download mode over USB. To run the app, reset the chip manually.
To suppress this note, set --after option to 'no_reset'.
FATAL ERROR: command exited with status 1: ...
```

As stated in the Warning-Message `esptool` can’t reset the board by itself and this message
can be ignored and the board needs to be reseted via the Reset-Button manually.

Open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has been manually reseted and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! adafruit_feather_esp32s2
```

## Debugging

ESP32-S2 support on OpenOCD is available at [OpenOCD](https://github.com/openocd-org/openocd) [[3]](#id9).

ESP32-S2 has a built-in JTAG circuitry and can be debugged without any
additional chip. Only an USB cable connected to the D+/D- pins is necessary.

Further documentation can be obtained from the SoC vendor
in [JTAG debugging for ESP32-S2](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s2/api-guides/jtag-debugging/index.html) [[9]](#id21).

You can debug an application in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

**Rev B**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@B samples/hello_world
west debug
```

**Rev C**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@C samples/hello_world
west debug
```

## Testing the On-Board-LED

There is a sample available to verify that the LEDs on the board are
functioning correctly with Zephyr:

**Rev B**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@B samples/basic/blinky
west flash
```

**Rev C**

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@C samples/basic/blinky
west flash
```

## Testing the NeoPixel

There is a sample available to verify that the NeoPixel on the board are
functioning correctly with Zephyr:

**Rev B**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@B samples/drivers/led/led_strip
> west flash
> ```

**Rev C**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@C samples/drivers/led/led_strip
> west flash
> ```

## Testing the Fuel Gauge

There is a sample available to verify that the MAX17048 or LC709203F fuel gauge on the board are
functioning correctly with Zephyr

Note

As of May 31, 2023 Adafruit changed the battery monitor chip from the now-discontinued LC709203F
to the MAX17048.

**Rev B**

For the Rev B a devicetree overlay for the LC709203F fuel gauge already exists in the
`samples/drivers/fuel_gauge/boards` folder.

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@B samples/drivers/fuel_gauge
west flash
```

**Rev C**

For the Rev C a devicetree overlay for the MAX17048 fuel gauge already exists in the
`samples/drivers/fuel_gauge/boards` folder.

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@C samples/drivers/fuel_gauge
west flash
```

For the LC709203F a devicetree overlay needs to be added to the build.
The overlay can be added via the `--extra-dtc-overlay` argument and should most likely includes
the following:

```devicetree
/ {
   aliases {
      fuel-gauge0 = &lc709203f;
   };
};

&i2c0 {
   lc709203f: lc709203f@0b {
      compatible = "onnn,lc709203f";
      status = "okay";
      reg = <0x0b>;
      power-domains = <&i2c_reg>;
      apa = "500mAh";
      battery-profile = <0x01>;
   };
};
```

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_esp32s2@C --extra-dtc-overlay="boards/name_of_your.overlay" samples/drivers/fuel_gauge
west flash
```

## Testing Wi-Fi

There is a sample available to verify that the Wi-Fi on the board are
functioning correctly with Zephyr:

Note

The Prerequisites must be met before testing Wi-Fi.

**Rev B**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@B samples/net/wifi/shell
> west flash
> ```

**Rev C**

> ```shell
> # From the root of the zephyr repository
> west build -b adafruit_feather_esp32s2@C samples/net/wifi/shell
> west flash
> ```

## References

[1]
([1](#id3),[2](#id4),[3](#id5))

[https://www.adafruit.com/product/5000](https://www.adafruit.com/product/5000)

[2]
([1](#id7),[2](#id8))

[https://www.adafruit.com/product/5303](https://www.adafruit.com/product/5303)

[[3](#id10)]

[https://github.com/openocd-org/openocd](https://github.com/openocd-org/openocd)

[[4](#id12)]

[https://github.com/zephyrproject-rtos/zephyr/issues/29394#issuecomment-2635037831](https://github.com/zephyrproject-rtos/zephyr/issues/29394#issuecomment-2635037831)

[[5](#id14)]

[https://learn.adafruit.com/adafruit-esp32-s2-feather/pinouts](https://learn.adafruit.com/adafruit-esp32-s2-feather/pinouts)

[[6](#id16)]

[https://learn.adafruit.com/adafruit-esp32-s2-feather/downloads](https://learn.adafruit.com/adafruit-esp32-s2-feather/downloads)

[[7](#id18)]

[https://www.sparkfun.com/qwiic](https://www.sparkfun.com/qwiic)

[[8](#id20)]

[https://learn.adafruit.com/introducing-adafruit-stemma-qt](https://learn.adafruit.com/introducing-adafruit-stemma-qt)

[[9](#id22)]

[https://docs.espressif.com/projects/esp-idf/en/stable/esp32s2/api-guides/jtag-debugging/index.html](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s2/api-guides/jtag-debugging/index.html)
