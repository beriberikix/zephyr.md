---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/nicla_sense_me/doc/index.html
original_path: boards/arduino/nicla_sense_me/doc/index.html
---

# Arduino Nicla Sense ME

Board Overview

[![../../../../_images/arduino_nicla_sense_me.jpg](../../../../_images/arduino_nicla_sense_me.jpg)
](../../../../_images/arduino_nicla_sense_me.jpg)

Arduino Nicla Sense ME

Name:
:   `arduino_nicla_sense_me`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/nicla_sense_me/doc/index.rst/../..)

## Overview

The [Arduino Nicla Sense ME](https://docs.arduino.cc/hardware/nicla-sense-me) [[1]](#id3) is designed around Nordic Semiconductor’s
nrf52832 ARM Cortex-M4F CPU. The board houses 4 low power industrial grade sensors
that can measure rotation, acceleration, pressure, humidity, temperature, air quality
and CO2 levels.

## Hardware

- nRF52832 ARM Cortex-M4 processor at 64 MHz
- 512 kB flash memory, 64 kB SRAM
- Bluetooth Low Energy
- Micro USB (USB-B)
- JST 3-pin 1.2 mm pitch battery connector
- 10 Digital I/O pins
- 2 Analog input pins
- 12 PWM pins
- One reset button
- RGB LED (I2C)
- On board sensors:

  - Accelerometer/Gyroscope: Bosch BHI260AP
  - Gas/Pressure/Temperature/Humidity: Bosch BME688
  - Geomagnetic: Bosch BMM150
  - Digital Pressure: Bosch BMP390

### Supported Features

The `arduino_nicla_sense_me` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### Available pins:

![Arduino Nicla Sense ME pinout](../../../../_images/arduino_nicla_sense_me_pinout.jpg)

Arduino Nicla Sense ME pinout (Credit: Arduino)

For more details please refer to the [datasheet](https://docs.arduino.cc/resources/datasheets/ABX00050-datasheet.pdf) [[2]](#id5), [full pinout](https://docs.arduino.cc/resources/pinouts/ABX00050-full-pinout.pdf) [[3]](#id7) and the [schematics](https://docs.arduino.cc/resources/schematics/ABX00050-schematics.pdf) [[4]](#id9).

## Programming and Debugging

The `arduino_nicla_sense_me` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `arduino_nicla_sense_me` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

First, connect the Arduino Nicla Sense ME board to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_nicla_sense_me samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arduino_nicla_sense_me
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_nicla_sense_me samples/hello_world
west debug
```

## References

[[1](#id4)]

[https://docs.arduino.cc/hardware/nicla-sense-me](https://docs.arduino.cc/hardware/nicla-sense-me)

[[2](#id6)]

[https://docs.arduino.cc/resources/datasheets/ABX00050-datasheet.pdf](https://docs.arduino.cc/resources/datasheets/ABX00050-datasheet.pdf)

[[3](#id8)]

[https://docs.arduino.cc/resources/pinouts/ABX00050-full-pinout.pdf](https://docs.arduino.cc/resources/pinouts/ABX00050-full-pinout.pdf)

[[4](#id10)]

[https://docs.arduino.cc/resources/schematics/ABX00050-schematics.pdf](https://docs.arduino.cc/resources/schematics/ABX00050-schematics.pdf)
