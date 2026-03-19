---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/usb/console-next/README.html
original_path: samples/subsys/usb/console-next/README.html
---

# Console over USB CDC ACM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/console-next/README.rst/..)

## Overview

This example application shows how to use the CDC ACM UART provided by the new
experimental USB device stack as a serial backend for the console.

## Requirements

This project requires an experimental USB device driver (UDC API).

## Building and Running

This sample can be built for multiple boards, in this example we will build it
for the reel\_board board:

```shell
west build -b reel_board samples/subsys/usb/console-next
west flash
```

Plug the board into a host device, for sample, a PC running Linux OS.
The board will be detected as a CDC ACM serial device. To see the console output
from the sample, use a command similar to **minicom -D /dev/ttyACM1**.

```shell
Hello World! arm
Hello World! arm
Hello World! arm
Hello World! arm
```

## See also

[USB device core API](../../../../doxygen/html/group__usbd__api.md)

[UART Interface](../../../../doxygen/html/group__uart__interface.md)
