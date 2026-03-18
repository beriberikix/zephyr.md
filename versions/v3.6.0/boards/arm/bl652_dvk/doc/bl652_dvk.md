---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/bl652_dvk/doc/bl652_dvk.html
original_path: boards/arm/bl652_dvk/doc/bl652_dvk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Laird Connectivity BL652 DVK

## Overview

The BL652 Development Kit hardware provides
support for the Laird Connectivity BL652 module powered by a Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

Available BL652 DVK part numbers:

- DVK-BL652-SA
- DVK-BL652-SC

![BL652 DVK](../../../../_images/bl652_dvk.jpg)

BL652 DVK Board

![BL652-SA DVK Box Contents](../../../../_images/BL652-SA_DVK_BoxContents.jpg)

BL652-SA DVK Box Contents

More information about the board can be found at the
[BL652 Module Website](https://connectivity.lairdtech.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl652-series-bluetooth-v5-nfc) [[1]](#id3).

## Hardware

### Supported Features

The BL652 DVK board configuration supports the following
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
| RADIO | on-chip | Bluetooth |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [BL652 Module Website](https://connectivity.lairdtech.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl652-series-bluetooth-v5-nfc) [[1]](#id3).

### Connections and IOs

#### LED

- LED1 (blue) = P0.17
- LED2 (blue) = P0.19

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.15
- Reset = SW3 = boot/reset

#### External Connectors

#### Arduino Headers

J33/J23 Power

| PIN # | Signal Name | NRF52832 Functions |
| --- | --- | --- |
| 1 | NC | N/A |
| 2 | IOREF (3v3) | N/A |
| 3 | RESET | P0.21 / RESET |
| 4 | 3v3 | N/A |
| 5 | 5V | N/A |
| 6 | GND | N/A |
| 7 | GND | N/A |
| 8 | VIN (12V) | N/A |

J31/J16 Analog in

| PIN # | Signal Name | NRF52832 Functions |
| --- | --- | --- |
| 1 | A0 | P0.03 / AIN1 |
| 2 | A1 | P0.04 / AIN2 |
| 3 | A2 | P0.28 / AIN4 |
| 4 | A3 | P0.29 / AIN5 |
| 5 | A4 | P0.30 / AIN6 |
| 6 | A5 | P0.31 / AIN7 |

J30/J15 Digital I/O

| PIN # | Signal Name | NRF52832 Functions |
| --- | --- | --- |
| 1 | D0 (RX) | P0.11 |
| 2 | D1 (TX) | P0.12 |
| 3 | D2 | P0.13 |
| 4 | D3 | P0.14 / TRACEDATA[3] |
| 5 | D4 | P0.15 / TRACEDATA[2] |
| 6 | D5 | P0.16 / TRACEDATA[1] |
| 7 | D6 | P0.17 |
| 8 | D7 | P0.18 / TRACEDATA[3] / SWO |

J32/J22 Digital I/O

| PIN # | Signal Name | NRF52832 Functions |
| --- | --- | --- |
| 1 | D8 | P0.19 |
| 2 | D9 | P0.20 / TRACECLK |
| 3 | D10 (SS) | P0.22 |
| 4 | D11 (MOSI) | P0.23 |
| 5 | D12 (MISO) | P0.24 |
| 6 | D13 (SCK) | P0.25 |
| 7 | GND | N/A |
| 8 | AREF | P0.02 / AIN0 |
| 9 | SDA | P0.26 |
| 10 | SCL | P0.27 |

## Programming and Debugging

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

NOTE: On the BL652 DVK, the FTDI USB should be used to access the UART console.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the BL652 DVK
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bl652_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic based boards with a
Segger IC.

## Testing Bluetooth on the BL652 DVK

Many of the Bluetooth examples will work on the BL652 DVK.
Try them out:

- [Bluetooth: Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble-peripheral)
- [Bluetooth: Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth-eddystone-sample)
- [Bluetooth: iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth-ibeacon-sample)

## Testing the LEDs and buttons in the BL652 DVK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/arm/bl652\_dvk/bl652\_dvk.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/bl652_dvk/bl652_dvk.dts).

## References

[1]
([1](#id4),[2](#id5))

[https://connectivity.lairdtech.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl652-series-bluetooth-v5-nfc](https://connectivity.lairdtech.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl652-series-bluetooth-v5-nfc)
