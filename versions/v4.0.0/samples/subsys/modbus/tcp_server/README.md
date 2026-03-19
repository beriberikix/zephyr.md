---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/modbus/tcp_server/README.html
original_path: samples/subsys/modbus/tcp_server/README.html
---

# Modbus TCP server

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/modbus/tcp_server/README.rst/..)

## Overview

This is a simple application demonstrating a Modbus TCP server implementation
in Zephyr RTOS.

## Requirements

This sample has been tested with FRDM-K64F board,
but it should work with any board or shield that has a network interface.
Additionally the board should have three LEDs.

TCP server example is running on an evaluation board. Client is running
on a PC or laptop.

The description of this sample uses [PyModbus](https://github.com/pymodbus-dev/pymodbus) (Pymodbus REPL).
The user can of course try out other client implementations with this sample.

## Building and Running

This sample can be found under
[samples/subsys/modbus/tcp\_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/tcp_server) in the Zephyr tree.

The following commands build and flash TCP server sample.

```shell
west build -b frdm_k64f samples/subsys/modbus/tcp_server
west flash
```

On the client side, PC or laptop, the following command connects PyModbus
to the TCP server.

```shell
# pymodbus.console tcp --host 192.0.2.1 --port 502
```

The LEDs on the board are controlled by Modbus commands FC01, FC05, FC15.
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
