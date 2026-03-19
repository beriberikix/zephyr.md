---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ezurio/bl654_sensor_board/doc/bl654_sensor_board.html
original_path: boards/ezurio/bl654_sensor_board/doc/bl654_sensor_board.html
---

# BL654 Sensor Board

Board Overview

[![../../../../_images/bl654_sensor_board.jpg](../../../../_images/bl654_sensor_board.jpg)
](../../../../_images/bl654_sensor_board.jpg)

BL654 Sensor Board

Name:
:   `bl654_sensor_board`

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/bl654_sensor_board/doc/bl654_sensor_board.rst/../..)

## Overview

The BL654 Sensor Board hardware provides support for the Ezurio
BL654 module which is powered by a Nordic Semiconductor nRF52840 ARM
Cortex-M4F CPU.

This sensor board has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

![BL654 Sensor Board connected to USB-SWD Programmer (UART and SWD access)](../../../../_images/bl654_sensor_board_usb_swd_programmer.jpg)

BL654 Sensor Board connected to USB-SWD Programmer (UART and SWD access)

More information about the BL654 module can be found on the [BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[2]](#id5),
more information about the USB-SWD Programmer can be found on the
[USB-SWD Programmer website](https://www.ezurio.com/usb-swd-programmer) [[4]](#id9).

## Hardware

### Supported Features

The `bl654_sensor_board` board supports the hardware features listed below.

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

- LED1 (blue) = P0.16 (active low)

#### Push button

- BUTTON1 (SW1) = P1.03 (active high)

#### Sensor

The BL654 Sensor Board has an on-board Bosch BME280
temperature/humidity/pressure sensor which is connected to the BL654 via I2C.

- SCL = P0.27
- SDA = P0.26

More information about the Bosch BME280 sensor can be found on the
[Bosch BME280 sensor website](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) [[1]](#id3).

## Powering the sensor

The sensor can be powered directly from a coin cell or from a voltage supplied
on the UART pins, the board accepts voltage from 1.8v-3.3v. Note that if using a
battery with a UART/debugger connected, the voltage of the UART/debugger (if it
does not automatically sense/adjust) must be within 0.3v of the voltage of the
coin cell to prevent suppression diodes in the nRF52840 silicon being activated
or possible back-powering of the battery.

To power the board from an external source via UART, the solder bridge SB1 must
be blobbed.

## Programming and Debugging

Applications for the `bl654_sensor_board` board configuration can be built,
flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running. An external
debugger/programmer is required which can be connected to using a Tag-Connect
TC2030-CTX cable, a Ezurio USB-SWD Programmer board or Segger JLink
programmer can be used to program and debug the BL654 sensor board.

### Flashing

If using an external JLink, follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger)
page to install and configure all the necessary software. Further information
can be found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash applications
as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details). If using a Ezurio USB-SWD Programmer Board, see the
[pyOCD website](https://github.com/pyocd/pyOCD) [[3]](#id7) to find details about the software and how to install it.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output - note that an
external UART is required to be connected to the BL654 sensor board’s UART, if
using the Ezurio USB-SWD Programmer Board, the BL654 sensor board
can be plugged in to the UART header. An FTDI cable can also be used - the
voltage of the I/O lines and power line must be between 1.8v and 3.3v, do not
connect an FTDI cable with a 5v power line to the BL654 sensor board.

J3 UART connector pinout (all pins referenced to operating voltage Vdd):

| Pin No. | Name | Description | Direction |
| --- | --- | --- | --- |
| 1 | GND | GND | (N/A) |
| 2 | RTS | UART Ready-to-send pin | OUT |
| 3 | VDD | Supply voltage (requires SB1 to be blobbed) | (N/A) |
| 4 | RXD | UART Receive pin | IN |
| 5 | TXD | UART Transmit pin | (N/A) |
| 6 | CTS | UART Clear-to-send pin | IN |

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BL654 sensor board
can be found. For example, under Linux, `/dev/ttyACM0`.

The BL654 sensor board needs an external programmer to program it, any SWD
programmer which has a 9-pin ARM debug port can be used with a Tag-Connect
TC2030-CTX cable. If using the Ezurio USB-SWD Programmer Board,
connect the cable to P1 and ensure the board is set to supply power to the
target at 3.3v.

J1 Tag-Connect SWD Pinout:

| Pin No. | Name | Description | Direction |
| --- | --- | --- | --- |
| 1 | VDD | Operating voltage | (N/A) |
| 2 | SWDIO | Serial wire data input/output pin | IN/OUT |
| 3 | nRESET | Module reset pin | IN |
| 4 | SWCLK | Serial wire clock input pin | IN |
| 5 | GND | GND | (N/A) |
| 6 | SWO | Serial wire output pin | OUT |

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl654_sensor_board samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic based
boards if using an external JLink debugger. If using a Ezurio
USB-SWD Programmer Board, pyOCD can be used for debugging.

## Testing Bluetooth on the BL654 Sensor Board

Many of the Bluetooth examples will work on the BL654 Sensor Board.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

## Testing the LED and button on the BL654 Sensor Board

There are 2 samples that allow you to test that the button (switch) and LED on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/ezurio/bl654\_sensor\_board/bl654\_sensor\_board.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl654_sensor_board/bl654_sensor_board.dts).

## References

[[1](#id4)]

[https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)

[[2](#id6)]

[https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series)

[[3](#id8)]

[https://github.com/pyocd/pyOCD](https://github.com/pyocd/pyOCD)

[[4](#id10)]

[https://www.ezurio.com/usb-swd-programmer](https://www.ezurio.com/usb-swd-programmer)
