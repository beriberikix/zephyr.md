---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/iso_receive/README.html
original_path: samples/bluetooth/iso_receive/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Synchronized Receiver

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
the Zephyr tree. Use -DEXTRA\_CONF\_FILE=overlay-bt\_ll\_sw\_split.conf to enable
required ISO feature support in Zephyr Bluetooth Controller on supported boards.

Use the sample found under [samples/bluetooth/iso\_broadcast](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/iso_broadcast) on
another board that will start periodic advertising, create BIG to which this
sample will establish periodic advertising synchronization and synchronize to
the Broadcast Isochronous Stream.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
