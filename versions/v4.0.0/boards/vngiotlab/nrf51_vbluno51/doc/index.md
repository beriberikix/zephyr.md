---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/vngiotlab/nrf51_vbluno51/doc/index.html
original_path: boards/vngiotlab/nrf51_vbluno51/doc/index.html
---

# nRF51-VBLUno51

Board Overview

[![../../../../_images/nrf51_vbluno51.jpg](../../../../_images/nrf51_vbluno51.jpg)
](../../../../_images/nrf51_vbluno51.jpg)

nRF51-VBLUno51

Vendor:
:   VNGIoTLab

Architecture:
:   arm

SoC:
:   nrf51822

## Overview

Zephyr uses the nrf51\_vbluno51 board configuration to run on the VBLUno51 board,
a VNG Bluetooth Low Energy UNO using an nRF51822 ARM processor.

![nRF51_VBLUno51 Bottom](../../../../_images/nrf51_vbluno51_bot.jpg)

nrf51\_vbluno51 Bottom

More information about the board can be found at the
[VBLUno51 wiki page](https://vngiotlab.github.io/vbluno/) [[1]](#id5).

## Hardware

VBLUno51 board has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 16 MHz.

### Supported Features

- CPU:
  :   - Nordic nRF51822: ARM® Cortex™ M0 32bit.
      - *Bluetooth Low Energy interface.*
      - 256KB Flash, 32KB RAM.
      - UART(1), I2C(2), SPI(1), PWM(3), SWD, Timer 16bit(3).
      - 21 digital channels, 6 ADC 10bit channels.
      - 1 Led and 1 Button onboard.
      - GPIO Voltage: 0 - 3.3V.
- DAPLink (CMSIS-DAP) interface for program and debug:
  :   - USB MSD: Drag and Drop programming flash memory.
      - USB HID (DAP): CMSIS-DAP compliant debug channel.
      - USB CDC: Virtual COM port for log, trace and terminal emulation.
- Supports hardware flow control features (RTS/CTS).
- *Energy monitoring for BLE module by current measurement (Only VBLUno51\_EM)*
- FOTA (Firmware over the air): Upgrade firmware over BLE interface.
- Build good applications with:
  :   - Compiler and IDE: GCC, Keil MDK, IAR, Eclipse, Qt Creator.
      - Frameworks: Arduino, ARM mbed-OS, Zephyr-OS, Nordic SDK, RIOT-OS, MyNewt-OS, ChibiOS, NuttX RTOS
      - A lot of tutorials for Arduino, mbed-os and more.
- Pinout: Arduino Uno Rev3 compliant.
- Power:
  :   - USB port.
      - Power adapter: +9 -> +12V.
      - 3V Battery: CR20xx holder
      - Rechargeable battery jump: +3.7 -> +12V
- Open source: Hardware design, firmware, packages, tutorial and example codes

See [VBLUno51 wiki page](https://vngiotlab.github.io/vbluno/) [[1]](#id5) for full documents and tutorials about the VBLUno51 board.

### Connections and IOs

#### LED

- LED = LED0 (green) = P0.7

#### Push buttons

- BUTTON = BUT = SW0 = P0.15

#### More details

![nRF51_VBLUno51 Pinout](../../../../_images/vbluno51_nordic_pinout.jpg)

nrf51\_vbluno51 Pinout

![nRF51_VBLUno51 Fritzing part](../../../../_images/vbluno51_frizting.jpg)

nrf51\_vbluno51 Fritzing part

## Programming and Debugging

Applications for the `nrf51_vbluno51` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The VBLUno51 board has on-board DAPLink (CMSIS-DAP) interface for flashing and debugging.
You do not need any other programming device.
You only need to install pyOCD tool ([https://pypi.python.org/pypi/pyOCD](https://pypi.python.org/pypi/pyOCD))

This tutorial uses the blinky application [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.").

See the [Getting Started Guide](../../../../develop/getting_started/index.md#getting-started) for general information on setting up
your development environment. Then build and flash the application in
the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf51_vbluno51 samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nrf51_vbluno51 samples/basic/blinky
west debug
```

## Testing the VBLUno51 with Zephyr: buttons, LEDs, UART, BLE

> Here are some sample applications that you can use to test different
> components on the VBLUno51 board:
>
> - [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
> - [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
> - [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")
> - [Beacon](../../../../samples/bluetooth/beacon/README.md#bluetooth_beacon "Advertise an Eddystone URL using GAP Broadcaster role.")
> - [Heart-rate Monitor (Peripheral)](../../../../samples/bluetooth/peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.")

## References

[1]
([1](#id6),[2](#id7))

[https://vngiotlab.github.io/vbluno/](https://vngiotlab.github.io/vbluno/)
