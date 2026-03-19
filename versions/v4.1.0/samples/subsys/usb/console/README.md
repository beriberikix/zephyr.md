---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/usb/console/README.html
original_path: samples/subsys/usb/console/README.html
---

# Console over USB CDC ACM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/console/README.rst/..)

## Overview

A simple Hello World sample, with console output coming via CDC ACM UART.
Primarily intended to show the required config options.

## Requirements

This project requires a USB device controller driver.

## Building and Running

This sample can be built for multiple boards, in this example we will build it
for the reel\_board board:

```shell
west build -b reel_board samples/subsys/usb/console
west flash
```

Plug the board into a host device, for sample, a PC running Linux OS.
The board will be detected as a CDC\_ACM serial device. To see the console output
from the sample, use a command similar to **minicom -D /dev/ttyACM0**.

```shell
Hello World! arm
Hello World! arm
Hello World! arm
Hello World! arm
```

### Troubleshooting

You may need to stop **modemmanager** via **sudo stop modemmanager**, if it is
trying to access the device in the background.

## See also

[USB Device Core API](../../../../doxygen/html/group____usb__device__core__api.md)

[USB device core API](../../../../doxygen/html/group__usbd__api.md)
