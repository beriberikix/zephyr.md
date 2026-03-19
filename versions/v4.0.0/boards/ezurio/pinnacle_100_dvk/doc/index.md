---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ezurio/pinnacle_100_dvk/doc/index.html
original_path: boards/ezurio/pinnacle_100_dvk/doc/index.html
---

# Pinnacle 100 DVK

Board Overview

[![../../../../_images/pinnacle_100_dvk.jpg](../../../../_images/pinnacle_100_dvk.jpg)
](../../../../_images/pinnacle_100_dvk.jpg)

Pinnacle 100 DVK

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf52840

## Overview

The Pinnacle™ 100 cellular modem seamlessly incorporates a powerful Cortex M4F
controller, full Bluetooth 5 and LTE-M/NB-IoT capabilities – all with full
regulatory certifications and LTE carrier approvals. The Pinnacle 100 also
delivers complete antenna flexibility, with pre-integrated internal or external
antenna options such as the Revie Flex family of LTE and NB-IoT
internal antennas.

Develop your application directly on the M4F controller using Zephyr RTOS to
cut BOM costs and power consumption. Take advantage of the Zephyr community,
Ezurio’s sample code (cellular, Bluetooth) and hardware interfaces,
or use our hosted mode AT commands set firmware.

Extremely power conscious, the Pinnacle 100 is ideal for battery-powered
devices operating at the edge of your IoT networks, seamlessly bridging the
cellular WAN to BLE. It’s never been easier to bridge wireless
Bluetooth 5 sensor data to cloud services like AWS IoT over a
low-power LTE connection.

More information about the board can be found at the [Pinnacle 100 website](https://www.ezurio.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem) [[1]](#id3).

The Pinnacle 100 Development Kit (453-00010-K1 or 453-00011-K1) hardware
provides support for the
Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU, [Sierra Wireless HL7800](https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs) [[2]](#id6) (Altair ALT1250)
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
- Segger RTT (RTT Console)
- SPI
- UART
- USB
- WDT
- QSPI
- BME680
- HL7800

## Hardware

### Supported Features

The Pinnacle 100 development board configuration supports the following
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
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |
| QSPI | on-chip | qspi/MX25R64(8MB) |
| BME680 | I2C(M) | sensor/bme680 |
| HL7800 | UART | HL7800 modem driver |

See [Pinnacle 100 website](https://www.ezurio.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem) [[1]](#id3) for a complete list
of Pinnacle 100 Development Kit hardware features.

### Connections and IOs

#### LED

- LED1 (blue) = P1.4
- LED2 (green) = P1.5
- LED3 (red) = P1.6
- LED4 (green) = P1.7

#### Push buttons

- BUTTON1 = SW1 = P0.31
- BUTTON2 = SW2 = P0.3
- BUTTON3 = SW3 = P0.4
- BUTTON4 = SW4 = P0.2
- NRF RESET = SW5 = reset

## Programming and Debugging

Applications for the `pinnacle_100_dvk` board configuration can be
built and flashed in the usual way. (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details)

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

Note

On the Pinnacle 100 development board,
the FTDI USB should be used to access the UART console.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board Pinnacle 100 DVK
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b pinnacle_100_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Software

### Canvas Software Suite

The Pinnacle 100 is a supported hardware platform for [Canvas Software Suite](https://www.ezurio.com/canvas/software-suite) [[4]](#id10).

### Sample Applications

[Pinnacle 100 Sample Applications](https://github.com/LairdCP/Pinnacle_100_Sample_Applications) [[3]](#id8) are available.

### Testing Bluetooth on the Pinnacle 100 DVK

Many of the Bluetooth examples will work on the Pinnacle 100 DVK.
Try them out:

- [Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
- [Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")
- [iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")

### Testing the LEDs and buttons in the Pinnacle 100 DVK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/ezurio/pinnacle\_100\_dvk/pinnacle\_100\_dvk.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/pinnacle_100_dvk/pinnacle_100_dvk.dts).

## References

[1]
([1](#id4),[2](#id5))

[https://www.ezurio.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem](https://www.ezurio.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem)

[[2](#id7)]

[https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs](https://source.sierrawireless.com/devices/hl-series/hl7800/#sthash.641qTTwA.dpbs)

[[3](#id9)]

[https://github.com/LairdCP/Pinnacle\_100\_Sample\_Applications](https://github.com/LairdCP/Pinnacle_100_Sample_Applications)

[[4](#id11)]

[https://www.ezurio.com/canvas/software-suite](https://www.ezurio.com/canvas/software-suite)
