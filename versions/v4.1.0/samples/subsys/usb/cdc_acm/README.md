---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/usb/cdc_acm/README.html
original_path: samples/subsys/usb/cdc_acm/README.html
---

# USB CDC-ACM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/cdc_acm/README.rst/..)

## Overview

This sample app demonstrates use of a USB Communication Device Class (CDC)
Abstract Control Model (ACM) driver provided by the Zephyr project.
Received data from the serial port is echoed back to the same port
provided by this driver.
This sample can be found under [samples/subsys/usb/cdc\_acm](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/cdc_acm) in the
Zephyr project tree.

## Requirements

This project requires an USB device driver, which is available for multiple
boards supported in Zephyr.

## Building and Running

### Reel Board

To see the console output of the app, open a serial port emulator and
attach it to the USB to TTL Serial cable. Build and flash the project:

```shell
west build -b reel_board samples/subsys/usb/cdc_acm
west flash
```

### Running

Plug the board into a host device, for example, a PC running Linux.
The board will be detected as shown by the Linux dmesg command:

```shell
usb 9-1: new full-speed USB device number 112 using uhci_hcd
usb 9-1: New USB device found, idVendor=8086, idProduct=f8a1
usb 9-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 9-1: Product: CDC-ACM
usb 9-1: Manufacturer: Intel
usb 9-1: SerialNumber: 00.01
cdc_acm 9-1:1.0: ttyACM1: USB ACM device
```

The app prints on serial output (UART1), used for the console:

```shell
Wait for DTR
```

Open a serial port emulator, for example minicom
and attach it to detected CDC ACM device:

```shell
minicom --device /dev/ttyACM1
```

The app should respond on serial output with:

```shell
DTR set, start test
Baudrate detected: 115200
```

And on ttyACM device, provided by zephyr USB device stack:

```shell
Send characters to the UART device
Characters read:
```

The characters entered in serial port emulator will be echoed back.

### Troubleshooting

If the ModemManager runs on your operating system, it will try
to access the CDC ACM device and maybe you can see several characters
including “AT” on the terminal attached to the CDC ACM device.
You can add or extend the udev rule for your board to inform
ModemManager to skip the CDC ACM device.
For this example, it would look like this:

```text
ATTRS{idVendor}=="8086" ATTRS{idProduct}=="f8a1", ENV{ID_MM_DEVICE_IGNORE}="1"
```

## See also

[USB device core API](../../../../doxygen/html/group__usbd__api.md)

[USB Device Core API](../../../../doxygen/html/group____usb__device__core__api.md)

[UART Interface](../../../../doxygen/html/group__uart__interface.md)
