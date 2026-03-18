---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/sockets/can/README.html
original_path: samples/net/sockets/can/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SocketCAN

## Overview

The socket CAN sample is a server/client application that sends and receives
raw CAN frames using BSD socket API.

The application consists of these functions:

- Setup function which creates a CAN socket, binds it to a CAN network
  interface, and then installs a CAN filter to the socket so that the
  application can receive CAN frames.
- Receive function which starts to listen the CAN socket and prints
  information about the CAN frames.
- Send function which starts to send raw CAN frames to the bus.

The source code for this sample application can be found at:
[samples/net/sockets/can](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/can).

## Requirements

You need a CANBUS enabled board like [ST Nucleo L432KC](../../../../boards/st/nucleo_l432kc/doc/index.md#nucleo-l432kc-board) or
[ST STM32F072B Discovery](../../../../boards/st/stm32f072b_disco/doc/index.md#stm32f072b-disco-board).

## Building and Running

Build the socket CAN sample application like this:

```shell
west build -b <board to use> samples/net/sockets/can -- -DCONF_FILE=<config file to use>
```

Example building for the nucleo\_l432kc:

```shell
west build -b nucleo_l432kc samples/net/sockets/can
west build -t run
```
