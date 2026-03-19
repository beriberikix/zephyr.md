---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/iso_receive/README.html
original_path: samples/bluetooth/iso_receive/README.html
---

# Synchronized Receiver

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/iso_receive/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth Low Energy Synchronized
Receiver functionality.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  CONFIG\_BT\_CTLR\_SYNC\_ISO=y

## Building and Running

This sample can be found under [samples/bluetooth/iso\_receive](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_receive) in
the Zephyr tree. Use `-DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf` to enable
required ISO feature support in Zephyr Bluetooth Controller on supported boards.

Use the sample found under [samples/bluetooth/iso\_broadcast](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_broadcast) on
another board that will start periodic advertising, create BIG to which this
sample will establish periodic advertising synchronization and synchronize to
the Broadcast Isochronous Stream.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Isochronous channels (ISO)](../../../doxygen/html/group__bt__iso.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
