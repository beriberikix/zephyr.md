---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ezurio/mg100/doc/index.html
original_path: boards/ezurio/mg100/doc/index.html
---

# Sentrius™ MG100 Gateway

Board Overview

[![../../../../_images/mg100.jpg](../../../../_images/mg100.jpg)
](../../../../_images/mg100.jpg)

Sentrius™ MG100 Gateway

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf52840

## Overview

The Sentrius™ MG100 Gateway offers a compact, out of box Bluetooth to low power cellular gateway
solution.

Based on the Pinnacle 100 socket modem, the Sentrius™ MG100 gateway captures data from any
Bluetooth 5 modules or devices and sends it to the cloud via a global low power cellular
(LTE-M/NB-IoT) connection. The MG100 seamlessly incorporates a powerful Cortex M4F controller,
full Bluetooth 5 connectivity, and dual-mode LTE-M/NB-IoT capabilities. The MG100 has full regulatory
and network certifications and End Device carrier approvals.

Develop your application directly on the integrated Cortex M4F microcontroller using Zephyr RTOS,
enabling your application development with a secure, open source RTOS with more than just kernel
services. Remotely debug your fleet of devices with the [Memfault Platform](https://docs.memfault.com/docs/mcu/pinnacle-100-guide) [[5]](#id12). Take advantage of the
Zephyr community and Ezurio’s [Canvas Software Suite](https://www.ezurio.com/canvas/software-suite) [[7]](#id16) to accelerate your development.
covering all aspects of the product’s capabilities and hardware interfaces. The MG100 also delivers
complete antenna flexibility with internal or external antenna options available, and the optional
battery backup provides uninterrupted reporting of remote Bluetooth sensor data.

More information about the board can be found at the [MG100 website](https://www.ezurio.com/iot-devices/iot-gateways/sentrius-mg100-gateway-lte-mnb-iot-and-bluetooth-5) [[1]](#id3).

The MG100 hardware provides support for the Nordic Semiconductor [nRF52840](https://www.nordicsemi.com/products/nrf52840) [[6]](#id14) ARM Cortex-M4F CPU,
[Sierra Wireless HL7800](https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs) [[2]](#id6)
and the following devices:

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
- SPI
- UART
- WDT
- QSPI
- LIS3DH
- HL7800
- SD Card

## Hardware

### Supported Features

The MG100 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |
| QSPI | on-chip | qspi/MX25R64(8MB) |
| LIS3DH | I2C(M) | sensor/lis3dh |
| HL7800 | UART | HL7800 modem driver |
| SDMMC | SPI(M) | SD Card via SPI |

See [MG100 website](https://www.ezurio.com/iot-devices/iot-gateways/sentrius-mg100-gateway-lte-mnb-iot-and-bluetooth-5) [[1]](#id3) for a complete list
of MG100 hardware features.

### Connections and IOs

#### LED

- LED1 (red) = P1.7
- LED2 (blue) = P1.6
- LED3 (green) = P1.5

#### Push buttons

- BUTTON1 = P0.3

#### External flash memory

A 64Mbit external flash memory part is available for storage of application
images and data. Refer to the [Macronix MX25R6435F datasheet](https://www.macronix.com/Lists/Datasheet/Attachments/7913/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.5.pdf) [[3]](#id8) for further
details.

The flash memory is connected to the on-board QSPI device controller.

- MX25R64 = QSPI

SCK = P0.19
IO0 = P0.20
IO1 = P0.21
IO2 = P0.22
IO3 = P0.23
CSN = P0.17

#### LIS3DH Motion Sensor

Motion sensor to detect if the gateway moves.

IRQ IO = P0.28
I2C SDA = P0.26
I2C SCL = P0.27

#### SD Card

SD card used to store large amounts of data.

SPI CS = P0.29
SPI SCK = P1.09
SPI MOSI = P0.11
SPI MISO = P0.12

## Programming and Debugging

Applications for the `mg100` board configuration can be
built and flashed in the usual way. (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details)

The [Ezurio USB-SWD Programming Kit](https://www.ezurio.com/wireless-modules/programming-kits/usb-swd-programming-kit) [[4]](#id10) contains all the necessary
hardware to enable programming and debugging an MG100.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

Note

On the MG100,
the USB connector should be used to access the UART console.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board MG100
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b mg100 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Software

### Canvas Software Suite

The MG100 is a supported hardware platform for [Canvas Software Suite](https://www.ezurio.com/canvas/software-suite) [[7]](#id16).

### Testing Bluetooth on the MG100

Many of the Bluetooth examples will work on the MG100.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

### Testing the LEDs and buttons in the MG100

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/ezurio/mg100/mg100.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/mg100/mg100.dts).

## References

[1]
([1](#id4),[2](#id5))

[https://www.ezurio.com/iot-devices/iot-gateways/sentrius-mg100-gateway-lte-mnb-iot-and-bluetooth-5](https://www.ezurio.com/iot-devices/iot-gateways/sentrius-mg100-gateway-lte-mnb-iot-and-bluetooth-5)

[[2](#id7)]

[https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs](https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs)

[[3](#id9)]

[https://www.macronix.com/Lists/Datasheet/Attachments/7913/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.5.pdf](https://www.macronix.com/Lists/Datasheet/Attachments/7913/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.5.pdf)

[[4](#id11)]

[https://www.ezurio.com/wireless-modules/programming-kits/usb-swd-programming-kit](https://www.ezurio.com/wireless-modules/programming-kits/usb-swd-programming-kit)

[[5](#id13)]

[https://docs.memfault.com/docs/mcu/pinnacle-100-guide](https://docs.memfault.com/docs/mcu/pinnacle-100-guide)

[[6](#id15)]

[https://www.nordicsemi.com/products/nrf52840](https://www.nordicsemi.com/products/nrf52840)

[7]
([1](#id17),[2](#id18))

[https://www.ezurio.com/canvas/software-suite](https://www.ezurio.com/canvas/software-suite)
