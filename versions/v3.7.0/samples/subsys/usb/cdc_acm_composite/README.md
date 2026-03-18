---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/usb/cdc_acm_composite/README.html
original_path: samples/subsys/usb/cdc_acm_composite/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB CDC-ACM composite

## Overview

This sample app demonstrates use of a USB Communication Device Class (CDC)
Abstract Control Model (ACM) driver provided by the Zephyr project in
Composite configuration.

Two serial ports are created when the device is plugged to the PC.
Received data from one serial port is sent to another serial port
provided by this driver.

## Running

Plug the board into a host device, for example, a PC running Linux.
The board will be detected as shown by the Linux dmesg command:

```shell
usb 1-1.5.4: new full-speed USB device number 28 using ehci-pci
usb 1-1.5.4: New USB device found, idVendor=2fe3, idProduct=0002, bcdDevice= 2.03
usb 1-1.5.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.5.4: Product: Zephyr CDC ACM Composite sample
usb 1-1.5.4: Manufacturer: ZEPHYR
usb 1-1.5.4: SerialNumber: 86FE679A598AC47A
cdc_acm 1-1.5.4:1.0: ttyACM1: USB ACM device
cdc_acm 1-1.5.4:1.2: ttyACM2: USB ACM device
```

The app prints on serial output, used for the console:

```shell
Wait for DTR
```

Open a serial port emulator, for example, minicom,
and attach it to both detected CDC ACM devices:

```shell
minicom --device /dev/ttyACM1
minicom --device /dev/ttyACM2
```

The app should respond on serial output with:

```shell
DTR set, start test
Baudrate detected: 115200
Baudrate detected: 115200
```

And on ttyACM devices provided by the Zephyr USB device stack:

```shell
Send characters to another UART device
```

The characters entered in one serial port will be sent to another
serial port.
