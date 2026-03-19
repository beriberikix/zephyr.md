---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/modbus/rtu_server/README.html
original_path: samples/subsys/modbus/rtu_server/README.html
---

# Modbus RTU server

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/modbus/rtu_server/README.rst/..)

## Overview

This is a simple application demonstrating a Modbus RTU server implementation
in Zephyr RTOS.

## Requirements

This sample has been tested with the nRF52840-DK and FRDM-K64F boards,
but it should work with any board that has a free UART interface or USB
device controller. Additionally the board should have three LEDs.

RTU server example is running on an evaluation board. Client is running
on a PC or laptop.

The description of this sample uses [PyModbus](https://github.com/pymodbus-dev/pymodbus) (Pymodbus REPL).
The user can of course try out other client implementations with this sample.

### Using RS-485 transceiver

It is the default configuration of this sample.
In addition to the evaluation board, an USB to RS-485 bus adapter and
a RS-485 shield are required. The shield converts UART TX, RX signals to RS-485.
An Arduino header compatible shield like [joy-it RS-485 shield for Arduino](https://joy-it.net/en/products/ARD-RS485)
can be used. This example uses DE signal, which is controlled by pin D9
on the JOY-IT shield. For other shields, `de-gpios` property must be adapted
or removed in the application overlay file
[samples/subsys/modbus/rtu\_server/app.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/rtu_server/app.overlay)

The USB to RS-485 adapter connects to the USB port of a computer.
The two A+, B- lines should be connected to the RS-485 shield.

### Using CDC ACM UART

Only an evaluation board with supported USB device controller is required.
USB device port should be connected to the USB port of a computer.
Although it is only a point to point connection and does not represent a bus,
it can, apart from testing the server implementation, also be used practically
for example to control relays or to read ADC values via USB connection without
implementing custom USB class or driver.

## Building and Running

This sample can be found under
[samples/subsys/modbus/rtu\_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/rtu_server) in the Zephyr tree.

The following commands build and flash RTU server sample.

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/modbus/rtu_server
west flash
```

The following commands build and flash RTU server sample using CDC ACM UART.

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/modbus/rtu_server -- -DDTC_OVERLAY_FILE=cdc-acm.overlay -DEXTRA_CONF_FILE=overlay-cdc-acm.conf
west flash
```

On the client side, PC or laptop, the following command connects PyModbus
to the RTU server. If CDC ACM UART is used, ttyUSB should be replaced by a
matching ttyACM device.

```shell
# pymodbus.console serial --port /dev/ttyUSB0 --baudrate 19200
                          --bytesize 8 --parity N --stopbits 2
```

The LEDs on the board are controlled by Modbus commands FC01, FC05, FC15.
For example, to set LED0 on use FC01 command (write\_coil).

```shell
> client.write_coil address=0 value=1 slave=1
```

Client should confirm successful communication and LED0 should light.

```shell
{
    "address": 0,
    "value": true
}
```

To set LED0 off but LED1 and LED2 on use FC15 command (write\_coils).

```shell
> client.write_coils address=0 values=0,1,1 slave=1
```

To read LED0, LED1, LED2 state FC05 command (read\_coils) can be used.

```shell
> client.read_coils address=0 count=3 slave=1
{
    "bits": [
        false,
        true,
        true,
        false,
        false,
        false,
        false,
        false
    ]
}
```

It is also possible to write and read the holding registers.
This however does not involve any special interaction
with the peripherals on the board yet.

To write single holding registers use FC06 command (write\_register),

```shell
> client.write_register address=0 value=42 slave=1
```

or FC16 command (write\_registers).

```shell
> client.write_registers address=0 values=42,42,42 slave=1
```

To read holding registers use FC03 command (read\_holding\_registers).

```shell
> client.read_holding_registers address=0 count=3 slave=1
{
    "registers": [
        42,
        42,
        42
    ]
}
```

## See also

[MODBUS](../../../../doxygen/html/group__modbus.md)
