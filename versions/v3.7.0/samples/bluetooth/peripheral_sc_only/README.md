---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/peripheral_sc_only/README.html
original_path: samples/bluetooth/peripheral_sc_only/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Peripheral SC-only

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble-peripheral) sample, except that this
application enables the Secure Connections Only mode, i.e. will only
accept connections that are secured using security level 4 (FIPS).

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_sc\_only](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_sc_only)
in the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
