---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf52_vbluno52/doc/index.html
original_path: boards/arm/nrf52_vbluno52/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF52-VBLUno52

## Overview

Zephyr can use the nrf52\_vbluno52 board configuration to run on the VBLUno52 board,
a VNG Bluetooth Low Energy UNO using an nRF52832 ARM Cortex-M4F processor.
It provides support for the Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU and
the following devices:

- NVIC
- RTC
- UART
- GPIO
- FLASH
- RADIO (Bluetooth Low Energy 5.0)

![nRF52 VBLUno52](../../../../_images/nrf52_vbluno52.jpg)

nRF52\_VBLUno52 board

## Hardware

The VBLUno52 board has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 64 MHz.

### Supported Features

The nrf52\_vbluno52 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| RTC | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| FLASH | on-chip | flash |
| RADIO | on-chip | Bluetooth |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

#### LED

- LED = LED0 (green) = P0.12

#### Push buttons

- BUTTON = BUT = SW0 = P0.17

## Programming and Debugging

### Flashing

The VBLUno52 board has an on-board DAPLink (CMSIS-DAP) interface for flashing and debugging.
You do not need any other programming device.
You only need to install the pyOCD tool ([https://pypi.python.org/pypi/pyOCD](https://pypi.python.org/pypi/pyOCD))

See the [Getting Started Guide](../../../../develop/getting_started/index.md#getting-started) for general information on setting up
your development environment.

You can build and flash applications in the usual way. Here is an
example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nrf52_vbluno52 samples/hello_world
west flash
```

## Testing the VBLUno52 with Zephyr: buttons, LEDs, UART, BLE

Here are some sample applications that you can use to test different
components on the VBLUno52 board:

- [Hello World](../../../../samples/hello_world/README.md#hello-world)
- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")
- [Bluetooth: Beacon](../../../../samples/bluetooth/beacon/README.md#bluetooth-beacon-sample)
- [Bluetooth: Peripheral HR](../../../../samples/bluetooth/peripheral_hr/README.md#peripheral-hr)
