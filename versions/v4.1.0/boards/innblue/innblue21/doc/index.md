---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/innblue/innblue21/doc/index.html
original_path: boards/innblue/innblue21/doc/index.html
---

# nRF9160 INNBLUE21

Board Overview

[![../../../../_images/nrf9160_innblue21.jpg](../../../../_images/nrf9160_innblue21.jpg)
](../../../../_images/nrf9160_innblue21.jpg)

nRF9160 INNBLUE21

Name:
:   `innblue21`

Vendor:
:   innblue UG

Architecture:
:   arm

SoC:
:   nrf9160

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/innblue/innblue21/doc/index.rst/../..)

## Overview

The nRF9160 innblue21 is a cellular IoT sensor development board, which
is based on the nRF9160 SiP, and features NB-IoT and LTE-M connectivity.

## Hardware

The following parts are built into the board:

- Accelerometer: ST LIS2DH12
- CryptoElement: Atmel ATECC608a
- Humidity Sensor: ST HTS221
- Qi charger: TI BQ51013
- Battery fuel gauge: TI BQ27421

### Supported Features

The `innblue21` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

- LED1 ( red ) = P0.7
- LED2 (green) = P0.6
- LED3 ( blue) = P0.5
- LED4 ( red ) = P0.4

#### Push buttons and Switches

- BUTTON1 = P0.31

### Security components

- Implementation Defined Attribution Unit. The IDAU is implemented
  with the System Protection Unit and is used to define secure and non-secure
  memory maps. By default, all of the memory space (Flash, SRAM, and
  peripheral address space) is defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

innblue21 supports the Armv8m Security Extension, and by default boots
in the Secure state.

### Building Secure/Non-Secure Zephyr applications

The process requires the following steps:

1. Build the Secure Zephyr application using `-DBOARD=innblue21` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` in the application project configuration file.
2. Build the Non-Secure Zephyr application using `-DBOARD=innblue21/nrf9160/ns`.
3. Merge the two binaries together.

When building a Secure/Non-Secure application, the Secure application will
have to set the IDAU (SPU) configuration to allow Non-Secure access to all
CPU resources utilized by the Non-Secure application firmware. SPU
configuration shall take place before jumping to the Non-Secure application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=innblue21`.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the nRF9160 innblue21
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b innblue21 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.
