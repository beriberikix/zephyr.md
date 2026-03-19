---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/eddystone/README.html
original_path: samples/bluetooth/eddystone/README.html
---

# Eddystone

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/eddystone/README.rst/..)

## Overview

Application demonstrating [Eddystone Configuration Service](https://github.com/google/eddystone/tree/master/configuration-service)

The Eddystone Configuration Service runs as a GATT service on the beacon while
it is connectable and allows configuration of the advertised data, the
broadcast power levels, and the advertising intervals. It also forms part of
the definition of how Eddystone-EID beacons are configured and registered with
a trusted resolver.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/eddystone](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/eddystone) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
