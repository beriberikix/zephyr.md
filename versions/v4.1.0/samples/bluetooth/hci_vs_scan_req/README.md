---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/hci_vs_scan_req/README.html
original_path: samples/bluetooth/hci_vs_scan_req/README.html
---

# HCI Vendor-Specific Scan Request

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_vs_scan_req/README.rst/..)

## Overview

This simple application is a usage example to manage HCI VS commands to obtain
scan request events even using legacy advertisements, while may result in lower
RAM usage than using extended advertising.
This is quite important in applications in which the broadcaster role is added
to the central role, where the RAM saving can be bigger.
This sample implements only the broadcaster role; the peripheral role with
connection can also be added, depending on configuration choices.

## Requirements

- A board with Bluetooth LE support
- A central device & monitor (e.g. nRF Connect) to check the advertiments and
  send scan requests.

## Building and Running

This sample can be found under [samples/bluetooth/hci\_vs\_scan\_req](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_vs_scan_req)
in the Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
