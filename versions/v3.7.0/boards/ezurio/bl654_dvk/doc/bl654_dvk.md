---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/ezurio/bl654_dvk/doc/bl654_dvk.html
original_path: boards/ezurio/bl654_dvk/doc/bl654_dvk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Ezurio BL654 DVK

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

![BL654 Development Kit](../../../../_images/bl654_dvk.jpg)

BL654 Development Kit Board

![455-00001 Box Contents](../../../../_images/455-00001_BoxContents.jpg)

455-00001 (BL654 DVK integrated antenna) Box Contents

More information about the board can be found at the
[BL654 website](https://ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/bl654-series) [[1]](#id3).

## Hardware

### Supported Features

The BL654 DVK board configuration supports the following
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

Other hardware features have not been enabled yet for this board.
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

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

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

- [Bluetooth: Peripheral](../../../../samples/bluetooth/peripheral/README.md#ble-peripheral)
- [Bluetooth: Eddystone](../../../../samples/bluetooth/eddystone/README.md#bluetooth-eddystone-sample)
- [Bluetooth: iBeacon](../../../../samples/bluetooth/ibeacon/README.md#bluetooth-ibeacon-sample)

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
