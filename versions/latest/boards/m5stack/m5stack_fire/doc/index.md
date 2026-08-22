---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/m5stack/m5stack_fire/doc/index.html
original_path: boards/m5stack/m5stack_fire/doc/index.html
---

# Fire

Board Overview

[![../../../../_images/m5stack_fire.webp](../../../../_images/m5stack_fire.webp)
](../../../../_images/m5stack_fire.webp)

Fire

Name:
:   `m5stack_fire`

Vendor:
:   M5Stack

Architecture:
:   xtensa

SoC:
:   esp32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/m5stack/m5stack_fire/doc/index.rst/../..)

## Overview

M5Stack Fire is an ESP32-based development board from M5Stack.

M5Stack Fire features the following integrated components:

- ESP32-D0WDQ6 chip (240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi)
- PSRAM 8MB
- Flash 16MB
- LCD IPS TFT 2”, 320x240 px screen (ILI9342C)
- Charger IP5306
- Audio NS4148 amplifier (1W-092 speaker)
- USB CH9102F
- SD-Card slot
- Grove connector
- IMO 6-axis IMU MPU6886
- MIC BSE3729
- Battery 500mAh 3,7V
- Three physical buttons
- LED strips

## Functional Description

The following table below describes the key components, interfaces, and controls
of the M5Stack Core2 board.

| Key Component | Description | Status |
| --- | --- | --- |
| ESP32-D0WDQ6-V2 module | This [MPU-ESP32](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/esp32_datasheet_en_v3.9.pdf) module provides complete Wi-Fi and Bluetooth functionalities and integrates a 16-MB SPI flash. | supported |
| USB Port | USB interface. Power supply for the board as well as the communication interface between a computer and the board. | supported |
| Power Switch | Power on/off button. | supported |
| General purpose buttons | Three buttons on the front face of the device accesible using the GPIO interface. | supported |
| LCD screen | Built-in LCD TFT display ([LCD-ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf), 2”, 320x240 px) controlled via SPI interface | supported |
| SD-Card slot | SD-Card connection via SPI-mode. | supported |
| 6-axis IMU MPU6886 | The [MPU-6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf) is a 6-axis motion tracker (6DOF IMU) device that combines a 3-axis gyroscope and a 3-axis accelerometer. | supported |
| Grove port | Used to interface with the many available modules and sensors. | supported |
| Built-in speaker | 1W speaker for analog audio output. | supported |
| Built-in microphone | The BSE3729 analog microphone. | todo |
| LED strip | LED strips on the side of the device. | todo |
| Battery-support | Charging is supported automatically via the [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf). But there is no possibility to query current battery status. | todo |

### Supported Features

The `m5stack_fire` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Start Application Development

Before powering up your M5Stack Fire, please make sure that the board is in good
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

The `m5stack_fire` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b m5stack_fire/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `m5stack_fire` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b m5stack_fire/esp32/procpu samples/hello_world
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
Hello World! m5stack_fire
```

#### Debugging

M5Stack Fire debugging is not supported due to pinout limitations.

## Related Documents

- [M5Stack-Fire schematic](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206.pdf) (PDF)
- [M5Stack-Fire docs](https://docs.m5stack.com/en/core/fire_v2.7)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) (PDF)
- [ESP32 Hardware Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html)
