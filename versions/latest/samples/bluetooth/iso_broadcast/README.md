---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/iso_broadcast/README.html
original_path: samples/bluetooth/iso_broadcast/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Isochronous Broadcaster

## Overview

A simple application demonstrating the Bluetooth Low Energy Isochronous
Broadcaster functionality.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  CONFIG\_BT\_CTLR\_ADV\_ISO=y

## Building and Running

This sample can be found under [samples/bluetooth/iso\_broadcast](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_broadcast) in
the Zephyr tree. Use -DEXTRA\_CONF\_FILE=overlay-bt\_ll\_sw\_split.conf to enable
required ISO feature support in Zephyr Bluetooth Controller on supported boards.

Use the sample found under [samples/bluetooth/iso\_receive](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_receive) in the
Zephyr tree that will scan, establish a periodic advertising synchronization,
generate BIGInfo reports and synchronize to BIG events from this sample.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
