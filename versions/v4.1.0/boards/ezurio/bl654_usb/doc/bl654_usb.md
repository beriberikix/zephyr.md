---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ezurio/bl654_usb/doc/bl654_usb.html
original_path: boards/ezurio/bl654_usb/doc/bl654_usb.html
---

# BL654 USB (451-00004)

Board Overview

[![../../../../_images/bl654_usb.jpg](../../../../_images/bl654_usb.jpg)
](../../../../_images/bl654_usb.jpg)

BL654 USB (451-00004)

Name:
:   `bl654_usb`

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/bl654_usb/doc/bl654_usb.rst/../..)

## Overview

The BL654 USB adapter hardware (Ezurio part 451-00004) provides
support for the Ezurio BL654 module powered by a Nordic
Semiconductor nRF52840 ARM Cortex-M4F CPU.

This USB adapter has the following features:

- CLOCK
- FLASH
- GPIO
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- USB
- WDT
- RTC

![451-00004 Box Contents](../../../../_images/bl654_usb_pcb.jpg)

BL654 USB Adapter PCB

More information about the BL654 USB adapter can be found on the [BL654 USB
Dongle Quick Start Guide](https://www.ezurio.com/documentation/user-guide-bl654-usb-nordic-sdk-zephyr) [[1]](#id3). There is more information on the BL654 range on
the [BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[2]](#id5).

## Hardware

### Supported Features

The `bl654_usb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

See [BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[2]](#id5)
for a complete list of BL654 USB adapter hardware features.

### Connections and IOs

#### LED

- LED1 (blue) = P0.13

#### Push buttons

- RESET = SW1 = nReset

### Serial Port

Zephyr console output is available as follows:

- using the USB connector, which may be used to make the console available on PC as
  USB CDC class.

## Programming and Debugging

Applications for the `bl654_usb` board configuration can be
built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details). The
`bl654_usb` board cannot be used for debugging. The compatible BL654 DVK
board can be used for development. Documentation can be found at the [BL654 DVK](../../bl654_dvk/doc/bl654_dvk.md#bl654_dvk)
site and [boards/ezurio/bl654\_dvk/doc/bl654\_dvk.rst](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl654_dvk/doc/bl654_dvk.rst)

### Flashing

The board supports programming using the built-in bootloader.

The board is factory-programmed with a Ezurio variation of Nordic’s
open bootloader from Nordic’s nRF5x SDK. With this option, you’ll use
Nordic’s [nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil) [[3]](#id8) program to create firmware packages supported by this
bootloader and flash them to the device. Before proceeding, make sure:

- `nrfutil` is installed.
- The `nrf5sdk-tools` command is installed within `nrfutil`.

1. With the adapter plugged in, reset the board into the bootloader by pressing
   the RESET button.

   The push button is in a pin-hole on the logo side of the USB adapter.

   ![Location of RESET button](../../../../_images/bl654_usb_reset.jpg)

   The blue LED should start a fade pattern, signalling the bootloader is
   running.
2. Compile a Zephyr application; we’ll use [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.").

   ```shell
   west build -b bl654_usb zephyr/samples/basic/blinky
   ```
3. Package the application for the bootloader using `nrfutil`:

   ```shell
   nrfutil nrf5sdk-tools pkg generate \
            --hw-version 52 \
            --sd-req=0x00 \
            --application build/zephyr/zephyr.hex \
            --application-version 1 \
            blinky.zip
   ```
4. Flash it onto the board. Note `/dev/ttyACM0` is for Linux; it will be
   something like `COMx` on Windows, and something else on macOS.

   ```shell
   nrfutil nrf5sdk-tools dfu usb-serial -pkg blinky.zip -p /dev/ttyACM0
   ```

   When this command exits, observe the blue LED on the board blinking.

## Testing Bluetooth on the BL654 USB

Many of the Bluetooth examples will work on the BL654 USB.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

## Testing the LED on the BL654 USB

There is a sample that allows you to test that the LED on
the board is working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")

You can build and flash the example to make sure Zephyr is running correctly on
your board. The LED definitions can be found in
[boards/ezurio/bl654\_usb/bl654\_usb.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl654_usb/bl654_usb.dts).

## References

[[1](#id4)]

[https://www.ezurio.com/documentation/user-guide-bl654-usb-nordic-sdk-zephyr](https://www.ezurio.com/documentation/user-guide-bl654-usb-nordic-sdk-zephyr)

[2]
([1](#id6),[2](#id7))

[https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series)

[[3](#id9)]

[https://github.com/NordicSemiconductor/pc-nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil)
