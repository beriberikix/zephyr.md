---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/wemos/esp32s2_lolin_mini/doc/index.html
original_path: boards/wemos/esp32s2_lolin_mini/doc/index.html
---

# ESP32-S2 Lolin Mini

Board Overview

[![../../../../_images/esp32_s2_lolin_mini.jpg](../../../../_images/esp32_s2_lolin_mini.jpg)
](../../../../_images/esp32_s2_lolin_mini.jpg)

ESP32-S2 Lolin Mini

Name:
:   `esp32s2_lolin_mini`

Vendor:
:   WEMOS Electronics

Architecture:
:   xtensa

SoC:
:   esp32s2

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wemos/esp32s2_lolin_mini/doc/index.rst/../..)

## Overview

ESP32-S2 is a highly integrated, low-power, single-core Wi-Fi Microcontroller SoC, designed to be secure and
cost-effective, with a high performance and a rich set of IO capabilities. [[1]](#id2)

The features include the following:

- RSA-3072-based secure boot
- AES-XTS-256-based flash encryption
- Protected private key and device secrets from software access
- Cryptographic accelerators for enhanced performance
- Protection against physical fault injection attacks
- Various peripherals:

  - 43x programmable GPIOs
  - 14x configurable capacitive touch GPIOs
  - USB OTG
  - LCD interface
  - camera interface
  - SPI
  - I2S
  - UART
  - ADC
  - DAC
  - LED PWM with up to 8 channels

## System requirements

### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

### Building & Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b esp32s2_lolin_mini samples/hello_world
```

The usual `flash` target will work with the `esp32s2_lolin_mini` board
configuration after putting the board into bootloader mode by holding the ‘0’
button then pressing ‘RST’ and releasing the ‘RST’ button.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b esp32s2_lolin_mini samples/hello_world
west flash
```

Open a serial port using e.g. screen

```shell
screen /dev/ttyUSB0 115200
```

After the board has been manually reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! esp32s2_lolin_mini
```

## References

[[1](#id1)]

[https://www.espressif.com/en/products/socs/esp32-s2](https://www.espressif.com/en/products/socs/esp32-s2)
