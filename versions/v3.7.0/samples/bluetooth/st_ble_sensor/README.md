---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/st_ble_sensor/README.html
original_path: samples/bluetooth/st_ble_sensor/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: ST BLE Sensor Demo

## Overview

This application demonstrates BLE peripheral by exposing vendor-specific
GATT services. Currently only button notification and LED service are
implemented. Other BLE sensor services can easily be added.
See [BlueST protocol](https://www.st.com/resource/en/user_manual/dm00550659.pdf) document for details of how to add a new service.

## Requirements

- [ST BLE Sensor Android app](https://play.google.com/store/apps/details?id=com.st.bluems)
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/st\_ble\_sensor](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/st_ble_sensor) in the
Zephyr tree.

Open ST BLE Sensor app and click on “CONNECT TO A DEVICE” button to scan BLE devices.
To connect click on the device shown in the Device List.
After connected, tap LED image on Android to test LED service.
Push SW0 button on embedded device to test button service.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
