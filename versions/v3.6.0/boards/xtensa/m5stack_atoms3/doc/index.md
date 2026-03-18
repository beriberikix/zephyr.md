---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/xtensa/m5stack_atoms3/doc/index.html
original_path: boards/xtensa/m5stack_atoms3/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# M5Stack AtomS3

## Overview

M5Stack AtomS3 is an ESP32-based development board from M5Stack.

It features the following integrated components:

- ESP32-S3FN8 chip (240MHz dual core, Wi-Fi/BLE 5.0)
- 512KB of SRAM
- 384KB of ROM
- 8MB of Flash
- LCD IPS TFT 0.85”, 128x128 px screen (ST7789 compatible)
- 6-axis IMU MPU6886
- Infrared emitter

![M5Stack AtomS3](../../../../_images/m5stack_atoms3.webp)

M5Stack AtomS3

### Supported Features

The Zephyr m5stack\_atoms3 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| CLOCK | on-chip | reset and clock control |
| COUNTER | on-chip | rtc |
| WATCHDOG | on-chip | independent watchdog |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| DAC | on-chip | dac |
| die-temp | on-chip | die temperature sensor |

## Start Application Development

Before powering up your M5Stack AtomS3, please make sure that the board is in good
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

#### Building & Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b m5stack_atoms3 samples/hello_world
```

The usual `flash` target will work with the `m5stack_atoms3` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world)
application.

```shell
# From the root of the zephyr repository
west build -b m5stack_atoms3 samples/hello_world
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
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! m5stack_atoms3
```

#### Debugging

M5Stack AtomS3 debugging is not supported due to pinout limitations.

## Related Documents

- [M5Stack AtomS3 schematic](https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3/img-b85e925c-adff-445d-994c-45987dc97a44.jpg)
- [ESP32S3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)
