---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/vngiotlab/nrf52_vbluno52/doc/index.html
original_path: boards/vngiotlab/nrf52_vbluno52/doc/index.html
---

# nRF52-VBLUno52

Board Overview

[![../../../../_images/nrf52_vbluno52.jpg](../../../../_images/nrf52_vbluno52.jpg)
](../../../../_images/nrf52_vbluno52.jpg)

nRF52-VBLUno52

Name:
:   `nrf52_vbluno52`

Vendor:
:   VNGIoTLab

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/vngiotlab/nrf52_vbluno52/doc/index.rst/../..)

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

## Hardware

The VBLUno52 board has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 64 MHz.

### Supported Features

The `nrf52_vbluno52` board supports the hardware features listed below.

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
example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nrf52_vbluno52 samples/hello_world
west flash
```

## Testing the VBLUno52 with Zephyr: buttons, LEDs, UART, BLE

Here are some sample applications that you can use to test different
components on the VBLUno52 board:

- [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")
- [Beacon](../../../../samples/bluetooth/beacon/README.md#bluetooth_beacon "Advertise an Eddystone URL using GAP Broadcaster role.")
- [Heart-rate Monitor (Peripheral)](../../../../samples/bluetooth/peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.")
