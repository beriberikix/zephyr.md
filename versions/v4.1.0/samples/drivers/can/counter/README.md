---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/can/counter/README.html
original_path: samples/drivers/can/counter/README.html
---

# Controller Area Network (CAN) counter

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/can/counter/README.rst/..)

## Overview

This sample demonstrates how to use the Controller Area Network (CAN) API.
Messages with standard and extended identifiers are sent over the bus.
Messages are received using message-queues and work-queues.
Reception is indicated by blinking the LED (if present) and output of
received counter values to the console.

## Building and Running

In loopback mode, the board receives its own messages. This could be used for
standalone testing.

The LED output pin is defined in the board’s devicetree.

The sample can be built and executed for boards with a SoC that have an
integrated CAN controller or for boards with a SoC that has been augmented
with a stand alone CAN controller.

### Integrated CAN controller

For the NXP TWR-KE18F board:

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/drivers/can/counter
west flash
```

### Stand alone CAN controller

For the nrf52dk/nrf52832 board combined with the DFRobot CAN bus V2.0 shield that
provides the MCP2515 CAN controller:

```shell
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 --shield dfrobot_can_bus_v2_0 samples/drivers/can/counter
west flash
```

### Sample output

```shell
Change LED filter ID: 0
Finished init.
Counter filter id: 4

uart:~$ Counter received: 0
Counter received: 1
Counter received: 2
Counter received: 3
```

Note

The values shown above might differ.

## See also

[CAN Interface](../../../../doxygen/html/group__can__interface.md)
