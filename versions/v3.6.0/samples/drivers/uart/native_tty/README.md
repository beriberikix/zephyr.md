---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/uart/native_tty/README.html
original_path: samples/drivers/uart/native_tty/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Native TTY UART

## Overview

This sample demonstrates the usage of the Native TTY UART driver. It uses two
UART to USB bridge dongles that are wired together, writing demo data to one
dongle and reading it from the other.”

The source code for this sample application can be found at:
[samples/drivers/uart/native-tty](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/uart/native-tty).

You can learn more about the Native TTY UART driver in the
[TTY UART](../../../../boards/posix/native_sim/doc/index.md#native-tty-uart) section of the native\_sim board
documentation.

## Requirements

1. Two UART to USB bridge dongles. Each dongle must have its TX pin wired to the
   other dongle’s RX pin. The ground connection is not needed. Both dongles must
   be plugged into the host machine.
2. The DT overlay provided with the sample expects the dongles to appear as
   `/dev/ttyUSB0` and `/dev/ttyUSB1` in the system. You can check what they
   are in your system by running the command `ls -l /dev/tty*`. If that is not
   the case on your machine you can either change the `serial-port` properties
   in the `boards/native_sim.overlay` file or using the command line options
   `-uart_port` and `-uart_port2`.

## Building and Running

This application can be built and executed on [native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim) as follows:

```shell
west build -b native_sim samples/drivers/uart/native_tty
west build -t run
```

### Sample Output

```shell
uart_1 connected to pseudotty: /dev/pts/6
uart2 connected to the serial port: /dev/ttyUSB1
uart connected to the serial port: /dev/ttyUSB0
*** Booting Zephyr OS build v3.4.0-rc2-97-ge586d02c137d ***
Device uart sent: "Hello from device uart, num 9"
Device uart2 received: "Hello from device uart, num 9"
Device uart sent: "Hello from device uart, num 8"
Device uart2 received: "Hello from device uart, num 8"
Device uart sent: "Hello from device uart, num 7"
Device uart2 received: "Hello from device uart, num 7"
Device uart sent: "Hello from device uart, num 6"
Device uart2 received: "Hello from device uart, num 6"
Device uart sent: "Hello from device uart, num 5"
Device uart2 received: "Hello from device uart, num 5"
Device uart sent: "Hello from device uart, num 4"
Device uart2 received: "Hello from device uart, num 4"
Device uart sent: "Hello from device uart, num 3"
Device uart2 received: "Hello from device uart, num 3"
Device uart sent: "Hello from device uart, num 2"
Device uart2 received: "Hello from device uart, num 2"
Device uart sent: "Hello from device uart, num 1"
Device uart2 received: "Hello from device uart, num 1"
Device uart sent: "Hello from device uart, num 0"
Device uart2 received: "Hello from device uart, num 0"

Changing baudrate of both uart devices to 9600!

Device uart sent: "Hello from device uart, num 9"
Device uart2 received: "Hello from device uart, num 9"
Device uart sent: "Hello from device uart, num 8"
Device uart2 received: "Hello from device uart, num 8"
Device uart sent: "Hello from device uart, num 7"
Device uart2 received: "Hello from device uart, num 7"
Device uart sent: "Hello from device uart, num 6"
Device uart2 received: "Hello from device uart, num 6"
Device uart sent: "Hello from device uart, num 5"
Device uart2 received: "Hello from device uart, num 5"
Device uart sent: "Hello from device uart, num 4"
Device uart2 received: "Hello from device uart, num 4"
Device uart sent: "Hello from device uart, num 3"
Device uart2 received: "Hello from device uart, num 3"
Device uart sent: "Hello from device uart, num 2"
Device uart2 received: "Hello from device uart, num 2"
Device uart sent: "Hello from device uart, num 1"
Device uart2 received: "Hello from device uart, num 1"
Device uart sent: "Hello from device uart, num 0"
Device uart2 received: "Hello from device uart, num 0"
```
