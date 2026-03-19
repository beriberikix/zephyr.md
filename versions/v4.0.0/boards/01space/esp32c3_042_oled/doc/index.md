---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/01space/esp32c3_042_oled/doc/index.html
original_path: boards/01space/esp32c3_042_oled/doc/index.html
---

# ESP32C3 0.42 OLED

Board Overview

[![../../../../_images/esp32c3_042_oled.webp](../../../../_images/esp32c3_042_oled.webp)
](../../../../_images/esp32c3_042_oled.webp)

ESP32C3 0.42 OLED

Vendor:
:   01Space

Architecture:
:   riscv

SoC:
:   esp32c3

## Overview

ESP32C3 0.42 OLED is a mini development board based on the [Espressif ESP32-C3](https://www.espressif.com/en/products/socs/esp32-c3) [[1]](#id3)
RISC-V WiFi/Bluetooth dual-mode chip.

For more details see the [01space ESP32C3 0.42 OLED](https://github.com/01Space/ESP32-C3-0.42LCD) [[2]](#id5) Github repo.

## Hardware

This board is based on the ESP32-C3-FH4 with WiFi and BLE support.
It features:

- RISC-V SoC @ 160MHz with 4MB flash and 400kB RAM
- WS2812B RGB serial LED
- 0.42-inch OLED over I2C
- Qwiic I2C connector
- One pushbutton
- Onboard ceramic chip antenna
- On-chip USB-UART converter

Note

The RGB led is not supported on this Zephyr board yet.

Note

The ESP32-C3 does not have native USB, it has an on-chip USB-serial converter
instead.

### Supported Features

The 01space ESP32C3 0.42 OLED board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| PMP | on-chip | arch/riscv |
| INTMTRX | on-chip | intc\_esp32c3 |
| PINMUX | on-chip | pinctrl\_esp32 |
| USB UART | on-chip | serial\_esp32\_usb |
| GPIO | on-chip | gpio\_esp32 |
| UART | on-chip | uart\_esp32 |
| I2C | on-chip | i2c\_esp32 |
| SPI | on-chip | spi\_esp32\_spim |
| RADIO | on-chip | Bluetooth |
| DISPLAY | off-chip | display |

### Connections and IOs

See the following image:

![01space ESP32C3 0.42 OLED Pinout](../../../../_images/esp32c3_042_oled_pinout.webp)

01space ESP32C3 0.42 OLED Pinout

It also features a 0.42 inch OLED display, driven by a SSD1306-compatible chip.
It is connected over I2C: SDA on GPIO5, SCL on GPIO6.

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs. Run the command below to
retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

## Programming and Debugging

### Standalone application

The board can be loaded using a single binary image, without 2nd stage bootloader.
It is the default option when building the application without additional configuration.

Note

This mode does not provide any security features nor OTA updates.

Use the following command to build a sample hello\_world application:

```shell
# From the root of the zephyr repository
west build -b esp32c3_042_oled samples/hello_world
```

### Sysbuild

[Sysbuild (System build)](../../../../build/sysbuild/index.md#sysbuild) makes it possible to build and flash all necessary images needed to
bootstrap the board.

By default, the ESP32 sysbuild configuration creates bootloader (MCUboot) and
application images.

To build the sample application using sysbuild, use this command:

```shell
west build -b esp32c3_042_oled --sysbuild samples/hello_world
```

### Flashing

For the `Hello, world!` application, follow the instructions below.
Assuming the board is connected to `/dev/ttyACM0` on Linux.

```shell
# From the root of the zephyr repository
west build -b esp32c3_042_oled samples/hello_world
west flash --esp-device /dev/ttyACM0
```

Since the Zephyr console is by default on the `usb_serial` device, we use
the espressif monitor utility to connect to the console.

```shell
$ west espressif monitor -p /dev/ttyACM0
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! esp32c3_042_oled
```

## References

[[1](#id4)]

[https://www.espressif.com/en/products/socs/esp32-c3](https://www.espressif.com/en/products/socs/esp32-c3)

[[2](#id6)]

[https://github.com/01Space/ESP32-C3-0.42LCD](https://github.com/01Space/ESP32-C3-0.42LCD)
