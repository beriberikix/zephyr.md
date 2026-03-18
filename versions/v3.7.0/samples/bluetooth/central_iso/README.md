---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/central_iso/README.html
original_path: samples/bluetooth/central_iso/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Central ISO

## Overview

This sample demonstrates how to use an isochronous channel as a central.
The sample scans for a peripheral, establishes a connection, and sets up a connected isochronous channel to it.
Once the isochronous channel is connected, isochronous data is transferred to the peer device every 10 milliseconds.
It is recommended to run this sample together with the [Bluetooth: Peripheral ISO](../peripheral_iso/README.md#peripheral-iso) sample.

To run the sample with an encrypted isochronous channel, enable [`CONFIG_BT_SMP`](../../../kconfig.md#CONFIG_BT_SMP "CONFIG_BT_SMP").

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  [`CONFIG_BT_CTLR_CENTRAL_ISO`](../../../kconfig.md#CONFIG_BT_CTLR_CENTRAL_ISO "CONFIG_BT_CTLR_CENTRAL_ISO").

## Building and Running

This sample can be found under [samples/bluetooth/central\_iso](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_iso) in
the Zephyr tree.

1. Start the application.
   In the terminal window, check that it is scanning for other devices.

   > Bluetooth initialized
   > Scanning successfully started
   > Device found: D3:3A:5D:F5:73:33 (random) (RSSI -78)
   > Device found: 70:7B:F4:2B:76:AD (random) (RSSI -68)
   > Device found: 65:CF:20:0D:CB:9D (random) (RSSI -82)
2. Observe that the device connects.

   > Connected: 65:CF:20:0D:CB:9D (random)
3. Observe that the ISO channel is connected

   > ISO Channel 0x200048f8 connected

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for more details.
