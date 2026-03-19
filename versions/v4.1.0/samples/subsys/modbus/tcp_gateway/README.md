---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/modbus/tcp_gateway/README.html
original_path: samples/subsys/modbus/tcp_gateway/README.html
---

# Modbus TCP-to-serial gateway

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/modbus/tcp_gateway/README.rst/..)

## Overview

This is a simple application demonstrating a gateway implementations between
an Ethernet TCP-IP network and a Modbus serial line.

## Requirements

This sample has been tested with FRDM-K64F board,
but it should work with any board or shield that has a network interface.

Gateway example is running on an evaluation board and communicates
with another board that has been prepared according to the instructions in
[Modbus RTU server](../rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.") sample. Client is running on a PC or laptop.

The description of this sample uses [PyModbus](https://github.com/pymodbus-dev/pymodbus) (Pymodbus REPL).
The user can of course try out other client implementations with this sample.

In addition to the evaluation boards RS-485 shields may be used.
The A+, B- lines of the RS-485 shields should be connected together.
Alternatively UART RX,TX signals of two boards can be connected crosswise.

## Building and Running

This sample can be found under
[samples/subsys/modbus/tcp\_gateway](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/tcp_gateway) in the Zephyr tree.

The following commands build and flash gateway sample.

```shell
west build -b frdm_k64f samples/subsys/modbus/tcp_gateway
west flash
```

On the client side, PC or laptop, the following command connects PyModbus
to the gateway.

```shell
# pymodbus.console tcp --host 192.0.2.1 --port 502
```

The LEDs on the server board are controlled by Modbus commands FC01, FC05, FC15.
For example, to set LED0 on use FC01 command (write\_coil).

```shell
> client.connect
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

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)
