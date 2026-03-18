---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/eddystone/README.html
original_path: samples/bluetooth/eddystone/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Eddystone

## Overview

Application demonstrating [Eddystone Configuration Service](https://github.com/google/eddystone/tree/master/configuration-service)

The Eddystone Configuration Service runs as a GATT service on the beacon while
it is connectable and allows configuration of the advertised data, the
broadcast power levels, and the advertising intervals. It also forms part of
the definition of how Eddystone-EID beacons are configured and registered with
a trusted resolver.

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/eddystone](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/eddystone) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
