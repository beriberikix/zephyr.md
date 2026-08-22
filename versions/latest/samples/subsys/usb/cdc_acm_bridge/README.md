---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/subsys/usb/cdc_acm_bridge/README.html
original_path: samples/subsys/usb/cdc_acm_bridge/README.html
---

# USB CDC-ACM bridge

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/cdc_acm_bridge/README.rst/..)

## Overview

This sample app demonstrates use of a USB CDC-ACM to bridge a standard hardware
UART on a supported board.
This sample can be found under [samples/subsys/usb/cdc\_acm\_bridge](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/cdc_acm_bridge) in the
Zephyr project tree.

## Requirements

This project requires an USB device driver, which is available for multiple
boards supported in Zephyr.

The board has to have an USB interface as well as hardware UART, the device
node for the hardware UART is board specific so each supported board needs an
explicit overlay.

## Building and Running

### Reel Board

To see the console output of the app, open a serial port emulator and
attach it to the USB to TTL Serial cable. Build and flash the project:

```shell
west build -b reel_board samples/subsys/usb/cdc_acm_bridge
west flash
```

### Running

Plug the board into a host device, for example, a PC running Linux, the board
should enumerate as a CDC-ACM device, the CDC-ACM input and output should be
echoed back to the real UART, and configuration changes to the CDC-ACM uart
such as bitrate will be propagated to the hardware port.

If the hardware port is connected to an on-board debugger then the output
should be echoed between the two ports, if it’s connected to some pins on the
boards the pins can be shorted together to test that the driver is working
correctly.

## See also

[UART Interface](../../../../doxygen/html/group__uart__interface.md)
