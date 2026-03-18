---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/hci_vs_scan_req/README.html
original_path: samples/bluetooth/hci_vs_scan_req/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: HCI VS Scan Request

## Overview

This simple application is a usage example to manage HCI VS commands to obtain
scan equest events even using legacy advertisements, while may result in lower
RAM usage than using extended advertising.
This is quite important in applications in which the broadcaster role is added
to the central role, where the RAM saving can be bigger.
This sample implements only the broadcaster role; the peripheral role with
connection can also be added, depending on configuration choices.

## Requirements

- A board with BLE support
- A central device & monitor (e.g. nRF Connect) to check the advertiments and
  send scan requests.

## Building and Running

This sample can be found under [samples/bluetooth/hci\_vs\_scan\_req](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_vs_scan_req)
in the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
