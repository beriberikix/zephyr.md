---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/can/README.html
original_path: samples/net/sockets/can/README.html
---

# SocketCAN

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/can/README.rst/..)

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

You need a CANBUS enabled board like [Nucleo L432KC](../../../../boards/st/nucleo_l432kc/doc/index.md#nucleo_l432kc) or
[STM32F072B Discovery](../../../../boards/st/stm32f072b_disco/doc/index.md#stm32f072b_disco).

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

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[SocketCAN library](../../../../doxygen/html/group__socket__can.md)
