---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/peripheral_sc_only/README.html
original_path: samples/bluetooth/peripheral_sc_only/README.html
---

# Peripheral SC-only

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_sc_only/README.rst/..)

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).") sample, except that this
application enables the Secure Connections Only mode, i.e. will only
accept connections that are secured using security level 4 (FIPS).

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_sc\_only](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_sc_only)
in the Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Connection management](../../../doxygen/html/group__bt__conn.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
