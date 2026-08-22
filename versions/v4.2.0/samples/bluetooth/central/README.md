---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/bluetooth/central/README.html
original_path: samples/bluetooth/central/README.html
---

# Central

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/central/README.rst/..)

## Overview

This application demonstrates basic Bluetooth LE Central role functionality
by scanning for other Bluetooth LE devices and establishing a connection
to the first one with a strong enough signal.

## Core features

### Scanning for devices

The application initiates a passive scan to detect nearby Bluetooth LE devices.
It specifically looks for devices that have a signal strength greater
than -50dBm. This threshold helps the app filter out weaker signals,
ensuring it only interacts with devices that are within a reasonable RSSI
range for communication.

### Connection handling

1. The Central scans for Peripheral devices and if it finds a Peripheral
   which has a signal strength higher than -50dBm, an attempt to establish
   LE connection is made.
2. If the connection is successful, the Central initiates disconnect to
   the Peripheral and then restarts the scan.
3. If there are no connections, the Central keeps scanning continuously.

The sample is used to demonstrate the Central mode capabilities of Bluetooth LE and
hence a disconnect is issued right immediately after establishing a connection with
a Peripheral, allowing the Central to resume scanning for other devices.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and running

Build and flash the sample as follows, replacing board\_name with your
target board:

```shell
west build -b board_name samples/bluetooth/central
west flash
```

To test Central’s scanning functionality, either flash the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")
sample on a second compatible board or use an off-the-shelf Bluetooth LE enabled
device that can act as a Peripheral (eg. smartphone, smartwatch, etc.).

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
