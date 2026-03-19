---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/iso_central/README.html
original_path: samples/bluetooth/iso_central/README.html
---

# ISO (Central)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/iso_central/README.rst/..)

## Overview

This sample demonstrates how to use an isochronous channel as a central.
The sample scans for a peripheral, establishes a connection, and sets up a connected isochronous channel to it.
Once the isochronous channel is connected, isochronous data is transferred to the peer device every 10 milliseconds.
It is recommended to run this sample together with the [ISO (Peripheral)](../iso_peripheral/README.md#ble_peripheral_iso "Implement a Bluetooth LE Peripheral that uses isochronous channels.") sample.

To run the sample with an encrypted isochronous channel, enable [`CONFIG_BT_SMP`](../../../kconfig.md#CONFIG_BT_SMP "CONFIG_BT_SMP").

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  [`CONFIG_BT_CTLR_CENTRAL_ISO`](../../../kconfig.md#CONFIG_BT_CTLR_CENTRAL_ISO "CONFIG_BT_CTLR_CENTRAL_ISO").

## Building and Running

This sample can be found under [samples/bluetooth/iso\_central](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_central) in
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

See [Bluetooth](../bluetooth.md#bluetooth) samples for more details.

## See also

[Isochronous channels (ISO)](../../../doxygen/html/group__bt__iso.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
