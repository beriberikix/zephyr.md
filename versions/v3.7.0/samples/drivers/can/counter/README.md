---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/can/counter/README.html
original_path: samples/drivers/can/counter/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Controller Area Network (CAN) counter

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
