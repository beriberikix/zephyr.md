---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ezurio/bl654_dvk/doc/bl654_dvk.html
original_path: boards/ezurio/bl654_dvk/doc/bl654_dvk.html
---

# BL654 DVK

Board Overview

[![../../../../_images/bl654_dvk.jpg](../../../../_images/bl654_dvk.jpg)
](../../../../_images/bl654_dvk.jpg)

BL654 DVK

Name:
:   `bl654_dvk`

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/bl654_dvk/doc/bl654_dvk.rst/../..)

## Overview

The BL654 Development Kit hardware provides
support for the Ezurio BL654 module powered by a Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU.

It is also pin compatible with the BL654PA which adds a power amplifier. The “pa” variant provides
this compatibility. Use board `bl654_dvk/nrf52840/pa` to build for that target.
Bluetooth LE regulatory certifications obtained by Ezurio are not applicable to BL654PA variant.
It should not be used in commercial applications prior to re-certification being performed - please review with the Ezurio team at www.ezurio.com/contact

This development kit has the following features:

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
- USB
- WDT

![455-00001 Box Contents](../../../../_images/455-00001_BoxContents.jpg)

455-00001 (BL654 DVK integrated antenna) Box Contents

More information about the board can be found at the
[BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[1]](#id3).

## Hardware

### Supported Features

The `bl654_dvk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

See [BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[1]](#id3)
for a complete list of BL654 Development Kit board hardware features.

### Connections and IOs

#### LED

- LED1 (blue) = P0.13
- LED2 (blue) = P0.14
- LED3 (blue) = P0.15
- LED4 (blue) = P0.16

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.12
- BUTTON3 = SW9 = P0.24
- BUTTON4 = SW10 = P0.25
- RESET = SW3 = nReset/IF BOOT

## Programming and Debugging

Applications for the `bl654_dvk` board configuration can be built, flashed,
and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

NOTE: On the BL654 DVK, the FTDI USB should be used to access the UART console.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF52 DK
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl654_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic based boards with a
Segger IC.

## Testing Bluetooth on the BL654 DVK

Many of the Bluetooth examples will work on the BL654 DVK.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

## Testing the LEDs and buttons on the BL654 DVK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/ezurio/bl654\_dvk/bl654\_dvk.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/bl654_dvk/bl654_dvk.dts).

## References

[1]
([1](#id4),[2](#id5))

[https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series)
