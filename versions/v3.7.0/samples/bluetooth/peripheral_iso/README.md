---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/peripheral_iso/README.html
original_path: samples/bluetooth/peripheral_iso/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Peripheral ISO

## Overview

This sample demonstrates how to use isochronous channels as a peripheral.
The sample starts advertising, waits for a central to connect to it and set up an isochronous channel.
Once the isochronous channel is set up, received isochronous data is printed out.
It is recommended to run this sample together with the [Bluetooth: Central ISO](../central_iso/README.md#bluetooth-central-iso) sample.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  CONFIG\_BT\_CTLR\_PERIPHERAL\_ISO=y

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_iso](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_iso) in the Zephyr tree.

1. Start the application.
   In the terminal window, check that it is advertising.

   > Bluetooth initialized
   > Advertising successfully started
2. Observe that the central device connects and sets up an isochronous channel.

   > Connected E8:DC:8D:B3:47:69 (random)
   > Incoming request from 0x20002260
   > ISO Channel 0x20000698 connected
3. Observe that incoming data is printed.

   > Incoming data channel 0x20000698 len 1
   > :   00
   >
   > Incoming data channel 0x20000698 len 2
   > :   0001
   >
   > Incoming data channel 0x20000698 len 3
   > :   000102
   >
   > Incoming data channel 0x20000698 len 4
   > :   00010203
   >
   > Incoming data channel 0x20000698 len 5
   > :   0001020304
   >
   > Incoming data channel 0x20000698 len 6
   > :   000102030405
   >
   > Incoming data channel 0x20000698 len 7
   > :   000102…040506
   >
   > Incoming data channel 0x20000698 len 8
   > :   000102…050607
   >
   > Incoming data channel 0x20000698 len 9
   > :   000102…060708
   >
   > Incoming data channel 0x20000698 len 10
   > :   000102…070809
   >
   > Incoming data channel 0x20000698 len 11
   > :   000102…08090a
   >
   > Incoming data channel 0x20000698 len 12
   > :   000102…090a0b

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for more details.
